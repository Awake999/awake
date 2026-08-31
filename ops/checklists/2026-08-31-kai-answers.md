# ANSWERING KAI — full checklist, audited numbers (2026-08-31)

> Kai's 8/30 voice note, verbatim: [`ops/prompts/2026-08-30-kai-feedback-transcript.md`](../prompts/2026-08-30-kai-feedback-transcript.md)
> (re-pasted by Alan inside [`2026-08-30-stage-accuracy-spec.md`](../prompts/2026-08-30-stage-accuracy-spec.md)).
> Every number below: **VERIFIED** (receipt linked) · **DERIVED** (computed from verified inputs) · **UNKNOWN** (honestly not answerable yet, with the unblock named).
> Live sources: Notion tracker (104 rows, queried 8/31), Lane 1's spend/booking audits, Lane 4's GHL pull (259 contacts · 144 appt events · Payments table EMPTY).
> Board rendering: Funnel tab → "Answering Kai" → https://claude.ai/code/artifact/c6ad801c-50fc-49d3-847a-e6a8b0ddd392

## 1. His readback, corrected line by line
| # | Kai said | The audited truth | Status |
|---|---|---|---|
| 1 | "you've spent 6100" | **$14,898 lifetime** (to the cent) — the $6,100 was the superseded SCIO draft | VERIFIED — [spend pull ↗](https://app.notion.com/p/3cc5bb1ffef4819ebfa1f800a8784d81) |
| 2 | "37 unique bookings … about a 170 cost per booked call" | **129 booking events · 79 unique people** (Mar 24–Aug 30, GHL). $14,898 ÷ 79 = **$189/unique booked**; $115/booking event | VERIFIED counts — [name-by-name audit ↗](https://app.notion.com/p/3cc5bb1ffef481138682fdca2cdd7d23) · DERIVED costs |
| 3 | "of those 15 showed … 41% … 410 cost per live call" | **34 verified show events · 26 unique people**. Where the outcome is decided: **59% showed** (✓29 / ✕20; ~34 still unknown). Honest band on raw L1: **33–35% floor → ~75% ceiling**. $14,898 ÷ 26 = **$573/unique shown** | VERIFIED shows (recordings) · DERIVED cost |
| 4 | "of the 15, 1 was qualified … 14 of the 15 … unqualified" | **False on the audited book.** Of the **24 people a closer actually assessed**: **8 Qualified – Main Offer (33%) · 10 Downsell fit (42%) · 6 Unqualified (25%)** (+5 not yet assessed). 75% of assessed were workable | VERIFIED — tracker Qualification field, queried 8/31 |
| 5 | "you're closing at 150, at least the one deal you did close" | No $150 deal exists. **Verified collected: $2,000 — Ed C., 7/1** ([recording ↗](https://fathom.video/calls/732157346)). Contracted-but-unverified-collected: Jill $15,000 · Leo $12,000 · Karl $7,500 (offer open) · Nick $500 (**verbal only, NOT paid** — Alan 8/30) · Michael $1,000 (nurture). GHL **Payments table is EMPTY**, so collection can only be verified by hand | VERIFIED ($2,000) · UNKNOWN (rest — unblock: Lane 4 payment records / bank truth) |

## 2. His core question — "why were the live calls unqualified… what's your specific ideal client and who was showing up?"
| # | Answer | Status |
|---|---|---|
| 6 | **Reasons, tallied from the tracker's Unqualified Reasons field (13 tagged people):** Late payments ×5 · Collections ×4 · Thin file/low limits ×4 · Hard inquiries ×3 · Charge-offs ×3 · Low income ×2 · No funds ×2 (e.g. "cannot cover ~$200") · Wants no-PG funding ×1 · Wants licensed-broker only ×1 · Bankruptcy ×1 · Child support ×1 | VERIFIED |
| 7 | **Who's showing up:** small-business owners with damaged or thin credit — that's why 10 of 24 assessed landed **Downsell (credit rebuild first)**, not the funding-ready primary ICP | VERIFIED pattern |
| 8 | **The ICP definition (Alan's verbatim criteria):** strong enough credit (≈700–720 gate) · no lates/collections/charge-offs/bankruptcies · needs funding (not license-broker, not no-liability) · has the money to pay us. Downsell ICP: has the money to pay for credit optimization toward eligibility | VERIFIED — Alan's dictation, on the board |
| 9 | **Root cause (Constantine, Aug 28):** ICP mismatch is the constraint — fix the SCIO ad campaign targeting (Alan + Clinton, Kai looped in) and move to owner-led video ads. Michael-type gray-area leads come out of the close-rate denominator: targeting data, not sales data | VERIFIED — [Aug 28 recording ↗](https://fathom.video/share/o39_ztNx7PqzcgbuLQYKt_5t8NDGAFXy) · [verbatim transcript](../prompts/2026-08-30-constantine-aug28-transcript.md) |

## 3. His target math ("50% show → $800/qualified live call → 25% close → 3200 CPA")
| # | Answer | Status |
|---|---|---|
| 10 | His arithmetic checks out **at his assumptions**. Real inputs today: CPB **$189** (not $170) · qualified-any on assessed **75%** (better than his 50% guess) but **primary-fit only 33%** · close on verified shows **23%** (6 of 26) — already inside Constantine's 20–30% live-call benchmark | DERIVED from verified inputs |
| 11 | Spend per Closed-Won person today: $14,898 ÷ 6 = **$2,483** — under his $3,200 CPA target — **but only $2,000 of revenue is verified collected**, so the funnel is cash-negative until contracted deals collect | DERIVED · collection UNKNOWN |
| 12 | The lever ordering he proposed (quality first, then show rate) **matches Constantine's**: pre-call contact by Alan lifts shows 10% → 33–50% — the single biggest measured lever in APW's own data | VERIFIED — Jul 22 session |

## 4. "Numbers dropped this month vs last month — what's changed?"
| # | Answer | Status |
|---|---|---|
| 13 | **Not answerable from the tracker yet — and provably so:** a month-cut query on 8/31 returns **August for every one of the 104 rows**, because Created timestamps are bulk-import stamps, not real arrival dates. Any month-over-month story read off this data (including the SCIO draft Kai read) is an artifact | VERIFIED (query receipt in lane log) |
| 14 | The real July-vs-August cut lives in **GHL's true appointment dates** (129 bookings span Mar 24–Aug 30, already pulled by Lane 4) — the date join is queued as a Lane 1/4 change order; the Sep 1 field discipline makes every future month answerable natively | UNKNOWN today · unblock named |
| 15 | What verifiably changed in August: the ICP mismatch surfaced and was diagnosed (Aug 28), pre-call-contact/triage was inconsistent (1 of 13 opt-in→fast→in-hours leads has triage recorded), and the SCIO draft was wrong on spend, bookings and qualification — the "drop" Kai saw is at least partly the draft's error, not proven performance decline | VERIFIED components, labeled |

## 5. What makes every answer above fully accurate (the "accurate data first" gate)
16. Board data-accuracy meter: **13% of partner-grade cells recorded** — the single honest number behind "the data is not correct."
17. Instant fixes available now: Alan's tap-to-correct + "Attest: everyone in view WAS triaged" (both live on the board, each tap queued in Pending sync).
18. Durable fixes: the Lane 1 change order — [`2026-08-31-lane1-change-order.md`](2026-08-31-lane1-change-order.md) (new Notion fields, Nick's row, triage backfill, GHL date join).
