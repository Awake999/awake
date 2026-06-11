# ICBA / Community Banks Reachable from Long Beach (One World Trade Center, 90831) and Fontana (6614 Tokay Ave, 92335)

Date: 2026-06-11. Companion CSV: `icba_community_banks.csv` (same directory).

## Method — locator worked, no fallback needed

1. **banklocally.org** (ICBA consumer site) 301-redirects to **banklocally.com** (Liferay/ICBA CMS), whose "find a bank" button points at **https://directory.icba.org/** — the actual ICBA member-bank locator.
2. The locator's map JS exposes a plain JSON API (no auth, browser UA sufficient):
   `https://directory.icba.org/api/directory?action=GetDirectoryMapLocations&qllat={lat}&qllong={lng}&qlr={radius_mi}&id=11928&pi=0&salt=70415`
   Queried 25-mi and 50-mi radii around both addresses (LB WTC ≈ 33.7679,-118.1985; Fontana ≈ 34.0875,-117.4640). Nearby zips 90802/92336/91730 fall inside these circles. Result: **67 member locations → 20 distinct ICBA member banks** (one of which, "Premier Foundation Bank," is a stale artifact — see below). A `qk=` name-filter parameter also works and was used to negative-check non-listed banks (Beneficial State, Fremont Bank → not members or not listed).
3. CERT / **Total Assets / Total Deposits** from the FDIC institutions API (`https://api.fdic.gov/banks/institutions`, REPDTE 2026-03-31, $ thousands).
4. Card screen: 18 of the 20 locator banks were already screened in the v6 funding table (`/home/user/awake/research/v6/deliverables/ca_business_credit_funding_v6_funding_table.csv`) — underwriter tells (mycommunitycc/mycardstatement = TCM; creditcardlearnmore/myaccountaccess = Elan; cardaccount.net/mypreferredpoints = TIB) carried over with their verification dates. Distances computed haversine from locator lat/lng (city-level accuracy).

## What the locator yielded

- **20 ICBA member banks** within 50 mi of one or both addresses (ICBA membership = VERIFIED via directory.icba.org, 2026-06-11).
- New intel vs v6 (enrichment):
  - **ICBA membership flags** for all 18 v6 banks — none of these were tagged as ICBA members in v6.
  - **First Foundation Bank** locator entry is stale: merged into **Sunflower Bank, N.A.** (FirstSun) **2026-04-01**; FDIC CERT 58647 now inactive (businesswire.com/news/home/20260331761127/en/).
  - **"Premier Foundation Bank"** (locator /120971, two Running Springs CA offices, website field = firstfoundationinc.com) has **no FDIC record** — a locator artifact left over from First Foundation's ex-Premier Business Bank sites. Excluded from candidate math.
  - Chino Commercial Bank appears twice in the locator (two ObjectIds, same CERT 35366) — merged to one row.
- **The headline pattern:** of the 18 real, active ICBA members with locations near these addresses, the card programs split: **6 TCM/TIB agent (NO-GO class)** — GBC International, Mega, Mission Valley, Woori America, Wallis (TCM) + HCN (TIB); **4 Elan (NO-GO)** — Poppy, Royal Business, Beach Cities, (First Foundation, legacy); **4 no card** — Chino Commercial, OneUnited, Tustin Community, TIB N.A. itself; **2 self-issuers** — Banner, Sunwest; **2 unknown/commercial** — American Business Bank, IDB New York. This confirms the TCM-as-ICBA-agent thesis: most small ICBA members here outsource their card paper.

## Top self-issuer candidates

### Near Fontana (6614 Tokay Ave)
1. **Banner Bank** — VERIFIED ICBA; self-issued Business Platinum MC, **0% 12 mo, $0 AF**; Rancho Cucamonga branch **~4.8 mi** away. $16.3B assets (over the $10B community line, but a verified ICBA member). Best combination of paper + proximity in the whole sheet.
2. **HCN Bank** — Riverside ~10 mi; has biz cards but on the **TIB agent rail → NO-GO class**; only useful if a phone screen reveals an in-house option.
3. **Chino Commercial Bank** — Rancho Cucamonga ~4.8 mi; **no biz card**, but its $10K–$100K unsecured business LOC is a no-doc-adjacent alternative.

### Near Long Beach (One World Trade Center)
1. **Sunwest Bank** — VERIFIED ICBA; self-underwrites Visionary Corporate Card on own balance sheet (Torpago/Marqeta rails); Irvine ~20.8 mi; **existing-clients-only** — open a deposit account first.
2. **American Business Bank** — VERIFIED ICBA; downtown LA ~19.9 mi; corporate cards with undisclosed issuer, no agent-portal tells → **screen by phone**, plausible sleeper self-issuer.
3. **Beneficial State Bank** — community-bank-only (not in locator); East LA branch ~18.5 mi; self-issues on Fiserv SpendTrack; CDFI, relationship-friendly; terms unpublished.
4. **Poppy Bank** — the closest ICBA member to LB WTC (PCH branch ~4.7 mi) but **Elan = NO-GO**; listed for completeness.

### Remote / statewide
- **Fremont Bank** — community-bank-only; self-issuer (CorServ Apex), **0% 6 mo**, online apply statewide; no SoCal branch but the cleanest pure self-issuer paper reachable from either address.

## Integrity notes
- ICBA_member column distinguishes **VERIFIED (locator, 2026-06-11)** from **COMMUNITY-BANK-ONLY** (FDIC <$10B definition; locator negative-checked).
- Assets/deposits: FDIC API, 2026-03-31 call data, $ thousands, pulled 2026-06-11.
- Underwriter verdicts inherit v6 verification dates (2026-05-28 … 2026-06-10); Wallis Bank's TCM tell is a 2020 archive (MED confidence) — re-verify by phone.
- Distances are straight-line haversine from locator coordinates, city-level precision as specified.
