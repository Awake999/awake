# NCUA Credit Union Census — 6-County SoCal Gap Report (v6)

**Retrieval date:** 2026-06-10
**Counties:** PRIORITY = Los Angeles, San Bernardino, Riverside, Orange | OUTLIER (lower priority) = Ventura, San Diego
**Companion file:** `ncua_cu_census_6cty.csv` (161 rows, one per credit union)

## Method (exact)

1. Downloaded NCUA quarterly call-report archive (cycle 2026-03-31, posted 2026-06-09):
   `https://ncua.gov/files/publications/analysis/call-report-data-2026-03.zip`
2. Parsed three files from the zip with python3 (csv module):
   - **`Credit Union Branch Information.txt`** — every CU site nationally; filtered `PhysicalAddressStateCode = CA` and `PhysicalAddressCountyName2` ∈ {Los Angeles, San Bernardino, Riverside, Orange, Ventura, San Diego}. Counted sites per CU per county (includes Corporate Office + Branch Office site types).
   - **`FOICU.txt`** — HQ name/city/state per charter number.
   - **`FS220.txt`** — `Acct_010` (TOTAL ASSETS, per `AcctDesc.txt`).
   - **`TradeNames.txt`** — d/b/a names, used for v5 name matching (e.g. FIRST TECHNOLOGY = "First Tech Federal Credit Union").
3. The NCUA Locator API was not needed; the branch file is the authoritative underlying dataset and covers all six counties in one pass.
4. v5 comparison: charter-number match against `v5_ncua_census.csv` (140 CUs, 2026-06-09), then normalized/fuzzy name match against `v5_all_institution_names.txt` (parentheticals and trade names indexed as aliases).
5. Top-10 gap business-lending spot checks via each CU's website / web search, 2026-06-10.

## Headline counts

| County | CUs with sites | Sites (raw) | Sites excl. vendor artifacts |
|---|---|---|---|
| Los Angeles | 104 | 354 | 353 |
| San Bernardino | 30 | 73 | 70 |
| Riverside | 16 | 65 | 65 |
| Orange | 35 | 121 | 121 |
| Ventura (OUTLIER) | 13 | 44 | 43 |
| San Diego (OUTLIER) | 32 | 192 | 183 |

- **Total unique CUs: 161** — 140 with sites in the 4 priority counties (**exactly matches the v5 census of 140 on 2026-06-09**; all 140 v5 charters reconciled 1:1, zero discrepancies in either direction), 21 outlier-county-only.
- **v5 status: 143 IN_V5, 18 NEW_GAP, 0 unresolved POSSIBLE_MATCH.** All 18 NEW_GAPs are Ventura/SD-only (OUTLIER) — confirming the v5 4-county census had no holes.
- 27 CUs have out-of-state HQ (`OOS_HQ_with_SoCal_branches = Y`).

## Data-integrity finding: vendor-address artifacts

The NCUA branch file lists some **core-processor / shared-network vendor addresses** as CU "Corporate Office" sites. Two San Diego addresses are vendor hubs, not branches:
- **8985/8975 Balboa Ave, San Diego** = Symitar/Jack Henry (incl. Centurion Disaster Recovery)
- **2305 Historic Decatur Rd, San Diego** = Corelation Inc (core processor)
- **9692 Haven Ave, Rancho Cucamonga (SB)** = CO-OP Shared Branching

11 such rows were found and are flagged `ARTIFACT` in the CSV's Match_note. **6 of the 18 NEW_GAP CUs are ALL-ARTIFACT** (no real SoCal retail presence): Point Breeze (MD), Carolinas Telco (NC), Guardian (WI), Carolina Foothills (SC), Ohio Healthcare (OH), Dixies (SC). Their own websites list no California branches (verified for Carolinas Telco and Guardian 2026-06-10). This is the mechanism by which OOS "branches" can be phantom — the real OOS gold (America First UT, CommunityAmerica MO, etc.) was already in v5.

## NEW_GAP credit unions (assets desc)

### Real-presence gaps (12) — all OUTLIER counties

