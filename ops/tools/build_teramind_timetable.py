#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the side-by-side timetable from a Teramind CSV export — every cell
hyperlinked back to the Teramind session player for that moment.

    python3 ops/tools/build_teramind_timetable.py export.csv --date 2026-09-02
    python3 ops/tools/build_teramind_timetable.py export.csv --interval 50 --out ops/data/TIMETABLE_2026-09-02.md

DEEP LINKS: Teramind's session-player URL shape differs by version, so this does
NOT guess one. Paste ONE real session URL from the address bar into
TERAMIND_LINK_TEMPLATE below (or pass --link-template) and every cell links.
Placeholders available: {session}, {user}, {ts}, {date}, {epoch}.
Example shapes seen in the wild:
    https://{instance}/#/sessionplayer/{session}
    https://{instance}/v2/session-player?session={session}&t={epoch}
Until a template is set, cells render as plain text — never as a fabricated link.
"""
import csv, sys, os, re, datetime, collections

INSTANCE = "ascendprimew.us.teramind.co"
TERAMIND_LINK_TEMPLATE = ""   # ← paste one real session URL shape here

WORK_START, WORK_END = 7, 17          # 07:00–17:00 PST
FLAG_PATTERNS = [                      # work-hours problem list
    (r"glassdoor|indeed\.com|ziprecruiter|monster\.com|careerbuilder", "🔴 job search"),
    (r"netflix|hulu|disneyplus|twitch\.tv", "🔴 streaming"),
    (r"chess\.com|steampowered|roblox|epicgames", "🔴 gaming"),
]
# Alan's ruling 9/3, verbatim: "indeed, glassdoor and zip recruiter monster are all still
# flagged for everybody. Is only linked in." → LinkedIn is the ONLY exemption, and it is a
# SITE exemption, not a person exemption. NO user is exempt from job-search flagging.
EXEMPT_USERS_JOBSEARCH = set()   # nobody — Alan included

def pick(row, *names):
    for n in names:
        for k in row:
            if k and k.strip().lower() == n:
                return row[k]
    return ""

def parse_ts(s):
    s = (s or "").strip()
    for f in ("%Y-%m-%d %H:%M:%S", "%Y-%m-%dT%H:%M:%S", "%m/%d/%Y %H:%M:%S",
              "%m/%d/%Y %I:%M:%S %p", "%Y-%m-%d %H:%M"):
        try:
            return datetime.datetime.strptime(s[:19], f)
        except ValueError:
            continue
    return None

def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__); return 1
    path = args[0]
    interval = int(next((a.split("=")[1] for a in args if a.startswith("--interval=")), 50))
    tmpl = next((a.split("=", 1)[1] for a in args if a.startswith("--link-template=")), TERAMIND_LINK_TEMPLATE)
    out = next((a.split("=", 1)[1] for a in args if a.startswith("--out=")), None)

    rows = list(csv.DictReader(open(path, encoding="utf-8-sig")))
    if not rows:
        print("✗ empty export"); return 1
    print(f"columns seen: {sorted(rows[0].keys())}\n")

    buckets = collections.defaultdict(lambda: collections.defaultdict(list))
    users, flags = set(), []
    for r in rows:
        ts = parse_ts(pick(r, "time", "timestamp", "date/time", "start time", "interval"))
        if not ts:
            continue
        user = (pick(r, "user", "employee", "username", "agent") or "?").strip()
        app = (pick(r, "application", "app", "process") or "").strip()
        site = (pick(r, "website", "url", "domain", "web page") or "").strip()
        title = (pick(r, "window title", "title", "activity") or "").strip()
        sess = (pick(r, "session", "session id", "record id", "id") or "").strip()
        users.add(user)
        label = site or app or title or "activity"
        mins = ts.hour * 60 + ts.minute
        slot = (mins // interval) * interval
        key = f"{slot//60:02d}:{slot%60:02d}"
        cell = label[:38]
        if tmpl and sess:
            url = (tmpl.replace("{instance}", INSTANCE).replace("{session}", sess)
                       .replace("{user}", user).replace("{ts}", ts.isoformat())
                       .replace("{date}", ts.date().isoformat())
                       .replace("{epoch}", str(int(ts.timestamp()))))
            cell = f"[{cell}]({url})"
        buckets[key][user].append(cell)
        # work-hours problem detection
        hay = f"{site} {app} {title}".lower()
        for pat, tag in FLAG_PATTERNS:
            if re.search(pat, hay):
                in_hours = WORK_START <= ts.hour < WORK_END
                exempt = False   # ruling 9/3: no person-level exemption for job-search sites
                flags.append((ts, user, tag, label, in_hours, exempt, cell))

    users = sorted(users)
    lines = [f"# 🗓 TERAMIND TIMETABLE — {interval}-minute intervals",
             f"*Built from `{os.path.basename(path)}` · {len(rows)} rows · work window {WORK_START:02d}:00–{WORK_END:02d}:00 PST*", ""]
    if not tmpl:
        lines += ["> ⚠️ **No session-player link template set** — cells are plain text. "
                  "Paste one real Teramind session URL into `TERAMIND_LINK_TEMPLATE` "
                  "(or pass `--link-template=`) and every cell becomes clickable. "
                  "No link is ever fabricated.", ""]
    lines += ["| Time | " + " | ".join(users) + " |",
              "|---|" + "---|" * len(users)]
    for slot in sorted(buckets):
        row = [slot]
        for u in users:
            items = buckets[slot].get(u, [])
            seen, uniq = set(), []
            for i in items:
                if i not in seen:
                    seen.add(i); uniq.append(i)
            row.append(" · ".join(uniq[:4]) or "—")
        lines.append("| " + " | ".join(row) + " |")

    lines += ["", "## ⚠️ PROBLEM LIST — during work hours"]
    during = [f for f in flags if f[4] and not f[5]]
    outside = [f for f in flags if not f[4]]
    exempted = [f for f in flags if f[5]]
    if during:
        lines.append("| Time | Person | Flag | What | Proof |")
        lines.append("|---|---|---|---|---|")
        for ts, u, tag, lbl, _, _, cell in sorted(during):
            lines.append(f"| {ts:%H:%M} | {u} | {tag} | {lbl[:40]} | {cell} |")
    else:
        lines.append("**None detected in the work window.**")
    if outside:
        lines.append(f"\n*{len(outside)} hit(s) outside {WORK_START:02d}:00–{WORK_END:02d}:00 — not flagged, per Alan's rule.*")
    lines.append("\n*LinkedIn is never flagged (Alan assigned the hiring campaign). "
                 "Glassdoor · Indeed · ZipRecruiter · Monster are flagged for EVERYONE, Alan included — ruling 9/3.*")

    md = "\n".join(lines) + "\n"
    if out:
        open(out, "w", encoding="utf-8").write(md)
        print(f"✓ wrote {out}  ({len(users)} people, {len(buckets)} intervals, {len(during)} in-hours flags)")
    else:
        print(md)
    return 0

if __name__ == "__main__":
    sys.exit(main())
