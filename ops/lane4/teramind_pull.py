#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Teramind true-log pull — REAL endpoints, from Teramind's published Postman collection
(archived at ops/archive/teramind/api/postman_collection_TW74jRAB.json, 239 endpoints).

    python3 ops/lane4/teramind_pull.py --check              # validate token (GET /tm-api/time)
    python3 ops/lane4/teramind_pull.py --all 2026-07-15     # FULL EXPORT before cancellation: every table, every day → ops/archive/teramind/export/
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

# ---------------------------------------------------------------------------
# --all START [END] : full account export (register #174 — "download all data
# from teramind right now before i cancel my subscription"). Everything the
# tm-api exposes as JSON, one file per table per day, plus the one-time tables.
# Video: requests server-side exports per computer per day (player/export-video)
# and records the job ids; download is a second pass once Teramind renders them.
# ---------------------------------------------------------------------------
ONE_TIME = [
    ("GET",  "/v1/agents",            None),
    ("GET",  "/v1/computers",         None),
    ("GET",  "/v1/departments",       None),
    ("GET",  "/behavior-policy",      None),
    ("GET",  "/behavior-group",       None),
    ("GET",  "/monitoring-profiles",  None),
    ("GET",  "/v1/rules",             None),
    ("GET",  "/schedules",            None),
    ("GET",  "/time",                 None),
]
DAILY_GRIDS = [
    "/report/web-pages-applications/grid", "/report/sessions/grid", "/report/keystrokes/grid",
    "/report/file-transfers/grid", "/report/printing/grid", "/report/audit/grid",
    "/report/emails/grid", "/report/im/grid", "/report/social-media/grid", "/report/searches/grid",
    "/report/clipboard/grid", "/report/network/grid", "/report/ocr/grid", "/report/login-sessions/grid",
    "/tt/r/time-records/grid", "/tt/r/time-records-by-day/grid",
]
CUBES = ["activity", "alerts", "web", "apps", "emails", "keystrokes", "files", "sessions", "productivity"]

def _safe(fn, *a, **k):
    try: return fn(*a, **k)
    except urllib.error.HTTPError as e:
        return e.code, {"_error": e.code, "_body": e.read().decode(errors="replace")[:500]}
    except Exception as e:
        return 0, {"_error": str(e)}

