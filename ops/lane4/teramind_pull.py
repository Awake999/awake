#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Teramind true-log pull — REAL endpoints, from Teramind's published Postman collection
(archived at ops/archive/teramind/api/postman_collection_TW74jRAB.json, 239 endpoints).

    python3 ops/lane4/teramind_pull.py --check              # validate token (GET /tm-api/time)
    python3 ops/lane4/teramind_pull.py                      # pull yesterday
    python3 ops/lane4/teramind_pull.py 2026-09-02           # pull a specific day
    python3 ops/lane4/teramind_pull.py 2026-08-19 2026-08-21   # a range (inclusive)

WHERE THE TOKEN COMES FROM (KB 8817613 — it is NOT under Settings):
    Teramind dashboard → click your USERNAME (top-right) → Access Tokens → ADD ACCESS TOKEN
    Put it in ~/apw-intel/.env as  TERAMIND_API_KEY=...   (or export TERAMIND_API_KEY=... in the shell)

AUTH:  header  x-access-token: <token>      BASE:  https://<instance>/tm-api

WHAT IT PULLS PER DAY (all written under ops/archive/teramind/<DATE>/raw/ + one flat CSV
into ops/archive/teramind/inbox/ so `python3 ops/tools/teramind_daily.py --date <DATE>` runs on it):
    agents.json      GET  /tm-api/v1/agents                          — roster with agent_id → name/email
    alerts.json      GET  /tm-api/v1/alerts?periodStart&periodEnd    — every alert, with rule + URL
    webapps.json     POST /tm-api/report/web-pages-applications/grid — the Web & Applications report
    sessions.json    POST /tm-api/report/sessions/grid               — login sessions
    activity.json    POST /tm-api/wip/tma-query  cube=activity        — THE minute-level record:
                     dims date·agent·computer·title·url, measures count·time_s·idle_time_s
