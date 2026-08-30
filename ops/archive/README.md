# APW Archive — the canonical data store

> 🧭 **New here? → [START HERE — the beginner-friendly landing page](START-HERE.md)** · hubs: [📞 Calls](calls/README.md) · [💬 Slack](slack/README.md) · [🧑 People](people/README.md)

**One rule: originals are sacred.** Summaries live NEXT TO transcripts, never instead of them. Nothing in here is ever rewritten or deleted — only added.

This folder is the hard-data backup of every conversation Ascend Prime Wealth has: sales calls, coaching calls, Slack threads, voice notes, and (via local deposit) GHL messages. It is plain markdown, Obsidian-compatible, backed up four ways at once: locally (your clone), on GitHub (private remote = cloud backup), in Obsidian (open this repo as a vault), and indexed in the cloud (Drive pointer to the indexes).

## Find what you need in one hop

| I want… | Go to |
|---|---|
| A specific call (Fathom) | `calls/fathom/INDEX.md` → every meeting, dated, linked, archive status |
| A specific call (Krisp) | `calls/krisp/INDEX.md` |
| Everything about one person | `people/<first-last>/index.md` — every call, thread, and file they appear in |
| A Slack conversation | `slack/channels/<channel>/YYYY-MM.md` — chronological, author-stamped |
| A Slack voice note | `slack/audio/README.md` — inventory + transcription status |
| GHL messages/audio | `ghl/README.md` — machine-bound; deposit instructions for the local session |
| Work on this from a new device / another chat | `SYNC.md` — the five rules that make simultaneous multi-device work loss-proof |
| Format/transcribe anything new (chapters, TOCs, splits) | [`SOP-formatting.md`](SOP-formatting.md) — the formatting + transcription SOP; tools live in [`tools/`](tools/) |

## How a call folder is laid out

```
calls/fathom/YYYY-MM-DD--short-title--recordingid/
  transcript.md   ← the ORIGINAL, verbatim, full transcript
  summary.md      ← AI companion summary — clearly labeled, never a replacement
  meta.md         ← date, attendees, fathom.video link, related Notion rows
```

Krisp calls use the identical pattern under `calls/krisp/`.

## Naming conventions (so Obsidian and humans both work)

- Folder dates are `YYYY-MM-DD` so everything sorts chronologically for free.
- No colons, slashes, or special characters in file/folder names.
- People folders are `first-last` lowercase (e.g. `people/constantine/`).
- Slack exports are one file per channel per month.

## Rules for every lane (and every human) contributing here

1. **Append-only.** Never rewrite or delete an existing archive file. Corrections get a new dated note beside the original.
2. **Transcript + summary in tandem.** A summary without its verbatim transcript in the same folder is incomplete.
3. **Verbatim means verbatim.** Full fidelity, full names, exact words — this is a private repo and that is by Alan's direction. Never publish anything from this archive to any public surface.
4. **Update the INDEX when you add a call.** `calls/fathom/INDEX.md` and `calls/krisp/INDEX.md` are the resume points for archiving runs.
5. **Small frequent commits.** Commits are the backup.

## Where the other truth lives

This archive stores *conversations*. Structured data (lead tables, checklists, SOPs) lives in Notion — IDs for everything are in `../data/pointer-map.md`. The ops vault map is `../README.md`.
