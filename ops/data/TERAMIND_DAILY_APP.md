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

## What the page shows, in this order

1. **WHOLE PICTURE** — every monitored person on one screen: role · first seen · last seen · tracked time · events · problem count. Anyone on the roster with **zero events is printed as ⚫ NO DATA**, never dropped, because absence from an export is not proof of absence of monitoring ([ruling #27](https://github.com/Awake999/awake/blob/claude/new-session-1ofk4w/ops/RULINGS.md)).
2. **SIDE BY SIDE** — 50-minute intervals across 07:00–17:00 PST, everyone in parallel columns. Every block in the window is printed even when empty, so gaps are visible instead of invisible. Blocks outside the window are shown and labelled *(outside)*, not hidden — that's Alan's own after-hours time.
3. **PROBLEM LIST** — flagged activity inside the work window: proof link first, then time, person, flag, what.
4. **PERSON BY PERSON** — where each person's time actually went, ranked, with the first-hit proof link on every row.
5. **VERIFY THIS PAGE** — source filename, sha256, rows read / used / skipped, the columns the export actually had, roster size, names seen that aren't on the roster, and whether session links were on. Every page can be audited without asking anyone.

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
