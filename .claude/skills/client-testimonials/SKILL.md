---
name: client-testimonials
description: Pull verbatim positive client quotes (testimonials) from Fathom call transcripts, GHL texts/emails, and GHL phone-call transcriptions into ops/data/CLIENT_TESTIMONIALS.md with a second-level jump link per quote. Use when Alan asks for testimonials, positive feedback, client quotes, "what did X say about us", marketing proof, or to refresh the testimonials doc after a new GHL/Fathom pull.
---

# Client testimonials — reusable procedure

The law: **every quote is verbatim, dated, named, source-labelled, and clickable to the exact spot.**
Nothing paraphrased. Anything Alan remembers that the record does not contain goes in the
"Not found" table, never into a quote. Full SOP: `ops/sops/CLIENT_TESTIMONIALS_SOP.md`.

## Files you touch
| File | Role |
|---|---|
| `ops/tools/testimonials_build.py` | THE data table (`CLIENTS`, `NOT_FOUND`, `EXCLUDED`, `CALLS`). Edit here only. |
| `ops/data/CLIENT_TESTIMONIALS.md` / `.json` | Generated. Never hand-edit. |
| `ops/tools/testimonials_verify.py` | Byte-checks every row against the raw source that is in the repo. |
| `ops/archive/ghl/<date>/raw/messages_by_conversation.json` | GHL texts/emails (inbound only). |
| `ops/archive/ghl/recordings/` | GHL phone-call transcriptions (exists only after the PC launcher ran step 2b). |
| `ops/archive/calls/{fathom,zoom,krisp}/` | Archived meeting transcripts. |

## Procedure (do all steps, in order)
1. **Register first.** Add the ask verbatim as a numbered REGISTER row before working.
2. **Enumerate sources, do not assume.** Run `ls ops/archive/ghl/` (newest export), `ls ops/archive/ghl/recordings/ 2>/dev/null`, and `mcp__Fathom__list_meetings` (created_after = first client date, max_pages 10, follow `next_cursor` until exhausted). State in the doc which of the three source kinds you actually swept.
3. **Fathom id rule.** `get_meeting_transcript` takes the `id:` field from `list_meetings`, NOT the number in `fathom.video/calls/<n>`. Jump link = `https://fathom.video/calls/<url-number>?timestamp=<seconds>` from the transcript output. Fetch max 3 transcripts per call; large results persist to a file — read them with grep, never skip.
4. **Sweep, then hand-read.** Keyword sweep (`amazing|awesome|wonderful|incredible|impress|appreciate|thank|grateful|godsend|the man|best|patient|smart|honest|10/10…`) on client-speaker lines only (exclude Alan/Carla/Lynn/Sabrina/staff). Then open every hit in context. Drop bare acknowledgements ("Okay, awesome", "Perfect.") unless attached to an evaluative sentence.
5. **GHL direction is unreliable on emails.** Only trust `direction == "inbound"` for SMS (`type == 2`). For emails, confirm the body is client-authored (Alan's replies get stored as inbound on reply chains). Quote nothing from automation.
6. **Speaker labels lie.** "iPad", "iPhone", "nazsa", "84844626214" are clients on their devices. Identify from context, record the label in the Note column.
7. **Context rule.** Praise inside a tense or negative exchange gets a `CONTEXT:` note or is excluded. Mixed messages (10/10 work, 2/10 communication) are quoted whole or not at all.
8. **Add rows** to `CLIENTS` in the builder: `(date, quote, source, link, note)`. Source ∈ {`Fathom audio transcript`, `GHL SMS`, `GHL email`, `GHL phone call (GHL transcription)`}. Use `[…]` for skipped words, never reword. Add the call to `CALLS`.
9. **Not-found table.** Every phrase Alan recalled that you could not find verbatim goes into `NOT_FOUND` with what the record actually shows (e.g. "saint" = the company Credit Saint) and links to the nearest real line.
10. **Build + verify.** `python3 ops/tools/testimonials_build.py` (fails if any row lacks a link) then `python3 ops/tools/testimonials_verify.py` — must report 0 mismatches for rows whose source is in the repo; rows verified only against a live Fathom fetch are listed as "verified live, not in repo".
11. **Ship.** Commit builder + generated md/json + REGISTER row + process-log line; push; reply through `ops/RESPONSE_TEMPLATE.md` and `python3 ops/tools/reply_check.py <draft>`.

## Reply shape
Lead with counts (quotes, people, per-source split) and the strongest 5 lines with jump links; then the honest not-found list; then consent note (no client has agreed to public use unless a REGISTER row says so).

## Never
- Never invent or "clean up" a quote; Fathom typos stay ("Your incredible").
- Never quote Alan's own outbound text as a client.
- Never publish names outside the private repo without a consent row.
