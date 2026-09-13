# 🔑 TERAMIND UNLOCK — the two things that weren't where we looked
*2026-09-03 · Lane 1 · verified against Teramind's own Knowledge Base and published API collection. Register #168.*

## 1. The API token is NOT under Settings — it's under your name
Teramind's KB, verbatim: *"Click the **Username** near the top-right corner of the Teramind Dashboard."* Then *"From the pop-up menu, select **Access tokens**"* → *"click the **ADD ACCESS TOKEN** button"* → name it → Done. Copy the token.
Source: [User Menu — kb.teramind.co/8817613](https://kb.teramind.co/en/articles/8817613-user-menu) · [How to use the Teramind API — 8791246](https://kb.teramind.co/en/articles/8791246-how-to-use-the-teramind-api)

The menu under your name has exactly four items: **My Profile · Download Teramind Agent · Access Tokens · Logout.** Your plan is **Teramind DLP** ([invoice 215808](https://mail.google.com/mail/u/0/#inbox/1a0273adc8bb59e2)), which includes the API.

**Then:** put it in `~/apw-intel/.env` as `TERAMIND_API_KEY=…` on the PC, or paste it in chat and Lane 1 stores it locally. Run `python3 ops/lane4/teramind_pull.py --check` — it prints your roster if the token works.

## 2. The export button — for the manual path
**BI REPORTS** (left nav) → **Applications & Websites** → green **EXPORT** button (top-right) → **CSV Export (Grid only)**.
To make it automatic by email: **EXPORT → Schedule export** → Enable Auto-Export → daily → time → `EXPORT TO EMAIL(S)` = support@ascendprimewealth.com → SAVE. Teramind requires you to **clone** the built-in report first (*"Please Clone dashboard first to configure scheduled export"*).
Source: [BI Reports — 8807080](https://kb.teramind.co/en/articles/8807080-bi-reports) · [Export / auto-deliver — 8791196](https://kb.teramind.co/en/articles/8791196-how-to-export-or-auto-deliver-bi-reports)

## 3. What the API actually gives us (from Teramind's Postman collection, 239 endpoints)
| Need | Endpoint | Proof |
|---|---|---|
| Base + auth | `https://ascendprimew.us.teramind.co/tm-api` · header `x-access-token` | collection `auth` block |
| Roster | `GET /tm-api/v1/agents` | returns agent_id, name, email, online |
| **Minute-level record — every person, every URL/title, time + idle** | `POST /tm-api/wip/tma-query` cube `activity`, dims `date·agent·computer·browser·title·url`, measures `count·time_s·idle_time_s` | the BI "Grid – Activity" query |
| Web & Applications report | `POST /tm-api/report/web-pages-applications/grid` `{periodStart, periodEnd}` (epoch) | the report behind the export button |
| Login sessions | `POST /tm-api/report/sessions/grid` | |
| Alerts with URL | `GET /tm-api/v1/alerts?periodStart&periodEnd` | |
| Work time / idle | `POST /tm-api/wip/tma-query` cube `work_time` | |
Archived: [postman_collection_TW74jRAB.json](https://github.com/Awake999/awake/blob/claude/new-session-1ofk4w/ops/archive/teramind/api/postman_collection_TW74jRAB.json) · pull script: [ops/lane4/teramind_pull.py](https://github.com/Awake999/awake/blob/claude/new-session-1ofk4w/ops/lane4/teramind_pull.py) — no more guessing base paths.

**With the token, the chain is:** `teramind_pull.py <date>` → CSV in `ops/archive/teramind/inbox/` → `teramind_daily.py --date <date>` → the full EODR/SODR page for everyone, with session-player links. Scheduled daily, it runs itself.
