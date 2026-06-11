# Bank & Credit Union Census — One World Trade Center, Long Beach, CA 90831

**Anchor point:** 1 World Trade Center, Long Beach, CA 90831 — geocoded to **33.767378, -118.199441** (US Census geocoder, Public_AR_Current benchmark, 2026-06-11). All distances are straight-line (haversine) miles from this point.

## Method

1. **FDIC SOD 2025** (local `research/v6/out/sod_2025_Los_Angeles.json` + `sod_2025_Orange.json`): 308 bank branches in 29 candidate cities; street addresses geocoded via the free **US Census batch geocoder** (382/406 matched), remainder via Census oneline + **OSM Nominatim** fallback. 406/406 geocoded.
2. **NCUA 2026-Q1 branch file** (`cr202603/Credit Union Branch Information.txt`): 98 CU branches in the same cities, geocoded identically. CU financials from **FS220** (`ACCT_010` total assets, `ACCT_018` total shares & deposits, cycle 2026-03-31).
3. **Organic map view — OpenStreetMap Overpass API**: `amenity=bank` within 8,047 m (5 mi) of the point → 45 elements, 26 distinct names; matched to institutions, stale tags investigated.
4. **Web searches** (banks near One WTC Long Beach; downtown business banking; downtown CUs) for LPO/business-center finds.
5. Bank assets/deposits from **FDIC institutions API** (`api.fdic.gov/banks/institutions`, fields ASSET/DEP, pulled 2026-06-11). One row per institution; nearest branch wins.

## Within 5 miles: 32 institutions (17 banks, 15 credit unions; 73 branch locations)

