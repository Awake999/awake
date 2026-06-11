# QUINTESSENCE-2 REPORT — ca_business_credit_funding_v7.xlsx (v7.4 state)

Reviewer: QUINTESSENCE-2 (fresh adversarial re-audit; independent of builder, QA-VERIFIER-2, and QUINTESSENCE-1)
Date: 2026-06-11
Artifact: `/home/user/awake/research/v7/deliverables/ca_business_credit_funding_v7.xlsx` — 20 tabs confirmed, incl. new `1C. EXECUTION CHECKLISTS` (64 rows, 6 sections, 30 hyperlinks) and `17. PROJECT CHECKLIST` (22 rows).
Baseline: prior audit `out/quintessence_report.md` scored 7.2/10 and listed 10 ranked enhancements; v7.2 (QUINTESSENCE-PATCH), v7.3 (REVERIFY), v7.4 (ENHANCE-99) claim to close them.
Method: full openpyxl read of Tabs 0/1/1B/1C/17 + targeted reads of Tabs 3/13; raw-XML hyperlink extraction (openpyxl's `_hyperlinks` returns 0 on this file — links live in sheet XML rels: Tab 1 = 220, 1B = 104, 1C = 30); 14 live HTTP spot-checks (curl, browser UA); cross-tab contradiction sweep focused on cells the patches touched; review of `out/reverify_findings.md` and change-log rows 208–235.

---

## SCORES

| # | Dimension | v1 | v2 (now) |
|---|---|---|---|
| 1 | Decision-readiness | 7.0 | **9.0** |
| 2 | Strategy soundness | 8.0 | **8.5** |
| 3 | Data integrity at the edges | 7.5 | **8.5** |
| 4 | Evidence decay risk | 6.5 | **8.5** |
| 5 | Completeness vs goal | 6.5 | **9.0** |
| 6 | Polish | 8.0 | **8.5** |
| — | **Overall (weighted toward 1/2/5)** | 7.2 | **8.8** |

---

## FIX VERIFICATION — did the promised v7.2–v7.4 patches land?

| Promised fix | Verdict | Evidence |
|---|---|---|
| Tab 1 banner + sprint-slot column | **LANDED** | Tab 1 R1 banner ("Rank = value… do not apply top-down"); col O "Sprint slot (1B)" populated on all 32 rows and consistent with 1B set/pick numbers (32/32 spot-matched, incl. the subtle "#3 pick / submit 2nd" Chase distinction); col P "Reports to personal?" populated. |
| Day 0–90 calendar + same-day rule | **LANDED** | 1B rows 3–13: Day 0 (freezes+self-pulls+Stanford clock, tally $0), Wk 1–2 deposits, Wk 3–4 Sprint A, Wk 6–7 B, Wk 9–10 C, Day 75+ D, Day 90 review; R11 explicit same-day rule with the 24h-posting rationale; R12 funding tally + stop rule. Echoed in 1C §2.3/§2.6. |
| Wells re-slot (CA = EQ-likely) | **HALF-LANDED — the one promised fix that did not fully execute.** | 1B R21 C4 carries the v7.3 append "RE-SLOT→EQ sprint: only CA DP = EQ (2024-06-07…)", but the row physically remains in the EX Set 2 block, the calendar row R9 still runs Wells inside Sprint D (EX thaw only), no Wells row exists in the EQ section (R33–37), and 1C §6.2's Why-cell still says "Decides Wells's **EX Set 2** slot." If Wells routes to EQ during Sprint D, EQ is frozen → likely decline/delay; the only guard is "confirm bureau at app." |
| PNC soft-EQ 2026 DP | **LANDED** | 1B R34 append "soft-EQ CONFIRMED MED-HIGH: 2026-04-17 DP — $50K BLOC… (myFICO 6862301)"; Tab 1 R12 append; 1C §6.1 with stale-by 2026-10; matches reverify_findings.md §2. Honest about EQ-ness being MED-HIGH. |
| First Citizens tri-merge quarantine | **LANDED** | 1B R8 calendar ("thaw all 3 for that visit; schedule LAST or standalone"), R35 append, R70 append, Tab 1 R17 col O, 1C §2.1 exception list. Fully consistent everywhere. |
| Reports-to-personal columns | **LANDED** | Tab 1 col P + 1B col M (13), sourced from Tab 3 col 24 (spot-checked Wells "NEVER" → "No (never)", Chase derog-only, USB never); drives 1C §5.4 utilization rule. |
| 1C all 6 sections with working links | **LANDED (2 dead links)** | §1 Day-0 (11 items), §2 pre-flight (7), §3 banker script (7 Qs + 5 named calls), §4 doc pack (Tier 1/2), §5 post-result (log/denial/45-day re-pull/utilization/CLI/cooling), §6 re-verify (8 claims with stale-by dates). 30 hyperlinks present — but see link audit: both IRS links 404. |
| Tab 17 tracker | **LANDED, and honest** | 22 rows; statuses verified against reality: the 5 ☐ rows are genuinely USER-gated (Enterprise terms, Stanford clock, banker calls, WaFd 6/30), the 2 🟡 are honest (5-bank DP vacuum, BCU/Skyla Diamond), the ✅ rows check out on inspection — with one quibble: R21 "CSVs in sync ✅" is true for text but the change-log's claimed "text (URL) pattern" is not honored (see below). |
| Re-verify schedule | **LANDED** | 1C §6.1–6.8 with stale-by dates; backed by a real re-verification sweep (reverify_findings.md): Wells 5×2024 DPs, PNC confirmed through 2026-04-17, Stanford verified live + archive URLs, Enterprise honestly still UNVERIFIED. |
| Prior polish items | **MOSTLY LANDED** | Tab 4 autofilter now A1:K30 ✓, Tab 13 now A1:I235 ✓, README inline index lines for 1B/1C/17 + "start at tabs 1 + 1B" ✓, Chex/EWS-freeze overreach corrected via appends (1B R2/R66/R73) ✓. NOT done despite being in QUICK-FIX #9: the 9 literal "source" labels (1B R66–74 C12) persist; tab colors still 2/20; Tab 13 freeze pane still A18. |

## LINK SPOT-CHECK (14 fetched live, 2026-06-11)

| Status | URL (cell) |
|---|---|
| 200 | chexsystems.com/request-reports/consumer-disclosure (1C E10/E52) |
| 200 | chexsystems.com/security-freeze/place-freeze (1B J4/G13) |
| 200 | earlywarning.com/consumer-information (1B K4/H13, 1C E11) |
| 200 | experian.com/freeze/center.html; equifax.com freeze; consumer.risk.lexisnexis.com/freeze (1C E6–E8) |
| 200 | bizfileonline.sos.ca.gov (1C E40); rizecu.com/business-visa (E34); calbanktrust.com biz cards (E33); wafdbank FAQ (E14/E63) |
| **404** | **irs.gov/businesses/small-businesses-self-employed/lost-or-misplaced-your-ein (1C E39)** — IRS reorganized; content now lives under irs.gov/businesses/employer-identification-number (confirmed 200 via the old EIN-path redirect) |
| **404** | **irs.gov/forms-pubs/about-form-4506-c (1C E47)** — about-form-4506 and about-form-4506-t both 200; the -c page is gone |
| 403 | transunion.com/credit-freeze (1C E5, 1B J7/D13) — TU bot-blocks curl; canonical freeze URL, almost certainly fine in a browser (inconclusive, not a defect) |
| 503 | ars-consumeroffice.com (1C E9, 1B J13) — correct domain; edge-block or outage, inconclusive |

Two genuinely dead links on a tab that shipped *today*, in the doc-pack section the user is told to "print." Evidence decay arrived before the courier did.

## NEW CONTRADICTIONS INTRODUCED/EXPOSED BY THE PATCHES

1. **Cooling-period arithmetic (1B internal + 1B↔1C).** 1B R72 states "~90d spacing between sprints on the same bureau" and R10 "(~90d same-bureau spacing)" — yet 1B's own calendar runs EX Set 1 at Week 3–4 (day ~21–28) and EX Set 2 at Day 75+, a gap of ~47–54 days. 1C §5.6 quietly introduces a third number: "SAME bureau: wait **30–45 days minimum** between sets (1B calendar runs conservative ~90d spacing **for Sprint E+ re-runs**)." The calendar satisfies 1C's 30–45d floor, but a plain reading of 1B's "~90d between sprints on the same bureau" forbids its own Day-75 Sprint D. Three texts, two rules, one calendar.
2. **Wells Fargo, three-way split.** 1B R21 append: "RE-SLOT→EQ sprint." 1B R9 calendar: Wells stays in Sprint D (EX). 1C §6.2: title says "EQ-likely (v7.3 re-slot)," Why-cell says "Decides Wells's EX Set 2 slot." And **Tab 3 R4 C23 was never appended** — the master table still reads "CA = Experian-dominant… expect EX or TU; confirm at application," with no trace of the v7.3 finding (the only CA DP = EQ; no TU DPs seen). The v1 audit's Wells *limit* contradiction was fixed; a Wells *bureau* contradiction was created in its place.
3. **1C §3.9 calls CB&T the "Rank-8 row."** CB&T is **rank 16** on Tab 1 (R18); rank 8 is Stanford FCU. Small, but it's in the highest-value section (who-to-call-first) and will misdirect a user cross-referencing Tab 1.
4. **Change-log R211 claims the bureau_strategy CSV uses a "text (URL) pattern"** — `grep http` finds **zero URLs** in best_targets, bureau_strategy, and the new checklists CSVs (only funding_table preserves URLs, 242 lines). The CSV mirrors silently lose all 354 front-tab source links; Tab 17 R21 marks CSV sync ✅ without this caveat.
5. Minor: 1B R5 calendar says open "CU SoCal → Premier America → Bank of Hope" deposits unconditionally, while R60/R66 say CU SoCal is "deposit pre-work decision **only if a deposit there matters**" — the calendar drops the conditional.
6. Minor: 1C §1.10/§6.7 label the WaFd link "biz card page"; the URL is the *personal* cash-back FAQ (where the pause notice lives — defensible, mislabeled).

What I hunted for and did NOT find: stop-rule inconsistency (1B R12 "≥$50K–$100K" = 1C §2.6 "≥$50K stretch $100K" = §1.11 goal framing — consistent); Tab 1 col O vs 1B set/pick mismatches (0 of 32); same-day rule divergence (R11 = §2.3 — consistent); First Citizens quarantine leaks (none); Tab 17 status inflation (none material); column misalignment from the v7.3/v7.4 in-cell appends (none — appends correctly use the in-cell " ‖ " convention); stale autofilters (all fixed).

## REMAINING COMPLETENESS GAP

The one v1 §5 item still missing anywhere in the workbook: **D&B/DUNS build steps**. Zero hits for "DUNS"/"Paydex"/"net-30" across all 20 tabs. The Sam's Club EIN-only lane (NO-PULL #4, Tab 1 rank 14) is gated on "Build D&B file first" with no instructions on how (DUNS request → 3–4 net-30 tradelines → Paydex 80 → ~30–60 days). Also: §5.1 tells the user to log results "in Tab 8 format" but no blank log block/columns exist to fill — minor, the format is specified.

---

# (a) SCORE NOW: **8.8 / 10** (up from 7.2)

# (b) EXACTLY WHAT SEPARATES IT FROM 9.9

## BUILD-FIXABLE (a script can close these today — worth ~+0.6)

| # | Defect | Exact fix |
|---|---|---|
| B1 | Wells re-slot half-landed | (i) 1B **R9 C1**: append " ‖ v7.5: Wells is EQ-likely in CA (v7.3) — for Sprint D either thaw EQ alongside EX for the Wells app, or move Wells to Sprint C/EQ standalone; do not submit it against a frozen EQ." (ii) Add a Wells cross-ref row in the EQ section (insert after **1B R36**, "EQ Set 1 #4 (conditional) — Wells Fargo, see EX Set 2 #6: CA DP = EQ"). (iii) 1C **E58/§6.2 Why-cell (D58)**: append "…v7.3 re-slot: treat as EQ-likely; EX Set 2 slot is the fallback." |
| B2 | Tab 3 master never got the v7.3 Wells finding | **Tab 3 R4 C23**: append " ‖ v7.5 2026-06-11: re-verified — 2024 biz DPs mixed EX/EQ; only CA DP = EQ (myFICO 6766003); BLOC pulled EQ (6756650). EX-dominant table is stale for the business product." |
| B3 | Cooling-rule triple-message | **1B R72 C1**: append " ‖ v7.5: '~90d' applies to Sprint E+ re-runs on an already-worked bureau; the A→D gap (~50d) meets the 30–45d minimum (1C §5.6)." Same one-liner appended to **1B R10 C1**. |
| B4 | Two dead IRS links | **1C E39** → `https://www.irs.gov/businesses/employer-identification-number` (200, contains lost-EIN guidance); **1C E47** → `https://www.irs.gov/forms-pubs/about-form-4506` (200) and amend the C47 text to "4506-C/4506 family". |
| B5 | 1C §3.9 "Rank-8 row" | **1C D33** ("Why" cell): change "Rank-8 row" → "Rank-16 / ASK Set 1 #1 row". |
| B6 | CSVs silently drop 354 links + change-log misclaim | Re-export best_targets / bureau_strategy / checklists CSVs with `label (URL)` pattern; or append a Tab 13 row + README note: "CSV mirrors are text-only; links live in the xlsx + funding_table CSV." |
| B7 | D&B build steps absent (Sam's EIN-only lane unexecutable) | Insert 1C §1.12 (or §4.11): "DUNS: request free at dnb.com/duns → open 3–4 net-30 vendor tradelines (Uline/Quill/Grainger class) → Paydex 80 after ~2–3 reporting cycles (~30–60d) → then Sam's in-club EIN-only app (NO-PULL #4)." with dnb.com link. |
| B8 | 9 literal "source" labels (promised in v1 QUICK-FIX #9, skipped) | **1B C12 rows 66–74**: rename to named labels (e.g. "DoC Chex list", "FNBO pre-qual", …) keeping the same targets. |
| B9 | Calendar/footnote tension on CU SoCal | **1B R5 C1**: append " ‖ v7.5: CU SoCal deposit is optional (open only if you want a relationship there — see NOT-SLOTTED note)." |
| B10 | Cosmetics (small but visible) | Color the lane tabs (1/1B/1C green, 17 grey); move Tab 13 freeze pane A18→A2; label 1C E14 "WaFd card FAQ (pause notice)". |

## USER-GATED (no file edit can close these — they cap the score at ~9.6 until done; worth ~+0.4 when closed)

1. **The 5 DP-minting calls** (1C §3.9–3.13): CB&T bureau at 444 W Ocean Blvd; Rize 800-866-6474; Valley Strong phone screen; Enterprise B&T *written* terms (rank 7 + Diamond D2 still rest on one unverified broker claim — re-confirmed unverified 2026-06-11); Banner bureau disclosure. ~11 AMBER rows unlock only with these answers.
2. **Day-0 clocks only the user can start**: Stanford $5 membership (matures ~2026-12-11), Premier America membership in the Chex-clean window, the actual freezes/self-pulls.
3. **WaFd 2026-06-30 re-check** and the logged-in read of myFICO 6674742.
4. **Bureau confirmations at application** (Wells Q1 above all) — the workbook can only instruct; the answer is minted at the desk.
5. Archive.org `/save` submissions for sfcu.org's new URL (this environment's egress hard-blocks web.archive.org saves; local HTML fallbacks exist in out/).

## INHERENT (no workbook can remove — the last ~0.3 is structural)

1. **Bureau routing variance**: Wells/Elan/Chase route by state, branch, even underwriter (the workbook's own 2024-05-02 DP: same applicant, same day, EX for the card and EQ for the LOC). A plan can hedge this; it cannot eliminate it.
2. **Community-DP epistemology**: PNC soft-EQ, BMO=TU, FNBO=EX all rest on self-reported forum DPs — honestly graded, but unverifiable short of applying.
3. **Policy drift between build and execution**: Synchrony EIN-path tightening, Chex/EWS list churn (the workbook's own quarterly re-check exists precisely because of this), product pauses (WaFd). Today's two dead IRS links are the in-sample proof of this class.

---

## VERDICT

The promised overhaul is real. The two structural complaints that anchored the 7.2 — a flagship tab that executed in a forbidden order, and a sprint plan with no dates, no same-day rule, no scripts, and no stop rule — are both demonstrably closed: Tab 1 now hands off to 1B in row 1 and per row in column O, the Day 0–90 calendar with same-day and stop rules exists and is internally cross-referenced, and 1C is a genuinely printable runbook (Day-0 freezes with working links, 7-question banker script, tiered doc pack, denial-to-DP conversion, and a re-verify schedule with stale-by dates that most professional research products don't ship). The re-verification sweep was honest work — it *downgraded* its own Wells claim and left Enterprise unverified rather than laundering it. What keeps this at 8.8 rather than 9.5+ is that one of the named promises only half-landed — Wells was re-slotted in an annotation but not in the calendar, the set table, or the master tab, leaving the workbook arguing with itself about which bureau Sprint D burns — plus a cluster of patch-induced friction: a 90d-vs-30–45d-vs-50d cooling-rule triangle, a wrong rank in the who-to-call list, two IRS links that died before delivery, CSV mirrors that silently shed every hyperlink, and a Sam's-lane dependency (D&B build) that is still named but nowhere specified. All ten of those are scriptable in one v7.5 pass (≈+0.6 → ~9.4); the rest of the distance to 9.9 belongs to the user's phone (≈+0.4 when the five calls and clocks land) and to the irreducible variance of bureau routing, which no spreadsheet — including a 9.9 one — can freeze.

Report: `/home/user/awake/research/v7/out/quintessence_v2_report.md`
