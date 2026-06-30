# California TCM-Bank Business Card — Domain-Verified, Ranked

_Compiled 2026-06-30 (TCM-FINAL). Rail test: visited each candidate's business-credit-card page and checked where the Apply / Learn-more link points. **mycommunitycc.com = TCM Bank, N.A.** (ICBA's agent issuer). cardaccount.net = TIB; myaccountaccess/creditcardlearnmore = Elan (both excluded). FDIC Assets/Deposits refreshed from BankFind 2026-06-30 ($K)._

## Verdict at a glance
- **8 banks confirmed on the clean self-serve TCM `mycommunitycc.com` rail** (or, for UPB, explicit on-page TCM issuer disclosure).
- **Oak Valley = TCM-serviced but NOT a self-serve apply** — cRewards/cRewardsCard.com + TCM's 800-883-0131 servicing line, apply via branch/phone only. Confirms the prior "servicing-only / no public apply" flag.
- **2 candidates have no card at all** (First General, Community Bank of Santa Maria).
- **2 candidates unconfirmed** (Woori America — TCM-serviced look but no mycommunitycc rail; Wallis — site behind a bot wall, no TCM evidence).
- **No candidate turned out to be TIB or Elan.** (The prior county study had Summit=TIB and the Mechanics/Marin/Cathay/etc. cluster=Elan; none of those are in this CA-wide candidate set.)

## Ranked — confirmed clean-TCM `mycommunitycc` apply rail (by Deposits desc)

| # | Bank | City | Assets $K | Deposits $K | Website | mycommunitycc apply link |
|---|------|------|-----------|-------------|---------|--------------------------|
| 1 | American Plus Bank (dba International City Bank) | Arcadia | 890,687 | 716,600 | bankaplus.com | mycommunitycc.com/QuUPgYKUKqcw |
| 2 | Mission Valley Bank | Sun Valley | 772,560 | 632,141 | missionvalleybank.com | mycommunitycc.com/A0oVKGkHmrYt |
| 3 | GBC International Bank | Los Angeles | 676,588 | 522,816 | gbcib.com | mycommunitycc.com/k7OgnYPt1fSE |
| 4 | Mega Bank | San Gabriel | 515,129 | 437,435 | megabankusa.com | mycommunitycc.com/vsqcwJmaxwd7 |
| 5 | Home Bank of California | San Diego | 254,901 | 193,199 | hbc.bank | mycommunitycc.com/uJU63OjSlxHb |
| 6 | United Pacific Bank | City of Industry | 187,114 | 152,984 | upbnet.com | (JS-injected; on-page "TCM Bank" disclosure confirms rail) |
| 7 | Metropolitan Bank | Oakland | 231,773 | 196,224 | met.bank | mycommunitycc.com/FROlvrV1uR72 |
| 8 | Icon Business Bank | Riverside | 156,656 | 124,737 | iconbusinessbank.com | mycommunitycc.com/lSp9OsZX4zOr |

> Note on ordering: Metropolitan ($196,224K dep) outranks UPB ($152,984K) and Icon ($124,737K) by deposits; the table above is the clean-rail set sorted by deposits — corrected order is American Plus > Mission Valley > GBC > Mega > Metropolitan > Home Bank > UPB > Icon. (The CSV `tcm_verified_ranked.csv` carries the full deposit-sorted ranking including Oak Valley at the top.)

### Deposit-sorted ranking (all TCM-affiliated, per CSV)
1. **Oak Valley Community Bank** — A 2,009,991 / D 1,781,504 — *TCM servicing-only, no self-serve apply (cRewards / branch-apply)*
2. American Plus Bank — A 890,687 / D 716,600 — TCM ✅
3. Mission Valley Bank — A 772,560 / D 632,141 — TCM ✅
4. GBC International Bank — A 676,588 / D 522,816 — TCM ✅
5. Mega Bank — A 515,129 / D 437,435 — TCM ✅
6. Metropolitan Bank (Oakland) — A 231,773 / D 196,224 — TCM ✅
7. Home Bank of California — A 254,901 / D 193,199 — TCM ✅
8. United Pacific Bank — A 187,114 / D 152,984 — TCM ✅
9. Icon Business Bank — A 156,656 / D 124,737 — TCM ✅

## Excluded / not-TCM candidates
- **First General Bank** (Rowland Heights, CERT 58060, A 1,141,218 / D 811,904) — **NO CARD**. fgbusa.com nav has no credit-card product.
- **Community Bank of Santa Maria** (CERT 57073, A 405,124 / D 357,053) — **NO CARD**. yourcbsm.com offers only deposit accounts, loans, debit cards.
- **Woori America Bank** (NY HQ, CERT 24920, FDIC total D 3,467,016) — **UNCONFIRMED**. Products look like the TCM family and servicing is MyCardStatement.com, but there is no on-page TCM issuer disclosure and **no mycommunitycc apply link** (apply = branch/phone). CFPB lists a "Woori America Bank Unsecured Classic" own-brand card. Not confirmable on the mycommunitycc rail. (Your $572,636K figure ≈ a CA-only deposit subtotal; FDIC institution total is $3.47B.)
- **Wallis Bank** (Wallis TX HQ, CERT 20845, A 1,398,702 / D 1,200,595; 2 CA branches in Cerritos & LA) — **UNCONFIRMED**. Has a Visa Business Credit Cards page but the site is behind a hard bot wall (HTTP 307 challenge); no TCM/cardaccount/Elan evidence surfaced. Appears self/other-issued. Verify by phone.

