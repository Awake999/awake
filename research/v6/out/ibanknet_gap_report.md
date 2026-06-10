# ibanknet.com CA Institution Gap Report

Retrieval date: **2026-06-10**. Reporting period shown by ibanknet: **quarter ended 2026-03-31** (banks/CUs/thrifts) and **2025 Summary of Deposits** (branch data). Comparison baseline: `/home/user/awake/research/v6/v5_all_institution_names.txt` (388 names).

## Summary

- ibanknet was UP and fully scrapable with plain curl + browser User-Agent. Data rows are present in raw HTML (server-rendered ASP.NET) - **no JS rendering needed, nothing blocked** for the list pages we used.
- Total CA-relevant institutions captured: **451**
  - CA-headquartered FFIEC/NCUA filers (`type=stateallfi&state=06`): 364 (113 banks, 242 credit unions, 9 federal savings banks)
  - Out-of-state banks with CA branch deposits (FDIC SOD via ibanknet, not CA-HQ): 58
  - Foreign Banking Organization offices in CA (FFIEC 002 filers): 29
  - Plus type flags merged in: 3 Industrial Loan Companies, 3 Non-Depository Trust Banks (CA)
- Match results: **IN_V5: 292**, **POSSIBLE_MATCH: 1**, **NEW_GAP: 158**

NEW_GAP by category: Credit Union: 112; Foreign Banking Organization (USB): 19; Out-of-state bank with CA branches (SOD): 12; Foreign Banking Organization (UFB): 8; Non-Depository Trust Bank: 3; Foreign Banking Organization (USA): 2; Bank: 1; Savings Institution (Federal Savings Bank): 1

## NEW_GAP institutions (sorted by assets desc; CA-branch deposits used for SOD rows)

### CA-headquartered depositories (banks / credit unions / savings) - 117 gaps

