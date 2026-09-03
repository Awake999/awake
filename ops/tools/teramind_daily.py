#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""APW DAILY — the Teramind tracking app. One command, one clean page.

    python3 ops/tools/teramind_daily.py                 # today, auto-find source
    python3 ops/tools/teramind_daily.py --date 2026-09-02
    python3 ops/tools/teramind_daily.py --src export.csv
    python3 ops/tools/teramind_daily.py --demo          # see the shape with LABELLED fake data

WHAT IT DOES
  1. finds a source  — Teramind API (Lane 4, key in ~/apw-intel/.env) → newest CSV in
     ops/archive/teramind/inbox/ → nothing (says exactly what's missing, invents nothing)
  2. normalises any Teramind export shape into one event record
  3. writes ONE page: ops/data/teramind/<DATE>.md  +  ops/data/TERAMIND_TODAY.md
  4. prints a Slack-ready digest to stdout

LAWS IT ENFORCES (SOP)
  · every number is followed by its names            (evidence law)
  · proof link is the FIRST column, not the last     (Alan 9/3)
  · no session link is ever fabricated — no template, no link, plain text instead
  · roster members with zero events are printed as NO DATA, never omitted (ruling #27)
  · linkedin.com is the only job-search exemption, and it is a SITE exemption (ruling #29)
"""
import csv, sys, os, re, json, hashlib, datetime, collections, pathlib

REPO = pathlib.Path(__file__).resolve().parents[2]
CFG_PATH = REPO / "ops/data/teramind/CONFIG.json"
INBOX = REPO / "ops/archive/teramind/inbox"
OUTDIR = REPO / "ops/data/teramind"
TODAY_PAGE = REPO / "ops/data/TERAMIND_TODAY.md"
BRANCH = "claude/new-session-1ofk4w"
GH = f"https://github.com/Awake999/awake/blob/{BRANCH}"

CFG = json.loads(CFG_PATH.read_text(encoding="utf-8"))
WORK_START, WORK_END = CFG["work_start_hour"], CFG["work_end_hour"]
INTERVAL = CFG["interval_minutes"]
TZ = CFG["timezone_label"]
UNBOUNDED = set(CFG["owner_unbounded"])

# ── identity ────────────────────────────────────────────────────────────────
ALIAS = {}
for p in CFG["roster"]:
    for i in p["tm_ids"]:
        ALIAS[i.strip().lower()] = p["name"]
ROLE = {p["name"]: p["role"] for p in CFG["roster"]}
ROSTER = [p["name"] for p in CFG["roster"]]

def canon(raw):
    return ALIAS.get((raw or "").strip().lower(), (raw or "?").strip())

# ── column-shape tolerance (Teramind exports differ by report) ──────────────
FIELDS = {
    "ts":    ["time", "timestamp", "date/time", "datetime", "start time", "started", "interval", "date"],
    "user":  ["user", "employee", "username", "agent", "person", "employee name"],
    "app":   ["application", "app", "process", "process name"],
    "site":  ["website", "url", "domain", "web page", "site"],
    "title": ["window title", "title", "activity", "window"],
    "sess":  ["session", "session id", "sessionid", "record id", "record", "id"],
    "dur":   ["duration", "time spent", "seconds", "active time", "length"],
}
def pick(row, key):
    for want in FIELDS[key]:
        for k, v in row.items():
            if k and k.strip().lower() == want:
                return (v or "").strip()
    for want in FIELDS[key]:                      # loose second pass
        for k, v in row.items():
            if k and want in k.strip().lower():
                return (v or "").strip()
    return ""

TS_FORMATS = ("%Y-%m-%d %H:%M:%S", "%Y-%m-%dT%H:%M:%S", "%m/%d/%Y %H:%M:%S",
              "%m/%d/%Y %I:%M:%S %p", "%Y-%m-%d %H:%M", "%m/%d/%Y %H:%M",
              "%m/%d/%y %I:%M %p", "%Y/%m/%d %H:%M:%S")
def parse_ts(s):
    s = (s or "").strip().replace("Z", "")
    for f in TS_FORMATS:
        try:
            return datetime.datetime.strptime(s[:len("2026-09-03 12:00:00")], f)
        except ValueError:
            pass
    for f in TS_FORMATS:
        try:
            return datetime.datetime.strptime(s, f)
        except ValueError:
            pass
    return None

def parse_dur(s):
    s = (s or "").strip()
    if not s:
        return 0
    if re.fullmatch(r"\d+", s):
        return int(s)
    m = re.fullmatch(r"(?:(\d+):)?(\d+):(\d+)", s)
    if m:
        h, mm, ss = (int(x or 0) for x in m.groups())
        return h * 3600 + mm * 60 + ss
    m = re.findall(r"(\d+)\s*([hms])", s.lower())
    return sum(int(n) * {"h": 3600, "m": 60, "s": 1}[u] for n, u in m) if m else 0

# ── classification ──────────────────────────────────────────────────────────
PROD = [(re.compile(p, re.I), t) for p, t in CFG["productive_patterns"]]
FLAG = [(re.compile(p, re.I), t) for p, t in CFG["flag_patterns"]]
LINKEDIN = re.compile(r"linkedin\.com", re.I)

def classify(hay):
    """→ (tag, is_flag). LinkedIn short-circuits: only site-level exemption there is."""
    if LINKEDIN.search(hay):
        return "🟢 hiring campaign (Alan-assigned)", False
    for rx, tag in FLAG:
        if rx.search(hay):
            return tag, True
    for rx, tag in PROD:
        if rx.search(hay):
            return tag, False
    return "⚪ unclassified", False

# ── source resolution ───────────────────────────────────────────────────────
def find_source(explicit=None):
    if explicit:
        p = pathlib.Path(explicit)
        return (p, "explicit --src") if p.exists() else (None, f"--src not found: {explicit}")
    env = REPO.parent / "apw-intel" / ".env"
    has_key = env.exists() and "TERAMIND_API_KEY=" in env.read_text()
    cands = sorted(INBOX.glob("*.csv"), key=lambda p: p.stat().st_mtime, reverse=True) if INBOX.exists() else []
    if cands:
        return cands[0], f"newest CSV in {INBOX.relative_to(REPO)}"
    if has_key:
        return None, "API key present — run `python3 ops/lane4/teramind_pull.py` first (Lane 4 only; cloud lanes cannot reach the key)"
    return None, "no source"

def load(path):
    rows = list(csv.DictReader(open(path, encoding="utf-8-sig")))
    sha = hashlib.sha256(pathlib.Path(path).read_bytes()).hexdigest()[:12]
    return rows, sha

# ── demo fixture (clearly labelled; never confusable with real data) ─────────
def demo_rows(date):
    base = datetime.datetime.combine(date, datetime.time(7, 0))
    script = [
        ("Carla",  0, "app.gohighlevel.com/contacts",      "GHL — lead follow-up",  2400),
        ("Carla",  55, "zoom.us/j/8842",                    "Triage call — K. Ruiz", 2100),
        ("Carla", 160, "indeed.com/jobs?q=remote",          "Indeed — job search",    600),
        ("Grace",  10, "app.gohighlevel.com/conversations", "GHL — SMS queue",       2800),
        ("Grace", 120, "linkedin.com/jobs/post",            "LinkedIn — hiring post", 900),
        ("Grace", 240, "mail.google.com",                   "Gmail",                 1500),
        ("Lynn",   30, "app.gohighlevel.com/opportunities", "GHL — pipeline",        2000),
        ("Lynn",  180, "netflix.com/browse",                "Netflix",               1800),
        ("Anne (Rosemarie) Fabian", 45, "docs.google.com",  "Script doc",            2600),
        ("nguye@a51", 0,  "github.com/Awake999/awake",      "claude.exe — ops",      3000),
        ("nguye@a51", 700, "business.facebook.com",         "Ads Manager",           1200),
    ]
    out = []
    for i, (u, off, site, title, dur) in enumerate(script):
        ts = base + datetime.timedelta(minutes=off)
        out.append({"Time": ts.strftime("%Y-%m-%d %H:%M:%S"), "User": u, "Website": site,
                    "Window Title": title, "Session": f"DEMO{i:04d}", "Duration": str(dur)})
    return out

# ── build ───────────────────────────────────────────────────────────────────
def hhmm(sec):
    return f"{sec//3600}h {(sec%3600)//60:02d}m"

def main():
    a = sys.argv[1:]
    def opt(name, default=None):
        for x in a:
            if x.startswith(name + "="):
                return x.split("=", 1)[1]
        if name in a:
            i = a.index(name)
            return a[i + 1] if i + 1 < len(a) else True
        return default
    demo = "--demo" in a
    date_s = opt("--date")
    date = datetime.date.fromisoformat(date_s) if date_s else datetime.date.today()

    if demo:
        rows, sha, src_label = demo_rows(date), "DEMO", "SYNTHETIC DEMO DATA — not real"
    else:
        path, why = find_source(opt("--src"))
        if not path:
            print(f"✗ No Teramind data to build from ({why}).\n"
                  f"  Fastest path: Teramind → Reports → Web & App activity → export CSV for {date} →\n"
                  f"  drop it in {INBOX.relative_to(REPO)}/ → re-run this command.\n"
                  f"  Or see the layout right now:  python3 ops/tools/teramind_daily.py --demo")
            return 2
        rows, sha = load(path)
        src_label = f"`{pathlib.Path(path).name}` · sha256 `{sha}` · {len(rows)} rows · {why}"

    tmpl = CFG["session_link_template"].strip()
    cols_seen = sorted(rows[0].keys()) if rows else []

    grid = collections.defaultdict(lambda: collections.defaultdict(list))
    per = collections.defaultdict(lambda: {"secs": 0, "first": None, "last": None,
                                           "what": collections.Counter(), "when": {},
                                           "flags": [], "events": 0})
    problems, offhours, skipped = [], [], 0

    for r in rows:
        ts = parse_ts(pick(r, "ts"))
        if not ts or ts.date() != date:
            skipped += 1
            continue
        user = canon(pick(r, "user"))
        raw_user = pick(r, "user")
        site, app, title = pick(r, "site"), pick(r, "app"), pick(r, "title")
        sess, dur = pick(r, "sess"), parse_dur(pick(r, "dur"))
        label = site or app or title or "activity"
        hay = f"{site} {app} {title}"
        tag, is_flag = classify(hay)

        link = ""
        if tmpl and sess:
            link = (tmpl.replace("{instance}", CFG["instance"]).replace("{session}", sess)
                        .replace("{user}", raw_user).replace("{ts}", ts.isoformat())
                        .replace("{date}", ts.date().isoformat())
                        .replace("{epoch}", str(int(ts.timestamp()))))
        proof = f"[▶ {ts:%H:%M}]({link})" if link else f"`{ts:%H:%M}`"

        p = per[user]
        p["secs"] += dur; p["events"] += 1
        p["first"] = min(p["first"], ts) if p["first"] else ts
        p["last"] = max(p["last"], ts) if p["last"] else ts
        wkey = f"{tag} {label[:34]}"
        p["what"][wkey] += max(dur, 1)
        prev = p["when"].get(wkey)
        if prev is None or ts < prev[0]:
            p["when"][wkey] = (ts, proof)

        # slots are anchored to the START OF THE WORK WINDOW, not to midnight, so the
        # columns read 07:00 / 07:50 / 08:40 … exactly as Alan asked, not 06:40.
        mins = ts.hour * 60 + ts.minute
        idx = (mins - WORK_START * 60) // INTERVAL
        slot = WORK_START * 60 + idx * INTERVAL
        cell = f"[{label[:26]}]({link})" if link else label[:26]
        grid[slot][user].append(cell)

        if is_flag:
            in_win = WORK_START <= ts.hour < WORK_END
            rec = (ts, user, tag, label[:44], proof)
            if in_win or user in UNBOUNDED:
                problems.append(rec); p["flags"].append(rec)
            else:
                offhours.append(rec)

    present = [u for u in per if per[u]["events"]]
    missing = [n for n in ROSTER if n not in present]
    extra = [u for u in present if u not in ROSTER]
    cols = [n for n in ROSTER if n in present] + sorted(extra)
    now = datetime.datetime.now()

    L = []
    L.append(f"# 🖥 APW DAILY — who did what, {date:%A %b %d, %Y}")
    if demo:
        L.append("> 🧪 **DEMO PAGE — synthetic data.** This shows the exact layout. Drop a real CSV in "
                 f"`ops/archive/teramind/inbox/` and re-run to replace it with real activity.\n")
    verdict = (f"**{len(present)} of {len(ROSTER)} monitored people produced activity** · "
               f"**{len(problems)} problem(s) in the work window** · "
               f"work window {WORK_START:02d}:00–{WORK_END:02d}:00 {TZ}")
    L.append(verdict)
    L.append(f"\n*Source: {src_label} · built {now:%Y-%m-%d %H:%M} · "
             f"[the rules this page applied](#-verify-this-page)*\n")
    if not tmpl:
        L.append("> ⚠️ **Session-player links are OFF.** Times show as plain `HH:MM` instead of ▶ jump links. "
                 "Paste one real Teramind session URL into `session_link_template` in "
                 f"[CONFIG.json]({GH}/ops/data/teramind/CONFIG.json) and every time on this page becomes clickable. "
                 "A link is never invented.\n")

    # 1. whole picture
    L.append("## 📍 WHOLE PICTURE — everyone, one screen\n")
    L.append("| Proof | Person | Role | First seen | Last seen | Tracked time | Events | 🔴 Problems |")
    L.append("|---|---|---|---|---|---|---|---|")
    for u in cols:
        p = per[u]
        anchor = "#" + re.sub(r"[^a-z0-9]+", "-", u.lower()).strip("-")
        L.append(f"| [jump]({anchor}) | **{u}** | {ROLE.get(u,'—')} | `{p['first']:%H:%M}` | `{p['last']:%H:%M}` "
                 f"| {hhmm(p['secs'])} | {p['events']} | {len(p['flags']) or '—'} |")
    for u in missing:
        L.append(f"| — | {u} | {ROLE.get(u,'—')} | — | — | — | **0** | ⚫ **NO DATA** |")
    if missing:
        L.append(f"\n**⚫ No data today ({len(missing)}):** {', '.join(missing)}. "
                 "*This means no events reached this export — NOT that they are unmonitored. "
                 "Absence in a report is never proof of absence of coverage (ruling #27); "
                 "confirm in the Teramind Employees page before drawing a conclusion.*")

    # 2. side by side
    L.append(f"\n## ⏱ SIDE BY SIDE — {INTERVAL}-minute intervals, {WORK_START:02d}:00–{WORK_END:02d}:00 {TZ}\n")
    L.append("| Time | " + " | ".join(cols) + " |")
    L.append("|---|" + "---|" * len(cols))
    window = list(range(WORK_START * 60, WORK_END * 60, INTERVAL))
    slots = sorted(set(window) | set(grid))          # every window slot, empty or not, plus any outside it
    for s in slots:
        lab = f"`{s//60:02d}:{s%60:02d}`"
        if s not in window:
            lab += " *(outside)*"
        row = [lab]
        for u in cols:
            items, seen, uniq = grid.get(s, {}).get(u, []), set(), []
            for i in items:
                if i not in seen:
                    seen.add(i); uniq.append(i)
            row.append(" · ".join(uniq[:3]) or "—")
        L.append("| " + " | ".join(row) + " |")
    L.append(f"\n*Blank cell = no captured event in that {INTERVAL}-minute block. "
             f"Rows marked* **(outside)** *fall before {WORK_START:02d}:00 or after {WORK_END:02d}:00 — "
             "shown because they are real, not counted against the window.*")

    # 3. problems
    L.append("\n## 🚩 PROBLEM LIST — inside the work window\n")
    if problems:
        L.append("| Proof | Time | Person | Flag | What |")
        L.append("|---|---|---|---|---|")
        for ts, u, tag, lbl, proof in sorted(problems):
            L.append(f"| {proof} | {ts:%H:%M} | **{u}** | {tag} | {lbl} |")
    else:
        L.append("**None.** No flagged activity inside "
                 f"{WORK_START:02d}:00–{WORK_END:02d}:00 {TZ} today.")
    if offhours:
        who = ", ".join(sorted({u for _, u, _, _, _ in offhours}))
        L.append(f"\n*{len(offhours)} flagged hit(s) outside the work window ({who}) — recorded, not counted as problems.*")
    L.append("\n> **The flagging rule** (ruling #29, Alan verbatim 9/3): *\"indeed, in glass stored and sip recruiter "
             "monster are all still flagged for everybody. Is only linked in.\"* — **linkedin.com is the only exemption "
             "and it is a SITE exemption.** Indeed · Glassdoor · ZipRecruiter · Monster are flagged for **everyone**, "
             "Alan included. No person is ever exempted.")

    # 4. per person
    L.append("\n## 👤 PERSON BY PERSON\n")
    for u in cols:
        p = per[u]
        L.append(f"### {u}")
        L.append(f"*{ROLE.get(u,'—')} · `{p['first']:%H:%M}`–`{p['last']:%H:%M}` · "
                 f"{hhmm(p['secs'])} tracked · {p['events']} events · "
                 f"{len(p['flags'])} problem(s)*\n")
        L.append("| Proof (first hit) | Where the time went | Time |")
        L.append("|---|---|---|")
        for what, secs in p["what"].most_common(10):
            wts, wproof = p["when"][what]
            L.append(f"| {wproof} | {what} | {hhmm(secs)} |")
        if p["flags"]:
            L.append("\n**Problems:** " + " · ".join(f"{proof} {tag} {lbl}" for _, _, tag, lbl, proof in sorted(p["flags"])))
        L.append("")
    for u in missing:
        L.append(f"### {u}\n*{ROLE.get(u,'—')} · **no events in this export.** Not a coverage claim — see ruling #27.*\n")

    # 5. verify
    L.append("## 🔍 VERIFY THIS PAGE\n")
    L.append("| What | Value |")
    L.append("|---|---|")
    L.append(f"| Source | {src_label} |")
    L.append(f"| Rows read | {len(rows)} |")
    L.append(f"| Rows used (this date) | {len(rows)-skipped} |")
    L.append(f"| Rows skipped (other date / unparseable time) | {skipped} |")
    L.append(f"| Columns the export actually had | `{'`, `'.join(cols_seen) or '—'}` |")
    L.append(f"| Roster | {len(ROSTER)} people, from [CONFIG.json]({GH}/ops/data/teramind/CONFIG.json) |")
    L.append(f"| Names seen that are NOT on the roster | {', '.join(extra) or 'none'} |")
    L.append(f"| Session links | {'ON' if tmpl else 'OFF — no template set, nothing fabricated'} |")
    L.append(f"| Builder | [ops/tools/teramind_daily.py]({GH}/ops/tools/teramind_daily.py) |")
    L.append(f"| Built at | {now:%Y-%m-%d %H:%M} local |")
    L.append("\n*Rebuild any day: `python3 ops/tools/teramind_daily.py --date YYYY-MM-DD`*")

    md = "\n".join(L) + "\n"
    OUTDIR.mkdir(parents=True, exist_ok=True)
    outp = OUTDIR / f"{date.isoformat()}{'-DEMO' if demo else ''}.md"
    outp.write_text(md, encoding="utf-8")
    TODAY_PAGE.write_text(
        f"<!-- generated by ops/tools/teramind_daily.py — do not hand-edit -->\n{md}", encoding="utf-8")

    print(f"✓ {outp.relative_to(REPO)}")
    print(f"✓ {TODAY_PAGE.relative_to(REPO)}  (the stable 'today' link)")
    print()
    print("── SLACK DIGEST ──────────────────────────────────────────")
    print(f"*APW daily — {date:%a %b %d}*")
    print(f"{len(present)}/{len(ROSTER)} people with activity · {len(problems)} problem(s) in-window")
    for u in cols:
        p = per[u]
        print(f"• *{u}* {p['first']:%H:%M}–{p['last']:%H:%M} · {hhmm(p['secs'])} · "
              f"{len(p['flags']) or 'no'} problem(s)")
    if missing:
        print(f"• _no data:_ {', '.join(missing)} (not a coverage claim — verify in Teramind)")
    print(f"Full page: {GH}/ops/data/TERAMIND_TODAY.md")
    print("──────────────────────────────────────────────────────────")
    return 0

if __name__ == "__main__":
    sys.exit(main())
