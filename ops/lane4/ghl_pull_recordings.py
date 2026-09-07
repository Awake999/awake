"""LANE 4 — GHL CALL RECORDINGS + TRANSCRIPTIONS pull (read-only). Stdlib-only.

Why this exists: the 2026-08-30 export has 1,473 TYPE_CALL rows but ZERO recordings or
transcriptions — the messages endpoint only returns duration/status. GHL keeps the audio and
its own transcript behind two per-message endpoints that need the location token:
  GET /conversations/locations/{loc}/messages/{msgId}/transcription   (JSON, small)
  GET /conversations/messages/{msgId}/locations/{loc}/recording        (audio bytes)

Runs on the PC (token in ../apw-intel/.env). For every answered call (duration >= MIN_SEC):
  ops/archive/ghl/recordings/<YYYY-MM-DD>--<contact>--<msgId>/transcript.json  (raw GHL)
  ops/archive/ghl/recordings/<YYYY-MM-DD>--<contact>--<msgId>/transcript.md    (readable)
  ops/archive/ghl/recordings/<YYYY-MM-DD>--<contact>--<msgId>/audio.mp3        (only with --audio)
  ops/archive/ghl/recordings/INDEX.md                                          (one row per call, GHL contact link)

Usage:  python3 ops/lane4/ghl_pull_recordings.py [--date 2026-08-30] [--audio] [--min-sec 30]
Idempotent: skips calls already on disk. Never writes to GHL.
"""
import json, sys, time, re, urllib.request, urllib.parse, urllib.error, pathlib, datetime

HERE = pathlib.Path(__file__).resolve(); REPO = HERE.parent.parent.parent
ENVF = REPO.parent / "apw-intel" / ".env"
ENV = {}
for line in ENVF.read_text().splitlines():
    if "=" in line and not line.startswith("#"):
        k, v = line.split("=", 1); ENV[k.strip()] = v.strip()
TOKEN, LOC = ENV["GHL_TOKEN"], ENV["GHL_LOCATION"]
BASE = "https://services.leadconnectorhq.com"
GHL_UI = f"https://app.gohighlevel.com/v2/location/{LOC}/contacts/detail/"

args = sys.argv[1:]
def opt(name, default=None):
    return args[args.index(name)+1] if name in args else default
WANT_AUDIO = "--audio" in args
MIN_SEC = int(opt("--min-sec", 30))
DATE = opt("--date") or sorted(p.name for p in (REPO/"ops/archive/ghl").iterdir() if re.fullmatch(r"\d{4}-\d{2}-\d{2}", p.name))[-1]
RAW = REPO / "ops/archive/ghl" / DATE / "raw"
OUT = REPO / "ops/archive/ghl/recordings"; OUT.mkdir(parents=True, exist_ok=True)

def get(url, version="2021-04-15", binary=False):
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {TOKEN}", "Version": version,
        "Accept": "*/*" if binary else "application/json", "User-Agent": "Mozilla/5.0"})
    for attempt in range(6):
        try:
            with urllib.request.urlopen(req, timeout=120) as r:
                data = r.read()
                return data if binary else json.loads(data.decode() or "{}")
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503, 504): time.sleep(2 ** attempt); continue
            return {"_error": e.code, "_body": e.read().decode(errors="ignore")[:300]}
        except Exception:
            time.sleep(2 ** attempt)
    return {"_error": "retries_exhausted"}

contacts = {c["id"]: c for c in json.load(open(RAW/"contacts.json"))}
msgs = json.load(open(RAW/"messages_by_conversation.json"))
def cname(cid):
    c = contacts.get(cid, {})
    return (f'{c.get("firstName") or ""} {c.get("lastName") or ""}'.strip() or c.get("contactName") or cid)
def slug(s): return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:40]

calls = []
for cv, ms in msgs.items():
    for m in ms:
        if m.get("type") == 1 or m.get("messageType") == "TYPE_CALL":
            dur = ((m.get("meta") or {}).get("call") or {}).get("duration") or 0
            if dur >= MIN_SEC:
                calls.append((m.get("dateAdded", ""), m.get("contactId"), m["id"], m.get("direction"), dur))
calls.sort()
print(f"{len(calls)} answered calls (>= {MIN_SEC}s) in export {DATE}")

rows, n_tx, n_au, n_none = [], 0, 0, 0
for when, cid, mid, direction, dur in calls:
    d = OUT / f"{when[:10]}--{slug(cname(cid))}--{mid}"
    d.mkdir(exist_ok=True)
    tj = d / "transcript.json"
    if not tj.exists():
        t = get(f"{BASE}/conversations/locations/{LOC}/messages/{mid}/transcription")
        tj.write_text(json.dumps(t, indent=1, ensure_ascii=False))
        # readable form: GHL returns a list of {sentence, startTime, endTime, ...} or {transcription: ...}
        segs = t if isinstance(t, list) else (t.get("transcription") or t.get("data") or [])
        lines = []
        for s in segs if isinstance(segs, list) else []:
            st = s.get("startTime") or s.get("start") or 0
            lines.append(f"[{int(st)//60}:{int(st)%60:02d}] {s.get('speaker') or s.get('role') or ''}: {s.get('sentence') or s.get('text') or ''}".strip())
        (d/"transcript.md").write_text(
            f"# {cname(cid)} — {when[:16]} — {direction} — {dur}s\n\nGHL contact: {GHL_UI}{cid}\n\n" +
            ("\n".join(lines) if lines else "_no transcription returned (see transcript.json for the raw reply)_") + "\n")
    tx = json.loads(tj.read_text())
    has_tx = not (isinstance(tx, dict) and tx.get("_error"))
    n_tx += has_tx; n_none += (not has_tx)
    if WANT_AUDIO and not (d/"audio.mp3").exists():
        a = get(f"{BASE}/conversations/messages/{mid}/locations/{LOC}/recording", binary=True)
        if isinstance(a, bytes) and len(a) > 1000:
            (d/"audio.mp3").write_bytes(a); n_au += 1
    rows.append(f"| {when[:16]} | [{cname(cid)}]({GHL_UI}{cid}) | {direction} | {dur}s | {'✅' if has_tx else '—'} | {'✅' if (d/'audio.mp3').exists() else '—'} | [{d.name}]({d.name}/transcript.md) |")
    time.sleep(0.25)

(OUT/"INDEX.md").write_text(
    f"# GHL phone-call recordings & transcriptions\n\nPulled {datetime.date.today()} from export {DATE} · {len(calls)} answered calls (>= {MIN_SEC}s) · transcripts {n_tx} · missing {n_none} · audio files {sum(1 for r in rows if '| ✅ | [' in r)}\n\n"
    "| Call time (UTC) | Contact (GHL link) | Dir | Length | Transcript | Audio | Folder |\n|---|---|---|---|---|---|---|\n" + "\n".join(rows) + "\n")
print(f"transcripts: {n_tx} · none/errored: {n_none} · audio downloaded this run: {n_au} · index: {OUT/'INDEX.md'}")
