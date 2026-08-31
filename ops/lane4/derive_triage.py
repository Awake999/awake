# -*- coding: utf-8 -*-
"""LANE 4 — DERIVED triage + recordings index from raw GHL messages.
Alan's spec (verbatim prompts, 8/30): "did they get triaged by a human, yes or
no? If not, when? ... how long it took from the time they booked to when we
triage them, actually in a real human conversation."
Method (DERIVED, labeled — never guessed): a human touch = message with
source=='app' (sent by a person from the app, not a workflow) or a connected
call (duration>0). Engaged = contact replied inbound after a human touch.
Outputs: triage_derived_<date>.csv · recordings_<date>.csv (links only) ·
folds summary into CANON_NUMBERS.json.
"""
import json, csv, sys, datetime, pathlib

DATE = sys.argv[1] if len(sys.argv) > 1 else datetime.date.today().isoformat()
REPO = pathlib.Path(__file__).resolve().parent.parent.parent
D = REPO / "ops" / "archive" / "ghl" / DATE
RAW = D / "raw"
J = lambda n: json.load(open(RAW / f"{n}.json", encoding="utf-8"))

contacts = J("contacts")
appts = J("appointments_by_contact")
convs = J("conversations")
msgs = J("messages_by_conversation")
LOC = "WFkoNzKa9J9PxhngsLfl"

conv_by_contact = {}
for cvid, cv in convs.items():
    conv_by_contact.setdefault(cv.get("contactId"), []).append(cvid)

def ts(t):
    try:
        d = datetime.datetime.fromisoformat(str(t).replace("Z", "+00:00"))
        if d.tzinfo is None:  # some appointment slots come back tz-naive (local wall time)
            d = d.replace(tzinfo=datetime.timezone.utc)
        return d
    except Exception:
        return None

rows, recs = [], []
n_triaged = n_before = n_engaged = 0
for c in contacts:
    cid = c["id"]
    nm = f'{c.get("firstNameRaw") or c.get("firstName") or ""} {c.get("lastNameRaw") or c.get("lastName") or ""}'.strip()
    first_human = None; first_human_kind = ""
    engaged = False
    events = []
    for cvid in conv_by_contact.get(cid, []):
        for m in msgs.get(cvid, []):
            t = ts(m.get("dateAdded"))
            if not t: continue
            mt = m.get("messageType")
            call = (m.get("meta") or {}).get("call") or {}
            human = (m.get("direction") == "outbound" and m.get("source") == "app") or \
                    (mt == "TYPE_CALL" and (call.get("duration") or 0) > 30)
            events.append((t, m.get("direction"), human))
            if human and (first_human is None or t < first_human):
                first_human, first_human_kind = t, ("call" if mt == "TYPE_CALL" else "message")
            if mt == "TYPE_CALL" and m.get("attachments"):
                recs.append([cid, nm, str(m.get("dateAdded"))[:19], m.get("direction"),
                             call.get("duration"), m["id"],
                             f"https://services.leadconnectorhq.com/conversations/messages/{m['id']}/locations/{LOC}/recording"])
    if first_human:
        n_triaged += 1
        for t, d, h in sorted(events):
            if t > first_human and d == "inbound":
                engaged = True; break
        if engaged: n_engaged += 1
    ap = appts.get(cid, [])
    booked_at = min((ts(e.get("dateAdded")) for e in ap if ts(e.get("dateAdded"))), default=None)
    slot = min((ts(e.get("startTime")) for e in ap if ts(e.get("startTime"))), default=None)
    before = bool(first_human and slot and first_human < slot)
    if before: n_before += 1
    hours = round((first_human - booked_at).total_seconds() / 3600, 1) if (first_human and booked_at and first_human >= booked_at) else None
    rows.append([cid, nm, "yes" if first_human else "no",
                 str(first_human)[:16] if first_human else "", first_human_kind,
                 "yes" if engaged else "no",
                 str(booked_at)[:16] if booked_at else "", str(slot)[:16] if slot else "",
                 "yes" if before else ("no" if slot else ""), hours])

with open(D / f"triage_derived_{DATE}.csv", "w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f)
    w.writerow(["contactId", "contact", "human_touch(DERIVED)", "first_human_touch_utc", "kind",
                "contact_engaged_back", "booked_at", "first_slot", "triaged_before_slot", "booking_to_touch_hrs"])
    w.writerows(rows)
with open(D / f"recordings_{DATE}.csv", "w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f)
    w.writerow(["contactId", "contact", "call_time_utc", "direction", "duration_s", "messageId", "recording_api_url(auth req)"])
    w.writerows(recs)

canon_path = REPO / "ops" / "data" / "CANON_NUMBERS.json"
canon = json.loads(canon_path.read_text(encoding="utf-8"))
canon["triage_DERIVED"] = {
    "method": "human touch = source=='app' outbound OR connected call >30s; DERIVED from raw messages, not Notion tags",
    "contacts_with_human_touch": n_triaged,
    "contacts_engaged_back": n_engaged,
    "bookers_touched_before_first_slot": n_before,
    "evidence": f"ops/archive/ghl/{DATE}/triage_derived_{DATE}.csv",
}
canon["recordings"] = {"call_recordings_found": len(recs),
                       "evidence": f"ops/archive/ghl/{DATE}/recordings_{DATE}.csv (links only, auth required)"}
canon_path.write_text(json.dumps(canon, indent=1), encoding="utf-8")
print(f"triaged(derived): {n_triaged}/{len(contacts)} · engaged back: {n_engaged} · touched-before-slot: {n_before} · recordings: {len(recs)}")