| # | Institution | Type | Nearest branch | Mi | CERT/Charter | HQ | Assets | Deposits | Br<=5mi | v6 table | Found by |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Banc of California | Bank | 1 World Trade Ctr, Ste 125, Long Beach, CA 90831 | 0.0 | CERT 24045 | Los Angeles, CA | $34.64B | $27.44B | 2 | Yes — Banc of California | SOD |
| 2 | Citibank, National Association | Bank | 1 World Trade Ctr, Ste 100, Long Beach, CA 90831 | 0.0 | CERT 7213 | Sioux Falls, SD | $1.93T | $1.50T | 1 | Yes — Citi (Citibank) | SOD+web |
| 3 | City National Bank | Bank | 100 Oceangate, Long Beach, CA 90802 | 0.09 | CERT 17281 | Los Angeles, CA | $99.95B | $81.07B | 2 | Yes — City National Bank | SOD+OSM |
| 4 | Zions Bancorporation, N.A. | Bank | 444 W Ocean Blvd, Long Beach, CA 90802 | 0.12 | CERT 2270 | Salt Lake City, UT | $87.96B | $76.93B | 1 | Yes — California Bank & Trust | SOD+OSM+web |
| 5 | Wells Fargo Bank, National Association | Bank | 111 W Ocean Blvd, Long Beach, CA 90802 | 0.37 | CERT 3511 | Sioux Falls, SD | $1.85T | $1.52T | 7 | Yes — Wells Fargo | SOD+OSM+web |
| 6 | JPMorgan Chase Bank, National Association | Bank | 257 Pine Ave, Long Beach, CA 90802 | 0.44 | CERT 628 | Columbus, OH | $4.02T | $2.79T | 10 | Yes — Chase (JPMorgan Chase) | SOD+OSM |
| 7 | Farmers and Merchants Bank of Long Beach | Bank | 302 Pine Ave, Long Beach, CA 90802 | 0.47 | CERT 1225 | Long Beach, CA | $11.86B | $8.94B | 5 | Yes — Farmers & Merchants Bank of Long Beach | SOD+OSM |
| 8 | American Plus Bank, N.A. | Bank | 249 E Ocean Blvd, Long Beach, CA 90802 | 0.56 | CERT 58469 | Arcadia, CA | $890.7M | $716.6M | 1 | Yes — American Plus Bank, N.A. | SOD+OSM+web |
| 9 | Comerica Bank | Bank | 301 E Ocean Blvd, Ste 102, Long Beach, CA 90802 | 0.58 | CERT 983 | Dallas, TX | $80.05B | $66.28B | 2 | Yes — Comerica Bank | SOD+OSM |
| 10 | BMO Bank National Association | Bank | 496 Long Beach Blvd, Long Beach, CA 90802 | 0.68 | CERT 16571 | Chicago, IL | $251.96B | $193.96B | 1 | Yes — BMO Bank | SOD |
| 11 | U.S. Bank National Association | Bank | 555 E Ocean Blvd, Long Beach, CA 90802 | 0.8 | CERT 6548 | Cincinnati, OH | $683.38B | $539.84B | 6 | No | SOD+OSM |
| 12 | SOUTHLAND | CU | 1050 Linden Ave, Long Beach, CA 90813 | 1.14 | Charter 68415 | Los Alamitos, CA | $1.29B | $1.07B | 3 | No | NCUA+OSM+web |
| 13 | Bank of America, National Association | Bank | 2000 E Anaheim St, Long Beach, CA 90804 | 2.11 | CERT 3510 | Charlotte, NC | $2.67T | $2.13T | 6 | Yes — Bank of America | SOD+OSM |
| 14 | First-Citizens Bank & Trust Company | Bank | 3500 E 7th St, Long Beach, CA 90804 | 2.82 | CERT 11063 | Raleigh, NC | $235.52B | $171.45B | 1 | Yes — First Citizens Bank | SOD+OSM |
| 15 | WESCOM CENTRAL | CU | 2600 Cherry Ave, Signal Hill, CA 90755 | 3.15 | Charter 66703 | Pasadena, CA | $6.47B | $4.40B | 1 | Yes — Wescom Credit Union | NCUA |
| 16 | LBS FINANCIAL | CU | 4341 E 10th St, Long Beach, CA 90804 | 3.39 | Charter 68460 | Long Beach, CA | $2.19B | $1.90B | 3 | Yes — LBS Financial Credit Union | NCUA+OSM+web |
| 17 | SCHOOLSFIRST | CU | 4725 E 2nd St Ste D, Long Beach, CA 90803 | 3.53 | Charter 24212 | Santa Ana, CA | $36.74B | $31.59B | 1 | Yes — SchoolsFirst Federal Credit Union | NCUA+OSM |
| 18 | LONG BEACH CITY EMPLOYEES | CU | 2801 Temple Ave, Signal Hill, CA 90755 | 3.65 | Charter 1438 | Signal Hill, CA | $279.3M | $235.3M | 2 | No | NCUA+web |
| 19 | VA DESERT PACIFIC | CU | 2845 Temple Ave, Signal Hill, CA 90755 | 3.68 | Charter 5530 | Long Beach, CA | $99.0M | $77.8M | 2 | No | NCUA |
| 20 | I.L.W.U. | CU | 3447 Atlantic Ave, Long Beach, CA 90807 | 3.69 | Charter 24916 | Long Beach, CA | $601.9M | $546.9M | 2 | No | NCUA |
| 21 | POSTCITY FINANCIAL | CU | 2371 Grand Ave, Long Beach, CA 90809 | 3.76 | Charter 86063 | Long Beach, CA | $78.2M | $68.7M | 1 | No | NCUA |
| 22 | SELF-HELP | CU | 1000 N Avalon Blvd, Wilmington, CA 90744 | 3.78 | Charter 24802 | Durham, NC | $2.41B | $1.74B | 1 | Yes — Self-Help Federal Credit Union | NCUA |
| 23 | ORANGE COUNTY'S | CU | 1802 Ximeno Ave, Long Beach, CA 90815 | 3.81 | Charter 24981 | Santa Ana, CA | $3.07B | $2.58B | 1 | Yes — Orange County's Credit Union | NCUA+OSM+web |
| 24 | U.S.B. EMPLOYEES | CU | 300 Falcon St, Wilmington, CA 90744 | 3.91 | Charter 5960 | Wilmington, CA | $3.2M | $2.6M | 1 | No | NCUA |
| 25 | Washington Federal Bank | Bank | 5348 E 2nd St, Long Beach, CA 90803 | 3.94 | CERT 28088 | Seattle, WA | $27.55B | $21.24B | 1 | Yes — WaFd Bank | SOD+OSM |
| 26 | United Business Bank | Bank | 3750 Kilroy Airport Way, Ste 130, Long Beach, CA 90806 | 4.09 | CERT 57716 | Walnut Creek, CA | $2.63B | $2.27B | 1 | Yes — United Business Bank | SOD |
| 27 | LONG BEACH FIREMEN S | CU | 2245 Argonne Ave, Long Beach, CA 90815 | 4.19 | Charter 67921 | Long Beach, CA | $204.3M | $145.6M | 1 | No | NCUA |
| 28 | NUVISION | CU | 2350 E 223rd St, Carson, CA 90810 | 4.38 | Charter 566 | Huntington Beac, CA | $3.94B | $3.30B | 2 | Yes — Nuvision Credit Union | NCUA+OSM |
| 29 | First Bank | Bank | 4040 Atlantic Ave, Long Beach, CA 90807 | 4.49 | CERT 12229 | St. Louis, MO | $6.69B | $5.94B | 2 | No | SOD+OSM |
| 30 | ARROWHEAD | CU | 5531 E Stearns St, Long Beach, CA 90815 | 4.75 | Charter 24973 | Rancho Cucamong, CA | $2.91B | $2.40B | 1 | Yes — Arrowhead Credit Union | NCUA+OSM |
| 31 | BOPTI | CU | 1451 S Seaside Ave, San Pedro, CA 90731 | 4.78 | Charter 10433 | San Pedro, CA | $64.4M | $48.3M | 1 | No | NCUA |
| 32 | Poppy Bank | Bank | 6290 E Pacific Coast Hwy, Long Beach, CA 90803 | 4.9 | CERT 57903 | Santa Rosa, CA | $7.80B | $6.02B | 1 | Yes — Poppy Bank | SOD |

