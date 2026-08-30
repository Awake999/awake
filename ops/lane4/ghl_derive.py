# -*- coding: utf-8 -*-
"""LANE 4 — derive dated CSV + markdown deliverables from the raw GHL pull.
Outputs into ops/archive/ghl/<date>/ :
  contacts_<date>.csv        (id, name, email, phone, source, UTMs, created, tags, dnd)
  appointments_<date>.csv    (contact, calendar, created/booked-at, slot, status)
  opportunities_<date>.csv   (pipeline, stage, status, timestamps)
  speed_to_lead_<date>.csv   (contact created -> first outbound message/call)
  conversations_meta_<date>.csv
  GHL_PULL_SUMMARY.md
"""
import json, csv, sys, datetime, pathlib, urllib.parse
from collections import Counter

DATE = sys.argv[1] if len(sys.argv) > 1 else datetime.date.today().isoformat()
REPO = pathlib.Path(__file__).resolve().parent.parent.parent
D = REPO / "ops" / "archive" / "ghl" / DATE
RAW = D / "raw"
J = lambda n: json.load(open(RAW / f"{n}.json", encoding="utf-8"))

contacts = J("contacts")
appts = J("appointments_by_contact")
convs = J("conversations")
msgs = J("messages_by_conversation")
opps = J("opportunities")
pipes = {p["id"]: p for p in J("pipelines")["pipelines"]}
cals = {c["id"]: c.get("name", "?") for c in J("calendars").get("calendars", [])}
cf = {f["id"]: f.get("fieldKey", f.get("name", "?")) for f in J("custom_fields").get("customFields", [])}

cby = {c["id"]: c for c in contacts}
try:
    details = J("contact_details")
except FileNotFoundError:
    details = {}

def attribution(c):
    """UTMs live on the contact DETAIL record's attributionSource; campaign_id/
    adset_id/ad_id are canonical in the attribution URL's query string."""
    d = details.get(c["id"], c)
    out = {}
    for src in (d.get("attributionSource") or {}, d.get("lastAttributionSource") or {}):
        for k in ["utmSource", "utmMedium", "campaign", "utmTerm", "utmContent",
                  "campaignId", "adId", "sessionSource", "medium", "url", "referrer"]:
            v = src.get(k)
            if v and k not in out: out[k] = v
    url = out.get("url")
    if url and "?" in url:
        q = urllib.parse.parse_qs(url.split("?", 1)[1])
        for uk in ["utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content",
                   "campaign_id", "adset_id", "ad_id"]:
            if q.get(uk): out.setdefault(uk, q[uk][0])
    return out

# ---- contacts CSV ----
with open(D / f"contacts_{DATE}.csv", "w", newline="", encoding="utf-8-sig") as fh:
    w = csv.writer(fh)
    w.writerow(["id", "first", "last", "email", "phone", "source", "type", "dateAdded", "tags", "dnd",
                "utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content",
                "campaign_id", "adset_id", "ad_id", "sessionSource", "referrer"])
    for c in contacts:
        a = attribution(c)
        w.writerow([c["id"], c.get("firstNameRaw") or c.get("firstName"), c.get("lastNameRaw") or c.get("lastName"),
                    c.get("email"), c.get("phone"), c.get("source"), c.get("type"), c.get("dateAdded"),
                    "|".join(c.get("tags") or []), c.get("dnd"),
                    a.get("utm_source") or a.get("utmSource"), a.get("utm_medium") or a.get("utmMedium"),
                    a.get("utm_campaign") or a.get("campaign"), a.get("utm_term") or a.get("utmTerm"),
                    a.get("utm_content") or a.get("utmContent"),
                    a.get("campaign_id") or a.get("campaignId"), a.get("adset_id"),
                    a.get("ad_id") or a.get("adId"), a.get("sessionSource"), a.get("referrer")])

# ---- appointments CSV ----
rows, status_ct = [], Counter()
for cid, evs in appts.items():
    c = cby.get(cid, {})
    nm = f'{c.get("firstNameRaw") or c.get("firstName") or ""} {c.get("lastNameRaw") or c.get("lastName") or ""}'.strip()
    for e in evs:
        st = e.get("appointmentStatus") or e.get("status") or "?"
        status_ct[st] += 1
        rows.append([cid, nm, c.get("email"), cals.get(e.get("calendarId"), e.get("calendarId")),
                     e.get("dateAdded") or e.get("createdAt"), e.get("startTime"), e.get("endTime"), st,
                     e.get("title"), e.get("id")])
rows.sort(key=lambda r: str(r[5]))
with open(D / f"appointments_{DATE}.csv", "w", newline="", encoding="utf-8-sig") as fh:
    w = csv.writer(fh)
    w.writerow(["contactId", "contact", "email", "calendar", "bookedAt", "slotStart", "slotEnd", "status", "title", "apptId"])
    w.writerows(rows)

