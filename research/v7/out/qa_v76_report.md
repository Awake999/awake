# QA-3 Adversarial Verification — v7.6 build of ca_business_credit_funding_v7.xlsx

- **Auditor:** QA-3 (did not build v7.6) · **Date:** 2026-06-11
- **File:** `/home/user/awake/research/v7/deliverables/ca_business_credit_funding_v7.xlsx` (21 tabs, confirmed)
- **Baseline:** `git show 53bd431` pre-build commit → `/tmp/v75_committed.xlsx` (20 tabs)
- **Methods:** openpyxl cell-level diff (full workbook), raw-XML hyperlink audit, multiset row-preservation checks, source-CSV tracing (`chex_socal_banks.csv`, `chex_socal_cus.csv`, `wgold_screen.csv`, `icba_community_banks.csv`, `chex_socal_cus.md`), 7 live WebFetch spot-clicks.

## VERDICT: **PASS-WITH-ISSUES** — 0 CRITICAL · 3 MAJOR · 7 MINOR

---

## CHECK 1 — User's main-target spec on '1A. MAIN TARGET ⭐'

### 1(a) Only SoCal-accessible self-UW non-majors — **PASS**
Full tab dump (43 rows, 32 institutions): no Chase, no U.S. Bank, no Wells Fargo, no BofA/Citi anywhere on 1A. Largest entities present are CB&T (Zions charter, self-UW, Tier 4 warning row) and City National LA (RBC sub, self-UW) — both defensible as non-money-center self-underwriters and both placed in caution tiers, not recommendations. Every row has a stated access path (branch miles or verified remote-join path). NO-GO geofenced institutions (DCU, Truliant, Northeast MN, CapFed) correctly kept OFF 1A and parked as master reference rows.

### 1(b) Tier truthfulness vs source CSVs — **PASS with 2 MAJOR exceptions**
- 🏆 Tier 1 = **exactly** the 5 CSV-verified fintechs (Mercury, Bluevine, Found, Novo, Lili). ✓
- Relay = marked "🥈 (T1 pending one call)" with the exact closing question — matches CSV "LIKELY-NO… own-doc language not located". ✓ Not promoted.
- Demotions (conservative): F&M LB and Banc of Cal moved from CSV "⚠ pulls one" into ❌ T5 because business scope is own-doc verified — matches the tab's stricter T5 definition and the user's spec. ✓
- 17 of 19 bank/CU verdict mappings exact (Beneficial 🥈, CBC 🥈, FNBO ❓, Enterprise ❓, Sunwest ❓, Citizens Business ❓, Chino ❓, ABB ❓, IDB ❓, UMB ⚠, WAB ⚠, TriCo ⚠, CB&T ⚠, Logix ⚠, CommunityAmerica ⚠, AdelFi ⚠, Valley Strong 🥈, Southland ❌, CU SoCal ❌).
- **MAJOR-2 (tier inflation, 2 rows):**
  - **City National Bank (R24):** source verdict `⚠ pulls one (Chex probable consumer…)` → tab places it ❓ Tier 3. One-tier promotion. The cell honestly carries the twin-risk rationale, but the band overstates.
  - **BCU (R19):** source verdict `❓ UNKNOWN (Chex)… 2019 DP hints Chex IS checked` → tab places it 🥈 Tier 2 "LIKELY-NO". The row's own D-cell ("UNKNOWN… hints Chex IS checked") contradicts the Tier-2 band promise.
- Stanford FCU ⚠4 with "DoC does-pull list" evidence: CSV says unconfirmed, but `chex_socal_cus.md` "Closed questions" section confirms it, and live DoC fetch shows "Stanford Credit Union — Does pull". ✓ Supported.
- Omissions: Skyla (Chex-confirmed, EWS-clean, NC FOM unverified) left off 1A — defensible, noted MINOR. Firefighters First / Wescom / SchoolsFirst correctly excluded (not joinable / no biz product).

