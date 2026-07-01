# Elan-Issued Banks Near Alameda, CA — Ranked Reference

**Anchor:** City of Alameda, CA (≈ 37.7652, -122.2416)
**Compiled:** 2026-07-01
**Sort:** distance to Alameda ASC, then total-bank deposits DESC (ties)
**Distance method:** straight-line (haversine) from Alameda city center to the geocoded nearest branch, via the free US Census geocoder (`geocoding.geo.census.gov`). Oakland branches sit across the estuary — add ~1 mi for driving via the Posey/Webster tubes or Park St bridge.
**Deposits:** TOTAL institution deposits from the FDIC API (`banks.data.fdic.gov`, latest call report), NOT the Alameda-branch subtotal.

## Ranked table

| # | Bank | Dist (mi) | Total deposits | Branch phone | Business / RM phone | Business-card link |
|---|------|-----------|----------------|--------------|---------------------|--------------------|
| 1 | Poppy Bank | 0.5 (in-city) | $6.02B | (510) 865-9040 | (888) 636-9994 (biz/commercial line) | poppy.bank/business-checking-accounts/ |
| 2 | Bank of Marin | 0.8 (in-city) | $3.46B | (510) 748-8400 | (510) 748-8803 — RM Wim Kees van Hout (Oakland) | bankofmarin.com/products-and-services/credit-cards/ |
| 3 | Metropolitan Bank | 2.5 (Oakland) | $196.2M | (510) 834-1933 | (510) 834-1933 (ask at branch) | mbonlineportal.com/business/business-credit-cards/ |
| 4 | EverBank, N.A. | 2.8 (Oakland) | $37.69B | 510.834.3830 | (888) 882-2021 (biz/commercial) | everbank.com — Elan card mgmt |
| 5 | Cathay Bank | 2.8 (Oakland) | $20.70B | (510) 208-3700 | 800-922-8429 (biz svc → RM) | cathaybank.com/business/credit-cards |
| 6 | East West Bank | 2.9 (Oakland) | $69.09B | (510) 451-5600 | 888-761-3967 (Biz & Commercial) | eastwestbank.com/…/corporate-card (One Card) |
| 7 | Heritage Bank of Commerce (now Citizens Business Bank) | 3.1 (Oakland) | $4.82B* | (510) 869-7000 | 510.869.7000 (Oakland Business Financial Center) | cbbank.com/business-cards/ |
| 8 | Mechanics Bank | 3.2 (Oakland) | $18.25B | (510) 251-6100 | 800-797-6324 (biz/commercial) | mymechanics.com/business/loans-credit/business-credit-cards/ |
| 9 | First Foundation Bank | 3.2 (Oakland) | $8.78B* | (510) 250-8130 | (510) 250-8130 (ask at branch) | firstfoundationinc.com/business-banking/business-lending/business-credit-cards |
| 10 | Farmers & Merchants Bank of Central California | 4.6 (Oakland hills) | $5.12B | (510) 902-5870 | none published (ask at branch) | cdwest.fmb.com/business/business-credit-card |
| 11 | Westamerica Bank | 17.8 (Pleasanton) | $4.79B | (925) 734-1510 | none published (ask at branch) | westamerica.com/credit-card-application/ |
| — | First Federal S&L of San Rafael | 9.2 (SF)† | $176.4M | see ffsavings.com | n/a | ffsavings.com |

\* Heritage (FDIC CERT 33905) and First Foundation (CERT 58647) both show FDIC ACTIVE=0 — figures are last-reported; see status notes.
† First Federal has **no Alameda County branch** (Marin/SF only) — excluded from the primary ranking per its own row note.

All 11 primary banks are **Elan-confirmed (Y)**. Evidence per bank is in the CSV `Elan_confirmed` column (each bank's own card page names Elan Financial Services as creditor/issuer, and/or servicing runs on the Elan platforms myaccountaccess.com / creditcardlearnmore.com).

## Status flags
- **Metropolitan Bank — RAIL CONFLICT (kept):** `mbonlineportal.com` is an Elan storefront and states the issuer is Elan Financial Services, but `mycommunitycc` points to a TCM / TransCard rail. Confirm which rail is live before relying on it.
- **Heritage Bank of Commerce — ACQUIRED by Citizens Business Bank:** merger completed (~2026-04-17); FDIC CERT 33905 now inactive, consolidated into Citizens Business Bank (CERT 21716). Still Elan rail — CBB business cards are Elan-issued (cbbank.com/business-cards/). The Oakland branch at 1111 Broadway is now a CBB Business Financial Center.
- **Farmers & Merchants Bank of Central California — Elan CONFIRMED (Lodi HQ):** site fmbonline.com / fmb.com; business-card storefront on cdwest.fmb.com names Elan as issuer. Nearest branch is the Oakland-hills Montclair Village office.
- **First Foundation Bank — entity change:** FDIC CERT 58647 shows ACTIVE=0; materials reference "Sunflower Bank, N.A. dba First Foundation Bank." Deposits are last-reported; verify current legal entity before use. Cards remain Elan-issued (Visa + American Express).
- **First Federal S&L of San Rafael — MARIN/SF ONLY:** branches in San Rafael (HQ, 1030 3rd St) and San Francisco (2521 San Bruno Ave; 2298 Lombard St). No Alameda County branch — nearest office is ~9 mi (SF, straight-line; ~13 mi driving via Bay Bridge). Included for completeness; not Alameda-reachable via a county branch.

## Notes on ties
- 2.8 mi tie: **EverBank ranked above Cathay** (deposits $37.69B > $20.70B).
- 3.2 mi tie: **Mechanics ranked above First Foundation** (deposits $18.25B > $8.78B).

## Sources (accessed 2026-07-01)
- FDIC BankFind / API: `https://banks.data.fdic.gov/api/institutions` (CERTs 57903, 32779, 25869, 34775, 18503, 31628, 33905/21716, 1768, 58647, 1331, 3430, 31406)
- US Census geocoder: `https://geocoding.geo.census.gov/geocoder/locations/onelineaddress`
- Each bank's own branch-locator, contact, and business-credit-card pages (URLs in the CSV `Source_links` column).
