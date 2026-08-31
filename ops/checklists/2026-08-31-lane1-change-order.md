# LANE-SYNC — CHANGE ORDER: Lane 2 → Lane 1 (2026-08-31)

> **Lane 1: this is the complete, paste-ready Track B list.** Alan asked why he has to relay
> between lanes — he shouldn't. Per the SOP sync ritual (pull first, grep LANE-SYNC), this file
> IS the handoff. Execute top to bottom; check items off in your own log. Lane 2 (dashboard)
> renders and filters every field below the moment it exists — no further coordination needed.
> Raw authority: Alan's prompts in `ops/prompts/2026-08-30-stage-accuracy-spec.md` and
> `2026-08-30-ux-clarity-sequential-pipeline-spec.md`.

## A. Notion tracker — field changes (source of truth stays with you)
1. `Human Triaged`: checkbox → select **Triaged / Not triaged / (empty = unrecorded)**; mandatory at lead arrival from Sep 1.
2. New: `Setter Verdict` (select: Primary fit / Downsell fit / Custom fit / Not qualified) — the setter's pre-booking call.
3. New: `Booked At` (datetime) — explicit booking moment (stop inferring from Stage).
4. New: `Setter Grade` (6 checkboxes or multi-select): followed process · asked all questions · booked the call · end-of-call briefing (unobstructed environment, focus-ready, on computer) · asked for credit report · got credit report.
5. New: `Offer Type` (select: Primary / Downsell / Custom) — which offer was actually made (closing ratios must not blend).
6. New: `Verbal Yes` (y/n) · `Agreement Sent` (y/n) · `Paid` (y/n) · `Follow-Up Call Required` (y/n).
7. New: `Reason No Close` (select): Not enough money · Credit not strong enough · Partner blocker · Offer mismatch · Other.
8. Sequence-spec fields (from v6.4 LANE-SYNC, still open): `Out-of-Hours` + time-to-contact · `Intro Text Sent` · `Connect Method` (connected/double-dial) · `Follow-Up Sent` (vm+text) · `BAMFAM'd` · `Contact Attempts` + `Attempt Methods`.

## B. Row corrections (Alan-attested)
9. **Nick S.**: Stage "Closed Won" is wrong — he verbally agreed, agreement sent, **NOT paid** (Alan 8/30). Set Verbal Yes = y, Agreement Sent = y, Paid = n; move Stage off Closed Won once taxonomy exists.
10. Triage backfill: only 1 of the 13 (Opt-In → ≤1min → In-hours) rows has Human Triaged recorded; Alan attests the rest were triaged — backfill from GHL notes/recordings, or accept Alan's board attestations from the Pending-sync panel.
11. Aug-10 import block: 7+ rows share Created `2026-08-10 20:09:51Z` (and the 8/9 batches likewise) — join real arrival datetimes from GHL so Speed-to-Lead and In-hours stop reading import artifacts. **Proof of urgency: a month-cut GROUP BY on 8/31 puts all 104 rows in August.**

## C. Standing items (from earlier LANE-SYNCs, still open)
12. Data disputes: Ma. Liza Tizon (junk/spam capture?) · Robert Morawitz ×4 dupes · Alan's "Robin" row — needs his pointer.
13. Payments ground truth: GHL Payments table is EMPTY — establish the collected-cash record (bank/processor) so "Paid" is verifiable; today only Ed C. $2,000 (7/1) is verified.
14. Lane 4: `build_ghl_book.py` must emit `var DATA = window.APW_GHL_DATA = [` (one token) and publish via the repo file, never by appending to the artifact.

## D. Done on Lane 2's side (no action, FYI)
- Board v6.9 renders/filters everything above (15 sequential groups), with local tap-to-correct stores (`apw-showed-fix`, `apw-triage-fix`, `apw-deal-fix`, `apw-setter-verdict`, `apw-setter-grade`) queued in the board's Pending-sync panel — that panel is your intake for Alan's corrections.
- Kai's questions answered with audited numbers: `ops/checklists/2026-08-31-kai-answers.md`.