# ---- opportunities CSV ----
with open(D / f"opportunities_{DATE}.csv", "w", newline="", encoding="utf-8-sig") as fh:
    w = csv.writer(fh)
    w.writerow(["oppId", "name", "contactId", "pipeline", "stage", "status", "monetaryValue",
                "source", "createdAt", "lastStageChangeAt", "lastStatusChangeAt", "updatedAt"])
    for o in opps:
        p = pipes.get(o.get("pipelineId"), {})
        stage = next((s["name"] for s in p.get("stages", []) if s["id"] == o.get("pipelineStageId")), o.get("pipelineStageId"))
        w.writerow([o["id"], o.get("name"), o.get("contactId"), p.get("name"), stage, o.get("status"),
                    o.get("monetaryValue"), o.get("source"), o.get("createdAt"),
                    o.get("lastStageChangeAt"), o.get("lastStatusChangeAt"), o.get("updatedAt")])

# ---- conversations metadata + speed-to-lead ----
conv_by_contact = {}
for cvid, cv in convs.items():
    conv_by_contact.setdefault(cv.get("contactId"), []).append(cvid)

def ms(t):
    if t is None: return None
    if isinstance(t, (int, float)): return t
    try: return datetime.datetime.fromisoformat(str(t).replace("Z", "+00:00")).timestamp() * 1000
    except Exception: return None

with open(D / f"conversations_meta_{DATE}.csv", "w", newline="", encoding="utf-8-sig") as fh:
    w = csv.writer(fh)
    w.writerow(["conversationId", "contactId", "contact", "type", "lastMessageDate", "messageCount",
                "channels", "callRecordingMsgIds"])
    for cvid, cv in convs.items():
        mm = msgs.get(cvid, [])
        chans = Counter(m.get("messageType") or m.get("type") for m in mm)
        recs = [m["id"] for m in mm if (m.get("messageType") in ("TYPE_CALL", "CALL") or m.get("type") == 1) and (m.get("attachments") or m.get("meta", {}).get("call"))]
        c = cby.get(cv.get("contactId"), {})
        nm = f'{c.get("firstNameRaw") or ""} {c.get("lastNameRaw") or ""}'.strip()
        w.writerow([cvid, cv.get("contactId"), nm, cv.get("type"), cv.get("lastMessageDate"),
                    len(mm), "|".join(f"{k}:{v}" for k, v in chans.items()), "|".join(recs)])

with open(D / f"speed_to_lead_{DATE}.csv", "w", newline="", encoding="utf-8-sig") as fh:
    w = csv.writer(fh)
    w.writerow(["contactId", "contact", "createdAt", "firstOutboundAt", "firstOutboundType", "minutesToFirstTouch"])
    for c in contacts:
        cid = c["id"]
        created = ms(c.get("dateAdded"))
        first, ftype = None, None
        for cvid in conv_by_contact.get(cid, []):
            for m in msgs.get(cvid, []):
                if (m.get("direction") or "").lower() != "outbound": continue
                t = ms(m.get("dateAdded"))
                if t and (first is None or t < first):
                    first, ftype = t, m.get("messageType") or m.get("type")
        mins = round((first - created) / 60000, 1) if (first and created and first >= created) else None
        w.writerow([cid, f'{c.get("firstNameRaw") or ""} {c.get("lastNameRaw") or ""}'.strip(),
                    c.get("dateAdded"), datetime.datetime.utcfromtimestamp(first/1000).isoformat()+"Z" if first else None,
                    ftype, mins])

# ---- summary ----
attr_n = sum(1 for c in contacts if attribution(c))
utm_n = sum(1 for c in contacts if attribution(c).get("utm_source") or attribution(c).get("utmSource"))
opp_status = Counter(o.get("status") for o in opps)
summary = f"""# GHL Full Pull — {DATE} (Lane 4, read-only)

Location `WFkoNzKa9J9PxhngsLfl` (Prismatic). Raw JSON in `raw/`, derived CSVs alongside this file.

| What | Count |
|---|---|
| Contacts | {len(contacts)} |
| ...with any attribution data | {attr_n} |
| ...with a utm_source | {utm_n} |
| Contacts with appointments | {len(appts)} |
| Appointment events | {sum(len(v) for v in appts.values())} |
| Appointment statuses | {dict(status_ct)} |
| Opportunities | {len(opps)} ({dict(opp_status)}) |
| Conversations | {len(convs)} |
| Messages | {sum(len(v) for v in msgs.values())} |
| Payment orders / transactions / subscriptions / invoices | 0 / 0 / 0 / 0 — GHL Payments is EMPTY; money moves outside GHL |

Statuses come from GHL `appointmentStatus` per event (confirmed / showed / noshow / cancelled / invalid).
"""
(D / "GHL_PULL_SUMMARY.md").write_text(summary, encoding="utf-8")
print(summary)