"""
import json, sys, os, csv, urllib.request, urllib.error, datetime, pathlib, time

REPO = pathlib.Path(__file__).resolve().parents[2]
ENVP = pathlib.Path.home() / "apw-intel" / ".env"
ENV = {}
if ENVP.exists():
    ENV = dict(l.split("=", 1) for l in ENVP.read_text().splitlines() if "=" in l and not l.startswith("#"))
INSTANCE = (os.environ.get("TERAMIND_INSTANCE") or ENV.get("TERAMIND_INSTANCE") or "ascendprimew.us.teramind.co").strip()
KEY = (os.environ.get("TERAMIND_API_KEY") or ENV.get("TERAMIND_API_KEY") or "").strip()
TZ = "America/Los_Angeles"
INBOX = REPO / "ops/archive/teramind/inbox"

def call(method, path, body=None, params=None):
    url = f"https://{INSTANCE}/tm-api{path}"
    if params:
        url += "?" + "&".join(f"{k}={v}" for k, v in params.items())
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, method=method, headers={
        "x-access-token": KEY, "Accept": "application/json",
        "Content-Type": "application/json", "User-Agent": "APW-ops/2.0"})
    with urllib.request.urlopen(req, timeout=120) as r:
        raw = r.read().decode()
        try: return r.status, json.loads(raw)
        except json.JSONDecodeError: return r.status, raw

def need_key():
    if not KEY:
        print(f"✗ TERAMIND_API_KEY missing (looked in env and {ENVP}).")
        print("  Create one: Teramind → click your USERNAME (top-right) → Access Tokens → ADD ACCESS TOKEN.")
        sys.exit(1)

def check():
    need_key()
    try:
        s, t = call("GET", "/time")
        print(f"✓ token works — HTTP {s}, server time: {t}")
        s, agents = call("GET", "/v1/agents")
        print(f"✓ {len(agents)} agents visible:")
        for a in agents: print(f"   {a.get('agent_id'):>5}  {a.get('name')}  <{a.get('email_address','')}>  {'online' if a.get('online') else ''}")
        return 0
    except urllib.error.HTTPError as e:
        print(f"✗ HTTP {e.code} on {e.url}\n  {e.read().decode()[:300]}"); return 1

def day_bounds(d):
    """epoch seconds for local-midnight → next-midnight in TZ (Teramind wants epoch strings)."""
    try:
        from zoneinfo import ZoneInfo
        tz = ZoneInfo(TZ)
        a = datetime.datetime.combine(d, datetime.time(0, 0), tzinfo=tz)
    except Exception:
        a = datetime.datetime.combine(d, datetime.time(0, 0))
    b = a + datetime.timedelta(days=1)
    return int(a.timestamp()), int(b.timestamp()), a, b

def pull(d):
    need_key()
    ps, pe, a, b = day_bounds(d)
    out = REPO / "ops/archive/teramind" / d.isoformat() / "raw"
    out.mkdir(parents=True, exist_ok=True)
    def save(name, obj):
        (out / name).write_text(json.dumps(obj, indent=1, ensure_ascii=False), encoding="utf-8")
        n = len(obj) if isinstance(obj, list) else (len(obj.get("data", obj.get("rows", []))) if isinstance(obj, dict) else "?")
        print(f"  ✓ {name}  ({n} records)")
        return obj

    print(f"── {d}  [{a:%Y-%m-%d %H:%M %Z} → {b:%H:%M}]  epoch {ps}–{pe}")
    agents = save("agents.json", call("GET", "/v1/agents")[1])
    save("alerts.json", call("GET", "/v1/alerts", params={
        "periodStart": a.astimezone(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "periodEnd":   b.astimezone(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")})[1])
    save("webapps.json", call("POST", "/report/web-pages-applications/grid",
                              {"periodStart": str(ps), "periodEnd": str(pe)})[1])
    save("sessions.json", call("POST", "/report/sessions/grid",
                               {"periodStart": str(ps), "periodEnd": str(pe)})[1])
    # THE minute-level record — page through it
    rows, offset, limit = [], 0, 1000
    while True:
        s, page = call("POST", "/wip/tma-query", {
            "cube": "activity", "timezone": TZ, "aggregate": True,
            "dims": ["date", "agent", "computer", "browser", "title", "url"],
            "measures": ["count", "time_s", "idle_time_s"],
            "dim_filters": {"date": {"range": [d.isoformat(), d.isoformat()]}},
            "data_filters": {}, "offset": offset, "limit": limit, "order": []})
        chunk = page.get("data") if isinstance(page, dict) else page
        if not chunk: break
        rows += chunk; offset += limit
        if len(chunk) < limit: break
    save("activity.json", rows)

    # flat CSV for teramind_daily.py (column names it already understands)
    byid = {str(x.get("agent_id")): x for x in agents} if isinstance(agents, list) else {}
    INBOX.mkdir(parents=True, exist_ok=True)
    csvp = INBOX / f"teramind_activity_{d.isoformat()}.csv"
    with open(csvp, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f); w.writerow(["Time", "User", "Computer", "Application", "Website", "Window Title", "Duration", "Idle", "Session"])
        for r in rows:
            g = lambda k: r.get(k, r.get(k.upper(), ""))
            ag = g("agent"); name = ag.get("name") if isinstance(ag, dict) else byid.get(str(ag), {}).get("name", ag)
            w.writerow([g("date"), name, g("computer"), g("browser"), g("url"), g("title"),
                        g("time_s"), g("idle_time_s"), ""])
    print(f"  ✓ {csvp.relative_to(REPO)}  → now run: python3 ops/tools/teramind_daily.py --date {d}")
    return 0

def main():
    a = sys.argv[1:]
    if "--check" in a: return check()
    ds = [x for x in a if not x.startswith("--")]
    if not ds:
        days = [datetime.date.today() - datetime.timedelta(days=1)]
    elif len(ds) == 1:
        days = [datetime.date.fromisoformat(ds[0])]
    else:
        s, e = (datetime.date.fromisoformat(x) for x in ds[:2])
        days = [s + datetime.timedelta(days=i) for i in range((e - s).days + 1)]
    for d in days:
        try: pull(d)
        except urllib.error.HTTPError as ex:
            print(f"  ✗ HTTP {ex.code} {ex.url}\n    {ex.read().decode()[:300]}"); return 1
    return 0

if __name__ == "__main__":
    sys.exit(main())
