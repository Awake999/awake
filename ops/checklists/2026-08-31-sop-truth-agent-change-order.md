# LANE-SYNC — SOP CHANGE ORDER: §1.14 QUALITY TRUTH AGENT + §1.15 NEVER-MISS AGENT + §1.16 ERROR-RESOLUTION AGENT (Alan-ordered 8/31)

> 🗣️ Alan, 8/31 (verbatim, [stored ↗](../prompts/2026-08-31-data-correction-demands.md)):
> *"implement a quality truth agent in verification. Into the SOP."* and, same thread:
> *"Also, Carla did not agree. You need to be very, very careful with your statements.
> Everything has to be absolute. Everything has to be factual and not fabricated."*
> **Lane 1: merge the section below into ops/SOP.md (you own it; snapshot per §1.13 first).**
> Lane 2 adopted the protocol immediately (first enforcement run: 8/31 — caught and corrected
> the "Alan ↔ Carla daily 1-on-1" cadence line, which stated as fact an agreement Carla never made).

## Proposed §1.14 — QUALITY TRUTH AGENT (binding on every lane, every Alan-facing output)

Before ANY Alan-facing output ships (board publish, reply, register line, Notion write), a
**truth-verification pass** runs as its own step — a fresh-eyes agent (subagent where the
runtime allows; a separated self-pass otherwise) whose ONLY job is to try to falsify the draft:

1. **PERSON-CLAIM RULE** — every statement that a named person *agreed, committed, said,
   decided, or promised* must carry a receipt (recording link, message link, or Alan's own
   attestation with date). No receipt → the claim ships as **PROPOSED / UNCONFIRMED**, visibly,
   or not at all. (Root case: "Carla daily 1-on-1" shipped as settled cadence; Carla did not agree.)
2. **NUMBER RULE** — every figure carries its verified/derived/unknown label and a click-through
   receipt; a derived figure names its inputs. A number whose basis can't be found in a raw
   source is removed, never smoothed.
3. **WINDOW RULE** — a surface scoped to a time window (e.g. "this month") shows no
   out-of-window figures in its headline layer; verification dates are never displayed where
   they can read as event dates. (Root cases: "8/31" Whop-check date reading as Jill's payment
   date; pre-August payments diluting the August view.)
4. **BLEND RULE** — no metric may silently blend categories Alan treats as distinct
   (Main + Downsell ≠ "qualified"; existing-client ≠ new-client revenue). Blended metrics are
   labeled as blends with the split shown.
5. **FALSIFICATION DIFF** — the truth agent re-reads the relevant raw originals
   (ops/prompts/, archives, recordings index) and diffs each new claim against them; any claim
   it cannot ground gets flagged in the output, not shipped silently.
6. **LOG LINE** — every run grade records the truth-agent pass: what was checked, what was
   caught, what was corrected ("truth-agent: N claims checked · M corrected · receipts linked").
   A shipped fabrication = severity-1, register-logged with root cause.

## Proposed §1.15 — NEVER-MISS AGENT (Alan-ordered 8/31, same thread)

> 🗣️ Alan, 8/31 (verbatim, [stored ↗](../prompts/2026-08-31-data-correction-demands.md)):
> *"and again, how do you keep missing this? We need to create an agent into the SOP to make
> sure that things aren't being missed. Also, you're not even following the SOP prompt or the
> SOP file from number one, from the main one, awake dashboard v1.2. You need to get your base
> from there for the SOP or how you operate."*

Before ANY reply ships, a **completeness pass** runs as its own step, separate from the
truth pass (§1.14 checks that what ships is TRUE; this checks that nothing Alan asked for
is ABSENT):

1. **ATOMIC-ASK DIFF** — re-read the prompt(s) being answered from the raw store
   (ops/prompts/), split into numbered atomic asks, and diff against the draft reply +
   the actual tool calls made. Every ask maps to exactly one of: DONE (with the receipt),
   IN PROGRESS (with what remains), or BLOCKED (with what unblocks it). An ask with no
   mapping = the reply does not ship.