| # | Name | Type | City | Assets ($K) | Deposits ($K) | Note |
|---|------|------|------|-------------|---------------|------|
| 1 | EDUCATIONAL EMPLOYEES CREDIT UNION | Credit Union | Fresno | 5,376,699 | 4,616,425 |  |
| 2 | STANFORD FEDERAL CREDIT UNION | Credit Union | Palo Alto | 4,800,514 | 3,709,005 |  |
| 3 | BLACKROCK INSTITUTIONAL TRUST COMPANY, NATIONAL ASSOCIATION | Non-Depository Trust Bank | San Francisco | 4,520,258 | 0 | Non-depository trust bank per ibanknet |
| 4 | VALLEY STRONG CREDIT UNION | Credit Union | Bakersfield | 4,074,429 | 3,642,703 |  |
| 5 | COAST CENTRAL CREDIT UNION | Credit Union | Eureka | 2,322,103 | 2,060,772 | Fuzzy hit on v5 "E-CENTRAL" rejected - different institution |
| 6 | MERIWEST CREDIT UNION | Credit Union | San Jose | 2,163,597 | 1,753,530 |  |
| 7 | MONTERRA CREDIT UNION | Credit Union | Redwood City | 1,920,135 | 1,654,172 |  |
| 8 | BAY FEDERAL CREDIT UNION | Credit Union | Capitola | 1,892,475 | 1,693,650 |  |
| 9 | COASTHILLS FEDERAL CREDIT UNION | Credit Union | Santa Maria | 1,765,233 | 1,489,558 |  |
| 10 | KEYPOINT CREDIT UNION | Credit Union | San Jose | 1,701,238 | 1,403,675 |  |
| 11 | SAN FRANCISCO FIRE CREDIT UNION | Credit Union | San Francisco | 1,604,300 | 1,454,032 |  |
| 12 | SAN FRANCISCO FEDERAL CREDIT UNION | Credit Union | San Francisco | 1,582,268 | 1,194,502 | Not the same as v5 "Bank of San Francisco" - different institution |
| 13 | SIERRA CENTRAL CREDIT UNION | Credit Union | Yuba City | 1,496,982 | 1,339,334 |  |
| 14 | NOBLE FEDERAL CREDIT UNION | Credit Union | Fresno | 1,494,031 | 1,139,517 |  |
| 15 | VENTURA COUNTY CREDIT UNION | Credit Union | Ventura | 1,467,597 | 1,303,082 |  |
| 16 | PACIFIC SERVICE CREDIT UNION | Credit Union | Concord | 1,345,715 | 1,121,940 |  |
| 17 | 1ST UNITED CREDIT UNION | Credit Union | Pleasanton | 1,253,077 | 1,099,282 |  |
| 18 | SESLOC CREDIT UNION | Credit Union | San Luis Obispo | 1,252,419 | 1,124,366 |  |
| 19 | UNITED SECURITY BANK | Bank | Fresno | 1,216,537 | 1,059,462 |  |
| 20 | SAFE 1 CREDIT UNION | Credit Union | Bakersfield | 1,120,422 | 958,618 |  |
| 21 | VALLEY FIRST FEDERAL CREDIT UNION | Credit Union | Modesto | 1,108,042 | 926,404 |  |
| 22 | THE POLICE CREDIT UNION | Credit Union | San Bruno | 1,054,903 | 936,056 |  |
| 23 | MIRASTAR FEDERAL CREDIT UNION | Credit Union | San Jose | 1,036,195 | 914,626 |  |
| 24 | ALTAONE FEDERAL CREDIT UNION | Credit Union | Ridgecrest | 974,029 | 880,101 |  |
| 25 | COMMUNITY FIRST CREDIT UNION | Credit Union | Santa Rosa | 922,089 | 817,032 |  |
| 26 | MERCED SCHOOL EMPLOYEES FEDERAL CREDIT UNION | Credit Union | Merced | 897,525 | 795,116 |  |
| 27 | OCEANAIR FEDERAL CREDIT UNION | Credit Union | Oxnard | 870,760 | 683,443 |  |
| 28 | SACRAMENTO CREDIT UNION | Credit Union | Sacramento | 851,939 | 719,015 |  |
| 29 | 1ST NORTHERN CALIFORNIA CREDIT UNION | Credit Union | Martinez | 825,393 | 718,336 |  |
| 30 | UNCLE CREDIT UNION | Credit Union | Livermore | 738,043 | 663,677 |  |
| 31 | MYPOINT CREDIT UNION | Credit Union | San Diego | 701,059 | 585,195 |  |
| 32 | PREMIER ONE CREDIT UNION | Credit Union | San Jose | 656,413 | 558,082 |  |
| 33 | COMMONWEALTH CENTRAL CREDIT UNION | Credit Union | San Jose | 626,858 | 533,064 |  |
| 34 | EXCITE CREDIT UNION | Credit Union | San Jose | 615,237 | 576,946 |  |
| 35 | CABRILLO CREDIT UNION | Credit Union | San Diego | 571,809 | 511,775 |  |
| 36 | FIRST U.S. COMMUNITY CREDIT UNION | Credit Union | Sacramento | 554,171 | 490,051 |  |
| 37 | DEUTSCHE BANK NATIONAL TRUST COMPANY | Non-Depository Trust Bank | Los Angeles | 553,623 | 0 | Non-depository trust bank per ibanknet |
| 38 | WHEELHOUSE CREDIT UNION | Credit Union | San Diego | 456,771 | 400,445 |  |
| 39 | MOCSE FEDERAL CREDIT UNION | Credit Union | Modesto | 430,486 | 396,495 |  |
| 40 | YOLO FEDERAL CREDIT UNION | Credit Union | Woodland | 410,982 | 344,210 |  |
| 41 | SEA WEST COAST GUARD FEDERAL CREDIT UNION | Credit Union | Oakland | 381,797 | 304,015 |  |
| 42 | MONTEREY CREDIT UNION | Credit Union | Monterey | 356,957 | 316,246 |  |
| 43 | STRATA FEDERAL CREDIT UNION | Credit Union | Bakersfield | 345,954 | 293,851 |  |
| 44 | TUCOEMAS FEDERAL CREDIT UNION | Credit Union | Visalia | 336,861 | 305,226 |  |
| 45 | FAMILIES AND SCHOOLS TOGETHER FEDERAL CREDIT UNION | Credit Union | Hanford | 328,114 | 261,901 |  |
| 46 | SANTA BARBARA TEACHERS FEDERAL CREDIT UNION | Credit Union | Santa Barbara | 309,564 | 266,368 |  |
| 47 | HERITAGE COMMUNITY CREDIT UNION | Credit Union | Rancho Cordova | 282,600 | 252,119 |  |
| 48 | CENTRAL STATE CREDIT UNION | Credit Union | Stockton | 255,165 | 208,593 |  |
| 49 | SRI FEDERAL CREDIT UNION | Credit Union | Menlo Park | 242,087 | 201,855 |  |
| 50 | CORAZO CREDIT UNION | Credit Union | El Centro | 241,842 | 206,427 |  |
| 51 | F3 CREDIT UNION | Credit Union | San Jose | 239,383 | 199,702 |  |
| 52 | FIRST FEDERAL SAVINGS AND LOAN ASSOCIATION OF SAN RAFAEL | Savings Institution (Federal Savings Bank) | San Rafael | 219,992 | 176,372 |  |
| 53 | MERCO CREDIT UNION | Credit Union | Merced | 207,012 | 179,941 |  |
| 54 | COMPASS COMMUNITY CREDIT UNION | Credit Union | Eureka | 180,859 | 159,219 |  |
| 55 | SANTA CRUZ COMMUNITY CREDIT UNION | Credit Union | Santa Cruz | 174,346 | 150,260 |  |
| 56 | SAN JOAQUIN POWER EMPLOYEES CREDIT UNION | Credit Union | Fresno | 173,280 | 145,080 |  |
| 57 | MISSION CITY FEDERAL CREDIT UNION | Credit Union | Santa Clara | 164,299 | 141,029 |  |
| 58 | KINGS FEDERAL CREDIT UNION | Credit Union | Hanford | 162,876 | 136,536 |  |
| 59 | TULARE COUNTY FEDERAL CREDIT UNION | Credit Union | Tulare | 156,588 | 142,040 |  |
| 60 | SAN DIEGO FIREFIGHTERS FEDERAL CREDIT UNION | Credit Union | San Diego | 151,718 | 140,134 |  |
| 61 | EAST COUNTY SCHOOLS FEDERAL CREDIT UNION | Credit Union | El Cajon | 147,542 | 132,714 |  |
| 62 | SISKIYOU CREDIT UNION | Credit Union | Yreka | 144,716 | 134,011 |  |
| 63 | UNITED LOCAL CREDIT UNION | Credit Union | Fresno | 121,096 | 96,434 |  |
| 64 | SMW 104 FEDERAL CREDIT UNION | Credit Union | Livermore | 116,776 | 101,569 |  |
| 65 | FIRST CALIFORNIA FEDERAL CREDIT UNION | Credit Union | Fresno | 109,872 | 98,476 |  |
| 66 | LASSEN COUNTY FEDERAL CREDIT UNION | Credit Union | Susanville | 109,310 | 94,778 |  |
| 67 | KAIPERM FEDERAL CREDIT UNION | Credit Union | Walnut Creek | 108,993 | 99,122 |  |
| 68 | MARIN COUNTY FEDERAL CREDIT UNION | Credit Union | San Rafael | 102,202 | 90,246 |  |
| 69 | UPWARD CREDIT UNION | Credit Union | Burlingame | 93,701 | 80,547 |  |
| 70 | MCKESSON & HEALTHCARE PROVIDERS FEDERAL CREDIT UNION | Credit Union | Martinez | 93,290 | 80,193 |  |
| 71 | VISION ONE CREDIT UNION | Credit Union | Sacramento | 91,602 | 76,400 |  |
| 72 | COUNTY SCHOOLS FEDERAL CREDIT UNION | Credit Union | Ventura | 91,466 | 83,564 |  |
| 73 | DESERT VALLEYS FEDERAL CREDIT UNION | Credit Union | Ridgecrest | 89,436 | 80,183 |  |
| 74 | VALLEY OAK CREDIT UNION | Credit Union | Three Rivers | 82,304 | 76,337 | Not the same as v5 "Oak Valley Community Bank" |
| 75 | SONOMA FEDERAL CREDIT UNION | Credit Union | Santa Rosa | 80,093 | 69,518 |  |
| 76 | CALIFORNIA COMMUNITY CREDIT UNION | Credit Union | Sacramento | 79,918 | 69,035 |  |
| 77 | BAY CITIES CREDIT UNION | Credit Union | Hayward | 78,848 | 68,941 |  |
| 78 | MODESTO'S FIRST FEDERAL CREDIT UNION | Credit Union | Modesto | 72,168 | 65,540 |  |
| 79 | SHELL WESTERN STATES FEDERAL CREDIT UNION | Credit Union | Martinez | 69,331 | 61,674 |  |
| 80 | ESCONDIDO FEDERAL CREDIT UNION | Credit Union | Escondido | 66,214 | 57,125 |  |
| 81 | DELTA SCHOOLS FEDERAL CREDIT UNION | Credit Union | Antioch | 65,943 | 58,718 |  |
| 82 | ROLLING F CREDIT UNION | Credit Union | Turlock | 65,939 | 58,241 |  |
| 83 | SANTA BARBARA COUNTY FEDERAL CREDIT UNION | Credit Union | Santa Barbara | 64,748 | 56,299 |  |
| 84 | MOKELUMNE FEDERAL CREDIT UNION | Credit Union | Lodi | 58,081 | 48,571 |  |
| 85 | FRESNO POLICE DEPARTMENT CREDIT UNION | Credit Union | Fresno | 50,082 | 38,001 |  |
| 86 | CENTRAL VALLEY FIREFIGHTERS CREDIT UNION | Credit Union | Fresno | 49,933 | 42,924 |  |
| 87 | SILVERADO CREDIT UNION | Credit Union | Angwin | 48,598 | 42,589 |  |
| 88 | DOW GREAT WESTERN CREDIT UNION | Credit Union | Antioch | 48,188 | 45,164 |  |
| 89 | ORGANIZED LABOR CREDIT UNION | Credit Union | Modesto | 40,538 | 36,457 |  |
| 90 | DIABLO VALLEY FEDERAL CREDIT UNION | Credit Union | Concord | 40,080 | 35,751 |  |
| 91 | GOLDEN VALLEY FEDERAL CREDIT UNION | Credit Union | Manteca | 39,417 | 34,733 | Not the same as v5 "Golden Valley Bank" |
| 92 | BEFIT FINANCIAL FEDERAL CREDIT UNION | Credit Union | Vacaville | 39,342 | 35,108 | Fuzzy hit on v5 "THE FIRST FINANCIAL" rejected |
| 93 | CORRECTIONS FEDERAL CREDIT UNION | Credit Union | Soledad | 36,391 | 33,269 |  |
| 94 | ANTIOCH COMMUNITY FEDERAL CREDIT UNION | Credit Union | Antioch | 34,322 | 29,187 |  |
| 95 | UTILITY DISTRICT CREDIT UNION | Credit Union | Oakland | 34,118 | 30,902 |  |
| 96 | GREATER VALLEY CREDIT UNION | Credit Union | Fresno | 33,435 | 28,339 |  |
| 97 | SAN MATEO CITY EMPLOYEES FEDERAL CREDIT UNION | Credit Union | San Mateo | 33,330 | 27,458 |  |
| 98 | SUN PACIFIC FEDERAL CREDIT UNION | Credit Union | Richmond | 29,840 | 24,506 |  |
| 99 | SLO CREDIT UNION | Credit Union | San Luis Obispo | 29,740 | 25,918 |  |
| 100 | BAKERSFIELD CITY EMPLOYEES FEDERAL CREDIT UNION | Credit Union | Bakersfield | 29,354 | 25,546 |  |
| 101 | FRESNO GRANGERS FEDERAL CREDIT UNION | Credit Union | Fresno | 26,954 | 20,723 |  |
| 102 | NORTHERN REDWOOD FEDERAL CREDIT UNION | Credit Union | Arcata | 24,492 | 22,577 |  |
| 103 | EMPLOYEES CHOICE FEDERAL CREDIT UNION | Credit Union | El Cajon | 22,980 | 20,191 |  |
| 104 | NORTHEAST COMMUNITY FEDERAL CREDIT UNION | Credit Union | San Francisco | 15,791 | 10,355 | Not the same as v5 "NORTH IOWA COMMUNITY" |
| 105 | BESSEMER TRUST COMPANY OF CALIFORNIA, NATIONAL ASSOCIATION | Non-Depository Trust Bank | San Francisco | 14,961 | 0 | Non-depository trust bank per ibanknet |
| 106 | INLAND FEDERAL CREDIT UNION | Credit Union | La Mesa | 14,796 | 13,587 |  |
| 107 | UNITED ASSOCIATION CREDIT UNION | Credit Union | Concord | 14,328 | 11,898 |  |
| 108 | ATCHISON VILLAGE CREDIT UNION | Credit Union | Richmond | 13,271 | 11,658 |  |
| 109 | ESPEECO FEDERAL CREDIT UNION | Credit Union | Bakersfield | 12,367 | 11,580 |  |
| 110 | SAN FRANCISCO LEE FEDERAL CREDIT UNION | Credit Union | San Francisco | 10,746 | 5,042 |  |
| 111 | DENOCOS FEDERAL CREDIT UNION | Credit Union | Crescent City | 6,295 | 5,322 |  |
| 112 | SANTA MARIA ASSOCIATED EMPLOYEES FEDERAL CREDIT UNION | Credit Union | Santa Maria | 4,918 | 4,464 |  |
| 113 | CHULA VISTA CITY EMPLOYEES FEDERAL CREDIT UNION | Credit Union | Chula Vista | 3,161 | 2,755 |  |
| 114 | MOJAVE PLANT EMPLOYEES FEDERAL CREDIT UNION | Credit Union | Mojave | 1,014 | 817 |  |
| 115 | DELANCEY STREET FEDERAL CREDIT UNION | Credit Union | San Francisco | 498 | 353 |  |
| 116 | JONES METHODIST CHURCH CREDIT UNION | Credit Union | Burlingame | 257 | 209 |  |
| 117 | HAVEN FEDERAL CREDIT UNION | Credit Union | San Francisco | 0 | 0 |  |

