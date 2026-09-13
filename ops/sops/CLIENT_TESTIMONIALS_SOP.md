# CLIENT TESTIMONIALS SOP — v1.0 (2026-09-07)

**Purpose.** Turn every positive thing a client said into a verifiable, clickable, verbatim record (`ops/data/CLIENT_TESTIMONIALS.md`) that setters, marketing, and Alan can use without re-listening to 300 calls — and that never puts words in a client's mouth.

**Skill.** This SOP is executable as the project skill `.claude/skills/client-testimonials/SKILL.md` (auto-loaded in every Claude session that starts inside this repo; invoke with `/client-testimonials` or by asking for testimonials). The skill is the procedure; this page is the law behind it.

## Laws
1. **Verbatim or nothing.** Quote text is copied from the transcript line or message body. `[…]` marks skipped words. Transcription typos stay.
2. **One link per row, to the spot.** Fathom: `fathom.video/calls/<n>?timestamp=<sec>`. GHL: the contact's detail URL. GHL phone transcript: the archived `transcript.md` (and audio if pulled).
3. **Six fields per row:** date · quote · source label · link · note · (speaker label if it is not the person's name).
4. **Recalled ≠ recorded.** Anything Alan remembers that is not found verbatim is listed in the Not-found table with what the record actually shows. Never promoted to a quote.
5. **Direction is data, not truth.** GHL marks Alan's email replies as inbound on threads. SMS direction is reliable; email must be read.
6. **Context travels with praise.** Praise in a hostile call, or a mixed message, carries a CONTEXT note or is excluded.
7. **Staff, coaches, brothers are not clients.** Constantine, Todd LoGuidice, team members are excluded.
8. **No public use without a consent row.** The doc is private; names go public only after a REGISTER row records consent.
9. **Sources swept are stated.** The doc lists exactly which source kinds were read (Fathom / GHL texts / GHL phone transcripts / Zoom / Krisp) and which were not, with the reason.
10. **Generated, never hand-edited.** Edit the data in `ops/tools/testimonials_build.py`; the md/json are outputs. `testimonials_verify.py` must pass before push.

## Source map
| Source | Where | Coverage today | How it gets there |
|---|---|---|---|
| Fathom (Zoom meetings) | live via Fathom MCP; 42 archived under `ops/archive/calls/fathom/` | Jun 21 → now | Archive grinder sessions |
| GHL SMS / email | `ops/archive/ghl/<date>/raw/messages_by_conversation.json` | to 2026-08-30 | `APW-PULL-ALL` step 2 on the PC |
| GHL phone-call transcriptions + audio | `ops/archive/ghl/recordings/` | **none yet** | `APW-PULL-ALL` step 2b (`ghl_pull_recordings.py`) on the PC |
| Zoom-cloud-only | `ops/archive/calls/zoom/` | 7 recordings | archived |
| Krisp | `ops/archive/calls/krisp/` | 9 coaching calls (not clients) | archived |

## Rerun trigger
Rerun the skill after any of: a new GHL export lands · `ops/archive/ghl/recordings/` appears or grows · a new client signs · Alan asks for a quote from a named person.

## Grade rubric for the run
A = every row links and verifies, not-found table honest, sources-swept stated · B = one of those missing · C = any paraphrase or any unverifiable row shipped.