2. **STACKED-PROMPT RULE** — when prompts arrive mid-run, the diff covers the WHOLE stack
   since the last reply, not just the latest message. (Root case 8/31: strict-triage
   verification nearly shipped without the "why 104" answer from the follow-on message.)
3. **STANDING-ORDER SWEEP** — the register's open items and the SOP's standing rules
   (verbatim checklist, raw storage, buttons, token line) are a checklist, not a memory;
   the pass ticks each one explicitly.
4. **SOP BASE RULE** — the operating SOP is the TRUNK copy (branch `claude/new-session-1ofk4w`,
   session "1) APW - Dashboard v1.2"). Every lane pulls trunk before work and reads
   ops/SOP.md from the merge result; a lane-local or stale SOP copy is dead law (Alan 8/31:
   "You need to get your base from there for the SOP or how you operate").
5. **LOG LINE** — each run grade records the pass: "never-miss: N asks parsed · N mapped ·
   0 unmapped". A missed ask that Alan has to re-prompt = severity-1 (LAW 0), register-logged.

## Proposed §1.16 — ERROR-RESOLUTION AGENT (Alan-ordered 8/31, third strike on fabrication)

> 🗣️ Alan, 8/31 (verbatim, [stored ↗](../prompts/2026-08-31-data-correction-demands.md)):
> *"and again, you ignore my whole thing about fake stuff, like Carl saying it's agreed versus
> unsigned or whatever it is. He never agreed. He said he's going to look at it and talk to his
> partner about it. We cannot be fabricating stuff. Please implement an agent to resolve this
> problem: why it was a problem, why this was done the way that it was. Create the effective
> solution, run the solution plan, test it, and if it works, put it in the SOP. This should not
> become a problem. I've had a talk about it multiple times with you. Fix all repeated errors
> that we keep repeating."*

