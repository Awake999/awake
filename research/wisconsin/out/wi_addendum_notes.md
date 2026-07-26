# WI ADDENDUM — ibanknet cross-check findings (2026-07-26)

## Source cross-validation
- ibanknet.com is UP (HTTP 200). WI (FIPS 55) lists pulled: statebank (148), statethrift (8), stateallfi (255).
- **ibanknet deposits/assets match FDIC exactly** (e.g., Associated Bank $35,800,709K dep / $45,537,550K assets on both) — figures cross-validated across both sources.
- ibanknet ALL-FI also surfaces **99 WI credit unions** (NCUA) that the FDIC institutions query does not cover. Largest: Summit CU $6.67B, Landmark CU $6.33B, Community First CU $5.78B, UW CU $5.73B, Royal CU $5.21B. NOTE: TCM Bank is ICBA's (bankers' association) agent issuer and serves community BANKS; CU card programs typically run Elan or CU processors (Velera/CURewards). CUs excluded from the TCM bank list by definition — flagged here for completeness.

## Gap found + RESOLVED
- **BANNER BANKS** (Birnamwood WI, dep $114,920K) appeared in ibanknet but not in the FDIC-derived screening list.
  - Now rebranded **Bank of Wisconsin** (bankofwisconsin.bank); offices Birnamwood, Hatley, Antigo, Wittenberg. Phone (715) 449-2556.
  - **Rail = ELAN, not TCM.** VERIFIED own-page disclosure: "The creditor and issuer of these cards is Elan Financial Services, pursuant to separate licenses from Visa U.S.A. Inc., and MasterCard International Incorporated."
  - Apply link: https://www.mycardapply.com/synindex/?ecdma-lc=00306&offertype=0 · Servicing: myaccountaccess.com (theme=elan1, loc=00306)
  - Source: https://bankofwisconsin.bank/business-credit-cards.html (fetched 2026-07-26)
  - ⚠️ NAME-TWIN: **Banner Banks / Bank of Wisconsin (Birnamwood WI) ≠ Banner Bank (Walla Walla WA)** — the WA bank is the one with the ChexSystems QualiFile auto-deny in our CA research. Do not merge.
- ASSOCIATED TRUST COMPANY, N.A. (Milwaukee, $0 deposits) — trust charter, no retail/business card products. Excluded.

## Net
Screening universe is complete: 152 FDIC-derived + Banner Banks/Bank of Wisconsin (now resolved = Elan) = 153 relevant WI banks; 2 excluded (Bankers' Bank = FI-only, John Deere Financial = captive) + 1 trust charter.