### 1(c) Tier 2/3 banker questions + phones — **PASS**
All 6 Tier-2 and all 8 Tier-3 rows carry a concrete, row-specific question in column J. Phones present exactly where the source CSVs have them: Rize 800-866-6474, Lafayette 240-292-5670 (T2); Logix 800-328-5328, CommunityAmerica 800-892-7957, AdelFi 800-921-1130 x1650 (T4). "—" only where no number exists in any source.

### 1(d) ❌ tier own-doc verbatims — **PASS**
- F&M LB (R41): "new accounts are subject to verification through ChexSystems®" + "apply to both personal account owners... and business account owners" — business-scope verbatim present. ✓
- Banc of Cal (R40): "by becoming an authorized signer" — signers verbatim present. ✓
- Southland (R42): "All new accounts are verified through ChexSystems". ✓
- CU SoCal (R43): "All accounts verified by ChexSystems" + inquiry-sensitivity (denied at 3/6mo). ✓

## CHECK 2 — Truth of key new claims (traced to source files + live fetch)

| Claim | Trace | Live fetch | Verdict |
|---|---|---|---|
| Lafayette FCU GOLD-candidate, 3 OPEN Qs, not certainty | Master R245 AI: "OPEN Qs: (1) creditor line… (2) remote business account for CA LLC… (3) screening vendor"; P col: "LIKELY SELF-ISSUED… creditor line pending" | lfcu.org/business/credit-card confirms "high limits"/CURewards/no-AF/employee cards, no published max, no issuer named — consistent with "pending" framing | **PASS** |
| Lafayette LA-twin warning | Master R245 AI tail: DoC slug "la-only-lafayette-federal-credit-union…" = "the LOUISIANA entity — do NOT import onto lfcu.org"; name cell "NOT Langley, NOT Lafayette Schools FCU of Louisiana"; 1A R15 carries abbreviated twin flag | — | **PASS** |
| DCU geofence + First Tech merger | Master R246: footer verbatim "Available in - MA, NH, RI, ME, VT and CT", $25K max, merger eff. 2026-01-01; cross-append on First Tech row 74 | dcu.org page confirms "MAXIMUM LINE $25,000", "Available in - MA, NH, RI, ME, VT and CT", merger text verbatim | **PASS** |
| Truliant in-branch verbatim | Master R247: "Business must be locally owned and have access to a Truliant branch" + "All owners/authorized signers… present" + "Please visit your nearest branch" | truliantfcu.org page confirms all three quotes verbatim | **PASS** |
| Gateway attribution FIX (MN twin) | Master R200 col R: "‖ v7.6: ATTRIBUTION FIX… Elan page at gateway.bank… = GATEWAY BANK, MENDOTA HEIGHTS MN… name-twin"; workbook-wide grep: no residual cell attributes Elan to Oakland (old row already said no-card/Underwriter "None", so the fix appends without duplicating a wrong claim; tabs 9/12 mentions are name-only) | — | **PASS** |
| Pinnacle disambiguation | Master R127 col AI append: Gilroy CERT 58297 only live CA Pinnacle, no card; TN/AL twins named | — | **PASS**, but see MINOR-4: legacy col Q still shows "✅ Mastercard business (via TIB)" un-reconciled with the new no-card finding |

Extra spot-clicks: Rize business-visa page confirms self-issued Business Visa Platinum "$5,000 to $50,000" ✓. Southland page 403s to bots (cannot re-verify own-site verbatim; no contradiction). **Bluevine: see MAJOR-3.**

## CHECK 3 — Overhaul quality