### Foreign Banking Organization offices in CA (invisible to FDIC-only methods) - 29 gaps

| # | Name | Type | City | Assets ($K) | Deposits ($K) | Note |
|---|------|------|------|-------------|---------------|------|
| 1 | WOORI BK LA BR | Foreign Banking Organization (USB) | Los Angeles | 7,461,409 | - | FBO branch of Woori Bank (Korea); v5 has US subsidiary Woori America Bank - separate charter |
| 2 | MUFG BK LOS ANGELES BR | Foreign Banking Organization (UFB) | Los Angeles | 3,913,711 | - | FBO office in CA (branch/agency/rep office of foreign bank) |
| 3 | BANK OF CHINA LA BR | Foreign Banking Organization (UFB) | Los Angeles | 3,138,633 | - | FBO branch of Bank of China; distinct from v5 ICBC USA N.A. |
| 4 | ADYEN NV SAN FRANCISCO BR | Foreign Banking Organization (UFB) | San Francisco | 2,376,702 | - | FBO office in CA (branch/agency/rep office of foreign bank) |
| 5 | E SUN CMRL BK LOS ANGELES BR | Foreign Banking Organization (USB) | City Of Industry | 2,293,367 | - | FBO office in CA (branch/agency/rep office of foreign bank) |
| 6 | BANK OF E ASIA LA BR | Foreign Banking Organization (UFB) | Alhambra | 1,547,894 | - | FBO office in CA (branch/agency/rep office of foreign bank) |
| 7 | LAND BK OF TAIWAN LA BR | Foreign Banking Organization (USB) | Los Angeles | 1,426,734 | - | FBO office in CA (branch/agency/rep office of foreign bank) |
| 8 | FIRST CMRL BK LA BR | Foreign Banking Organization (USB) | Los Angeles | 1,344,900 | - | FBO branch of First Commercial Bank (Taiwan); v5 has US subsidiary First Commercial Bank (USA) - separate charter |
| 9 | CHANG HWA CMRL BK LA BR | Foreign Banking Organization (USB) | Los Angeles | 1,340,859 | - | FBO office in CA (branch/agency/rep office of foreign bank) |
| 10 | STATE BK OF INDIA LA BR | Foreign Banking Organization (USB) | Los Angeles | 1,267,285 | - | FBO branch of State Bank of India; v5 has US subsidiary State Bank of India (California) - separate charter |
| 11 | BANK SINOPAC LA BR | Foreign Banking Organization (USB) | Pasadena | 1,141,570 | - | FBO office in CA (branch/agency/rep office of foreign bank) |
| 12 | HUA NAN CMRL BK LA BR | Foreign Banking Organization (USB) | Los Angeles | 1,088,880 | - | FBO office in CA (branch/agency/rep office of foreign bank) |
| 13 | TAIWAN CO-OP BK LA BR | Foreign Banking Organization (USB) | Los Angeles | 961,279 | - | FBO office in CA (branch/agency/rep office of foreign bank) |
| 14 | BANK OF TAIWAN LA BR | Foreign Banking Organization (USB) | Los Angeles | 916,923 | - | FBO office in CA (branch/agency/rep office of foreign bank) |
| 15 | MEGA INTL CMRL BK LA BR | Foreign Banking Organization (USB) | Los Angeles | 913,677 | - | FBO branch of Mega International Commercial Bank (Taiwan); distinct from v5 "Mega Bank" (San Gabriel CA) |
| 16 | MEGA INTL CMRL SILICON VALL BR | Foreign Banking Organization (USB) | San Jose | 835,263 | - | FBO office in CA (branch/agency/rep office of foreign bank) |
| 17 | TAIWAN BUS BK LA BR | Foreign Banking Organization (USB) | Los Angeles | 749,822 | - | FBO office in CA (branch/agency/rep office of foreign bank) |
| 18 | SHANGHAI CMRL BK SF BR | Foreign Banking Organization (USB) | San Francisco | 614,107 | - | FBO office in CA (branch/agency/rep office of foreign bank) |
| 19 | CHINA CITIC BK INTL LA BR | Foreign Banking Organization (UFB) | Alhambra | 542,745 | - | FBO office in CA (branch/agency/rep office of foreign bank) |
| 20 | SHANGHAI CMRL BK LA BR | Foreign Banking Organization (USB) | Alhambra | 338,338 | - | FBO office in CA (branch/agency/rep office of foreign bank) |
| 21 | BANK OF CMNTNS SF BR | Foreign Banking Organization (UFB) | San Francisco | 220,896 | - | FBO office in CA (branch/agency/rep office of foreign bank) |
| 22 | CMB WING LUNG BK LA BR | Foreign Banking Organization (UFB) | Irvine | 146,587 | - | FBO office in CA (branch/agency/rep office of foreign bank) |
| 23 | BANK OF INDIA SF AGY | Foreign Banking Organization (USA) | San Francisco | 138,714 | - | FBO agency of Bank of India; distinct from v5 "State Bank of India (California)" |
| 24 | CMB WING LUNG BK SF BR | Foreign Banking Organization (UFB) | San Francisco | 131,405 | - | FBO office in CA (branch/agency/rep office of foreign bank) |
| 25 | PHILIPPINE NB LA BR | Foreign Banking Organization (USB) | Los Angeles | 49,496 | - | FBO office in CA (branch/agency/rep office of foreign bank) |
| 26 | SUMITOMO MITSUI BKG CORP LA BR | Foreign Banking Organization (USB) | Los Angeles | 3,063 | - | FBO office in CA (branch/agency/rep office of foreign bank) |
| 27 | MIZUHO BK LOS ANGELES BR | Foreign Banking Organization (USB) | Los Angeles | 2,067 | - | FBO office in CA (branch/agency/rep office of foreign bank) |
| 28 | OVERSEA-CHINESE BKG LA AGY | Foreign Banking Organization (USA) | Los Angeles | 1,134 | - | FBO office in CA (branch/agency/rep office of foreign bank) |
| 29 | SUMITOMO MITSUI BKG CORP SF BR | Foreign Banking Organization (USB) | San Francisco | 0 | - | FBO office in CA (branch/agency/rep office of foreign bank) |

