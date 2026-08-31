# LANE-SYNC — SOP CHANGE ORDER: §1.14 QUALITY TRUTH AGENT (Alan-ordered 8/31)

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

## Lane 2 implementation (already live, 8/31)
- Pre-publish step added to the dashboard lane's ritual: person-claim grep (agreed/committed/
  said/promised/1-on-1/mandatory) → receipt check → PROPOSED labels where unreceipted;
  number/window/blend sweep on any touched section; result logged in the lane process log.
- First enforcement catches (8/31): Carla 1-on-1 → PROPOSED · "Showed → qualified" blend →
  split with PRIMARY-only · Whop verification dates fenced from payment dates · pre-August
  payments removed from the month surfaces · new-vs-existing client revenue separated.