- **README START-HERE flow — PASS.** Steps 1→4 reference `1A. MAIN TARGET ⭐`, `1B. FUNDING BY BUREAU`, `1C. EXECUTION CHECKLISTS`, `1. BEST TARGETS` — all tab names/positions match reality. Tab map groups (GOLD action 1/1A/1B/1C/2 · BLUE data 3–12 · GRAY 13–17) match actual tab colors exactly (FFD966/9DC3E6/B0B0B0). Old README content preserved below the new guide (add-only insert). MINOR-3: R55 says "master rows 244–249" (rank numbers); physical sheet rows are 245–250 — Change Log R250 states it correctly.
- **Geo band rows — PASS.** LB: band R2 (0.0–0.8 mi), R14 (1.14–2.82), R18 (3.15–4.9) — all rows within boundaries. Fontana: R2 (0.46), R4 (1.18–2.82), R12 (3.47–7.91) — correct. Distance sort preserved, zero rows lost (multiset: 33→33, 28→28 data-equivalent).
- **ICBA regrouping — PASS.** 21 bank rows in CSV ↔ 21 data rows on tab, set difference empty both directions; group counts match Change Log R272 (4/2/5/1/4/4/1). Zero rows lost.
- **Guide rows — PASS.** Present on 1 (R2), 1A (R2–R4), 1B (R2 HOW-TO, pre-existing), 1C (R2 HOW-TO, pre-existing), 2 (R2).
- **Tab colors — PASS** (as above; tab 4 correctly re-colored gold→blue, values untouched).
- **1A tier band fills:** C6EFCE green / E2EFDA lt-green / FFE699 amber / F8CBAD orange / FFC7CE red — matches README legend. ✓

## CHECK 4 — Mechanical

- **Hyperlinks — PASS (with MINOR-1).** 570 embedded links (old 471 + 99 new on 1A; counts per tab otherwise unchanged — tabs 3/9/12/13 never had embedded links; their URLs are Sources-column text by design, both versions). Raw-XML audit: **0 links anchored on empty cells**; text→target pairing multiset identical pre/post on every row-shifted tab (1, 2, 5, 6, 7) → the openpyxl shift bug did NOT occur; links were re-anchored. 12-link sample across 1A/7/1/5: 11 sensible; 1 mismatch — 1A **L7** displays "mercury.com/business-banking" but targets the DoC don't-pull list (MINOR-1).
- **Freeze panes — PASS.** All updated for inserted rows: 1 A3→A4, 2 A3→A4, 1A A6, 9 A3, others unchanged-correct.
- **Autofilters — FAIL (MAJOR-1).** No filter range was extended after v7.6 inserts/appends; every restructured/appended tab keeps its stale v7.5 ref:
  - Tab 3: `A1:AJ244` vs 250 rows — **all 6 new v7.6 rows (Lafayette, DCU, Truliant, Northeast, CapFed, Mokelumne) outside the filter**.
  - Tab 1: `A2:P34` — anchored on the new guide row, last data row 35 (rank 32) excluded.
  - Tab 2: `A2:G16` — header misaligned, last row 17 (CB&T) excluded.
  - Tab 5: `A1:M33` — rows 34–36 excluded; Tab 6: `A1:N28` — rows 29–31 excluded (**includes Rize CU**, a key new target); Tab 7: `A1:N22` — rows 24–29 excluded (Chino Commercial, OneUnited, Tustin, TIB, Premier).
  - Tab 9: `A1:L214` — filter header sits on the new NOTE row; row 215 excluded. Tab 13: `A1:I246` — all 29 new log rows excluded.
  - This is the same defect class fixed in the v7.1 QA-2 patch ("filters extended"); Change Log R275's self-check covered links/freezes but not filters. (1A itself ships with no autofilter — MINOR-5, defensible given tier bands, consistent with 1B/1C.)
- **CSV mirrors — PASS.** `main_target.csv` = 43 rows, 1:1 with 1A; all diffs are the intentional "text (URL)" embedded-link convention from the v7.5 patch. Mercury L7 mismatch is faithfully mirrored into the CSV (inherits MINOR-1).
- **Change Log 1:1 sample of 8 — PASS (with MINOR-2).** Verified against the actual cell diff: R251 (Preferred R59/R ✓), R252 (Gateway R200/R ✓), R253 (Pinnacle R127/AI ✓), R254 (F&M R56/G ✓), R255 (Banc of Cal R46/G ✓), R256 (City National R42/G ✓), R263 (Firefighters R17/E ✓), R264 (First Tech R74/AI ✓). Structural entries R249/R250/R265–R267/R270/R272 also verified. One error: R271 logs Fontana band rows as "2, 4, 13" — actual 2, 4, **12** (MINOR-2).

## CHECK 5 — Add-only vs committed v7.5

