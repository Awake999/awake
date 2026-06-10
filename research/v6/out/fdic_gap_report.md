# FDIC SOD 2025 — Southern California 6-County Census: Gap Report

**Retrieval date:** 2026-06-10
**Data source:** FDIC Summary of Deposits (SOD) API, YEAR=2025 (index `sod_1769439439907`, built 2026-01-26 by FDIC)
**Counties:** Los Angeles, San Bernardino, Riverside, Orange (PRIORITY-4CTY) + Ventura, San Diego (OUTLIER)

## Result summary

- **122 distinct FDIC-insured institutions** operate branch offices across the 6 counties (2,939 branch records).
- **113 institutions** have branches in the 4 priority counties — exactly matching the prior 4-county census of 2026-06-09 (~113). All 113 CERTs in `v5_fdic_census.csv` were re-confirmed present in the 2025 SOD data (zero attrition, zero unexplained additions).
- **8 outlier-only institutions** (Ventura/San Diego only) matched the v5 names list exactly: Axos Bank, Endeavor Bank, Bank of the Sierra, Montecito Bank & Trust, Home Bank of California, Neighborhood National Bank, Community West Bank, Hatch Bank.
- **43 of 122 institutions have out-of-state HQs** (`OOS_HQ_with_SoCal_branches = Yes`).
- **1 NEW_GAP institution** (below).
- Total branch deposits across the 6 counties: **$895,891,627K (~$895.9B)**.

## Counts per county (institutions / branch offices)

| County | Institutions | Branches | Priority |
|---|---|---|---|
| Los Angeles | 92 | 1,394 | PRIORITY-4CTY |
| Orange | 72 | 535 | PRIORITY-4CTY |
| San Bernardino | 29 | 202 | PRIORITY-4CTY |
| Riverside | 28 | 252 | PRIORITY-4CTY |
| San Diego | 45 | 437 | OUTLIER |
| Ventura | 20 | 119 | OUTLIER |

## NEW_GAP institutions (sorted by 6-county deposits, descending)

### 1. Monet Bank — CERT 32574 — HQ Plano, TX — OOS_HQ: Yes
- **6-county footprint:** 1 branch, San Diego County only (San Diego Branch, 8880 Rio San Diego Dr Ste 103, San Diego CA 92108), deposits **$52,451K**.
- **Who they are:** This is the renamed **Beal Bank, SSB** — Andy Beal's Plano, TX savings bank (est. 1988, ~$3.17B assets per FDIC institutions API, ACTIVE=1). Name change verified via the FDIC history API (CERT 32574 records appear under "Beal Bank"/"Beal Bank, SSB" through 2021, "Monet Bank" currently). Neither "Beal" nor "Monet" appears anywhere in the v5 lists.
- **Why interesting:** Out-of-state-HQ bank with a SoCal deposit-taking branch — exactly the profile flagged as the prize. Caveat: Beal/Monet is historically a loan-acquisition/CD-funding specialist, not a mainstream business-credit issuer; screen accordingly.
- **Why it was missed in v5:** San Diego is outside the prior 4-county scope; the bank has no LA/SB/Riverside/Orange branches.

*(No other NEW_GAP institutions — the 4-county universe is fully covered by v5, and the remaining outlier-county banks all match v5 names.)*

## Method notes

