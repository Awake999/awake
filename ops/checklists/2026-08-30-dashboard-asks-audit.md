# DASHBOARD LANE — ASKED vs ACTUALLY COMPLETED (audit, 2026-08-30)

> Alan (8/30, late): "we're going to have to go back and make sure everything was actually
> done… actually see what was asked and what was actually completed."
> One line per ask. Statuses: ✅ done+verified · 🟡 partial · ❌ not done · 🔒 blocked on data
> owner (Lane 1 = Notion, Lane 4 = GHL; Lane 2 never writes those — Alan's hard rule).
> Sources: `ops/prompts/*.md` (raw originals), `ops/process-log/2026-08-30-dashboard-lane.md`,
> board v6.8 = commit 5f90451, live at
> https://claude.ai/code/artifact/c6ad801c-50fc-49d3-847a-e6a8b0ddd392

## Design / experience asks
| # | Ask (Alan's words) | Status | Evidence |
|---|---|---|---|
| 1 | "organized, easy, with visuals, graphs, charts, images / icons… simplicity UI, with the opportunity to go advanced" | ✅ | 7 tabs, icon headers, expandable rows, explorer drill-down |
| 2 | brand colors; "I don't like the orange… disgusting"; "purple, purple light purple" not pink | ✅ | tokens; palette validator ALL-PASS both themes |
| 3 | dark background; later "toggle… dark mode, to liquid glass white / pure mode" | ✅ | PURE toggle, persisted |
| 4 | "put the actual logo," centered | ✅ | real logo embedded (data URI) |
| 5 | "tony stark future" reactivity: plexus heavenly colors, moving gradient edges, instant lift, "all 3D," glass | ✅ | conic rings, tilt engine, glass tokens |
| 6 | "clickable URL, not just freaking digits" | ✅ | full links everywhere since |
| 7 | tables "glitches out… unusable" → no tilt on data; no sideways scrolling; mobile | ✅ | data-no-tilt; 0px overflow verified 390px |
| 8 | tap-to-correct must be beginner-obvious: instant hover popups, big before→after change display, "does it save?" clarity | ❌ → v6.9 | today's ask |
| 9 | results "highlighted and colorful… also at the bottom somewhere" | ❌ → v6.9 | today's ask |

## Data-view asks
| # | Ask | Status | Evidence |
|---|---|---|---|
| 10 | "literally every single person… the date that they came in," newest-first, date windows | ✅ live / 🟡 | live roster + windows; historical *time-of-contact* exists only where GHL has it |
| 11 | "why don't we have the data from Lane 4… number of leads" / "all our leads" | ✅ | universe toggle +259 GHL |
| 12 | "one big sync system, not fragmented" | ✅ / 🟡 ongoing | single repo file → both URLs; lane merges done; discipline is forever-work |
| 13 | "prospect query failed" | ✅ | merged single watch; honest quota copy (workspace SQL cap remains a Notion-plan limit) |
| 14 | "the show rate is BS… make it easy for me to modularly modify" | ✅ | tap-to-correct verdicts + pending-sync panel |
| 15 | booked calls show/no-show + rates + common toggles | ✅ | chips + rate strip |

## Sequence-spec asks (8-stage dictation)
| # | Ask | Status | Evidence |
|---|---|---|---|
| 16 | 8 stages rendered with what's tracked vs missing | ✅ | The Sequence (Funnel tab) |
| 17 | **filters/fields for**: intro text y/n · connected/double-dial · voicemail+text follow-up · BAMFAM'd · contact attempts + methods · out-of-hours time-to-contact | ❌ 🔒 Lane 1 | fields don't exist in Notion yet — mapped ➕ in The Sequence, LANE-SYNC posted v6.4; board can't filter on data that isn't recorded |
| 18 | qualification criteria verbatim (primary + downsell) | ✅ | rendered verbatim |

## Funnel-explorer asks (17-item confirmed spec + v6.7 + v6.8)
| # | Ask | Status | Evidence |
|---|---|---|---|
| 19 | multi-toggle groups, live counts/%, AND/OR, booking right | ✅ | verified headless |
| 20 | in-hours = M–F 7:00–5:45 PT | ✅ | laClock |
| 21 | filter-chain bug (table emptied) | ✅ | shared facet builders; exact repro passes |
| 22 | Owner/Closer removed; big animated spotlight | ✅ | v6.7 |
| 23 | **sequential order** ("closer verdict… has to be sequential"), setter verdict after triage, explicit **Booked Call** stage, offer-type before disposition, Won/Lost **separate** from Offer Made/Nurture, "reason no close" rename | ❌ → v6.9 | today's ask |
| 24 | setter grading expandable checklist (process, all questions, booked, show-up briefing, on computer, ask/get credit report) | ❌ → v6.9 + 🔒 Lane 1 fields | today's ask |

## Stage-accuracy asks (v6.8 round)
| # | Ask | Status | Evidence |
|---|---|---|---|
| 25 | Nick ≠ Closed Won → "Verbal Yes… agreement sent… paid yes or no" | ✅ board / 🔒 Notion row | both rosters show "Verbal Yes · not paid" + ⚠; Lane 1 must fix the actual row |
| 26 | filters: verbal yes · agreement/paid · follow-up required · closer verdict incl. Custom · no-sign-up reasons | ✅ | groups 8–11 (being re-ordered in v6.9) |
| 27 | "Why is there 12 unknown… resolve it for all future uses" | 🟡 | ROOT-CAUSED (field empty on 12 of 13; checkbox can't say "not triaged"; 8 timestamps are import artifacts). **Truth not yet entered** — needs Alan's taps / bulk attest / Lane 1 backfill → v6.9 + Track B |
| 28 | "tie all this together with what Kai was requesting… get accurate data first" | 🟡 | Answering Kai answers his 3 questions with receipts; accuracy meter shows the honest 13% — *accurate* answers land as fields fill |
| 29 | Constantine Aug 28 integration | ✅ | expansion table + verbatim transcript stored |

## Process asks
| # | Ask | Status |
|---|---|---|
| 30 | verbatim checklists before building; raw originals stored; "Your buttons" every reply | ✅ (5 raw prompt files) |
| 31 | draft PR "Dashboard lane: publish + polish" | 🟡 branch pushed; PR **creation blocked by environment policy** — one click: https://github.com/Awake999/awake/pull/new/claude/dashboard-lane-polish |

## The honest ❌/🔒 list in one place (what "not done" actually is)
1. v6.9 build (today's asks): instant popups, big before→after toast, sequential group order w/ Setter Verdict + Booked Call + Setter Grading + Offer Type + separated Outcome + Reason No Close, bottom results bar, bulk triage attest. — **Lane 2, buildable now.**
2. Notion fields that don't exist yet (board can render but nothing records them): sequence fields (#17), setter grading (#24), setter verdict, offer type, reason-no-close, triage 3-value, Nick's row, GHL real arrival datetimes. — **Lane 1/4, LANE-SYNC posted.**
3. Triage truth for the 12 (and the wider book): someone who was there must attest — via board taps/bulk attest (instant) or Lane 1 backfill from GHL notes+recordings (durable).