- **Master rows 1–244: PASS, zero violations.** Cell diff: 0 deletions, 0 rewrites. Exactly 16 cells modified, all true `‖ v7.6:`-style appends (verified `new.startswith(old)`), on rows {17, 42, 46, 56, 59, 67, 74, 80, 127, 152, 153, 200, 216, 239} — matching the Change Log claims. All new cells confined to rows 245–250.
- **Untouched tabs: PASS.** Exactly 11 tabs byte-value-identical: 1B, 1C, 4, 8, 10, 11, 12, 14, 15, 16, 17.
- **Restructured tabs (0, 1, 2, 5, 6, 7, 9): PASS.** Row-multiset comparison: `lost_exact = 0` on every tab — all old rows survive verbatim; diffs are inserted guide/band/note rows and row shifts only. README old content preserved below new guide; tab-9 v6 map carried unchanged under the new note row.

---

## Severity register

### CRITICAL — none

### MAJOR (3)
1. **Stale autofilters workbook-wide** (tabs 1, 2, 3, 5, 6, 7, 9, 13): no range extended after v7.6 inserts/appends. Concrete harm: a user filtering the master will never see the 6 new v7.6 rows; filtering Fontana hides Rize CU; tab-1/2/9 filter headers sit on guide/note rows. Recurring defect class; missed by the build's own self-check row.
2. **Tier inflation on 1A, 2 rows:** City National promoted ⚠ (source verdict "pulls one") → ❓ Tier 3; BCU promoted ❓ UNKNOWN-leaning-yes → 🥈 Tier 2 "LIKELY-NO". Both cells disclose the underlying evidence honestly, but the band placement overstates vs `chex_socal_banks.csv` / `chex_socal_cus.csv`.
3. **Bluevine Tier-1 "VERIFIED own" verbatim not reproducible at cited sources:** live fetch of bluevine.com/faq (the row's hyperlink) contains no ChexSystems language, and the DoC don't-pull list fetch did not show Bluevine (Found ✓ does appear). The 🏆 grade rests on the upstream CSV's claim; the tab is faithful to its source, but the source verbatim failed both spot-clicks. Recommend re-locating the quote (likely bluevine.com/business-checking or an archived FAQ) or downgrading Bluevine's evidence grade.

### MINOR (7)
1. 1A L7 (Mercury source link): display text "mercury.com/business-banking" → actual target doctorofcredit.com don't-pull list (text/target mismatch; mirrored into main_target.csv).
2. Change Log R271 off-by-one: Fontana band rows logged "2, 4, 13"; actual 2, 4, 12.
3. README R55 "master rows 244–249" uses Rec-Rank numbers; physical rows are 245–250 (ambiguous; Change Log R250 has it right).
4. Pinnacle master R127: legacy col Q "✅ Mastercard business (via TIB)" / col AE card list left standing beside the v7.6 no-card disambiguation — add-only constraint honored, but a column-Q-only reader is misled; deserves a pointer in col Q.
5. 1A has no autofilter (spec wording "autofilters on all action tabs"); defensible with tier bands — 1B/1C likewise have none.
6. Skyla CU (Chex confirmed, EWS-clean, in `chex_socal_cus.csv`) omitted from 1A; defensible (NC FOM, remote eligibility unverified) but unexplained on the tab.
7. Southland own-site verbatim not re-verifiable by bot (HTTP 403); claim rests on build-time capture — no contradiction found.

## 30-second test on 1A
**PASS.** The tab is position 3 with a ⭐ in the name and gold color; README Step 1 points to it. Opening it: title + 1-line purpose + how-to + legend (rows 1–4), frozen header at row 5, then five color-banded tiers in priority order. Within ~10 seconds the user sees: 🏆 green block = "open now" (Mercury, Bluevine, Found, Novo, Lili + Relay-pending), each with apply path; 🥈 next-best with the ONE call to make (question in col J, phone in col K). The main target is visible instantly without scrolling past row 12.

## Files
- Report: `/home/user/awake/research/v7/out/qa_v76_report.md`
- Deliverable audited: `/home/user/awake/research/v7/deliverables/ca_business_credit_funding_v7.xlsx`
- Baseline: commit `53bd431` (extracted to `/tmp/v75_committed.xlsx`)