1. Queried the FDIC SOD API directly with `curl -L` (the `banks.data.fdic.gov/api/sod` endpoint 301-redirects; `-L` resolves it). One query per county, `limit=10000`; every query returned `meta.total == len(data)` so no pagination was needed.
2. Raw per-county JSON responses saved alongside this report (`sod_2025_<County>.json`).
3. Aggregated branch rows to institution level by CERT (`aggregate.py` in this directory). `DEPSUMBR` is in $thousands as reported by FDIC; institution HQ from SOD fields `CITY`/`STALP`.
4. v5 matching: (a) exact CERT match against `v5_fdic_census.csv` (113/113 hit); (b) normalized name match (lowercase, punctuation stripped, suffixes like "National Association"/"N.A."/"SSB" removed) against the 388-name `v5_all_institution_names.txt` (8 hits); (c) loose token-overlap candidates would have been labeled POSSIBLE_MATCH — none were needed.
5. Sanity check passed: 4-county institution count = 113, matching the 2026-06-09 census exactly.
6. Uncertainty labels: none material. The SOD index is FDIC's official 2025 release (created 2026-01-26). Branch counts include all SOD branch records with `STALPBR:CA` and the county name in `CNTYNAMB`; SOD includes some non-retail/administrative offices by FDIC convention, same convention as the v5 census.

## Exact API URLs used (retrieved 2026-06-10)

County pulls (replace county name; these are the literal URLs called):
- `https://banks.data.fdic.gov/api/sod?filters=YEAR:2025%20AND%20STALPBR:CA%20AND%20CNTYNAMB:%22Los%20Angeles%22&fields=CERT,NAMEFULL,CITY,STALP,NAMEBR,CITYBR,CNTYNAMB,STALPBR,DEPSUMBR,ADDRESBR,ZIPBR&limit=10000&format=json`
- `https://banks.data.fdic.gov/api/sod?filters=YEAR:2025%20AND%20STALPBR:CA%20AND%20CNTYNAMB:%22San%20Bernardino%22&fields=CERT,NAMEFULL,CITY,STALP,NAMEBR,CITYBR,CNTYNAMB,STALPBR,DEPSUMBR,ADDRESBR,ZIPBR&limit=10000&format=json`
- `https://banks.data.fdic.gov/api/sod?filters=YEAR:2025%20AND%20STALPBR:CA%20AND%20CNTYNAMB:%22Riverside%22&fields=CERT,NAMEFULL,CITY,STALP,NAMEBR,CITYBR,CNTYNAMB,STALPBR,DEPSUMBR,ADDRESBR,ZIPBR&limit=10000&format=json`
- `https://banks.data.fdic.gov/api/sod?filters=YEAR:2025%20AND%20STALPBR:CA%20AND%20CNTYNAMB:%22Orange%22&fields=CERT,NAMEFULL,CITY,STALP,NAMEBR,CITYBR,CNTYNAMB,STALPBR,DEPSUMBR,ADDRESBR,ZIPBR&limit=10000&format=json`
- `https://banks.data.fdic.gov/api/sod?filters=YEAR:2025%20AND%20STALPBR:CA%20AND%20CNTYNAMB:%22Ventura%22&fields=CERT,NAMEFULL,CITY,STALP,NAMEBR,CITYBR,CNTYNAMB,STALPBR,DEPSUMBR,ADDRESBR,ZIPBR&limit=10000&format=json`
- `https://banks.data.fdic.gov/api/sod?filters=YEAR:2025%20AND%20STALPBR:CA%20AND%20CNTYNAMB:%22San%20Diego%22&fields=CERT,NAMEFULL,CITY,STALP,NAMEBR,CITYBR,CNTYNAMB,STALPBR,DEPSUMBR,ADDRESBR,ZIPBR&limit=10000&format=json`

Monet Bank verification:
- `https://banks.data.fdic.gov/api/sod?filters=YEAR:2025%20AND%20CERT:32574%20AND%20STALPBR:CA&fields=NAMEBR,CITYBR,CNTYNAMB,DEPSUMBR,ADDRESBR,ZIPBR&limit=10&format=json`
- `https://banks.data.fdic.gov/api/institutions?filters=CERT:32574&fields=NAME,CITY,STALP,ESTYMD,ACTIVE,ASSET&format=json`
- `https://banks.data.fdic.gov/api/history?filters=CERT:32574&fields=INSTNAME,EFFDATE,CHANGECODE_DESC&limit=30&format=json`
