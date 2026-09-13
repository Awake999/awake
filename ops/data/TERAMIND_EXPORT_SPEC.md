# 📤 GET ME THE FULL TERAMIND DATA — three paths, fastest first (register #158)
*2026-09-03 · Alan: "Teramind traps everything. There's no reason why we can't have more info." **Correct.** Teramind captures apps, URLs, window titles, keystrokes, screen, and per-second active/idle. None of that reaches this session — the ONLY channel today is the marketing digest email, which is a top-3 teaser. This is a pipe problem, not a data problem. Below: how to open the pipe.*

---

## ⚡ PATH A — FULL DATA IN THE NEXT 5 MINUTES (manual export → Drive)
No API, no key, no scheduling, no waiting for tomorrow's digest.

1. Teramind → **Reports** → **Web & Application Usage** *(or **Time Records** / **Activity Log**)*
2. Date range: **Sep 1 – Sep 3** · Users: **All**
3. **Export → CSV**
4. Drop the file into **Google Drive** (any folder — the Drive connector is already live in this session)
5. Say "it's in Drive" — **I read it immediately and rebuild the timetable at full resolution today**, per person, per interval, with real app/URL time instead of self-reports.

**This is the shortest distance between the data existing and you seeing it analysed.** Everything else below is about making it automatic.

### ⚠️ MUST-HAVE COLUMN — the one that makes cells clickable
When exporting, **include the `Session ID` / `Record ID` column** (sometimes "Session", "Record", or "ID"). That field is what turns every cell in the timetable into a **hyperlink straight to the Teramind session player** for that moment — the video and detail for that exact interval.

**And send me ONE sample link:** open any session in Teramind, copy the URL from the address bar, paste it here. That single URL gives the shape (e.g. `https://<instance>/#/sessionplayer/<id>`), and from then on **every cell in every future timetable links automatically**. Until that sample exists, cells render as plain text — [the builder](https://github.com/Awake999/awake/blob/claude/new-session-1ofk4w/ops/tools/build_teramind_timetable.py) never fabricates a URL.

### The reports worth exporting, in priority order
| Report | What it unlocks | Why it matters here |
|---|---|---|
| **Web & Application Usage** | every app + URL + **time spent**, per user, timestamped | Kills the "149 websites, instance-wide" blindness — becomes per-person |
| **Time Records** | login/logout, **active vs idle**, per session | Fixes ML's 21% and Alan's 43% — shows call time as work |
| **Activity Log / Session details** | window titles + URL, near-continuous | Fills the 09:30–14:30 five-hour gap in the current chart |
| **Behavior Alerts** | every rule hit, per user, timestamped | The real job-search / Glassdoor / Indeed answer |
| **Productivity** | productive vs unproductive split | Only meaningful AFTER the app classification is applied |

---

## 🔁 PATH B — MAKE IT AUTOMATIC (the scheduled BI report)
Teramind → **BI Reports** → **+ Create**

**Report 1 — "APW Interval Activity"**
- Fields: `user` · `date` · `time (interval start)` · `active time` · `idle time` · `productive time` · `application` · `website/URL` · `window title`
- Group by: **User**, then **Time**
- Granularity: **10 minutes** (5 if offered)
- Filter: none — all users
- **Schedule: every 4 hours** (or hourly) → **CSV** → **support@ascendprimewealth.com**

**Report 2 — "APW Alerts"**
- Fields: `user` · `timestamp` · `rule` · `application/URL` · `action taken`
- **Schedule: daily 9 PM PT** → CSV → support@

Both land in the inbox this session already sweeps. From the first delivery, the daily timetable is machine-built at 10-minute resolution — no self-reports required.

---

## 🔌 PATH C — LIVE (already written, needs one install)
[`ops/lane4/teramind_pull.py`](https://github.com/Awake999/awake/blob/claude/new-session-1ofk4w/ops/lane4/teramind_pull.py) (commits history to the repo) and [`ops/mcp/teramind_mcp_server.py`](https://github.com/Awake999/awake/blob/claude/new-session-1ofk4w/ops/mcp/teramind_mcp_server.py) (live querying, `mcp__teramind__timeline` at any interval). Both need `TERAMIND_API_KEY` in `~/apw-intel/.env` and one `--discover` run. See [the three-rail SOP](https://github.com/Awake999/awake/blob/claude/new-session-1ofk4w/ops/data/TERAMIND_TRUE_LOGS_SOP.md).

---

## ⚙️ AND FIX THESE, OR THE PRECISION LIES
Full-resolution data through an uncalibrated instrument is precise nonsense. Before or alongside the export:
1. **Apply the app classification** — [the list](https://github.com/Awake999/awake/blob/claude/new-session-1ofk4w/ops/data/TERAMIND_APP_CLASSIFICATION.md), ~15 min
2. **Exclude Zoom/Meet from idle detection** — the single highest-impact setting
3. **Raise idle timeout to 10+ min**
4. **Turn ON IM capture** — off 4 days running; most team coordination is invisible
5. **Owner exemption on the "job search websites" rule** — it already false-positived on Alan's own hiring research