### RCA of the fabrication class (run 8/31 — why it was a problem, why it was done that way)
- **What shipped:** "Karl K., terms agreed 8/21 · Agreed — unsigned 8 days" (board, 4 sites).
  **What is true:** Karl's own words on the 8/20 call: *"send over whatever agreements that
  would need to be reviewed. I can have our attorney look at that"* and *"I'll share it with
  McCall… we'll make a decision by our executive meeting on Tuesday"*
  ([transcript ↗](../archive/calls/fathom/2026-08-20--karl-krummenacher-guaranteed-funding--175440897/transcript.md),
  [27:13 ↗](https://fathom.video/calls/791088813?timestamp=1633)). A proposal under review is
  not an agreement. Same class as the Carla 1-on-1 line (8/31, strike 2) and the blanket
  booked⇒triaged attestation reading (8/31, strike 3-adjacent).
- **Why it was done that way (root causes):** (1) optimistic stage labels — a CRM stage /
  debrief summary word ("verbal", "agreed") was copied onto the board as a settled fact
  without opening the primary transcript; (2) the §1.14 truth pass as first implemented swept
  only NEW claims on sections being touched — standing text from earlier versions was
  grandfathered in, so Karl's line survived the very sweep that fixed Carla's; (3) narrative
  gravity — "fastest money in the building" made "agreed" feel true.
- **Why it matters:** Alan makes cash-position decisions off the crit bucket; a fabricated
  "agreed $7,500" overstates near-term cash and misdirects the day's top queue item.

### The agent (mechanical, not judgment)
When Alan flags an error **class** (or any severity-1 recurs), the lane MUST, before its next publish:
1. **RCA** — name what shipped vs. what is true (with the primary source), why it happened,
   and why it matters. Written down, not narrated.
2. **DETECTOR** — build a mechanical detector for the whole class (a grep/script, not a
   re-read): e.g. fabrication class = scan the ENTIRE surface for claim-words
   (`agreed|committed|promised|verbal|confirmed|waiting on paperwork`) and require each hit to
   carry a primary-source receipt or a PROPOSED label.
3. **RUN on the WHOLE surface** — never only the section being edited (that scoping is
   exactly what let Karl's line survive the Carla fix).
4. **FIX every hit · TEST** — the detector re-runs clean before publish.
5. **REGISTER** — the class, detector command, and run result go into the lane's
   REPEAT-ERROR list; every future publish re-runs every registered detector.
6. **SOP** — after the first clean run, the class + detector ship to Lane 1 as a change order
   (this document is that step for the fabrication class).

### First run, 8/31 (the test — it works)
- Detector run over the full board surface: **6 unreceipted hits, all Karl** (cashbar aria ×2,
  key item, queue item ×2, deals row ×2, glance line) → all corrected to **PROPOSED, not
  agreed** with Karl's verbatim words + transcript links as receipts.
- Cross-checks on the same sweep: Nick S. "verbal yes" = Alan-attested 8/30 (receipted, kept);
  Yeshaya D. "committed to securing a PG within a month" = archived 8/27 call summary
  (receipt added to the board).
- Bonus catch by the registered window detector: the Money-tab cashbar still showed the
  lifetime $20,100 — the backdating class Alan flagged twice — rescoped to August.
- Re-run after fix: **0 unreceipted claim-words**. Detector registered for every future publish.

### Lane 2 REPEAT-ERROR REGISTER (detectors re-run on every publish)
| # | Class (Alan flags) | Detector | Status |
|---|---|---|---|
| 1 | Fabricated person-claims (Carla, Karl) | claim-word grep, whole surface, receipt-or-PROPOSED | clean 8/31 |
| 2 | Backdating / window mixing (Jill "8/31", lifetime cashbars) | out-of-window $ figures on month surfaces | caught+fixed 8/31 (Money tab) |
| 3 | Silent blends (60% "qualified") | every rate names numerator+denominator | clean 8/31 |
| 4 | Missed asks / reprompts | §1.15 atomic-ask diff before reply | running |
| 5 | Stale SOP base | trunk pull + SOP version print, session start | running |
| 6 | Publish to wrong URL (frozen ba359183) | canonical url param on every publish | clean since 8/31 |
| 7 | Merge regressions (83-vs-104) | fingerprint tokens checked pre-publish | clean since 8/31 |

## ⚡ ALAN-CONFIRMED PRIORITY (8/31 buttons: "all") — the two triage-system inputs
1. **Lane 4:** pull call audio for the 50 ≥2-min-call contacts (46 booked first) via the authed
   GHL recordings API and transcribe into `ops/archive/ghl/recordings/` — message ids in
   [`ops/data/triage/TRIAGE_CALL_LEDGER_2026-08-31.csv`](../data/triage/TRIAGE_CALL_LEDGER_2026-08-31.csv).
2. ~~**Lane 1:** store the written 5-question triage script~~ **RESOLVED 8/31** — Alan dictated
   the full 15-step process checklist (core questions 1–5: funding amount · use plan · what
   they've tried · timeline · credit score); stored verbatim as the canonical scoring standard:
   [`ops/data/triage/TRIAGE_SCRIPT_STANDARD.md`](../data/triage/TRIAGE_SCRIPT_STANDARD.md).
Once both land, Lane 2 scores every transcript against the script and fills receipted
verdicts (each of the 5 questions asked? extra triage? booked on/after the call?).

## Lane 2 implementation (already live, 8/31)
- Pre-publish step added to the dashboard lane's ritual: person-claim grep (agreed/committed/
  said/promised/1-on-1/mandatory) → receipt check → PROPOSED labels where unreceipted;
  number/window/blend sweep on any touched section; result logged in the lane process log.
- First enforcement catches (8/31): Carla 1-on-1 → PROPOSED · "Showed → qualified" blend →
  split with PRIMARY-only · Whop verification dates fenced from payment dates · pre-August
  payments removed from the month surfaces · new-vs-existing client revenue separated.