## Found only by organic map/web search (not a current SOD/NCUA branch)

- **Opus Bank, 211 E Ocean Blvd (0.50 mi)** — stale OSM tag (way/238272353). Opus merged into Pacific Premier Bank (2020; Pacific Premier merged into Columbia Banking System 2025); the downtown LB office is closed. Pacific Premier's nearest live SOD branch is San Pedro, 6.37 mi.
- **International City Bank, 249 E Ocean Blvd (0.54 mi)** — OSM tag (way/351202548). ICB merged into United Fidelity Bank fsb (2021); the branch was then acquired by **American Plus Bank, N.A.** and still operates dba International City Bank — captured above under American Plus Bank (rank 8).
- **One West Bank, 3500 E 7th St (2.83 mi)** — stale OSM tag; OneWest -> CIT -> First-Citizens Bank & Trust (rank 14).
- **Luther Burbank Savings, 5348 E 2nd St (3.94 mi)** — stale OSM tag; Luther Burbank merged into WaFd; SOD lists it as Washington Federal Bank (in table).
- **Union Bank (downtown, OSM/Chamber web listing)** — stale; MUFG Union Bank merged into U.S. Bank (2023).
- **Nix Neighborhood Lending, ~2.78 mi (node/5640830050)** — check-cashing/consumer-lending storefront (ex-Kinecta 'Nix'), not an insured bank or CU branch; excluded from the census.
- **Beach Business Bank, 180 E Ocean Blvd** — web find (Yelp): CLOSED; was merged into First Foundation Bank lineage. Excluded.

No live, insured institution within 5 mi was found by OSM/web that is absent from FDIC SOD / NCUA data — the organic layer's net new value was confirming on-the-ground presence and flagging the four stale tags above.

## Notables 5-10 miles out