| # | Charter | Credit Union | HQ | Assets | County | Note |
|---|---|---|---|---|---|---|
| 1 | 68458 | VENTURA COUNTY CU | Ventura, CA | $1.47B | Ventura (6 br) | **Business accounts + commercial loans advertised** (vccuonline.net/business). Strongest gap. |
| 2 | 7608 | OCEANAIR FCU (fka CBC FCU) | Oxnard, CA | $871M | Ventura (6 br) | **"Epic Business Checking" + business products** (oceanair.org). Navy-base heritage, community charter. |
| 3 | 68377 | MYPOINT CU (fka PLCU) | San Diego, CA | $701M | SD (5 br) | **Business checking, business loans, commercial RE** (mypointcu.com/business). |
| 4 | 68409 | CABRILLO CU | San Diego, CA | $572M | SD (4 br) | Consumer-focused site; no business products found (cabrillocu.com). Border-Patrol heritage. |
| 5 | 61003 | WHEELHOUSE CU (fka SD Metropolitan) | San Diego, CA | $457M | SD (4 br) | Was an SBA PPP lender; current site shows mainly consumer products. Marginal. |
| 6 | 24110 | SAN DIEGO FIREFIGHTERS FCU | San Diego, CA | $152M | SD (1 br) | Firefighter/family FOM; no business line found. |
| 7 | 11099 | EAST COUNTY SCHOOLS FCU | El Cajon, CA | $148M | SD (2 br) | School-employee FOM; consumer focus. |
| 8 | 13495 | COUNTY SCHOOLS FCU | Ventura, CA | $91M | Ventura (1 br) | Ventura County school-employee FOM. |
| 9 | 13402 | ESCONDIDO FCU | Escondido, CA | $66M | SD (1 br) | Small community/municipal CU. |
| 10 | 13526 | EMPLOYEES CHOICE FCU | (SD area), CA | $23M | SD (1 br) | Small SEG CU. |
| 11 | 14016 | INLAND FCU | (SD area), CA | $15M | SD (1 br) | Very small. |
| 12 | 18405 | CHULA VISTA CITY EMPLOYEES | Chula Vista, CA | $3M | SD (1 br) | Municipal micro-CU. |

### Artifact-only "gaps" (6) — no real SoCal branch, listed for traceability

| Charter | Credit Union | HQ | Assets | Artifact address |
|---|---|---|---|---|
| 66585 | POINT BREEZE CU | Hunt Valley, MD | $1.00B | Corelation, 2305 Historic Decatur Rd, SD (has full business banking in MD — pbcu.com/business — but no CA retail branch) |
| 23494 | CAROLINAS TELCO FCU | Charlotte, NC | $514M | Corelation, SD. Own site: Carolinas-only locations. |
| 66638 | GUARDIAN CU | Oak Creek, WI | $291M | Symitar, 8985 Balboa Ave, SD. Own site: SE-Wisconsin-only branches. |
| 13476 | CAROLINA FOOTHILLS FCU | Spartanburg, SC | $220M | Symitar, 8985 Balboa Ave, SD |
| 24725 | OHIO HEALTHCARE FCU | OH | $109M | Symitar, 8985 Balboa Ave, SD |
| 5569 | DIXIES FCU | SC | $47M | Jack Henry, 8985 Balboa Ave, SD |

### Top-10 business-lending quick-check summary (real gaps)

Checked 2026-06-10: Ventura County CU (**yes — biz accounts + commercial loans**), OceanAir (**yes — business checking**), MyPoint (**yes — biz loans + CRE**), Cabrillo (no), Wheelhouse (ex-PPP lender, weak), SD Firefighters (no, FOM-gated), plus the four artifact OOS CUs above which have no real CA presence. **Screen order for outlier counties: Ventura County CU → OceanAir → MyPoint.**

Note: large SD-county CUs already IN_V5 via trade-name/charter match and therefore not gaps: Mission Fed ($7.2B, 36 SD br), First Tech ($28.6B, SD), SDCCU, California Coast, Frontwave, BluPeak.

## Sources
- https://ncua.gov/files/publications/analysis/call-report-data-2026-03.zip (cycle 2026-03-31; files: Credit Union Branch Information.txt, FOICU.txt, FS220.txt, TradeNames.txt, AcctDesc.txt) — retrieved 2026-06-10
- https://ncua.gov/analysis/credit-union-corporate-call-report-data (index page)
- Spot checks 2026-06-10: vccuonline.net/business, oceanair.org, mypointcu.com/business, cabrillocu.com, wheelhousecu.com, pbcu.com/business, ctelco.org, guardiancu.org, carolinafoothillsfcu.coop, sdffcu.org
- Comparison baselines: /home/user/awake/research/v6/v5_ncua_census.csv (2026-06-09), /home/user/awake/research/v6/v5_all_institution_names.txt
