# TIER-QA Adversarial Verification — SoCal_SelfUW_Tiered_NoChex_v1.xlsx

**Verifier:** TIER-QA (independent; did not build the deliverable)
**Date:** 2026-06-20
**Target:** `/home/user/awake/research/ibanknet/deliverables/SoCal_SelfUW_Tiered_NoChex_v1.xlsx`
**Method:** python3 + openpyxl structural/color extraction; trace to source CSVs in `out/` and `v6/out/`; 6 WebFetch spot-checks.

---

## VERDICT: PASS-WITH-ISSUES

The structural rebuild succeeded — the **core bug is fixed**: zero green/Tier-1 rows carry Chex=YES or EWS=YES, no Tier-3 row is mis-colored green, every row has a county, color/star coding is 100% consistent, and SoCal/county data matches the FDIC SOD + NCUA census exactly. **However, the Tier-1 answer the user cares most about does not hold up**: City National's Tier-1 placement rests on a Chex=NO cell that its own cited source contradicts, and a systematic "absence-read-as-NO / lenient-read-as-NO" pattern mislabels several Chex cells against the source data.

**Counts by severity:** CRITICAL = 2, MAJOR = 3, MINOR = 3.

---

## CRITICAL

### C1 — City National Bank Tier-1 placement is source-contradicted (the headline failure)
Row 3 codes **ChexSystems = NO (COMMUNITY-DP)**, green cell, and this is the *sole* basis for Tier-1 (EWS=NO is own-doc-absence; no-doc is only "partial"). The cited Chex source is `crediful.com/chexsystems/city-national-bank/`.
- **WebFetch of that exact URL** returns: *"City National Bank does use ChexSystems to review new account applications."* The page does **NOT** disambiguate cnb.com (CA) from City National Bank of West Virginia (the twin).
- The build's own source file confirms this: `deep_chex_results_1.csv` grades City National Chex as **"Yes-probable (DoC 2 DPs, twin-caution CNB WV)"** with new finding **"twin-AMBIGUOUS … cannot confirm it covers cnb.com LA vs CNB WV/OK"** and Notes: *"Twin ambiguity persists — verify with banker which CNB any DP covers."*
- The deliverable converted a "Yes-probable / twin-ambiguous" into a clean green **NO**. By the user's own rule (UNKNOWN → Tier 2, never green), this is at best **Tier 2 (UNDETERMINED)**, not Tier 1. The Chex=NO cell is affirmatively wrong per its own source link.
- **Correct tier: TIER 2.** City National is NOT genuinely Tier-1.

### C2 — America's Christian CU: "lenient = YES" rule violated
Row 24 codes **ChexSystems = NO (COMMUNITY-DP)**, green cell (row is Tier 2). Source `deep_chex_results` says: **"Yes-lenient — community reports ACCU DOES use ChexSystems 'but you can still qualify'."** The user's spec explicitly states *'lenient'/'uses-but-lenient' = YES*. This row should be **Chex = YES → Tier 3 (red)**, not a green NO cell. Direct violation of the stated acceptance rule.

---

## MAJOR

### M1 — Beneficial State Bank Tier-1 rests on absence-of-clause (UNKNOWN over-read as NO)
Row 5: Chex=NO and EWS=NO both graded **VERIFIED-own-doc**. Source `deep_chex_results_2.csv` actually grades it **"Lean-NO … VERIFIED-absence"** with leniency note **"silver tier — verify by phone before relying."** Bureau source (`rerun_bureau_results_4.csv`) says cards exist "but no public terms; issuer/rail and bureau not disclosed." Absence of a Chex/EWS clause in a deposit agreement is being read as a definitive NO. Per the user's framing this is the textbook "absence over-read" case → it should be **Tier 2**, not Tier 1. (Card existence itself is unverified: the cited card page returned **HTTP 403** on WebFetch.)

### M2 — First-Citizens Chex=NO contradicts source
Row 8 codes **Chex = NO (COMMUNITY-DP)**, green cell. Source: *"Re-confirmed — Crediful first-citizens page: 'does use ChexSystems when reviewing applications'."* Source says USES; cell says NO. The row is Tier 2 (so no green-tier bug), but the Chex cell is mislabeled against its own source and should be YES/UNK. If YES, the row is Tier 3.

### M3 — Tier-1 set as a whole does not meet the user's "verified NO Chex + NO EWS" bar
The user's definition of Tier 1 is *verified* no-Chex AND no-EWS. The build's own Guide (Tab 0) and Change Log (Tab 5, item D5) admit Tier 1 is "own-document **likely-no** cases" / "**verified-absence**," and the Honesty Note says "almost no traditional SoCal self-UW bank is verified no-Chex AND no-EWS." Net: of the 3 Tier-1 members, **City National = source-contradicted (Tier 2)**, **Beneficial State = absence-only (Tier 2)**, **CBC = genuine verified-absence but deposit-only (no card)**. Under a strict reading, the Tier-1 tier is effectively empty of a self-UW + business-card bank that is genuinely verified-clean.

---

## MINOR