| Institution | Type | Nearest branch | Mi | Assets |
|---|---|---|---|---|
| MATTEL | CU | 3748 Bayer Avenue, Long Beach | 5.15 | $29.1M |
| CALCOM | CU | 3748 Bayer Ave Ste 104, Long Beach | 5.15 | $82.6M |
| NAVY FEDERAL CREDIT UNION | CU | 4201 McGowen St ste 270, Long Beach | 5.4 | $203.56B |
| FINANCIAL PARTNERS | CU | 4210 McGowen St, Long Beach | 5.43 | $2.25B |
| East West Bank | Bank | 22008 Avalon Blvd, Carson | 5.56 | $82.47B |
| NIKKEI | CU | 146 W Carson St, Carson | 6.36 | $80.6M |
| Pacific Premier Bank, National Association | Bank | 1000 N Western Ave, Ste 101, San Pedro | 6.37 | $17.78B |
| HomeStreet Bank | Bank | 26650 Western Ave Ste C, Harbor City | 6.38 | $7.60B |
| THE FIRST FINANCIAL | CU | 4018 Hardwick ST, Lakewood | 6.54 | $746.5M |
| KINECTA | CU | 4055 Hardwick St, Lakewood | 6.55 | $6.44B |
| FIRST CITY | CU | 4107 Candlewood St, Lakewood | 6.78 | $952.4M |
| COMMUNITYAMERICA | CU | 4637 Candlewood St, Lakewood | 6.93 | $8.98B |
| SEA AIR | CU | 800 Seal Beach Blvd Bldg 12, Seal Beach | 6.99 | $118.2M |
| First Foundation Bank | Bank | 13962 Seal Beach Blvd, Seal Beach | 7.0 | $11.34B |
| Malaga Bank F.S.B. | Bank | 1460 W 25th St, San Pedro | 7.16 | $1.44B |
| CALIFORNIA | CU | 633 E UNIVERSITY DR STE A, CARSON | 7.32 | $5.41B |
| SOUTH BAY | CU | 24520 Narbonne Ave, Lomita | 7.34 | $164.3M |
| SCHOOLS | CU | 20101 Hamilton Ave Ste 150, Torrance | 7.5 | $192.7M |
| HONDA | CU | 19701 Hamilton Ave ste 130, Torrance | 7.69 | $1.20B |
| FARMERS INSURANCE | CU | 19191 S Vermont Ave, Torrance | 8.11 | $1.37B |
| TORRANCE COMMUNITY | CU | 1511 Cravens Ave, Torrance | 8.16 | $160.0M |
| Bank of Hope | Bank | 2424 Sepulveda Blvd, Ste A, Torrance | 8.19 | $18.65B |
| SMBC MANUBANK | Bank | 970 W 190th St, Ste 500, Torrance | 8.25 | $7.73B |
| Citizens Business Bank | Bank | 970 W 190th St, Ste 120, Torrance | 8.25 | $15.51B |
| Shinhan Bank America | Bank | 22501 Crenshaw Boulevard, Suite 400 & 500, Torrance | 8.31 | $1.97B |
| Woori America Bank | Bank | 2390 Crenshaw Blvd, Torrance | 8.33 | $4.04B |
| PARISHIONERS | CU | 2355 Crenshaw Blvd Ste 100, Torrance | 8.38 | $67.2M |
| US Metro Bank | Bank | 2742 Sepulveda Blvd, Torrance | 8.58 | $1.56B |
| Royal Business Bank | Bank | 11304 1/2 South St, Cerritos | 8.76 | $4.19B |
| LOS ANGELES | CU | 11306 South St, Cerritos | 8.76 | $1.28B |
| MID-CITIES | CU | 325 S Santa Fe Ave, Compton | 8.79 | $16.3M |
| EverTrust Bank | Bank | 11458 South St, Cerritos | 8.9 | $1.11B |
| Open Bank | Bank | 11811 South St, Cerritos | 9.24 | $2.70B |
| Cathay Bank | Bank | 23211 Hawthorne Blvd, Ste 108, Torrance | 9.33 | $24.04B |
| Wallis Bank | Bank | 11900 South St, Cerritos | 9.33 | $1.40B |
| Industrial and Commercial Bank of China USA, National Association | Bank | 23133 Hawthorne Blvd, Ste 100, Torrance | 9.36 | $2.86B |
| Commonwealth Business Bank | Bank | 3770 Sepulveda Blvd, Torrance | 9.51 | $1.99B |
| Habib American Bank | Bank | 18357 Pioneer Blvd, Artesia | 9.53 | $2.98B |
| Hanmi Bank | Bank | 21838 Hawthorne Blvd, Torrance | 9.73 | $7.79B |
| First General Bank | Bank | 17808 Pioneer Blvd, Ste 108, Artesia | 9.74 | $1.14B |
| PCB Bank | Bank | 17709 Pioneer Blvd, Artesia | 9.78 | $3.40B |
| OneUnited Bank | Bank | 1495 N Wilmington Ave, Compton | 9.82 | $609.0M |
| CTBC Bank Corp. (USA) | Bank | 21705 Hawthorne Blvd, Torrance | 9.85 | $5.37B |
| Preferred Bank | Bank | 21615 Hawthorne Blvd, Ste 100, Torrance | 9.89 | $7.66B |

## Sources

- US Census geocoder: https://geocoding.geo.census.gov/geocoder/locations/onelineaddress and /addressbatch (benchmark Public_AR_Current)
- FDIC institutions API: https://api.fdic.gov/banks/institutions (ASSET/DEP in $000s, current quarter)
- FDIC SOD 2025: local research/v6/out/sod_2025_Los_Angeles.json, sod_2025_Orange.json
- NCUA 2026-03 call report files: research/v6/out/cr202603/ (branch file, FS220, FOICU)
- Overpass API: https://overpass-api.de/api/interpreter — amenity=bank around:8047 of 33.767378,-118.199441
- OSM Nominatim (fallback geocoding): https://nominatim.openstreetmap.org/search
- Web: yelp.com/biz/citibank-long-beach-2; yelp.com/biz/banc-of-california-long-beach; wellsfargo.com locator 111 W Ocean Blvd; bankbranchlocator.com international-city-bank-history; business.lbchamber.com (Union Bank downtown, stale)