### Out-of-state banks with CA branch presence (FDIC SOD) - 12 gaps

| # | Name | Type | City | Assets ($K) | Deposits ($K) | Note |
|---|------|------|------|-------------|---------------|------|
| 1 | Citizens Bank, National Association | Out-of-state bank with CA branches (SOD) | - | - | 3,715,621 | Citizens Bank N.A. (Citizens Financial Group, RI) - distinct from v5 "Citizens Business Bank" |
| 2 | UMB Bank, National Association | Out-of-state bank with CA branches (SOD) | - | - | 1,202,740 | 7 CA offices; deposits shown are CA branch deposits (FDIC SOD via ibanknet); HQ outside CA |
| 3 | Cornerstone Community Bank | Out-of-state bank with CA branches (SOD) | - | - | 580,953 | 4 CA offices; deposits shown are CA branch deposits (FDIC SOD via ibanknet); HQ outside CA |
| 4 | Amalgamated Bank | Out-of-state bank with CA branches (SOD) | - | - | 397,338 | 1 CA offices; deposits shown are CA branch deposits (FDIC SOD via ibanknet); HQ outside CA |
| 5 | Safra National Bank of New York | Out-of-state bank with CA branches (SOD) | - | - | 173,127 | 1 CA offices; deposits shown are CA branch deposits (FDIC SOD via ibanknet); HQ outside CA |
| 6 | SoFi Bank, National Association | Out-of-state bank with CA branches (SOD) | - | - | 167,233 | 3 CA offices; deposits shown are CA branch deposits (FDIC SOD via ibanknet); HQ outside CA |
| 7 | Beal Bank USA | Out-of-state bank with CA branches (SOD) | - | - | 163,167 | 1 CA offices; deposits shown are CA branch deposits (FDIC SOD via ibanknet); HQ outside CA |
| 8 | Monet Bank | Out-of-state bank with CA branches (SOD) | - | - | 60,278 | 2 CA offices; deposits shown are CA branch deposits (FDIC SOD via ibanknet); HQ outside CA |
| 9 | Bank of Guam | Out-of-state bank with CA branches (SOD) | - | - | 53,145 | 1 CA offices; deposits shown are CA branch deposits (FDIC SOD via ibanknet); HQ outside CA |
| 10 | Citizens National Bank of Texas | Out-of-state bank with CA branches (SOD) | - | - | 33,108 | 1 CA offices; deposits shown are CA branch deposits (FDIC SOD via ibanknet); HQ outside CA |
| 11 | CIBC Bank USA | Out-of-state bank with CA branches (SOD) | - | - | 16,966 | 1 CA offices; deposits shown are CA branch deposits (FDIC SOD via ibanknet); HQ outside CA |
| 12 | LendingClub Bank, National Association | Out-of-state bank with CA branches (SOD) | - | - | 0 | 1 CA offices; deposits shown are CA branch deposits (FDIC SOD via ibanknet); HQ outside CA |