### m1 — Chex=NO cells on BofA (R34) and Chase (R36) contradict source ("does use ChexSystems" / "CONFLICT logged"). No tier impact — both are correctly Tier 3 via EWS=YES — but the individual green Chex cells are wrong-by-source.
### m2 — Beneficial State business-card page (`/business-banking/credit-cards`) returns **HTTP 403** (dead/blocked link, used as Card link + Apply + Sources on R5). City National's "Card link" points to a *commercial* card product (`commercial.html`); WebFetch confirms a self-issued **Visa Commercial Card** exists, so eligibility (self-issued business card) holds, but it is a commercial purchasing card, not a credit-underwritten business card — the bureau column itself notes the only credit-pull DP is the **consumer** Crystal Visa Infinite.
### m3 — Montecito (R30) EWS graded "UNK (VERIFIED-own-doc)" while source notes "Furnishes-YES (closures)"; furnishing ≠ inquiry-screening, so UNK-for-inquiry is defensible, but the cell is ambiguous.

---

## CHECK-BY-CHECK RESULTS

| # | Check | Result |
|---|-------|--------|
| 1 | **CORE BUG** — zero green/Tier-1 rows with Chex=YES or EWS=YES; no Tier-3 mis-green | **PASS.** Tier-1 rows R3–R5 all Chex=NO + EWS=NO. No green tier band on any Chex/EWS=YES row. No "lenient" string sits in a green *tier band* (the lenient problem is at cell level — see C2). |
| 2 | **TIER-1 SCRUTINY** | **FAIL.** City National Chex=NO is twin-contaminated and source-contradicted (C1). Beneficial State is absence-only (M1). CBC correctly labeled deposit-only ("NO (deposit-only)", no card link). City National *does* have a self-issued Visa Commercial Card (not consumer Crystal, not commercial-only) — confirmed by WebFetch. |
| 3 | **SOCAL/COUNTY** | **PASS.** 10/10 spot-checked rows match FDIC SOD + NCUA census counties exactly (banks via `fdic_sod_census_6cty_2025.csv`, CUs via `ncua_cu_census_6cty.csv`). Valley National (R48): NJ HQ, 2 LA branches, 0 elsewhere → County=Los Angeles, SoCal=YES is **correct**. All 47 Tab-1 rows are SoCal=YES; no non-SoCal institution on the main tab. |
| 4 | **ELIGIBILITY** | **PASS (with allowed exception).** 46/47 rows are SELF + Biz card YES + SoCal. The 1 exception is CBC (Self-UW="—", Biz card="NO (deposit-only)") — explicitly labeled deposit-only as the user permits. |
| 5 | **COLUMNS/COLOR/LINKS** | **PASS.** All 11 required columns present (plus Card link, No-doc, Bureau, Est. limit, Apply, Sources). Website hyperlink on 47/47 rows. Card link on 46/47 (missing one = CBC, correct). Sources non-empty on 47/47. Chex/EWS cell coloring 100% consistent (NO=green / YES=red / UNK=gray); no-doc stars match YES values. Two dead links found (see m2). |
| 6 | **COHERENCE vs prior** | **PASS.** D1 fixed: green is decoupled from self-UW (CBC is green with Self-UW="—"). D3 fixed: county present on 47/47 rows. Tier counts in Tab 5 (3/24/20) match computed values. Tab 5 log is largely honest and even self-flags the "likely-no / verified-absence" nature of Tier 1. |
| 7 | **DATA FIDELITY** | **PARTIAL FAIL.** 8 rows traced to `deep_chex_results`, `secondary_bureaus.csv`, `rerun_bureau_results`. 4 Chex=NO cells (R3, R8, R24, R34, R36) are contradicted by their own source CSVs which say "uses ChexSystems / yes-lenient / yes-probable." No *invented* determinations found, but determinations were **softened** from the source (Yes-probable/Yes-lenient → NO). |

---

## TIER-1 SCRUTINY VERDICT
**The 3 Tier-1 members are NOT all genuinely Tier-1.**
- **City National Bank → should be TIER 2.** Chex=NO is twin-contaminated (CNB-WV vs cnb.com) and the cited Crediful source literally says it *does* use ChexSystems; the build's own file grades it "Yes-probable / twin-AMBIGUOUS." Has a real self-issued Visa Commercial Card (eligibility OK), but the no-Chex claim is not supported.
- **Beneficial State Bank → should be TIER 2.** Clean grade is pure absence-of-clause ("Lean-NO / verified-absence"; build note says "verify by phone before relying"). Card page is a dead (403) link.
- **Commercial Bank of California → legitimately verified-absence, but deposit-only.** Correctly labeled "NO (deposit-only)"; not a card-bearing answer. Its NO-Chex is the only one backed by an own-doc WebFetch (no CRA language found in the disclosure PDF), though absence remains weaker than a positive no-Chex statement.

Under the user's strict definition, **Tier 1 effectively has zero qualifying self-UW + business-card institutions**; the honest result is CBC as a deposit-only no-Chex anchor + everything else Tier 2/3.

## DEAD LINKS
1. `https://www.beneficialstatebank.com/business-banking/credit-cards` — HTTP 403 (R5 Card link / Apply / Sources).
2. (Probe only, not a cited deliverable source) `https://www.valley.com/about-us/company-overview` — HTTP 404; Valley county was instead validated against FDIC SOD and passes.

## REPORT PATH
`/home/user/awake/research/ibanknet/out/qa_tiered_report.md`
