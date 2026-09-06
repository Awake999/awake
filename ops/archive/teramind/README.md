# 🖥 TERAMIND — everything we hold (pre-cancellation export, register #174)

> 🧭 [Start Here](../START-HERE.md) · [Archive home](../README.md)

**Alan, 2026-09-06 01:3xZ:** *"download all data from teramind right now before i cancel my subscription, store it somewhere in the git hub"*

## What is in this folder NOW (pulled from Gmail, no login needed)
| Folder / file | What | Coverage |
|---|---|---|
| [digests/DIGESTS_ALL.json](digests/DIGESTS_ALL.json) | every daily **Snapshot** digest: alerts, emails in/out per user, IM, printed, websites + minutes (top-3), activity % (headline + **top-3 leaderboard**, ruling #27), new users | **48 days** (44 re-parsed here + Aug 29–Sep 1 in the legacy block), Jul 7 → Sep 4 (no digest exists in Gmail for Jul 13–21, Aug 15, Aug 22–23) |
| [alerts/ALERTS_ALL.json](alerts/ALERTS_ALL.json) | every rule-violation alert email, verbatim detail + **player deep-link** + Gmail source | **49 alerts** Jul 7 → Sep 4 (blossom 36 · Anne 9 · Alan 2 · Lynn 2) |
| [api/postman_collection_TW74jRAB.json](api/postman_collection_TW74jRAB.json) | Teramind's own API collection, 239 endpoints | — |
| [2026-08-31/](2026-08-31/) | the one UI pull (employees page, licence count) | Aug 31 |
| [export/](export/) | **the full API export lands here** (`teramind_pull.py --all`) | empty until a token exists |

## What is NOT here yet and needs ONE thing from Alan
Everything behind the login — minute-level activity per person, web/app grids, sessions, keystrokes, file transfers, printing, audit log, **screen recordings** — is reachable only with an API token or a signed-in browser.

**Fastest path (you are logged in right now — a single-use code was sent 01:14Z):**
1. Teramind → click your **username (top-right)** → **Access Tokens** → **ADD ACCESS TOKEN**.
2. On the PC: paste it into `~/apw-intel/.env` as `TERAMIND_API_KEY=…` and run
   `python3 ops/lane4/teramind_pull.py --check` then `python3 ops/lane4/teramind_pull.py --all 2026-07-07`
   → every table for every day → `ops/archive/teramind/export/` → `git add/commit/push`.
3. Video: `--all` requests a server-side export per computer per day; run `--video-download` ~30 min later. MP4s stay on disk + Drive (GitHub caps at 100 MB); the index commits.

**Manual fallback (no token):** BI REPORTS → Applications & Websites → EXPORT → CSV; Reports → Sessions → export; Configure → Behavior Policies → export. Drop the files in `export/manual/` or Drive.

**Do not cancel until `export/EXPORT_LOG.txt` says DONE** — Teramind deletes tenant data on cancellation.
