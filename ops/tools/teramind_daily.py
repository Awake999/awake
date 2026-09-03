#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""APW DAILY — the Teramind day record. Minute-level, every person, whole day.

    python3 ops/tools/teramind_daily.py                 # today, auto-find source
    python3 ops/tools/teramind_daily.py --date 2026-09-02
    python3 ops/tools/teramind_daily.py --src export.csv
    python3 ops/tools/teramind_daily.py --demo          # LABELLED sample day, real layout

ORDER OF THE PAGE (record first, analysis second — Alan 9/3):
    1 COVERAGE MAP      hour-by-hour density per person — the whole day at a glance
    2 TIMETABLE         50-minute side-by-side
    3 ALL-HANDS STREAM  every event, everyone, chronological, to the minute
    4 FULL LEDGER       per person: start→end, duration, activity, WHAT WAS BEING DONE, proof
    5 PROBLEMS          flagged activity inside the work window, proof first
    6 ANALYSIS          where time actually went, per person, by category
    7 VERIFY            source sha, rows read/used/skipped, columns, rules applied

LAWS IT ENFORCES
  · every event carries start, end, duration and an explanation — not just a label
  · explanations are DERIVED from the captured URL path + window title, never invented
  · gaps longer than gap_minutes print as explicit ⚪ NO CAPTURE rows with their length
  · roster members with zero events print as NO DATA, never dropped (ruling #27)
  · linkedin.com is the only job-search exemption and it is a SITE exemption (ruling #29)
  · no session-player URL is ever fabricated — no template means plain text
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
GAP_MIN = CFG.get("gap_minutes", 4)
TZ = CFG["timezone_label"]
UNBOUNDED = set(CFG["owner_unbounded"])
TM_IDS = CFG.get("teramind_ids", {})

ALIAS, ROLE, ROSTER = {}, {}, []
for _p in CFG["roster"]:
    ROSTER.append(_p["name"]); ROLE[_p["name"]] = _p["role"]
    for _i in _p["tm_ids"]:
        ALIAS[_i.strip().lower()] = _p["name"]

def canon(raw):
    return ALIAS.get((raw or "").strip().lower(), (raw or "?").strip())

# ── column-shape tolerance ──────────────────────────────────────────────────
FIELDS = {
    "ts":    ["time", "timestamp", "date/time", "datetime", "start time", "started", "interval", "date"],
    "end":   ["end time", "ended", "finish", "end"],
    "user":  ["user", "employee", "username", "agent", "person", "employee name"],
    "app":   ["application", "app", "process", "process name"],
    "site":  ["website", "url", "domain", "web page", "site"],
    "title": ["window title", "title", "activity", "window", "page title"],
    "sess":  ["session", "session id", "sessionid", "record id", "record", "id"],
    "dur":   ["duration", "time spent", "seconds", "active time", "length"],
}
def pick(row, key):
    for want in FIELDS[key]:
        for k, v in row.items():
            if k and k.strip().lower() == want:
                return (v or "").strip()
    for want in FIELDS[key]:
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
        try: return datetime.datetime.strptime(s[:19], f)
        except ValueError: pass
    for f in TS_FORMATS:
        try: return datetime.datetime.strptime(s, f)
        except ValueError: pass
    return None

def parse_dur(s):
    s = (s or "").strip()
    if not s: return 0
    if re.fullmatch(r"\d+", s): return int(s)
    m = re.fullmatch(r"(?:(\d+):)?(\d+):(\d+)", s)
    if m:
        h, mm, ss = (int(x or 0) for x in m.groups()); return h*3600 + mm*60 + ss
    m = re.findall(r"(\d+)\s*([hms])", s.lower())
    return sum(int(n) * {"h":3600, "m":60, "s":1}[u] for n, u in m) if m else 0

def shorten(s, n):
    """Trim on a word boundary so the tail never reads like 'SMS/em'."""
    if len(s) <= n: return s
    cut = s[:n]
    return cut[:cut.rfind(" ")].rstrip(" -—\"") + "…"

def dur_str(sec):
    if sec >= 3600: return f"{sec//3600}h {(sec%3600)//60:02d}m"
    if sec >= 60:   return f"{sec//60}m {sec%60:02d}s"
    return f"{sec}s"

# ── classification + explanation (both DERIVED, never invented) ─────────────
FLAG = [(re.compile(p, re.I), t) for p, t in CFG["flag_patterns"]]
PROD = [(re.compile(p, re.I), t) for p, t in CFG["productive_patterns"]]
EXPLAIN = [(re.compile(p, re.I), cat, tpl) for p, cat, tpl in CFG["explain_rules"]]
HINTS = CFG["url_hints"]
LINKEDIN = re.compile(r"linkedin\.com", re.I)

def classify(hay):
    if LINKEDIN.search(hay): return "🟢 hiring campaign (Alan-assigned)", False
    for rx, tag in FLAG:
        if rx.search(hay): return tag, True
    for rx, tag in PROD:
        if rx.search(hay): return tag, False
    return "⚪ unclassified", False

def explain(site, app, title):
    """Plain-English 'what was being done', built only from what was captured."""
    hay = f"{site} {app} {title}"
    hint = ""
    low = site.lower()
    for frag, phrase in HINTS.items():
        if frag in low:
            hint = phrase; break
    titlepart = f' — "{title}"' if title else ""
    for rx, cat, tpl in EXPLAIN:
        if rx.search(hay):
            s = tpl.format(hint=hint, titlepart=titlepart, site=site, app=app, title=title)
            s = re.sub(r"(\s*—\s*){2,}", " — ", s)          # empty {hint} left a double dash
            s = re.sub(r"\s*—\s*(?=$|\()", "", s)
            s = re.sub(r"\s{2,}", " ", s).strip()
            return cat, s
    # nothing matched: say exactly what was captured, claim nothing about intent
    if title: return "Unclassified", f'{app or site or "activity"} — "{title}"'
    if site:  return "Unclassified", f"{site} (no window title captured — intent unknown)"
    if app:   return "Unclassified", f"{app} (no title or URL captured — intent unknown)"
    return "Unclassified", "activity recorded with no app, URL or title — intent unknown"

# ── source ──────────────────────────────────────────────────────────────────
def find_source(explicit=None):
    if explicit:
        p = pathlib.Path(explicit)
        return (p, "explicit --src") if p.exists() else (None, f"--src not found: {explicit}")
    env = REPO.parent / "apw-intel" / ".env"
    has_key = env.exists() and "TERAMIND_API_KEY=" in env.read_text()
    cands = sorted(INBOX.glob("*.csv"), key=lambda p: p.stat().st_mtime, reverse=True) if INBOX.exists() else []
    if cands: return cands[0], f"newest CSV in {INBOX.relative_to(REPO)}"
    if has_key: return None, "API key present — run `python3 ops/lane4/teramind_pull.py` first (Lane 4 only)"
    return None, "no source"

# ── demo day (clearly labelled; a full realistic day so the format is judgeable) ──
def demo_rows(date):
    import random
    random.seed(7)
    day = [
        ("Carla", [
            ("07:02", 22, "app.gohighlevel.com/contacts", "Contacts — Smart List: New Leads 24h"),
            ("07:24", 31, "app.gohighlevel.com/conversations", "Conversation — Teresa Graham (SMS)"),
            ("07:56", 12, "app.gohighlevel.com/conversations", "Conversation — Marx Todjro (SMS)"),
            ("08:09", 8,  "mail.google.com", "Inbox (14) — cvstivala@icloud.com"),
            ("08:20", 41, "zoom.us/j/8842013", "Triage call — Karl Ruiz"),
            ("09:05", 14, "app.gohighlevel.com/opportunities", "Pipeline — Karl Ruiz moved to Qualified"),
            ("09:22", 9,  "docs.google.com", "Triage Script v3"),
            ("09:38", 18, "indeed.com/jobs?q=remote+customer+success", "remote customer success jobs - Indeed"),
            ("10:02", 27, "app.gohighlevel.com/conversations", "Conversation — Stanley Carter (SMS)"),
            ("10:35", 6,  "slack.com/client/T01/C09", "#sales — Slack"),
            ("11:14", 38, "app.gohighlevel.com/calendars", "Calendar — Sep 4 Funding Calls"),
            ("12:04", 45, "", "(idle — no capture)"),
            ("13:10", 33, "zoom.us/j/8842019", "Discovery — Ashwini Anand"),
            ("13:50", 21, "app.gohighlevel.com/conversations", "Conversation — Ashwini Anand (notes)"),
            ("14:20", 16, "fathom.video/calls/44120", "Ashwini Anand — call summary"),
            ("14:44", 29, "app.gohighlevel.com/contacts", "Contacts — Smart List: No Show 7d"),
            ("15:30", 24, "mail.google.com", "Compose — follow-up sequence"),
            ("16:05", 35, "app.gohighlevel.com/conversations", "Conversation queue — 9 unread"),
            ("16:48", 11, "notion.so/apw/ops-hub", "APW OPS HUB — Notion"),
        ]),
        ("Grace", [
            ("07:12", 28, "app.gohighlevel.com/conversations", "Conversation — inbound SMS queue"),
            ("07:44", 19, "app.gohighlevel.com/contacts", "Contacts — Smart List: Unresponsive"),
            ("08:08", 42, "app.gohighlevel.com/conversations", "Conversation — Nick Samara (SMS)"),
            ("08:55", 23, "linkedin.com/jobs/post/edit", "Edit job post — Appointment Setter"),
            ("09:25", 15, "linkedin.com/messaging", "Messaging — 4 applicants"),
            ("09:45", 37, "app.gohighlevel.com/conversations", "Conversation queue"),
            ("10:28", 12, "mail.google.com", "Inbox — langubinagrace@gmail.com"),
            ("10:45", 52, "app.gohighlevel.com/conversations", "Conversation queue — 22 threads"),
            ("11:42", 18, "docs.google.com", "Setter SOP — reheat script"),
            ("12:05", 40, "", "(idle — no capture)"),
            ("12:50", 44, "app.gohighlevel.com/conversations", "Conversation queue"),
            ("13:40", 26, "instagram.com/direct/inbox", "Instagram Direct — 6 unread"),
            ("14:12", 31, "manychat.com/fb/flows", "ManyChat — IG Leads flow"),
            ("14:50", 22, "app.gohighlevel.com/contacts", "Contacts — tag: IG lead"),
            ("15:20", 48, "app.gohighlevel.com/conversations", "Conversation queue"),
            ("16:15", 29, "app.gohighlevel.com/opportunities", "Pipeline — 3 moved to Booked"),
        ]),
        ("Lynn", [
            ("07:31", 24, "app.gohighlevel.com/opportunities", "Pipeline — Sep week 1"),
            ("08:00", 33, "app.gohighlevel.com/conversations", "Conversation — Chris Bowers (SMS)"),
            ("08:40", 17, "mail.google.com", "Inbox — neves.lynn7@gmail.com"),
            ("09:05", 21, "docs.google.com", "Objection handling — draft"),
            ("09:35", 46, "netflix.com/browse", "Home - Netflix"),
            ("10:28", 14, "app.gohighlevel.com/conversations", "Conversation queue"),
            ("10:50", 39, "zoom.us/j/8842022", "Funding call — Teresa Graham"),
            ("11:35", 19, "app.gohighlevel.com/opportunities", "Pipeline — Teresa Graham → Offer Made"),
            ("12:00", 55, "", "(idle — no capture)"),
            ("13:05", 42, "app.gohighlevel.com/conversations", "Conversation queue"),
            ("13:55", 26, "amazon.com/gp/cart", "Shopping Cart - Amazon.com"),
            ("14:30", 37, "app.gohighlevel.com/conversations", "Conversation queue"),
            ("15:15", 28, "sheets.google.com", "Setter tracker — week 36"),
            ("15:50", 33, "app.gohighlevel.com/contacts", "Contacts — Smart List: Reheat"),
        ]),
        ("Anne (Rosemarie) Fabian", [
            ("07:46", 36, "docs.google.com", "Call script — Medical vertical"),
            ("08:28", 27, "app.gohighlevel.com/conversations", "Conversation queue"),
            ("09:02", 44, "app.gohighlevel.com/conversations", "Conversation — Robert Morawitz (SMS)"),
            ("09:55", 18, "mail.google.com", "Inbox — rosemarieannefabian@gmail.com"),
            ("10:20", 51, "app.gohighlevel.com/conversations", "Conversation queue — 17 threads"),
            ("11:20", 22, "fathom.video/calls/44098", "Robert Morawitz — call summary"),
            ("11:50", 35, "", "(idle — no capture)"),
            ("12:35", 47, "app.gohighlevel.com/contacts", "Contacts — Smart List: Never Booked"),
            ("13:30", 29, "app.gohighlevel.com/conversations", "Conversation queue"),
            ("14:10", 24, "ziprecruiter.com/candidate/search", "Job search - ZipRecruiter"),
            ("14:45", 41, "app.gohighlevel.com/conversations", "Conversation queue"),
            ("15:35", 32, "docs.google.com", "Call script — Professionals vertical"),
        ]),
        ("nguye@a51", [
            ("06:48", 52, "github.com/Awake999/awake", "Awake999/awake — commits"),
            ("07:45", 38, "claude.ai/code", "Claude Code — ops session"),
            ("08:30", 26, "business.facebook.com/adsmanager", "Ads Manager — SCIO 1821085838595242"),
            ("09:05", 31, "business.facebook.com/adsmanager", "Ads Manager — CCA 1299632422083575"),
            ("09:45", 44, "app.gohighlevel.com/reporting", "Reporting — attribution"),
            ("10:40", 29, "zoom.us/j/8842030", "Partner sync — Kai"),
            ("11:20", 35, "notion.so/apw/ops-hub", "APW OPS HUB"),
            ("12:10", 48, "claude.ai/code", "Claude Code — funnel rebuild"),
            ("13:15", 22, "fathom.video/calls/44131", "Partner sync — summary"),
            ("13:50", 41, "app.gohighlevel.com/opportunities", "Pipeline review"),
            ("14:40", 33, "business.facebook.com/adsmanager", "Ads Manager — creative review"),
            ("15:25", 39, "claude.ai/code", "Claude Code — Teramind app"),
            ("16:15", 44, "github.com/Awake999/awake", "Awake999/awake — push"),
            ("17:20", 51, "claude.ai/code", "Claude Code — after hours"),
            ("18:40", 37, "business.facebook.com/adsmanager", "Ads Manager — budget check"),
            ("20:15", 46, "claude.ai/code", "Claude Code — after hours"),
        ]),
    ]
    out, n = [], 0
    for user, evs in day:
        for hhmm, mins, site, title in evs:
            if not site:            # explicit idle marker in the fixture → just skip, the
                continue            # gap detector will print it as ⚪ NO CAPTURE
            h, m = (int(x) for x in hhmm.split(":"))
            ts = datetime.datetime.combine(date, datetime.time(h, m))
            n += 1
            out.append({"Time": ts.strftime("%Y-%m-%d %H:%M:%S"), "User": user,
                        "Website": site, "Window Title": title,
                        "Session": f"DEMO{n:05d}", "Duration": str(mins * 60)})
    return out

# ── build ───────────────────────────────────────────────────────────────────
BARS = " ▁▂▃▄▅▆▇█"
def density(mins):
    if not mins: return "·"
    return BARS[max(1, min(8, int(round(mins / 60 * 8))))]   # any capture ≥ ▁, never blank

def main():
    a = sys.argv[1:]
    def opt(name, default=None):
        for x in a:
            if x.startswith(name + "="): return x.split("=", 1)[1]
        if name in a:
            i = a.index(name); return a[i+1] if i+1 < len(a) else True
        return default
    demo = "--demo" in a
    date = datetime.date.fromisoformat(opt("--date")) if opt("--date") else datetime.date.today()

    if demo:
        rows, sha, src_label = demo_rows(date), "DEMO", "**SYNTHETIC DEMO DATA — not real activity**"
    else:
        path, why = find_source(opt("--src"))
        if not path:
            print(f"✗ No Teramind data to build from ({why}).\n"
                  f"  Teramind → Reports → Web & Applications → {date} → Export CSV →\n"
                  f"  drop it in {INBOX.relative_to(REPO)}/ → re-run.\n"
                  f"  See the layout now:  python3 ops/tools/teramind_daily.py --demo")
            return 2
        rows = list(csv.DictReader(open(path, encoding="utf-8-sig")))
        sha = hashlib.sha256(pathlib.Path(path).read_bytes()).hexdigest()[:12]
        src_label = f"`{pathlib.Path(path).name}` · sha256 `{sha}` · {len(rows)} rows · {why}"

    tmpl = CFG["session_link_template"].strip()
    cols_seen = sorted(rows[0].keys()) if rows else []

    events, skipped = [], 0
    for r in rows:
        ts = parse_ts(pick(r, "ts"))
        if not ts or ts.date() != date:
            skipped += 1; continue
        raw_user = pick(r, "user")
        site, app, title = pick(r, "site"), pick(r, "app"), pick(r, "title")
        dur = parse_dur(pick(r, "dur"))
        end_ts = parse_ts(pick(r, "end")) or (ts + datetime.timedelta(seconds=dur))
        if not dur and end_ts > ts: dur = int((end_ts - ts).total_seconds())
        sess = pick(r, "sess")
        tag, is_flag = classify(f"{site} {app} {title}")
        cat, what = explain(site, app, title)
        link = ""
        ids = TM_IDS.get(canon(raw_user), {})
        if tmpl and (sess or ids):
            link = (tmpl.replace("{instance}", CFG["instance"]).replace("{session}", sess)
                        .replace("{userid}", ids.get("user_id", ""))
                        .replace("{computerid}", ids.get("computer_id", ""))
                        .replace("{user}", raw_user).replace("{ts}", ts.isoformat())
                        .replace("{date}", ts.date().isoformat())
                        .replace("{epoch}", str(int(ts.timestamp()))))
            if "userId=&" in link or "computerId=&" in link:
                link = ""      # id unknown for this person — plain text, never a broken link
        events.append(dict(ts=ts, end=end_ts, dur=dur, user=canon(raw_user), raw=raw_user,
                           site=site, app=app, title=title, sess=sess, link=link,
                           tag=tag, flag=is_flag, cat=cat, what=what))
    events.sort(key=lambda e: (e["ts"], e["user"]))

    def proof(e, label=None):
        lab = label or f"{e['ts']:%H:%M}"
        return f"[▶ {lab}]({e['link']})" if e["link"] else f"`{lab}`"

    by_user = collections.defaultdict(list)
    for e in events: by_user[e["user"]].append(e)
    present = [u for u in by_user]
    missing = [n for n in ROSTER if n not in present]
    extra = [u for u in present if u not in ROSTER]
    cols = [n for n in ROSTER if n in present] + sorted(extra)
    now = datetime.datetime.now()

    # gaps
    gaps = collections.defaultdict(list)
    for u, evs in by_user.items():
        for prev, nxt in zip(evs, evs[1:]):
            g = (nxt["ts"] - prev["end"]).total_seconds()
            if g >= GAP_MIN * 60: gaps[u].append((prev["end"], nxt["ts"], int(g)))

    problems = [e for e in events if e["flag"] and (WORK_START <= e["ts"].hour < WORK_END or e["user"] in UNBOUNDED)]
    offhours = [e for e in events if e["flag"] and e not in problems]

    L = []
    L.append(f"# 🖥 APW DAILY — the full day, minute by minute · {date:%A %b %d, %Y}")
    if demo:
        L.append("> 🧪 **DEMO PAGE — synthetic data.** Every number here is invented to show the format. "
                 f"Drop a real CSV in `ops/archive/teramind/inbox/` and re-run to replace it.\n")
    total_tracked = sum(e["dur"] for e in events)
    L.append(f"**{len(events)} events · {len(present)} of {len(ROSTER)} people · "
             f"{dur_str(total_tracked)} tracked · {len(problems)} problem(s) in-window · "
             f"work window {WORK_START:02d}:00–{WORK_END:02d}:00 {TZ}**")
    L.append(f"\n*Source: {src_label} · built {now:%Y-%m-%d %H:%M} · "
             f"[how to audit this page](#-7-verify-this-page)*")
    L.append(f"\n**Jump:** [1 Coverage](#-1-coverage-map--the-whole-day-at-a-glance) · "
             f"[2 Timetable](#-2-timetable--{INTERVAL}-minute-blocks) · "
             f"[3 All-hands stream](#-3-all-hands-stream--every-event-to-the-minute) · "
             f"[4 Full ledger](#-4-full-ledger--person-by-person) · "
             f"[5 Problems](#-5-problems--inside-the-work-window) · "
             f"[6 Analysis](#-6-analysis--where-the-time-went) · "
             f"[7 Verify](#-7-verify-this-page)\n")
    if not tmpl:
        L.append("> ⚠️ **Session-player links are OFF** — times render as plain `HH:MM` instead of ▶ jump links. "
                 f"Paste one real Teramind session URL into `session_link_template` in "
                 f"[CONFIG.json]({GH}/ops/data/teramind/CONFIG.json) and every timestamp on this page becomes a "
                 "click into the video. **A URL shape is never guessed.**\n")

    # ── 1 coverage map
    L.append("## 📶 1. COVERAGE MAP — the whole day at a glance\n")
    L.append("*Captured minutes per hour. `█` = a full hour captured, `·` = nothing captured at all.*\n")
    hours = list(range(min([e["ts"].hour for e in events], default=WORK_START),
                       max([e["end"].hour for e in events], default=WORK_END) + 1))
    L.append("| Person | " + " | ".join(f"{h:02d}" for h in hours) + " | Tracked | Gaps |")
    L.append("|---|" + "---|" * (len(hours) + 2))
    for u in cols:
        per_hour = collections.Counter()
        for e in by_user[u]:
            t = e["ts"]
            left = e["dur"]
            while left > 0:                       # split an event across hour boundaries
                room = 3600 - (t.minute * 60 + t.second)
                take = min(left, room)
                per_hour[t.hour] += take / 60
                t += datetime.timedelta(seconds=take); left -= take
        bar = " | ".join(density(per_hour.get(h, 0)) for h in hours)
        tot = sum(e["dur"] for e in by_user[u])
        L.append(f"| **{u}** | {bar} | {dur_str(tot)} | {len(gaps[u])} |")
    for u in missing:
        L.append(f"| {u} | " + " | ".join("·" for _ in hours) + " | — | ⚫ **NO DATA** |")
    if missing:
        L.append(f"\n**⚫ No data today ({len(missing)}):** {', '.join(missing)}. "
                 "*No events reached this export — that is **not** a claim they are unmonitored. "
                 "Absence in a report is never proof of absence of coverage (ruling #27); check the "
                 "Teramind Employees page before concluding anything.*")

    # ── 2 timetable
    L.append(f"\n## 🗓 2. TIMETABLE — {INTERVAL}-minute blocks\n")
    grid = collections.defaultdict(lambda: collections.defaultdict(list))
    for e in events:
        idx = ((e["ts"].hour * 60 + e["ts"].minute) - WORK_START * 60) // INTERVAL
        grid[WORK_START * 60 + idx * INTERVAL][e["user"]].append(e)
    window = list(range(WORK_START * 60, WORK_END * 60, INTERVAL))
    slots = sorted(set(window) | set(grid))
    L.append("| Time | " + " | ".join(cols) + " |")
    L.append("|---|" + "---|" * len(cols))
    for s in slots:
        lab = f"`{s//60:02d}:{s%60:02d}`" + ("" if s in window else " *(outside)*")
        row = [lab]
        for u in cols:
            evs = grid.get(s, {}).get(u, [])
            if not evs: row.append("—"); continue
            cats = collections.Counter(e["cat"] for e in evs)
            top = " · ".join(f"{c}" for c, _ in cats.most_common(2))
            mark = " 🔴" if any(e["flag"] for e in evs) else ""
            row.append(f"{proof(evs[0])} **{len(evs)}×** {top}{mark}")
        L.append("| " + " | ".join(row) + " |")
    L.append(f"\n*Cell = how many events in that block and what kind. The events themselves are in "
             f"[section 3](#-3-all-hands-stream--every-event-to-the-minute) and "
             f"[section 4](#-4-full-ledger--person-by-person). Blank = nothing captured. "
             f"Rows marked* **(outside)** *fall before {WORK_START:02d}:00 or after {WORK_END:02d}:00.*")

    # ── 3 all-hands stream
    L.append("\n## 🌊 3. ALL-HANDS STREAM — every event, to the minute\n")
    L.append(f"*Everyone, chronological, {len(events)} rows. This is the record; nothing is summarised away.*\n")
    L.append("| Proof | Start–End | Length | Person | What was being done | Where |")
    L.append("|---|---|---|---|---|---|")
    for e in events:
        mark = " 🔴" if e["flag"] else ""
        L.append(f"| {proof(e)} | {e['ts']:%H:%M:%S}–{e['end']:%H:%M:%S} | {dur_str(e['dur'])} "
                 f"| **{e['user']}** | {e['what']}{mark} | `{e['site'] or e['app'] or '—'}` |")

    # ── 4 full ledger
    L.append("\n## 📒 4. FULL LEDGER — person by person\n")
    for u in cols:
        evs = by_user[u]
        tot = sum(e["dur"] for e in evs)
        gp = gaps[u]
        L.append(f"### {u}")
        L.append(f"*{ROLE.get(u,'—')} · first `{evs[0]['ts']:%H:%M:%S}` · last `{evs[-1]['end']:%H:%M:%S}` · "
                 f"{len(evs)} events · {dur_str(tot)} captured · {len(gp)} gap(s) ≥{GAP_MIN}m · "
                 f"{sum(1 for e in evs if e['flag'])} flagged*\n")
        L.append("| Proof | Start–End | Length | What was being done | Where | Type |")
        L.append("|---|---|---|---|---|---|")
        merged = sorted([("e", e["ts"], e) for e in evs] + [("g", g[0], g) for g in gp], key=lambda x: x[1])
        for kind, _, item in merged:
            if kind == "e":
                e = item
                L.append(f"| {proof(e)} | {e['ts']:%H:%M:%S}–{e['end']:%H:%M:%S} | {dur_str(e['dur'])} "
                         f"| {e['what']} | `{e['site'] or e['app'] or '—'}` | {e['tag']} |")
            else:
                a_, b_, g = item
                L.append(f"| `{a_:%H:%M}` | {a_:%H:%M:%S}–{b_:%H:%M:%S} | **{dur_str(g)}** "
                         f"| ⚪ **NO CAPTURE** — nothing recorded in this window | — | ⚪ gap |")
        L.append("")
    for u in missing:
        L.append(f"### {u}\n*{ROLE.get(u,'—')} · **no events in this export.** "
                 "Not a coverage claim — see ruling #27.*\n")

    # ── 5 problems
    L.append("## 🚩 5. PROBLEMS — inside the work window\n")
    if problems:
        L.append("| Proof | Start–End | Length | Person | Flag | What was being done |")
        L.append("|---|---|---|---|---|---|")
        for e in sorted(problems, key=lambda e: e["ts"]):
            L.append(f"| {proof(e)} | {e['ts']:%H:%M:%S}–{e['end']:%H:%M:%S} | **{dur_str(e['dur'])}** "
                     f"| **{e['user']}** | {e['tag']} | {e['what']} |")
        tot = dur_str(sum(e['dur'] for e in problems))
        L.append(f"\n**Total flagged time in the work window: {tot}** across "
                 f"{len(set(e['user'] for e in problems))} people — "
                 + ", ".join(f"{u} ({dur_str(sum(e['dur'] for e in problems if e['user']==u))})"
                             for u in sorted(set(e['user'] for e in problems))) + ".")
    else:
        L.append(f"**None.** No flagged activity inside {WORK_START:02d}:00–{WORK_END:02d}:00 {TZ}.")
    if offhours:
        L.append(f"\n*{len(offhours)} flagged event(s) outside the work window "
                 f"({', '.join(sorted(set(e['user'] for e in offhours)))}) — recorded, not counted as problems.*")
    L.append("\n> **The rule** (ruling #29, Alan verbatim 9/3): *\"indeed, in glass stored and sip recruiter monster "
             "are all still flagged for everybody. Is only linked in.\"* — **linkedin.com is the only exemption and "
             "it is a SITE exemption.** Indeed · Glassdoor · ZipRecruiter · Monster are flagged for **everyone**, "
             "Alan included. There is no exempt-people list and none can be added.")

    # ── 6 analysis
    L.append("\n## 📊 6. ANALYSIS — where the time went\n")
    L.append("*Now that the record above is complete, this is what it adds up to.*\n")
    L.append("| Person | Captured | Longest unbroken stretch | Biggest gap | Top 3 by time |")
    L.append("|---|---|---|---|---|")
    for u in cols:
        evs = by_user[u]
        bycat = collections.Counter()
        for e in evs: bycat[e["cat"]] += e["dur"]
        top3 = " · ".join(f"{c} {dur_str(s)}" for c, s in bycat.most_common(3))
        longest = max(evs, key=lambda e: e["dur"])
        big = max(gaps[u], key=lambda g: g[2]) if gaps[u] else None
        L.append(f"| **{u}** | {dur_str(sum(e['dur'] for e in evs))} "
                 f"| {dur_str(longest['dur'])} — {shorten(longest['what'], 64)} ({proof(longest)}) "
                 f"| {(dur_str(big[2]) + f' at `{big[0]:%H:%M}`') if big else '—'} | {top3} |")
    L.append("\n### Time by category, everyone\n")
    allcat = collections.Counter()
    for e in events: allcat[e["cat"]] += e["dur"]
    L.append("| Category | Time | Share | Who |")
    L.append("|---|---|---|---|")
    for c, s in allcat.most_common():
        who = sorted({e["user"] for e in events if e["cat"] == c})
        L.append(f"| {c} | {dur_str(s)} | {s*100//max(total_tracked,1)}% | {', '.join(who)} |")

    # ── 7 verify
    L.append("\n## 🔍 7. VERIFY THIS PAGE\n")
    L.append("| What | Value |")
    L.append("|---|---|")
    L.append(f"| Source | {src_label} |")
    L.append(f"| Rows read | {len(rows)} |")
    L.append(f"| Events used (this date) | {len(events)} |")
    L.append(f"| Rows skipped (other date / unparseable time) | {skipped} |")
    L.append(f"| Columns the export actually had | `{'`, `'.join(cols_seen) or '—'}` |")
    L.append(f"| Roster | {len(ROSTER)} people, from [CONFIG.json]({GH}/ops/data/teramind/CONFIG.json) |")
    L.append(f"| Names seen not on the roster | {', '.join(extra) or 'none'} |")
    L.append(f"| Gap threshold | {GAP_MIN} minutes |")
    L.append(f"| Session links | {'ON' if tmpl else '**OFF** — no template set, nothing fabricated'} |")
    L.append(f"| Explanations | **derived** from the captured URL path + window title only — never inferred intent |")
    L.append(f"| Builder | [ops/tools/teramind_daily.py]({GH}/ops/tools/teramind_daily.py) |")
    L.append(f"| Built at | {now:%Y-%m-%d %H:%M} local |")
    L.append("\n*Rebuild any day: `python3 ops/tools/teramind_daily.py --date YYYY-MM-DD`*")

    md = "\n".join(L) + "\n"
    OUTDIR.mkdir(parents=True, exist_ok=True)
    outp = OUTDIR / f"{date.isoformat()}{'-DEMO' if demo else ''}.md"
    outp.write_text(md, encoding="utf-8")
    TODAY_PAGE.write_text(f"<!-- generated by ops/tools/teramind_daily.py — do not hand-edit -->\n{md}",
                          encoding="utf-8")

    print(f"✓ {outp.relative_to(REPO)}  ({len(events)} events, {len(cols)} people, "
          f"{sum(len(g) for g in gaps.values())} gaps, {len(md.splitlines())} lines)")
    print(f"✓ {TODAY_PAGE.relative_to(REPO)}")
    print("\n── SLACK DIGEST ──────────────────────────────────────────")
    print(f"*APW daily — {date:%a %b %d}* · {len(events)} events · {dur_str(total_tracked)} tracked · "
          f"{len(problems)} problem(s) in-window")
    for u in cols:
        evs = by_user[u]
        print(f"• *{u}* {evs[0]['ts']:%H:%M}–{evs[-1]['end']:%H:%M} · {dur_str(sum(e['dur'] for e in evs))} "
              f"· {len(evs)} events · {len(gaps[u])} gap(s) · "
              f"{sum(1 for e in evs if e['flag']) or 'no'} flagged")
    if missing:
        print(f"• _no data:_ {', '.join(missing)} (not a coverage claim — verify in Teramind)")
    print(f"Full page: {GH}/ops/data/TERAMIND_TODAY.md")
    print("──────────────────────────────────────────────────────────")
    return 0

if __name__ == "__main__":
    sys.exit(main())
