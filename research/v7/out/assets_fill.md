# ASSETS-FILL — Total Assets & Total Deposits backfill

Date: 2026-06-11. Output: `research/v7/out/assets_fill.csv` (261 rows).

## Gap counts

| Sheet | Gap rows found | Filled with figures | Filled with explicit N/A | Unfillable |
|---|---|---|---|---|
| funding_table (`research/v6/deliverables/ca_business_credit_funding_v6_funding_table.csv`, 236 data rows) | 174 | 174 | 0 | 0 |
| ibanknet (`research/v6/out/ibanknet_ca_institutions.csv`, 451 data rows) | 87 | 58 | 29 (FBO offices, deposits column only) | 0 |
| **Total** | **261** | **232** | **29** | **0** |

A gap row = Assets or Deposits blank / '—' / 'N/M' / missing. 100% of gap rows appear in assets_fill.csv.

## Sources & methods

- **FDIC banks** (174 rows): `https://api.fdic.gov/banks/institutions` (note: the documented `api.fdic.gov/api/...` path now 404s; the working path is `/banks/institutions`). ASSET/DEP in $thousands; as-of `REPDTE` = 2026-03-31 for active charters. Matched by CERT where curated, otherwise unique-legal-name match with city confirmation; any legal-HQ/corporate-HQ divergence is flagged in Match_method (e.g. U.S. Bank → Cincinnati OH, PNC → Wilmington DE).
- **Credit unions** (58 rows): NCUA 5300 cycle 2026-03 from `research/v6/out/cr202603/` — FS220 `Acct_010` = TOTAL ASSETS, `Acct_018` = Total Amount of Shares and Deposits (confirmed in AcctDesc.txt), joined to FOICU for name/city. Matched by charter for ambiguous names (incl. Langley charter 1261; Self-Help **Federal** charter 24802, distinct from state-chartered Self-Help CU also in Durham NC), else name+city.
- **Fintech/card programs** (4 rows): labeled `issuer: <bank> $X` — Ramp → Celtic Bank (CERT 57056; Sutton Bank also issues), Mercury IO → Patriot Bank, N.A. (CERT 33928), BILL Spend & Expense → Cross River Bank (CERT 58410; WEX Bank also issues), Sam's Club → Synchrony Bank (CERT 27314). American Express filled with issuer American Express National Bank (CERT 27471).
- **FBO offices** (29 rows): office-level FFIEC 002 assets were already in the sheet (restated in fill). Total deposits are **not** on the reachable ibanknet fast-facts page (assets only) and the detailed RAL report redirects to a captcha — so Deposits = `N/A (FFIEC 002 office)` per fallback rule, with reason on every row.

## Notable resolutions (mergers/renames since the sheets were built)

- **Comerica Bank** (funding_table): Charter inactive 2026-02-01 (merged into Fifth Third Bank, N.A.); last reported figures
- **First Foundation Bank** (funding_table): Charter inactive 2026-04-01 (merger); last reported figures
- **Pacific Premier Bank** (funding_table): Charter inactive 2025-09-01 (merged into Columbia Bank / Columbia Banking System); last reported figures
- **HomeStreet Bank** (funding_table): HomeStreet Bank merged into Mechanics Bank (Walnut Creek, CA; CERT 1768) in 2025; figures are Mechanics Bank
- **Heritage Bank of Commerce** (funding_table): Charter inactive 2026-04-17 (merger); last reported figures
- **First IC Bank** (funding_table): Charter inactive 2025-12-01 (acquired); last reported figures
- **Pacific Enterprise Bank** (funding_table): Charter inactive 2022-02-02 (acquired); last reported figures at close
- **Community Valley Bank** (funding_table): Charter inactive 2026-03-31 (merger); last reported figures
- **Comerica Bank** (ibanknet): Charter inactive 2026-02-01 (merged into Fifth Third Bank, N.A.); last reported figures
- **Pacific Premier Bank, National Association** (ibanknet): Charter inactive 2025-09-01 (merged into Columbia Bank / Columbia Banking System); last reported figures
- **HomeStreet Bank** (ibanknet): HomeStreet Bank merged into Mechanics Bank (CERT 1768) in 2025; figures are Mechanics Bank
- **Cornerstone Community Bank** (ibanknet): Charter inactive 2025-07-01 (acquired by Plumas Bank); last reported figures
- **Community Valley Bank** (ibanknet): Charter inactive 2026-03-31 (merger); last reported figures
- **First IC Bank** (ibanknet): Charter inactive 2025-12-01 (acquired); last reported figures

## ibanknet SOD rows (58 bank rows)

These rows had CA-office SOD deposits but blank Assets. Filled with **consolidated** FDIC ASSET and DEP; every such row's Note flags that the sheet's existing Deposits value is CA-office SOD, not total. Mizrahi Tefahot Bank, Ltd. is an FDIC-insured branch (CERT 33661) and got full FDIC figures.

## Matching discipline

CERT/charter used wherever curated (48 rows); all name matches required unique legal-name hit plus city confirmation. Known name-twins explicitly disambiguated by CERT: First Bank (MO) 12229, Pinnacle Bank (Gilroy) 58297, Legacy Bank (Murrieta) 59204, Summit Bank (Oakland) 23864, Genesis Bank (Newport Beach) 59245, Neighborhood National Bank (El Cajon) 34548, First Commercial Bank (USA) (Alhambra) 34496, State Bank of India (California) 23998 (not the NY/Chicago branches).
