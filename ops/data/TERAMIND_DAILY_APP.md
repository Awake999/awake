# 🖥 APW DAILY — the Teramind app

**One command. One page. Anyone who opens it knows what everyone did today, with proof next to every claim.**

| | |
|---|---|
| **Open today's page** | [ops/data/TERAMIND_TODAY.md](https://github.com/Awake999/awake/blob/claude/new-session-1ofk4w/ops/data/TERAMIND_TODAY.md) — always the latest build |
| **See the layout right now** | [2026-09-03-DEMO.md](https://github.com/Awake999/awake/blob/claude/new-session-1ofk4w/ops/data/teramind/2026-09-03-DEMO.md) — synthetic data, real layout |
| **Run it (Windows)** | double-click [`ops/lane4/APW-DAILY.bat`](https://github.com/Awake999/awake/blob/claude/new-session-1ofk4w/ops/lane4/APW-DAILY.bat) |
| **Run it (Mac/Linux)** | `./ops/lane4/APW-DAILY.sh` |
| **Any past day** | `python3 ops/tools/teramind_daily.py --date 2026-09-02` |
| **Change roster / rules / links** | [ops/data/teramind/CONFIG.json](https://github.com/Awake999/awake/blob/claude/new-session-1ofk4w/ops/data/teramind/CONFIG.json) — edit this, never the code |

---

## What the page shows, in this order — **record first, analysis second**

| § | Section | What it gives you |
|---|---|---|
| 1 | **COVERAGE MAP** | Hour-by-hour density bar per person. `█` a full hour captured, `·` nothing. The whole day, everyone, in one strip. |
| 2 | **TIMETABLE** | 50-minute side-by-side blocks anchored to 07:00. Each cell: how many events and what kind, with a proof link. |
| 3 | **ALL-HANDS STREAM** | **Every event, everyone, chronological, to the second.** Start–End · length · person · what was being done · where. Nothing summarised away. |
| 4 | **FULL LEDGER** | Per person, the complete day: every event *and every gap*. A gap over 4 minutes prints as ⚪ **NO CAPTURE** with its length — silence is shown, never closed over. |
| 5 | **PROBLEMS** | Flagged activity inside the work window, proof first, with total flagged time per person. |
| 6 | **ANALYSIS** | Only after the record: captured time, longest unbroken stretch, biggest gap, top categories per person, and time-by-category across everyone. |
| 7 | **VERIFY** | Source file + sha256, rows read / used / skipped, the exact columns the export had, off-roster names, gap threshold, links on/off. |

## "What was being done" — derived, never invented

Every row carries a plain-English explanation built **only from what Teramind captured**: the URL path and the window title.

- `app.gohighlevel.com/conversations` + title `Conversation — Teresa Graham (SMS)` → **GHL — working the conversation inbox (SMS/email threads) — "Conversation — Teresa Graham (SMS)"**
- `zoom.us/j/8842013` + title `Triage call — Karl Ruiz` → **On a Zoom call — "Triage call — Karl Ruiz"**
- `indeed.com/jobs?q=...` → **Job-search site — on a job listing page — "..."** 🔴

If a row has no title and no recognisable URL, it says so — *"no title or URL captured — intent unknown"* — rather than guessing what someone was doing. The mapping lives in `explain_rules` and `url_hints` in CONFIG.json, so it is editable and auditable.


## The rules it enforces (so it can't drift)

- **Proof in front.** The proof link is the **first** column of every table, not the last.
- **No invented links.** Until one real Teramind session-player URL is pasted into `session_link_template`, times render as plain `HH:MM`. The app never guesses a URL shape.
- **Job search:** `linkedin.com` is the **only** exemption and it is a **site** exemption. Indeed · Glassdoor · ZipRecruiter · Monster stay flagged for **everyone, Alan included** — [ruling #29](https://github.com/Awake999/awake/blob/claude/new-session-1ofk4w/ops/RULINGS.md). There is no list of exempt people and there must never be one.
- **Alan's hours are unbounded** by his own statement ("I'm here until I go to sleep") — after-hours activity is shown, never counted as a violation.
- **Names with every count** — no number appears without the people behind it.

---

## 🔑 To make it fully live — two things, both quick

| # | What | Who | Why it's blocked |
|---|---|---|---|
| 1 | **A data source.** Either (a) export CSV: Teramind → Reports → Web & Applications → today → Export, saved into `ops/archive/teramind/inbox/`; or (b) put `TERAMIND_API_KEY` in `~/apw-intel/.env` and run `python3 ops/lane4/teramind_pull.py --discover` once | Lane 4 (Alan's PC) | Cloud lanes have no path to the Teramind instance or the key — the key is local-only by design |
| 2 | **One session-player URL.** Open any recorded session in Teramind, copy the address bar, paste it into `session_link_template` in CONFIG.json | Alan, 10 seconds | The URL shape differs by Teramind version; guessing it would fabricate evidence |

With #1 the page is real. With #2 every timestamp on it becomes a click that jumps to the video.

**Daily rhythm:** run the launcher once each morning → the page rebuilds, commits and pushes itself → the Slack digest prints to the terminal, ready to paste.