## What ibanknet adds beyond our FDIC-based method

1. **Foreign Banking Organization (FBO) branches/agencies in CA** - 29 offices filing FFIEC 002 (e.g., MUFG Bank LA Branch $3.9B, Bank of China LA Branch $3.1B, Adyen NV SF Branch $2.4B, plus the Taiwanese commercial-bank LA branches). These are NOT FDIC-insured entities and never appear in FDIC institution lists; several do middle-market/trade-finance commercial lending in CA. All 29 FBO-typed rows are NEW_GAP vs v5 (where a parent group has a v5-covered US subsidiary, e.g. Woori, First Commercial, SBI, the FBO branch is a separate charter and is flagged as such; the one insured FBO branch already in v5, Mizrahi Tefahot Bank Ltd., appears in the SOD section as IN_V5).
2. **Non-depository trust banks** - call-report filers with no deposits (e.g., BlackRock Institutional Trust Company N.A., $4.5B assets, San Francisco). Not relevant for business credit but confirms coverage boundary.
3. **Industrial Loan Company flagging** - ibanknet tags CA ILCs explicitly; the CA ILCs it lists are already in the stateallfi set.
4. **Out-of-state banks ranked by CA branch deposits** (2025 FDIC SOD rollup) - convenient cross-check of who actually operates in CA. 58 such banks are not CA-HQ; 12 of them are NEW_GAP vs v5 (the rest were already in v5). Notable gaps include Citizens Bank N.A. ($3.7B CA deposits) and UMB Bank N.A. ($1.2B CA deposits) - see table.
5. **Holding-company relationships** - each institution page (`getbank.aspx?ibnid=...`) shows the holding company; the FR Y-9 list exists but is **national top-100 only and cannot be filtered by state** (the `state` parameter is ignored). We did not crawl 364 individual institution pages for HC links in this pass.

