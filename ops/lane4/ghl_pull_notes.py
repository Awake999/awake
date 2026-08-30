# -*- coding: utf-8 -*-
"""LANE 4 — pull per-contact NOTES (read-only) -> raw/notes_by_contact.json"""
import json, sys, time, urllib.request, urllib.error, datetime, pathlib

REPO = pathlib.Path(__file__).resolve().parent.parent.parent
ENV = dict(l.split("=", 1) for l in (REPO.parent / "apw-intel" / ".env").read_text().splitlines() if "=" in l and not l.startswith("#"))
TOKEN = ENV["GHL_TOKEN"].strip()
DATE = sys.argv[1] if len(sys.argv) > 1 else datetime.date.today().isoformat()
RAW = REPO / "ops" / "archive" / "ghl" / DATE / "raw"

def api(path):
    req = urllib.request.Request("https://services.leadconnectorhq.com" + path, headers={
        "Authorization": f"Bearer {TOKEN}", "Version": "2021-07-28", "Accept": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"})
    for attempt in range(6):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.loads(r.read().decode())
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503, 504):
                time.sleep(2 ** attempt); continue
            return {"_error": e.code}
        except Exception:
            time.sleep(2 ** attempt)
    return {"_error": "retries_exhausted"}

contacts = json.load(open(RAW / "contacts.json", encoding="utf-8"))
notes = {}
for i, c in enumerate(contacts):
    r = api(f"/contacts/{c['id']}/notes")
    if r.get("notes"):
        notes[c["id"]] = r["notes"]
    if i % 50 == 0: print(f"  notes {i}/{len(contacts)}", flush=True)
    time.sleep(0.1)
(RAW / "notes_by_contact.json").write_text(json.dumps(notes, indent=1, default=str), encoding="utf-8")
print("DONE notes:", len(notes), "contacts with notes")
