# -*- coding: utf-8 -*-
"""LANE 4 — NAMES UNDER EVERY FILTER (Alan 8/31: "I should see all the names
of people that apply with that filter"). Kills the Unknowns that already have
answers in the raws: August cohort, opt-in vs direct entry, speed-to-lead,
derived triage, GHL showed-status. One JSON + one scannable MD, per-person.
Sources: ops/archive/ghl/2026-08-30/raw + triage_derived CSV. Labels: VERIFIED
(GHL field) / DERIVED (computed, method stated).
"""
import json, csv, sys, datetime, pathlib
from collections import defaultdict

DATE = sys.argv[1] if len(sys.argv) > 1 else "2026-08-30"
REPO = pathlib.Path(__file__).resolve().parent.parent.parent
D = REPO / "ops" / "archive" / "ghl" / DATE
RAW = D / "raw"
J = lambda n: json.load(open(RAW / f"{n}.json", encoding="utf-8"))

contacts = J("contacts")
details = J("contact_details")
appts = J("appointments_by_contact")

triage = {}
with open(D / f"triage_derived_{DATE}.csv", encoding="utf-8-sig") as f:
    for r in csv.DictReader(f):
        triage[r["contactId"]] = r
stl_min = {}
with open(D / f"speed_to_lead_{DATE}.csv", encoding="utf-8-sig") as f:
    for r in csv.DictReader(f):
        try: stl_min[r["contactId"]] = float(r["minutesToFirstTouch"])
        except Exception: pass

def name(c):
    return (f'{c.get("firstNameRaw") or c.get("firstName") or ""} {c.get("lastNameRaw") or c.get("lastName") or ""}'.strip() or "(no name)")

def entry_path(cid):
    d = details.get(cid, {})
    for src in (d.get("attributionSource") or {}, d.get("lastAttributionSource") or {}):
        if src.get("medium") == "survey": return "Opt-In Form (VERIFIED: attribution medium=survey)"
        if src.get("medium") == "calendar": return "Direct Booked (VERIFIED: attribution medium=calendar)"
        if src.get("url"): return "Ad click, path unlabeled (VERIFIED attribution, medium=%s)" % (src.get("medium") or "?")
    return "No attribution captured (UNKNOWN - nothing recorded)"

F = defaultdict(list)
per_person = {}
for c in contacts:
    cid = c["id"]; nm = name(c)
    t = triage.get(cid, {})
    ep = entry_path(cid)
    stl = t.get("booking_to_touch_hrs") or ""
    stlm = stl_min.get(cid)  # true speed-to-lead: contact created -> first outbound touch, minutes
    evs = appts.get(cid, [])
    aug_slots = [e for e in evs if str(e.get("startTime", "")).startswith("2026-08")]
    statuses = sorted({(e.get("appointmentStatus") or "?").lower() for e in evs})
    rec = {
        "name": nm, "ghl_id": cid,
        "entry_path": ep,
        "human_touch_DERIVED": t.get("human_touch(DERIVED)") or "no",
        "first_touch": t.get("first_human_touch_utc") or "",
        "engaged_back": t.get("contact_engaged_back") or "no",
        "touched_before_slot": t.get("triaged_before_slot") or "",
        "booking_to_touch_hrs": stl,
        "appt_statuses_VERIFIED": statuses,
        "august_slots": [str(e.get("startTime"))[:16] for e in aug_slots],
    }
    rec["speed_to_lead_min"] = stlm
    per_person[nm + " · " + cid[-6:]] = rec  # suffix keeps duplicate/blank names distinct
    if aug_slots: F["AUGUST — booked slot in August (%d)" % 0].append(nm)
    if str(c.get("dateAdded", "")).startswith("2026-08"): F["AUGUST — became a contact in August"].append(nm)
    if ep.startswith("Opt-In"): F["ENTRY — Opt-In Form (verified)"].append(nm)
    elif ep.startswith("Direct"): F["ENTRY — Direct Booked (verified)"].append(nm)
    elif ep.startswith("Ad click"): F["ENTRY — ad click, form path unlabeled"].append(nm)
    else: F["ENTRY — no attribution captured"].append(nm)
    if t.get("human_touch(DERIVED)") == "yes":
        F["TRIAGE — human touch (derived)"].append(nm)
        if t.get("contact_engaged_back") == "yes": F["TRIAGE — two-way conversation (derived)"].append(nm)
        if t.get("triaged_before_slot") == "yes": F["TRIAGE — touched BEFORE first slot (derived)"].append(nm)
    else:
        F["TRIAGE — never humanly touched (derived)"].append(nm)
    if stlm is not None:
        if stlm <= 5: F["SPEED-TO-LEAD — first touch ≤5 min"].append(nm)
        elif stlm <= 60: F["SPEED-TO-LEAD — 5–60 min"].append(nm)
        else: F["SPEED-TO-LEAD — over 60 min"].append(nm)
    for s in statuses:
        if s in ("showed", "noshow", "cancelled"): F["OUTCOME — GHL status: " + s].append(nm)
    if evs and statuses == ["confirmed"]:
        F["OUTCOME — booked, status never updated (the real 'unknown')"].append(nm)

# rename august booked key with count fixed
for k in list(F):
    if k.startswith("AUGUST — booked slot in August"):
        F["AUGUST — booked slot in August"] = F.pop(k)

out_json = REPO / "ops" / "data" / "NAMES_BY_FILTER.json"
out_json.write_text(json.dumps({"generated": DATE + " pull, built 2026-08-31",
                                "filters": {k: sorted(v) for k, v in F.items()},
                                "per_person": per_person}, indent=1, ensure_ascii=False), encoding="utf-8")
md = ["# NAMES UNDER EVERY FILTER — no more count-without-names (Alan 8/31)",
      "*Click-equivalent: every filter lists its people. VERIFIED = GHL field · DERIVED = computed from raw messages (method in ops/lane4/derive_triage.py). Source of truth: ops/data/NAMES_BY_FILTER.json*", ""]
for k in sorted(F):
    v = sorted(set(F[k]))
    md.append("## %s (%d)" % (k, len(v)))
    md.append(" · ".join(v)); md.append("")
(REPO / "ops" / "data" / "NAMES_BY_FILTER.md").write_text("\n".join(md), encoding="utf-8")
print("filters:", {k: len(set(v)) for k, v in sorted(F.items())})