## Exact URLs fetched + HTTP results

| URL | HTTP | Outcome |
|-----|------|---------|
| https://www.ibanknet.com/scripts/callreports/getbanklist.aspx?type=031,032,033,034&state=CA | 200 | **ASP.NET error page**: 'The file /scripts/callreports/getbanklist.aspx does not exist' - old endpoint removed; site migrated to fiList.aspx |
| https://www.ibanknet.com/ | 200 | Homepage; discovered fiList.aspx type codes |
| https://www.ibanknet.com/robots.txt | 200 | Disallows viewreport.aspx, reportlist.aspx, printreport.aspx, getsec.aspx, secreport.aspx (we did not fetch those) |
| https://www.ibanknet.com/bankmap/index.shtml | 200 | State map; led to state-FIPS list URLs |
| https://www.ibanknet.com/scripts/bankmap/getstatecounty.aspx?state=CA | 200 | CA county page; exposed state list types |
| https://www.ibanknet.com/scripts/callreports/fiList.aspx?type=stateallfi&state=06 | 200 | **364 CA institutions w/ name, regulator, city, deposits, assets** (primary source) |
| https://www.ibanknet.com/scripts/callreports/fiList.aspx?type=statebank&state=06 | 200 | 113 CA banks |
| https://www.ibanknet.com/scripts/callreports/fiList.aspx?type=statecreditunion&state=06 | 200 | 242 CA credit unions |
| https://www.ibanknet.com/scripts/callreports/fiList.aspx?type=statethrift&state=06 | 200 | 9 CA federal savings banks |
| https://www.ibanknet.com/scripts/callreports/fiList.aspx?type=sodstatebanks&state=06 | 200 | 177 banks with CA branch deposits (2025 SOD) |
| https://www.ibanknet.com/scripts/callreports/fiList.aspx?type=ilc | 200 | 23 ILCs nationally (state column; 3 CA) |
| https://www.ibanknet.com/scripts/callreports/fiList.aspx?type=ndtrust | 200 | 58 non-depository trust banks (3 CA) |
| https://www.ibanknet.com/scripts/callreports/fiList.aspx?type=fbo | 200 | 170 FBO offices nationally (29 CA) |
| https://www.ibanknet.com/scripts/callreports/fiList.aspx?type=031,032,033,034&state=CA | 200 | 'List Type Error' page - combined type codes not supported on new endpoint |
| https://www.ibanknet.com/scripts/callreports/fiList.aspx?type=031 | 200 | National top-100 banks only (no state filter on this type) |
| https://www.ibanknet.com/scripts/callreports/fiList.aspx?type=fry9&state=06 | 200 | FR Y-9 holding companies - **state param ignored**, national top-100 returned; no state-level HC list available |
| https://www.ibanknet.com/scripts/callreports/fiList.aspx?type=statebhc&state=06 / type=stateholdingcompany&state=06 | 200 | 'List Type Error' - no such list types |

## Honest limitations

- **Holding companies**: no state-filtered holding-company list exists on ibanknet; only a national top-100 FR Y-9 list. Holding-company relationships are on per-institution pages, which we did not crawl in bulk.
- The SOD out-of-state rows carry CA **branch deposits only** (no total assets, no HQ city) because that is all the sodstatebanks list shows.
- FBO rows show assets but no deposits (FFIEC 002 lists on ibanknet do not display deposits).
- Nothing we needed was bot-blocked or JS-empty; the only inaccessible areas were the robots.txt-disallowed report viewers, which we deliberately did not fetch.
- Matching to v5 was name-based (normalized + token rules + 13 manually adjudicated cases). POSSIBLE_MATCH (1 row: The Bank of New York Mellon) needs human confirmation.
