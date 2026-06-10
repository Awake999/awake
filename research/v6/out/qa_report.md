# QA-VERIFIER REPORT — ca_business_credit_funding_v6.xlsx
**Audit date:** 2026-06-10 · **Auditor:** QA-VERIFIER agent (independent; did not build the workbook)
**Target:** `/home/user/awake/research/v6/deliverables/ca_business_credit_funding_v6.xlsx` + `ca_business_credit_funding_v6_funding_table.csv`
**Baselines:** `ca_business_credit_funding_v5.xlsx` · research inputs in `/home/user/awake/research/v6/out/` · standing rule "we can add and organize, do not delete"

## VERDICT: **PASS-WITH-ISSUES**
| Severity | Count |
|---|---|
| CRITICAL | **0** |
| MAJOR | **1** |
| MINOR | **3** |

No fabrication found anywhere. Every claim spot-checked traces to a source file in `out/`. The single MAJOR is a letter-of-the-rule add-only deviation on 2 cells, fully disclosed in the workbook's own Change Log.

---

## 1. ADD-ONLY COMPLIANCE — PASS with 1 MAJOR + 1 MINOR

- **All 4 v5 tabs present** with identical names. `FDIC SOD Census (4cty)` and `NCUA CU Census (4cty)`: **0 changed cells** (cell-by-cell). `Legend`: all 51 original rows byte-identical; 7 rows appended (52–58). Funding Table rows 1–214 carried with row alignment intact (all 22 new rows appended below).
- **Independent cell-by-cell diff, Funding Table rows 1–214 × 36 cols:** 117 changed cells total = 67 compliant appends (full original text + ` ‖ v6 2026-06-10:` marker), 46 fills over blank/`N/M`/`—` cells, **4 overwrites of non-bare-N/M cells** (below).

