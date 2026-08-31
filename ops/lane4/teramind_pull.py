# -*- coding: utf-8 -*-
"""LANE 4 — Teramind puller. Logs into the instance API with the dashboard
credentials from apw-intel/.env (TERAMIND_USER / TERAMIND_PASS — use a
read-only dashboard user), then pulls employee/agent/activity data.
First run is DISCOVERY MODE: it probes the known endpoint families, records
which respond, and writes raw JSON per the raw-originals law.
Output: ops/archive/teramind/<date>/raw/*.json + TERAMIND_PULL_SUMMARY.md
"""
import json, sys, datetime, pathlib, urllib.request, urllib.error

REPO = pathlib.Path(__file__).resolve().parent.parent.parent
ENV = dict(l.split("=", 1) for l in (REPO.parent / "apw-intel" / ".env").read_text().splitlines()
           if "=" in l and not l.startswith("#"))
USER = ENV.get("TERAMIND_USER", "").strip()
PASS = ENV.get("TERAMIND_PASS", "").strip()
if not USER or not PASS:
    sys.exit("Add TERAMIND_USER=... and TERAMIND_PASS=... to apw-intel/.env (read-only dashboard user), then rerun.")

BASE = "https://ascendprimew.us.teramind.co"
DATE = sys.argv[1] if len(sys.argv) > 1 else datetime.date.today().isoformat()
OUT = REPO / "ops" / "archive" / "teramind" / DATE / "raw"
OUT.mkdir(parents=True, exist_ok=True)

def req(path, method="GET", body=None, token=None):
    url = BASE + path
    data = json.dumps(body).encode() if body is not None else None
    h = {"Accept": "application/json", "Content-Type": "application/json",
         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    if token: h["Authorization"] = "Bearer " + token
    r = urllib.request.Request(url, data=data, method=method, headers=h)
    try:
        with urllib.request.urlopen(r, timeout=60) as resp:
            return resp.status, json.loads(resp.read().decode() or "{}")
    except urllib.error.HTTPError as e:
        return e.code, {"_body": e.read().decode()[:300]}
    except Exception as ex:
        return 0, {"_err": str(ex)[:200]}

# ---- login: Teramind cloud accepts dashboard creds on the tm-api login route ----
token = None
for login_path in ("/tm-api/v1/login", "/tm-api/login", "/api/v1/login"):
    st, resp = req(login_path, "POST", {"email": USER, "password": PASS})
    if st == 200 and isinstance(resp, dict):
        token = resp.get("token") or resp.get("access_token") or (resp.get("data") or {}).get("token")
        if token:
            print("login OK via", login_path); break
    print("login probe", login_path, "->", st)
if not token:
    sys.exit("Login failed on all known routes — check creds; if 2FA is on for this user, create a read-only user without 2FA for the API.")

# ---- discovery probe: known endpoint families (all read-only GETs) ----
PROBES = {
    "employees": "/tm-api/v1/employees",
    "agents": "/tm-api/v1/agents",
    "departments": "/tm-api/v1/departments",
    "computers": "/tm-api/v1/computers",
    "activity_worktime": "/tm-api/v1/reports/worktime?from=%sT00:00:00&to=%sT23:59:59" % (DATE, DATE),
    "activity_webpages": "/tm-api/v1/reports/webpages?from=%sT00:00:00&to=%sT23:59:59" % (DATE, DATE),
    "activity_applications": "/tm-api/v1/reports/applications?from=%sT00:00:00&to=%sT23:59:59" % (DATE, DATE),
    "alerts": "/tm-api/v1/alerts?from=%sT00:00:00&to=%sT23:59:59" % (DATE, DATE),
}
summary = []
for name, path in PROBES.items():
    st, resp = req(path, token=token)
    ok = st == 200
    if ok:
        (OUT / f"{name}.json").write_text(json.dumps(resp, indent=1, default=str), encoding="utf-8")
    n = len(resp) if isinstance(resp, list) else (len(resp.get("data", [])) if isinstance(resp, dict) else 0)
    summary.append((name, st, n if ok else 0))
    print(f"{name}: HTTP {st}" + (f" ({n} items) saved" if ok else ""))

md = ["# Teramind pull — %s (LANE 4, read-only)" % DATE, "",
      "| Endpoint | HTTP | Items |", "|---|---|---|"]
md += ["| %s | %s | %s |" % s for s in summary]
md += ["", "Raw JSON in `raw/`. Non-200 rows = endpoint not on this plan/version — adjust PROBES from Teramind's API docs for this instance release."]
(OUT.parent / "TERAMIND_PULL_SUMMARY.md").write_text("\n".join(md), encoding="utf-8")
print("->", OUT.parent)
