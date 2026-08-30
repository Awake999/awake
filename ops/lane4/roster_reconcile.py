# -*- coding: utf-8 -*-
"""LANE 4 — reconcile the roster audit's Unknown show outcomes against GHL
appointment statuses. Reads ops/data/BOOKING_ROSTER_AUDIT.md + the day's pull;
writes ops/archive/ghl/<date>/ROSTER_RECONCILIATION.md.

Matching rule (conservative, per Alan's accuracy doctrine): a GHL appointment
resolves an Unknown row only when the contact name matches (normalized) AND the
GHL slot start falls on the audit row's booked-slot date (+/- 1 day for TZ) AND
the GHL status is a terminal outcome (showed / noshow / cancelled). 'confirmed'
or 'new' are NOT outcomes and resolve nothing.
"""
import json, re, sys, datetime, pathlib, unicodedata
from collections import Counter

DATE = sys.argv[1] if len(sys.argv) > 1 else datetime.date.today().isoformat()
REPO = pathlib.Path(__file__).resolve().parent.parent.parent
D = REPO / "ops" / "archive" / "ghl" / DATE
RAW = D / "raw"
J = lambda n: json.load(open(RAW / f"{n}.json", encoding="utf-8"))

contacts = J("contacts")
appts = J("appointments_by_contact")
cby = {c["id"]: c for c in contacts}

def norm(s):
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z ]", "", s.lower()).strip()

# GHL appointment index: normalized contact name -> list of (slot_date, status, title, apptid)
ghl = []
for cid, evs in appts.items():
    c = cby.get(cid, {})
    nm = norm(f'{c.get("firstNameRaw") or c.get("firstName") or ""} {c.get("lastNameRaw") or c.get("lastName") or ""}')
    for e in evs:
        st = (e.get("appointmentStatus") or e.get("status") or "").lower()
        start = e.get("startTime")
        try:
            dt = datetime.datetime.fromisoformat(str(start).replace("Z", "+00:00")).date()
        except Exception:
            dt = None
        ghl.append({"cid": cid, "name": nm, "date": dt, "status": st,
                    "title": e.get("title"), "id": e.get("id"), "start": start})

# Parse audit rows
MON = {m: i + 1 for i, m in enumerate(["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"])}
audit = REPO / "ops" / "data" / "BOOKING_ROSTER_AUDIT.md"
rows = []
for line in audit.read_text(encoding="utf-8").splitlines():
    m = re.match(r"\|\s*(\d+)\s*\|([^|]+)\|([^|]+)\|([^|]+)\|([^|]+)\|([^|]+)\|", line)
    if not m: continue
    num, name, alert, slot, entry, showed = [g.strip() for g in m.groups()]
    rows.append({"num": int(num), "name": name, "alert": alert, "slot": slot, "showed": showed})

def slot_date(row):
    m = re.search(r"([A-Z][a-z]{2})\s+(\d+)", row["slot"])
    if not m: return None
    mon, day = MON.get(m.group(1)), int(m.group(2))
    if not mon: return None
    year = 2026
    return datetime.date(year, mon, day)

unknown = [r for r in rows if r["showed"].lower().startswith("unknown")]
TERMINAL = {"showed", "noshow", "no-show", "cancelled", "canceled", "invalid"}
resolved, unresolved = [], []
for r in unknown:
    nm = norm(re.sub(r"\(.*?\)", "", r["name"]))
    sd = slot_date(r)
    hits = [g for g in ghl if g["name"] == nm and g["date"] and sd and abs((g["date"] - sd).days) <= 1]
    term = [h for h in hits if h["status"] in TERMINAL]
    if term:
        resolved.append((r, term))
    else:
        unresolved.append((r, hits))

status_ct = Counter(h["status"] for _, hs in resolved for h in hs[:1])
out = ["# Roster reconciliation — GHL appointment statuses vs the 79 Unknown events (%s)" % DATE, ""]
out.append("GHL terminal statuses found for **%d of %d** Unknown events.\n" % (len(resolved), len(unknown)))
out.append("Resolution statuses (first matching appt per row): %s\n" % dict(status_ct))
out.append("| Audit # | Name | Booked slot | GHL status | GHL slot start | Appt ID |")
out.append("|---|---|---|---|---|---|")
for r, hs in resolved:
    h = hs[0]
    out.append("| %d | %s | %s | **%s** | %s | %s |" % (r["num"], r["name"], r["slot"], h["status"], h["start"], h["id"]))
out.append("")
out.append("## Still unresolved (%d)" % len(unresolved))
out.append("| Audit # | Name | Booked slot | GHL non-terminal matches |")
out.append("|---|---|---|---|")
for r, hs in unresolved:
    out.append("| %d | %s | %s | %s |" % (r["num"], r["name"], r["slot"],
               "; ".join("%s@%s" % (h["status"], h["date"]) for h in hs) or "no matching appt"))
(D / "ROSTER_RECONCILIATION.md").write_text("\n".join(out), encoding="utf-8")
print("unknown rows:", len(unknown), "resolved:", len(resolved), dict(status_ct))