def export_all(start, end=None):
    need_key()
    end = end or datetime.date.today()
    root = REPO / "ops/archive/teramind/export"
    (root / "meta").mkdir(parents=True, exist_ok=True)
    log = open(root / "EXPORT_LOG.txt", "a", encoding="utf-8")
    def L(msg): print(msg); log.write(f"{datetime.datetime.utcnow():%Y-%m-%dT%H:%MZ} {msg}\n"); log.flush()
    L(f"== FULL EXPORT {start} → {end} on {INSTANCE}")
    # 1. one-time tables
    for m, path, body in ONE_TIME:
        s, obj = _safe(call, m, path, body)
        name = path.strip("/").replace("/", "_") + ".json"
        (root / "meta" / name).write_text(json.dumps(obj, indent=1, ensure_ascii=False), encoding="utf-8")
        L(f"  meta {name:40} HTTP {s} {'ERR' if isinstance(obj, dict) and obj.get('_error') else 'ok'}")
    agents = json.loads((root / "meta" / "v1_agents.json").read_text())
    computers = json.loads((root / "meta" / "v1_computers.json").read_text())
    # 2. per-day tables
    d = start
    while d <= end:
        ps, pe, a, b = day_bounds(d)
        day = root / d.isoformat(); day.mkdir(exist_ok=True)
        for path in DAILY_GRIDS:
            s, obj = _safe(call, "POST", path, {"periodStart": str(ps), "periodEnd": str(pe), "limit": 5000, "offset": 0})
            name = path.strip("/").replace("/", "_") + ".json"
            (day / name).write_text(json.dumps(obj, indent=1, ensure_ascii=False), encoding="utf-8")
            n = len(obj.get("data", obj.get("rows", []))) if isinstance(obj, dict) and not obj.get("_error") else ("ERR" if isinstance(obj, dict) else len(obj))
            L(f"  {d} {name:45} HTTP {s} rows={n}")
        for cube in CUBES:
            rows, offset, limit = [], 0, 1000
            while True:
                s, page = _safe(call, "POST", "/wip/tma-query", {
                    "cube": cube, "timezone": TZ, "aggregate": False, "dims": [], "measures": [],
                    "dim_filters": {"date": {"range": [d.isoformat(), d.isoformat()]}},
                    "data_filters": {}, "offset": offset, "limit": limit, "order": []})
                if isinstance(page, dict) and page.get("_error"): rows = page; break
                chunk = page.get("data") if isinstance(page, dict) else page
                if not chunk: break
                rows += chunk; offset += limit
                if len(chunk) < limit: break
            (day / f"cube_{cube}.json").write_text(json.dumps(rows, indent=1, ensure_ascii=False), encoding="utf-8")
            L(f"  {d} cube_{cube:20} rows={len(rows) if isinstance(rows, list) else 'ERR'}")
        s, al = _safe(call, "GET", "/v1/alerts", params={
            "periodStart": a.astimezone(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "periodEnd":   b.astimezone(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")})
        (day / "v1_alerts.json").write_text(json.dumps(al, indent=1, ensure_ascii=False), encoding="utf-8")
        # 3. video: what exists, and request an export per computer that has data
        vids = []
        for c in (computers if isinstance(computers, list) else []):
            cid = c.get("id") or c.get("computer_id")
            s, av = _safe(call, "GET", "/player/available-video-data", params={"computer": cid, "start": ps, "end": pe})
            if isinstance(av, (list, dict)) and av and not (isinstance(av, dict) and av.get("_error")):
                s2, job = _safe(call, "POST", "/player/export-video", {"computer": cid, "start": ps, "end": pe, "format": "mp4"})
                vids.append({"computer": cid, "name": c.get("name"), "available": av, "export_request": job, "http": s2})
        (day / "video_exports.json").write_text(json.dumps(vids, indent=1, ensure_ascii=False), encoding="utf-8")
        L(f"  {d} video: {len(vids)} computers with data → export requested (download pass: --video-download)")
        d += datetime.timedelta(days=1)
    L("== DONE. Next: git add ops/archive/teramind/export && git commit && git push")
    return 0

def video_download():
    need_key()
    root = REPO / "ops/archive/teramind/export"
    got = 0
    for vj in sorted(root.glob("*/video_exports.json")):
        for v in json.loads(vj.read_text()):
            job = v.get("export_request") or {}
            jid = job.get("id") if isinstance(job, dict) else None
            if not jid: continue
            s, st = _safe(call, "GET", f"/player/export-video/status/{jid}")
            if isinstance(st, dict) and str(st.get("status", "")).lower() in ("done", "ready", "completed", "finished"):
                url = f"https://{INSTANCE}/tm-api/player/export-video/download/{jid}"
                req = urllib.request.Request(url, headers={"x-access-token": KEY})
                out = vj.parent / f"video_{v.get('name', v.get('computer'))}_{jid}.mp4"
                with urllib.request.urlopen(req, timeout=600) as r, open(out, "wb") as f: f.write(r.read())
                got += 1; print(f"  ✓ {out.relative_to(REPO)} ({out.stat().st_size//1024} KB)")
            else:
                print(f"  … job {jid} ({v.get('name')}, {vj.parent.name}): {st if isinstance(st, dict) else s}")
    print(f"{got} video file(s) downloaded. NOTE: mp4s > 100 MB will not push to GitHub — keep them on disk + Drive, commit the index only.")
    return 0

def main():
    a = sys.argv[1:]
    if "--check" in a: return check()
    if "--video-download" in a: return video_download()
    if "--all" in a:
        ds = [x for x in a if not x.startswith("--")]
        st = datetime.date.fromisoformat(ds[0]) if ds else datetime.date(2026, 7, 15)
        en = datetime.date.fromisoformat(ds[1]) if len(ds) > 1 else None
        return export_all(st, en)
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
