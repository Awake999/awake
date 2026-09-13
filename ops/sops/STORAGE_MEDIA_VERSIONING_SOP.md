# STORAGE, MEDIA & VERSIONING SOP (Lane 4 draft 8/31 - Lane 1 to ratify into SOP.md)
*Alan's ruling: Drive for audio via shareable folder; Notion in addition where it fits; dated versioned states so nothing breaks and we can always reroll.*

## 1. Where each thing lives (one home each, pointers everywhere else)
| Data | Canonical home | Why | Pointers |
|---|---|---|---|
| Code, SOPs, logs, canon, derived CSVs, transcripts (text) | **GitHub private repo** (`ops/`) | versioned, mergeable, every lane syncs it | Notion + board link to raw files |
| Audio recordings (calls, voice memos, Looms) | **Drive folder [APW Audio Recordings](https://drive.google.com/drive/folders/1UWmGoq4o3KbNOnIxIty0PnuxexPEbUBI)** | git is wrong for binary media (100MB/file cap, repo bloat) | repo + Notion store the Drive link + the TRANSCRIPT text |
| Meeting recordings + native transcripts | **Fathom / Krisp** (they already host + transcribe) | never re-host what the source system serves | Call Library links; transcript text archived to repo |
| Numbers on any surface | **CANON_NUMBERS.json** | Canon Law | board/register bake from it |
| Payments truth | **Whop** | GHL payments empty (verified) | canon carries pending markers until wired |

## 2. Temporary storage during transcription (Alan's question, answered honestly)
- TODAY nothing is downloaded: GHL has ZERO call recordings (verified 8/31 - recording is off), and Fathom/Krisp deliver transcripts as text over their APIs; no audio ever touches a disk.
- WHEN we do pull audio (Slack voice memos, future GHL recordings): it downloads to the working machine's session scratchpad (temp), gets transcribed, then AUDIO -> the Drive folder above, TRANSCRIPT (text) -> `ops/archive/<source>/<date>/`, temp copy deleted. Raw audio never enters git.
- Summary-in-synchrony law applies: transcript = raw; any summary sits BESIDE it, never replaces it.

## 3. Notion's role + its real limits
- Use Notion for: the editable tracker (master), SOP mirrors, pointers, per-person pages. Fine at our scale.
- Hard limits that bite: **file uploads capped ~5MB/file below Business tier** (audio mostly won't fit - link to Drive instead); API ~3 requests/sec; the SQL query quota we already hit (register #85 - live board falls back to snapshot until Business).
- Rule: Notion stores TEXT + LINKS, never binary media. Audio in Notion = a Drive link.

## 4. Versioned states (nothing breaks, always re-rollable)
- Every pull writes to its own dated folder: `ops/archive/<source>/<YYYY-MM-DD>/raw/...` - prior dates are IMMUTABLE, never edited or deleted.
- Derived artifacts regenerate per date beside the raw (`*_<date>.csv`); CANON_NUMBERS.json carries its pull_date; git history is the version chain (every state recoverable via `git log` / checkout).
- Generated pages (board, hub) rebuild from raw at any past date by rerunning the builder with that date argument - reroll is one command.

## 5. Cross-lane git ritual (restated as law)
Pull (rebase) BEFORE work -> commit small -> push after every batch -> conflicts resolved by taking the other lane's file and re-applying your generator (idempotent markers), never hand-merging generated content -> LANE-SYNC notes in your own process log for anything another lane must know.