### 🟠 MAJOR-1 — Overwrite of qualified-N/M cells with semantic reversal (2 cells)
- **Funding Table H10** (BMO Bank, EWS): `N/M (not on DoC EWS list)` → `Reports to EWS (no inquiry DP) (DOC-LIST + COMMUNITY-DP; DP 2026-05-22; v6 2026-06-10)`
- **Funding Table H19** (First Citizens Bank, EWS): `N/M (not on DoC EWS list)` → `Reports to EWS (no inquiry DP) (DOC-LIST + COMMUNITY-DP; DP 2022-11-20; v6 2026-06-10)`
- Issue: the prior cells were N/M-class but carried an evidentiary parenthetical that was **removed from the cell and contradicted** (new evidence says they DO report to EWS) instead of using the append format. Strict reading of the #1 rule requires full original text + append for any non-blank/non-bare-N/M cell.
- Mitigations (why not CRITICAL): (a) both new values are **fully supported** by `out/ews_chex_mapping.csv` rows for ranks 9 and 18 (Dealgamer 2026-05-22 #2326911; Gadget 2022-11-20 #1492418); (b) the **v6 Change Log entries #2 and #7 preserve the complete old values verbatim** and label the operation `WRITE (was '…')` — nothing is unrecoverable; (c) the corresponding Sources cells (AJ10/AJ19) received compliant appends carrying the evidence trail.
- Recommended remediation (do NOT fix without owner sign-off): convert the two cells to append format, e.g. `N/M (not on DoC EWS list) ‖ v6 2026-06-10: Reports to EWS …`.

### 🟡 MINOR-1 — Same overwrite pattern, meaning-preserving (2 cells)
- **G27** (Enterprise B&T, Chex): `N/M (no disclosure, no DPs)` → `N/M re-confirmed 2026-06-10: absent from DoC Chex+EWS lists…` — restates and strengthens the original meaning; no information lost.
- **W27** (Enterprise B&T, HP Bureau): `N/M (zero public DPs — datapoint desert)` → `confirmed datapoint desert as of 2026-06-10…` — same meaning; loses the leading `N/M` token only.
- Both logged in Change Log with full old values. Cosmetic-process deviation, data correct (matches `enterprise_bt_dossier.md` §4–5).

---

## 2. PROVENANCE SPOT-CHECKS — PASS (0 findings; ~20 cells checked, all trace)

**Mandated checks:**
- **Enterprise B&T (row 27):** Self-UW `VERIFIED HIGH — LNCRCD $3.155M credit-card loans on OWN call report 2026-03-31` traces exactly to `enterprise_bt_dossier.md` §1 item 1 (api.fdic.gov LNCRCD CERT 27237). Banker = **Jessica Morrow** with explicit `NOT "Jordan"` correction (dossier line 60). **$50K still marked UNVERIFIED in all 4 cells where it appears** (Est. Limit, Approval Info, Best For, Confidence) — NOT overstated. ✓
- **LAFCU (row 13):** second-chance claim **DOWNGRADED to UNVERIFIED** verbatim (dossier §5: "DOWNGRADED"); Chex+hard-pull at membership re-verified on 2 live pages ✓; NCUA charter **1207**, chartered 1936-03-31 ✓ (dossier header). Card-bureau conflict (EQ-or-EX vs TU) faithfully carried. ✓
- **FNBO (row 215):** `$50,000 stated MAX (VERIFIED fnbo.com 2026-06-10)` + DPs `$7.1K instant / $13.9K / $15K prequal` match `w2_banks_screen.md` §E exactly; myFICO thread IDs match. ✓
- **Stanford FCU (row 216):** gates `min 640 FICO + 2 years in business + 6 months SFCU membership` present and quoted (matches `w2_cus_screen.md` §H verbatim); Chex cell = `N/M (pull type unconfirmed — DoC checking-bonus pages note it; sfcu.org 403s scrapers)` — **UNKNOWN, not invented**. ✓
- **Sam's Club (row 222):** no-PG qualified as **in-club EIN-only** in 5 separate cells; "ONLINE app FORCES PG + personal hard pull" matches `w2_banks_screen.md` §H; rewards detail (5% gas / 3% dining) traces to `w2_banks_screen.csv` Products field. ✓
- **BILL/Divvy (row 221):** `⚠️ PG CONFLICT: Nav "no PG" vs Merchant Maverick "PG sometimes"` flagged in 3 cells — matches `w2_banks_screen.md` §G. ✓
- **Citizens Bank N.A. (row 227):** remains `NOT CA-accessible` — Private-Bank-only CA presence, 15-state footprint gate, "Re-flag if retail CA branches open" — matches `w2_banks_screen.md` §C. ✓
- **UMB (row 217):** own-card claim (`issued by UMB Bank n.a.`), Central-CA-only branches, `$200/20K-pt bonus @$2K/90d`, limits UNKNOWN — all trace to `w2_banks_screen.csv` row D. ✓

**12 random enriched Chex/EWS cells** (rows 13, 19, 24, 27, 42, 51, 57, 82, 84, 99, 133, 151) cross-checked against `ews_chex_mapping.csv` by Rec Rank: **all 12 match** pull/sensitivity/evidence-grade/DP-date, including the City National Bank "DOC-LIST (ambiguous)" caveat and Tech CU's dated-2016 EWS DP. **No fabricated claims found.**

---

## 3. DIAMOND/PLATINUM TAB LOGIC — PASS (0 findings)

- States **"STRICT DIAMOND QUALIFIERS TODAY: 0 (zero)"** — honest. ✓
- D1 FNBO: `No Chex/EWS = ❓ UNKNOWN — zero DPs either way`; missing leg = "Chex/EWS behavior" ✓ (matches w2_banks).
- D2 Enterprise B&T: labeled "Diamond candidate (Platinum verdict)" — matches dossier's verdict ("PLATINUM-CANDIDATE, not Diamond"); $50K leg ⚠️ UNVERIFIED ✓.
- D3/D4 BCU/Skyla "EWS-clean VERIFIED, Chex UNVERIFIED, one call from Diamond" — traces to `ews_chex_report.md` §2 (#2326911) ✓.
- D5 Ramp/Mercury honestly labeled "DIFFERENT ANIMAL — not a substitute for a $50K revolver" ✓.
- Platinum criteria (self-UW + $20K+ + no Chex/EWS evidence + SoCal-accessible): P1 Stanford fits with remote-onboarding caveat stated; P2 EBT fits; P3 UMB "candidate" with limits-UNKNOWN caveat; P4 Sam's Club explicitly caveated `✗ Synchrony co-brand (not self-UW — included for the no-PG angle)` and `below $20K at approval` — non-fits are caveated, none silently passed. ✓
- Near-misses: LAFCU fails exactly on membership-stage Chex (verbatim quote) ✓; Citizens fails geo ✓.

---

## 4. NEW DATA TABS — PASS (0 findings)

| Tab | Sheet | Source CSV | Match | Spot-check |
|---|---|---|---|---|
| FDIC SOD 6cty 2025 | 123r×18c | fdic_sod_census_6cty_2025.csv 123r×18c | ✓ exact | 5 random rows, 0 mismatches |
| NCUA CU 6cty 2026Q1 | 162r×18c | ncua_cu_census_6cty.csv 162r×18c | ✓ exact | 5 random rows, 0 mismatches |
| EWS-Chex Map v6 | 214r×12c | ews_chex_mapping.csv 214r×12c | ✓ exact | 5 random rows, 0 mismatches |
| ibanknet CA 2026Q1 | 452r×12c | ibanknet_ca_institutions.csv 452r×12c | ✓ exact | 5 random rows, 0 mismatches |

---

## 5. INTERNAL CONSISTENCY — PASS (0 findings)

- **Rec Rank contiguity:** new rows occupy sheet rows 215–236 with Rec Rank exactly **214–235, contiguous, no gaps/dupes**. ✓
- **No duplicate institutions:** all 22 new-row names absent from v5 (`v5_all_institution_names.txt` + `v5_funding_table.csv` grep). Specifically verified: v5's only "UMB Bank" reference is as agent issuer behind Farmers & Merchants Bank (`UMB Bank, N.A. (Card Center Direct)`) — the new row 217 is UMB's **own** card and explicitly notes "UMB also runs cobrand/agent programs for OTHER banks" — **no contradiction**. v5 "Firefighters" = Firefighters First CU (≠ new San Diego Firefighters FCU); v5 FNBO mentions = agent behind Flagstar/Pacific Premier (new row 215 is FNBO direct, as `w2_banks_screen.md` documents); v5 "Ventura County" hit = membership text inside another row, not a VCCU row; v5 Ramp/Mercury = mentions inside Capital One/Column rows. ✓
- **CSV export:** 236×36, **0 mismatches** against the xlsx Funding Table across all 8,496 cells. ✓
- **Change Log:** my independent diff found 117 changed cells in rows 2–214; the log's Funding-Table entries for rows ≤214 = exactly those same 117 (row, field) pairs — **0 unlogged changes, 0 phantom entries**. Plus 22 new-row entries (215–236) + 5 new-tab entries + 1 Legend entry = 145, matching the stated "145 entries". WRITE-type entries preserve full old values. ✓

---

## 6. USABILITY — PASS with 2 MINOR

- Frozen panes: Funding Table D2 (same as v5), all data tabs A2, Change Log A18. ✓
- Autofilters: Funding Table `A1:AJ236` (covers all 236 rows — improved over v5's header-only `A1:AJ1`); all 4 new data tabs cover full extents; Change Log `A17:I162`. ✓
- Legend updated: 7 appended rows documenting the v6 marker convention, new tabs, tier definitions, and sequencing. ✓

### 🟡 MINOR-2 — 141 text cells stored as formulas (pre-existing v5 defect, carried forward)
98 cells in `FDIC SOD Census (4cty)` + 43 in `NCUA CU Census (4cty)` contain note text beginning with `=` (e.g., `= California Bank & Trust (CB&T branches report under…)`) stored as `<f>` formula elements — these render as `#NAME?` errors in Excel. **Identical in v5 (141 = 141, same coordinates)** — v6 faithfully preserved them per add-only, so this is NOT a v6 regression, but "no broken formulas" is technically not met. Fix candidate for v7 (prefix with `'` or space), with owner approval.

### 🟡 MINOR-3 — 💎 Diamond-Platinum Tiers tab has no frozen panes / autofilter
It is a sectioned narrative-table layout (3 sections with repeated header rows), so an autofilter is arguably inapplicable, but a freeze at row 7 would help. Cosmetic.

---

## Method notes
- Tooling: python3 + openpyxl 3.1.5; raw XML inspection of both xlsx archives for formula elements.
- Diff basis: cell-by-cell string comparison, rows 1–214 × cols 1–36, plus full comparison of all carried tabs.
- Random sampling seeds disclosed in audit scripts (seed 42 for data tabs, seed 7 for enriched-cell sample).
- Nothing was modified. All findings are report-only.
