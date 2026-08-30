"""LANE 4 — GHL FULL PULL (read-only). Stdlib-only.
Pulls: all contacts (w/ attribution + custom fields), per-contact appointments
with statuses, pipelines + opportunities, payments (orders/transactions/
subscriptions/invoices), conversations metadata + first-message timestamps
(speed-to-lead). Writes JSON to ops/archive/ghl/<date>/raw/ .
Token read from apw-intel/.env on this machine (never committed).
"""
import json, sys, time, urllib.request, urllib.parse, urllib.error, datetime, pathlib

HERE = pathlib.Path(__file__).resolve()
REPO = HERE.parent.parent.parent  # awake/
ENVF = REPO.parent / "apw-intel" / ".env"
ENV = {}
for line in ENVF.read_text().splitlines():
    if "=" in line and not line.startswith("#"):
        k, v = line.split("=", 1); ENV[k.strip()] = v.strip()
TOKEN, LOC = ENV["GHL_TOKEN"], ENV["GHL_LOCATION"]
BASE = "https://services.leadconnectorhq.com"
DATE = sys.argv[1] if len(sys.argv) > 1 else datetime.date.today().isoformat()
RAW = REPO / "ops" / "archive" / "ghl" / DATE / "raw"
RAW.mkdir(parents=True, exist_ok=True)

def api(path, params=None, version="2021-07-28"):
    url = BASE + path + ("?" + urllib.parse.urlencode(params, doseq=True) if params else "")
    req = urllib.request.Request(url, headers={
        "Authorization": f"Bearer {TOKEN}", "Version": version, "Accept": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"})
    for attempt in range(6):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.loads(r.read().decode())
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503, 504):
                time.sleep(2 ** attempt); continue
            return {"_error": e.code, "_body": e.read().decode()[:300], "_url": url}
        except Exception:
            time.sleep(2 ** attempt)
    return {"_error": "retries_exhausted", "_url": url}

def save(name, obj):
    (RAW / f"{name}.json").write_text(json.dumps(obj, indent=1, default=str), encoding="utf-8")
    n = len(obj) if isinstance(obj, (list, dict)) else "?"
    print(f"saved {name}: {n}", flush=True)

# ---- contacts (all, paginated) ----
contacts, params = [], {"locationId": LOC, "limit": 100}
while True:
    r = api("/contacts/", params)
    if "_error" in r: print("contacts error", r); break
    batch = r.get("contacts", [])
    contacts += batch
    meta = r.get("meta", {})
    if not batch or not meta.get("startAfterId"): break
    params.update({"startAfterId": meta["startAfterId"], "startAfter": meta["startAfter"]})
    time.sleep(0.12)
save("contacts", contacts)

# ---- reference data ----
save("users", api("/users/", {"locationId": LOC}))
save("calendars", api("/calendars/", {"locationId": LOC}, version="2021-04-15"))
save("tags", api(f"/locations/{LOC}/tags"))
save("custom_fields", api(f"/locations/{LOC}/customFields"))
save("pipelines", api("/opportunities/pipelines", {"locationId": LOC}))

# ---- opportunities (paginated search) ----
opps, page = [], 1
while True:
    r = api("/opportunities/search", {"location_id": LOC, "limit": 100, "page": page})
    if "_error" in r: print("opps error", r); break
    batch = r.get("opportunities", [])
    opps += batch
    if not batch or len(batch) < 100: break
    page += 1; time.sleep(0.12)
save("opportunities", opps)

# ---- payments ----
save("payment_orders", api("/payments/orders", {"altId": LOC, "altType": "location", "limit": 100}))
save("payment_transactions", api("/payments/transactions", {"altId": LOC, "altType": "location", "limit": 100}))
save("payment_subscriptions", api("/payments/subscriptions", {"altId": LOC, "altType": "location", "limit": 100}))
save("invoices", api("/invoices/", {"altId": LOC, "altType": "location", "limit": 100, "offset": 0}))

# ---- per-contact appointments + conversations (metadata + messages for speed-to-lead) ----
appts, convs, msgs = {}, {}, {}
for i, c in enumerate(contacts):
    cid = c["id"]
    a = api(f"/contacts/{cid}/appointments")
    if a.get("events"): appts[cid] = a["events"]
    cv = api("/conversations/search", {"locationId": LOC, "contactId": cid}, version="2021-04-15")
    for conv in cv.get("conversations", []):
        convs[conv["id"]] = conv
        allm, last = [], None
        while True:
            p = {"limit": 100}
            if last: p["lastMessageId"] = last
            m = api(f"/conversations/{conv['id']}/messages", p, version="2021-04-15")
            mm = m.get("messages", {})
            batch = mm.get("messages", []) if isinstance(mm, dict) else []
            allm += batch
            if not (isinstance(mm, dict) and mm.get("nextPage")) or not batch: break
            last = mm.get("lastMessageId") or batch[-1]["id"]
            time.sleep(0.1)
        msgs[conv["id"]] = allm
    if i % 25 == 0: print(f"  contact {i}/{len(contacts)}", flush=True)
    time.sleep(0.1)
save("appointments_by_contact", appts)
save("conversations", convs)
save("messages_by_conversation", msgs)
print("DONE", RAW, flush=True)