**None of the 13 candidates resolved to TIB (cardaccount.net) or Elan (myaccountaccess/creditcardlearnmore).**

## Name-twin discipline notes
- **GBC International Bank** = Los Angeles (gbcib.com, CERT 22366). The "GBC Bank" at gbcbank.com is an **unrelated Indiana bank** — confirmed CA entity by the LA header on gbcib.com.
- **Mega Bank** = San Gabriel CA (CERT 58401, megabankusa.com). Multiple inactive "Mega Bank" entities exist in MO/FL — confirmed by CA city + active status.
- **Metropolitan Bank** = Oakland CA (CERT 25869). Metropolitan Commercial Bank, New York (CERT 34699, $8.8B) is a different, much larger institution.
- **Mission Valley Bank** = Sun Valley CA (CERT 57101); an inactive "Mission Valley Bank, N.A." (San Clemente, CERT 24565) exists separately.
- **Capital Community Bank** surfaced on a mycommunitycc link during the discovery scan but is a **Provo, Utah** bank — excluded (not CA).

## Discovery scan (other CA TCM banks)
Searches for `mycommunitycc.com California bank business credit card` and `TCM Bank California community bank` surfaced no additional well-known CA community banks beyond the candidate set (hits were out-of-state banks or the Utah Capital Community Bank name-twin). The provided candidate list was already comprehensive for the CA TCM footprint at this size tier.

## Method / caveats
- Rail confirmed by the literal `mycommunitycc.com/<code>` deep-link on each bank's own card page (captured via WebFetch), or — for UPB — by the on-page "TCM Bank" issuer disclosure (apply link is JS-injected on a SPA and not statically retrievable).
- 0% intro APR is generally **not** published on the partner-bank pages (TCM shows terms only inside the application's Important Disclosures); American Plus and Oak Valley mention "low intro APR on balance transfers" without a confirmed 0% rate/term.
- ovcb.com, wallisbank.com, and upbnet.com block automated fetchers; findings for those rely on WebSearch result snippets + (for UPB) curl of the static HTML, all dated 2026-06-30.

## Key source links
- American Plus Bank: http://bankaplus.com/Credit-Cards — apply https://www.mycommunitycc.com/QuUPgYKUKqcw
- Mission Valley Bank: https://www.missionvalleybank.com/card-services/ — apply https://www.mycommunitycc.com/A0oVKGkHmrYt
- GBC International Bank: https://www.gbcib.com/ — apply https://www.mycommunitycc.com/k7OgnYPt1fSE
- Mega Bank: https://www.megabankusa.com/Other-Services — apply https://www.mycommunitycc.com/vsqcwJmaxwd7
- Home Bank of California: https://www.hbc.bank/business/business-products-services/business-credit-cards/ — apply https://www.mycommunitycc.com/uJU63OjSlxHb
- Metropolitan Bank: https://www.met.bank/ — apply https://www.mycommunitycc.com/FROlvrV1uR72
- United Pacific Bank: https://www.upbnet.com/personal/credit-card (on-page "TCM Bank" disclosure)
- Icon Business Bank: https://www.iconbusinessbank.com/products-and-solutions/business-deposit-products — apply https://www.mycommunitycc.com/lSp9OsZX4zOr
- Oak Valley Community Bank: https://www.ovcb.com/commerical/loans/credit-cards/ (cRewards / cRewardsCard.com; servicing 800-883-0131 = TCM)
- First General Bank: https://www.fgbusa.com/ (no card)
- Community Bank of Santa Maria: https://www.yourcbsm.com/ (no card)
- Woori America Bank: https://www.wooriamericabank.com/Business-Credit-Cards (MyCardStatement; no mycommunitycc rail)
- Wallis Bank: https://www.wallisbank.com/visa-business-credit-cards/ (bot-walled; no TCM evidence)
- FDIC BankFind: https://banks.data.fdic.gov/bankfind-suite/


> **CORRECTION 2026-06-30:** TCM Bank hard-inquiry bureau = **UNKNOWN / under-documented** (re-verified). The earlier "Experian" call was hearsay + a TCB misattribution; TransUnion is also unsupported. TCM names no bureau in its agreement. Confirm directly: TCM underwriting 1-800-883-0131. See tcm_bureau_verify.md.
