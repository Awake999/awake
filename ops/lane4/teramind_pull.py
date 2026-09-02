#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""LANE 4 — Teramind true-log pull. Same pattern as ghl_pull_details.py:
the private key lives ONLY in the local .env, never in this repo.

    python3 ops/lane4/teramind_pull.py --discover        # find the working API path
    python3 ops/lane4/teramind_pull.py                   # pull yesterday
    python3 ops/lane4/teramind_pull.py 2026-09-01        # pull a specific day

Writes ops/archive/teramind/<DATE>/raw/*.json + a flat activity CSV.

⚠️ HONEST NOTE: Teramind's REST base path differs by deployment/version. This
script does NOT assume one — --discover probes the documented candidates and
reports which answers, then you set TERAMIND_API_BASE in .env. Nothing here
fabricates an endpoint.
"""
import json, sys, os, time, csv, urllib.request, urllib.error, datetime, pathlib

REPO = pathlib.Path(__file__).resolve().parent.parent.parent
ENVP = REPO.parent / "apw-intel" / ".env"
ENV = {}
if ENVP.exists():
    ENV = dict(l.split("=", 1) for l in ENVP.read_text().splitlines() if "=" in l and not l.startswith("#"))

INSTANCE = ENV.get("TERAMIND_INSTANCE", "ascendprimew.us.teramind.co").strip()
KEY = ENV.get("TERAMIND_API_KEY", "").strip()
BASE = ENV.get("TERAMIND_API_BASE", "").strip()

CANDIDATES = ["/api/v1", "/rest/v1", "/api", "/bi/api/v1"]

def call(path, params=None):
    url = f"https://{INSTANCE}{path}"
    if params:
        url += "?" + "&".join(f"{k}={v}" for k, v in params.items())
    req = urllib.request.Request(url, headers={
        "Authorization": f"Bearer {KEY}",
        "Accept": "application/json",
        "User-Agent": "APW-ops/1.0"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.status, r.read().decode()

def discover():
    if not KEY:
        print("✗ TERAMIND_API_KEY missing from", ENVP)
        print("  Add it (Teramind → Settings → API / Access tokens), then re-run.")
        return 1
    print(f"Probing https://{INSTANCE} …\n")
    for c in CANDIDATES:
        for probe in ("/users", "/employees", "/agents"):
            try:
                status, body = call(c + probe)
                print(f"  ✓ {c+probe} → HTTP {status}  ({body[:80]!r})")
                print(f"\nSet in {ENVP}:  TERAMIND_API_BASE={c}")
                return 0
            except urllib.error.HTTPError as e:
                print(f"  · {c+probe} → HTTP {e.code}")
            except Exception as e:
                print(f"  · {c+probe} → {type(e).__name__}")
    print("\n✗ No candidate answered. Open the Teramind API docs for your version")
    print("  (Settings → API, or <instance>/api/docs) and set TERAMIND_API_BASE by hand.")
    return 1

def pull(date):
    if not KEY or not BASE:
        print("✗ Need TERAMIND_API_KEY and TERAMIND_API_BASE in", ENVP)
        print("  Run with --discover first.")
        return 1
    out = REPO / "ops" / "archive" / "teramind" / date
    (out / "raw").mkdir(parents=True, exist_ok=True)
    got = {}
    # endpoint name varies by version; try each and keep whatever answers
    for name, path, params in [
        ("users",    "/users",              None),
        ("activity", "/reports/activity",   {"from": date, "to": date}),
        ("timeline", "/reports/timeline",   {"from": date, "to": date, "interval": "10m"}),
        ("apps",     "/reports/applications", {"from": date, "to": date}),
    ]:
        try:
            status, body = call(BASE + path, params)
            (out / "raw" / f"{name}.json").write_text(body, encoding="utf-8")
            got[name] = len(body)
            print(f"  ✓ {name}: {len(body)} bytes")
        except urllib.error.HTTPError as e:
            print(f"  · {name}: HTTP {e.code} (endpoint may not exist on this version)")
        except Exception as e:
            print(f"  · {name}: {type(e).__name__}")
        time.sleep(1)
    if not got:
        print("✗ Nothing returned — check the key's permissions.")
        return 1
    # flatten whatever timeline/activity we got into one CSV for the ops pipeline
    src = out / "raw" / "timeline.json"
    if not src.exists():
        src = out / "raw" / "activity.json"
    if src.exists():
        try:
            data = json.loads(src.read_text())
            rows = data if isinstance(data, list) else (data.get("data") or data.get("results") or [])
            if rows and isinstance(rows[0], dict):
                with open(out / f"activity_{date}.csv", "w", newline="", encoding="utf-8") as f:
                    w = csv.DictWriter(f, fieldnames=sorted({k for r in rows for k in r}))
                    w.writeheader()
                    w.writerows(rows)
                print(f"  ✓ CSV: {len(rows)} rows → {out}/activity_{date}.csv")
        except Exception as e:
            print(f"  · CSV flatten skipped ({type(e).__name__}) — raw JSON is still saved")
    print(f"\nDone. Commit with:\n  git add ops/archive/teramind && git commit -m 'Teramind pull {date}' && git push")
    return 0

if __name__ == "__main__":
    args = [a for a in sys.argv[1:]]
    if "--discover" in args:
        sys.exit(discover())
    date = next((a for a in args if a[:2] == "20"), None) or \
           (datetime.date.today() - datetime.timedelta(days=1)).isoformat()
    print(f"Teramind pull for {date}")
    sys.exit(pull(date))
