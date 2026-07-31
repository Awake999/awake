# TCM Bank (mycommunitycc.com rail) — Branch-Level Detail near Alameda, CA

**Anchor:** Alameda city (37.7652, −122.2416) · **Date:** 2026-07-26 · Sorted by distance ASC
FDIC financials as of call report **03/31/2026** (api.fdic.gov). Distances are great-circle miles from the anchor, branch addresses geocoded via `geocoding.geo.census.gov`.

---

## Headline

Only **two** banks near Alameda actually issue **business** credit cards on the TCM rail today:

| # | Bank | Nearest branch to Alameda | Miles | Business cards on TCM? |
|---|------|---------------------------|-------|------------------------|
| 1 | **Metropolitan Bank** (Oakland) | 250 E 18th St, Oakland 94606 | **2.5** | ✅ Yes |
| 2 | Tri Counties Bank (Chico) | 311 California St, San Francisco 94104 | 8.9 | ❌ Personal only |
| 3 | **BAC Community Bank** (Stockton) | 2090 Diamond Blvd Ste 10, Concord 94520 | **17.6** | ✅ Yes |
| 4 | Pinnacle Bank (Gilroy) | 1999 S Bascom Ave Ste 100, Campbell 95008 | 37.4 | ❌ Not TCM at all (TIB) |
| 5 | Oak Valley Community Bank (Oakdale) | 1034 N Central Ave, Tracy 95376 | 44.6 | ❌ Left TCM; now self-issued |

Three of the four banks handed to this task needed correction. Details below.

---

## 1. Metropolitan Bank — Oakland, CA · CERT 25869 · **2.5 mi** ✅ TCM

| Field | Value |
|---|---|
| Total deposits | **$196,224K** |
| Total assets | **$231,773K** |
| Nearest branch | **250 E 18th St, Oakland, CA 94606** (Head Office) — 2.5 mi |
| Branch phone | **(510) 834-1933** (fax 510.834.1909) |
| 2nd branch | 381 8th St, Oakland 94607 (Chinatown) — 2.9 mi — **(510) 834-7534** |
| Business RM phone | None published. Bank says "contact your personal banker" / "contact your local branch" → use **(510) 834-1933** |
| Business-card page | **https://www.met.bank/** — the bank has *no* on-site card page at all; nav + footer "Credit Card" links jump straight to the storefront |
| TCM application link | **https://www.mycommunitycc.com/FROlvrV1uR72** (business view: `/FROlvrV1uR72/business`) |
| Business card products | **Visa Business Edition · Visa Business Rewards · Visa Business Cash Rewards** |
| Personal card products | Visa Platinum Rewards · Visa Platinum Edition · Visa Platinum Cash Rewards |

> ⚠️ **Branch relocation:** met.bank posts that the Oakland Chinatown office is "relocating to **360 8th Street**, Oakland California effective on or about **August 31, 2026**." As of the 2026-07-26 report date the address is still 381 8th St.

Other branches (farther): San Francisco Chinatown 1355 Stockton St 94133, (415) 986-6999 — 9.4 mi; San Jose Lion Plaza 1816 Tully Rd #192 95122, (408) 274-3707.

### ✅ The Elan-vs-TCM conflict, resolved: **it is TCM.**

Four independent lines of evidence, all pointing the same way:

1. **The bank's own site has exactly one outbound card link, and it is TCM.** `met.bank` renders six `<a>` tags with the anchor text "Credit Card" (nav + footer, personal and business), and **every one** has `href="https://www.mycommunitycc.com/FROlvrV1uR72"`. A regex sweep of the homepage and the full `page-sitemap.xml` (70 URLs) for `elan|myaccountaccess|creditcardlearnmore|mycardapply|cardaccount.net|applycommunitycard|yourcommunitycard` returns **zero hits**. There is no `/credit-cards/` or `/business-credit-cards/` page — both 404.

2. **The routing table names TCM explicitly.** The mycommunitycc Angular bundle (`chunk-3I5JGJXI.js`) carries the CreditSnap production tenant map verbatim:
   ```js
   {url:"mycommunitycc.com",      institutionId:"TCM",  cxUrl:"https://apply.mycommunityccard.com"},
   {url:"www.mycommunitycc.com",  institutionId:"TCM",  cxUrl:"https://apply.mycommunityccard.com"},
   {url:"lp.applycommunitycard.com", institutionId:"2471", cxUrl:"https://sm.lp.applycommunitycard.com"},
   {url:"lp.apply.cardsupportcenter.com", institutionId:"BBOK", ...},
   {url:"lp.apply.ubb.com",       institutionId:"2512", ...}
   ```
   This is the same table cited in the prior definitive resolution, re-pulled live. It also surfaces a **second TCM-owned domain: `mycommunityccard.com`** — worth adding to future rail-detection regexes.

3. **The slug's own branding asset is this bank.** `https://creditsnap-public.s3.amazonaws.com/images/TCM/FROlvrV1uR72_logo.png` (HTTP 200, 30,013 bytes) renders the **"METROPOLITAN BANK 加州金城銀行"** wordmark — unmistakably the Oakland Chinatown institution, not Metropolitan Commercial Bank (NY) or any other Metropolitan.

4. **The servicing phone is TCM's.** met.bank/locations lists the lost-or-stolen **credit** card line as **(800) 883-0131** — TCM Bank's cardholder services number. (Its debit line is a separate 800-500-1044.)

**Why the earlier pass saw Elan:** `mbonlineportal.com` **does not exist**. It returns NXDOMAIN for both apex and `www` (`getent hosts` fails; curl exits 000 — not a 403, not a timeout, no DNS record at all). It appears nowhere in met.bank's HTML. That finding was either a different "Metropolitan" bank or a stale/garbled artifact; it should be discarded.

---

## 2. Tri Counties Bank — Chico, CA · CERT 21943 · **8.9 mi** — 🆕 NEW TCM BANK, **personal cards only**

| Field | Value |
|---|---|
| Total deposits | **$8,408,678K** |
| Total assets | **$9,946,447K** |
| Nearest branch | **311 California St, San Francisco, CA 94104** (SF Downtown / Commercial Banking Center) — 8.9 mi |
| Branch phone | **(415) 488-2725** |
| Business RM phone | **1-800-982-2660** ("Speak with a Banker"); Walnut Creek Business Center LPO, 1981 N Broadway (13.8 mi) |
| Business-card page | https://www.tcbk.com/business/credit-cards |
| Personal-card page | https://www.tcbk.com/personal/credit-cards ← the TCM one |
| TCM application link | **https://www.mycommunitycc.com/jh5XCu3CeG3u/personal/** — personal only; no business storefront exists |
| TCM (personal) products | Rewards Platinum · Cash Rewards Platinum · Platinum Edition · Visa Signature |
| Business products (NOT TCM) | Visa Business · Visa Business Platinum · Visa Commercial · Visa Purchasing · Visa Fleet |

This is the one genuinely new Bay-Area-relevant TCM bank the sweep turned up, and it is by far the largest ($9.9B). **But it is not usable for a business-card play.** The split is clean and triple-confirmed:

- **Personal = TCM.** tcbk.com/personal/credit-cards states verbatim: *"Tri Counties Bank personal credit cards are issued by TCM Bank, N.A."* and links `mycommunitycc.com/jh5XCu3CeG3u/personal/` plus four deep links of the form `mycommunitycc.com/card-detail/CC/VISA_PLATINUM_REWARDS?merchantId=jh5XCu3CeG3u`.
- **Business ≠ TCM.** The business page carries **no** TCM issuer disclosure. Its only occurrence of the string `mycommunitycc.com` sits inside a **site-wide JavaScript exit-link exclusion array** (`var excludes = [... 'mycardstatement.com','crewardscard.com','mycommunitycc.com']`), not in an `href` — a classic false positive for naive rail-grepping. The business platforms actually referenced are **ezbusinesscardmanagement.com / ezcardinfo.com / 360control.firstdata.com** (Fiserv / First Data commercial card).
- **Asset probe agrees.** Probing `images/TCM/jh5XCu3CeG3u_<CODE>.png` returns HTTP 200 for exactly the four personal codes (`VISA_SIGNATURE`, `VISA_PLATINUM_REWARDS`, `VISA_PLATINUM_EDITION`, `VISA_PLATINUM_CASH_REWARDS`) and **404 for every `VISA_BUSINESS_*` code** — whereas the same probe against Metropolitan and BAC returns 200 for the business codes. TCM simply does not carry a business program for this bank.

---

## 3. BAC Community Bank — Stockton, CA · CERT 19434 · **17.6 mi** ✅ TCM

| Field | Value |
|---|---|
| Total deposits | **$684,849K** |
| Total assets | **$780,102K** |
| Nearest branch | **2090 Diamond Blvd, Suite 10, Concord, CA 94520** — 17.6 mi |
| Branch phone | **(925) 609-1970** — Branch Manager Jolynne Harrison |
| Business RM phone | **1-877-226-5820** (main / card services); Jerry Marquez, Relationship Officer **(925) 634-2113** |
| Business-card page | **https://www.bankbac.com/business/loans-credit/business-credit-cards.html** |
| TCM application link | **https://www.mycommunitycc.com/2f497f80fb2c/business/** |
| Business card products | Small Business Rewards Credit Card · Small Business Cash Rewards Credit Card · Small Business Edition Credit Card · Company Rewards Charge Card |

> 📍 **Correction to the brief's distance assumption.** BAC was scoped as "Stockton ~75 mi." Its Stockton HQ is 53.8 mi, but BAC has a **Contra Costa footprint** and its **Concord** branch is only **17.6 mi** from Alameda — making it the #2 practical business-card option. Antioch (3448 Deer Valley Rd, (925) 776-2200) and both Brentwood offices are also far closer than Stockton.

**Rail evidence — the cleanest of the set.** The business-card page carries the disclosure verbatim:

> *"This card is issued by **TCM Bank, N.A.** Subject to credit approval."*

…and its **EXPLORE & APPLY** button is literally `<a class="confirm primary-button" href="https://www.mycommunitycc.com/2f497f80fb2c/business/" target="_blank">`. Servicing stack is TCM's throughout: **MyCardStatement.com**, **cRewardsCard.com**, **1-877-226-5820**. The slug's logo asset renders the "BAC Community Bank" mark.

Card descriptions from the page: *Small Business Rewards* — "earn unlimited reward points… one point per dollar on net purchases"; *Small Business Cash Rewards* — "1% cash back on all net purchases. Cash rewards never expire."; *Small Business Edition* — "no penalty APR and low interest rates"; *Company Rewards Charge Card* — "intended for large corporations, non-profits and municipalities. No annual fee. Pay-in-full account."

---

## 4. Pinnacle Bank — Gilroy, CA · CERT 58297 · 37.4 mi · ❌ **NOT TCM — prior finding corrected**

| Field | Value |
|---|---|
| Total deposits | $823,506K |
| Total assets | $945,774K |
| Nearest branch | 1999 S Bascom Ave, Suite 100, Campbell, CA 95008 — 37.4 mi *(not Gilroy at 63.9 mi)* |
| Branch phone | (408) 385-3900 · Gilroy HQ (408) 842-8200 |
| Rail | **TIB (The Independent Bankers Bank)** |

The brief listed `mycommunitycc.com/byyCrDXEpmcO/business` as Pinnacle Gilroy's apply link. **That slug is a different bank.**

**Evidence the Gilroy bank is not TCM:**
- Its own site says so, twice and unambiguously:
  > *"Pinnacle Bank's MasterCard branded Credit Cards are issued by **The Independent Bankers Bank**."* (business/financing.php)
  > *"MasterCard Business Credit Cards are offered through Pinnacle Bank's partner, **The Independent Bankers Bank**."* (business/cashmanagement.php)
- A **45-page crawl** of pinnacle.bank (all nav pages + sitemap) found **zero** occurrences of `mycommunitycc` or `mycommunityccard`.
- Its product name is the TIB "**Preferred Points**" card.

**Evidence for who `byyCrDXEpmcO` really is — Pinnacle Bank of Marshalltown, IOWA (CERT 252, bankpinnacle.us, $313M assets).** There are eight active "Pinnacle Bank" charters. Fetching `images/TCM/byyCrDXEpmcO_logo.png` renders a serif **"Pinnacle"** with a **diagonally-hatched peak** above it and letterspaced **"B A N K"** beneath. That is a pixel-match for the Marshalltown IA mark (`bankpinnacle.us/assets/images/pinnaclebankspot.svg`, which adds the tagline *"Reaching New Heights"*). It is **not** Gilroy's mark (all-caps **"PINNACLE BANK"** on one line with a maroon peak over the "A", colors `#42494E`/`#8E0C3A`), and not Pinnacle Bank of Jasper AL — that one is slug **`YI1LnodPLyKY`**, a black mountain with a green peak, whose site says *"Pinnacle Bank customers have the ability to apply for business and consumer credit cards through our partnership with TCM."*

Likely root cause of the original error: name collision across the eight Pinnacle charters, with the CA bank's CERT attached to an out-of-state bank's slug.

---

## 5. Oak Valley Community Bank — Oakdale, CA · CERT **33457** · 44.6 mi · ❌ **left TCM**

| Field | Value |
|---|---|
| Total deposits | $1,781,504K |
| Total assets | $2,009,991K |
| Nearest branch | **1034 N Central Ave, Tracy, CA 95376** — 44.6 mi *(not Oakdale at 76.1 mi)* |
| Branch phone | **(209) 834-3340** |
| Business RM phone | **Kim Parco, VP Commercial Banking — (209) 834-3347**; Dan Greene, VP Branch Manager (209) 834-3349; general 866-844-7500 |
| Business-card page | https://www.ovcb.com/creditcards/ → /creditcards/business-cards |
| How to apply | **MeridianLink**: `https://app.consumer.meridianlink.com/apply.aspx?lenderref=oakvalleycb_temp&list=CCBLST` |
| Products | Visa Business · Visa Signature Business (self-issued, ScoreCard rewards) |

**Two corrections.**

1. **CERT was wrong.** The brief's 19608 is **The Park Bank, Madison WI** ($1.53B, CERT 19608). Oak Valley Community Bank is **CERT 33457**.
2. **It is no longer a TCM bank — and the prior "TCM-serviced, branch-only apply" read is now stale.** The old `/commerical/loans/credit-cards/` URL 404s; the live page at `ovcb.com/creditcards/` leads with:

   > *"**Big News — OVCB Credit Cards Are Here!** You can now apply for a credit card **issued directly by Oak Valley Community Bank**, featuring competitive rates, valuable rewards, and the local service you know and trust."*
   > *"Ready to keep your card local? Learn more & make the switch today!"*

   TCM now appears **only as legacy portfolio servicing**:
   > *"Have a **TCM-issued** OVCB credit card? Continue managing your account here: TCM Credit Card Access | Manage cRewards"*
   > *"To manage your OVCB credit card **issued by TCM Bank**, click here."*

   New applications route to **MeridianLink**; rewards moved from cRewards to **ScoreCard**. There is no mycommunitycc storefront for this bank, and there is no branch-only TCM path either — the "make the switch" language is an active migration off TCM.

---

## Hunt for additional Bay Area / NorCal TCM banks

**Method.** Pulled all **116 active CA-chartered banks** from the FDIC and filtered to the 18 Bay Area / near-Central-Valley counties → **33 banks**. Then a two-pass automated crawl of each bank's site (homepage + sitemap + up to 45 pages, prioritizing card/business/commercial URLs) grepping for rail fingerprints:

| Rail | Fingerprint |
|---|---|
| **TCM** | `mycommunitycc.com`, `mycommunityccard.com`, `crewardscard.com`, `tcmbank.com`, `800-883-0131` |
| TIB | `cardaccount.net`, "Independent Bankers Bank" |
| Elan | `myaccountaccess.com`, `creditcardlearnmore.com`, `mycardapply.com` |
| Bankers' Bank | `lp.applycommunitycard.com`, `*.yourcommunitycard.com`, `mkdecision` |

I verified that the county filter dropped **no** Bay Area bank (all 83 excluded charters are SoCal or far-north), and separately swept 8 additional NorCal banks with Bay Area reach.

### Result: exactly one new TCM bank — Tri Counties (personal only)

| Bank | County | Rail found |
|---|---|---|
| **Metropolitan Bank** (Oakland) | Alameda | **TCM** ✅ |
| **BAC Community Bank** | San Joaquin | **TCM** ✅ |
| **Tri Counties Bank** (Chico) | Butte | **TCM — personal only** 🆕 |
| Oak Valley Community Bank | Stanislaus | TCM legacy servicing only (migrated off) |
| Mechanics Bank, Bank of Marin, Bank of San Francisco, Bank of Stockton, First Northern Bank of Dixon, Poppy Bank, Exchange Bank, First Federal S&L of San Rafael, Golden Valley Bank, River Valley Community Bank, Savings Bank of Mendocino County | — | **Elan** |
| Gateway Bank FSB (Oakland), Pinnacle Bank (Gilroy), Plumas Bank, Redwood Capital Bank | — | **TIB** |
| Fremont Bank, California Pacific Bank, Summit Bank, Beneficial State Bank, Pacific Coast Bankers' Bank, United Business Bank, Monterey County Bank, Five Star Bank, River City Bank, Bank of the Orient, Mission National Bank, Beacon Business Bank, Farmers & Merchants Bank of Central CA, Avidbank, Altos Bank, West Coast Community Bank, Summit State Bank | — | no card rail detected (45-page deep crawl each) |
| Westamerica Bank, Pacific Valley Bank | Marin / Monterey | **not determined** — sites return 403/307 to automated clients |

**No Bankers' Bank (`lp.applycommunitycard.com` / `yourcommunitycard.com`) rail appears anywhere in NorCal**, consistent with the prior finding that those map to tenant `2471`/bbow, not TCM.

### Verification techniques worth reusing

- **Tenant routing table** — `mycommunitycc.com/chunk-*.js` holds CreditSnap's live domain→`institutionId` map. Authoritative for rail attribution.
- **Slug → bank identification** — `https://creditsnap-public.s3.amazonaws.com/images/TCM/<slug>_logo.png` is public and returns the bank's actual wordmark. This is what settled the Pinnacle mix-up, and it is the reliable way to confirm a slug belongs to the bank you think it does.
- **Product lineup probe** — `.../images/TCM/<slug>_<PRODUCT_CODE>.png` (codes `VISA_SIGNATURE`, `VISA_PLATINUM_REWARDS`, `VISA_PLATINUM_EDITION`, `VISA_PLATINUM_CASH_REWARDS`, `VISA_BUSINESS_EDITION`, `VISA_BUSINESS_REWARDS`, `VISA_BUSINESS_CASH_REWARDS`). 200 vs 404 reveals whether a bank has a **business** TCM program — this is how Tri Counties' personal-only status was confirmed independently of its marketing copy.
- **Beware JS exit-link arrays.** Tri Counties' business page matches a naive `mycommunitycc` grep purely via an exclusion list. Always confirm the match is inside an `href`, and pair it with an issuer disclosure.

### Limits of this sweep
- Two banks (Westamerica, Pacific Valley) block automated fetches and were not classified.
- Coverage is CA-chartered banks; out-of-state charters with Bay Area branches were not enumerated beyond the 8 NorCal additions.
- The CreditSnap slug-resolution API (`prod-api-elb2.creditsnap.com/csb2b/lp/lender/TCM/TCM/<slug>`) requires OAuth and returns 401 unauthenticated; S3 bucket listing is also denied (403). Neither was pursued — all findings rest on public bank websites and individually-addressed public assets.

---

## Bottom line

- For a **business** credit card on the TCM rail near Alameda there are **two** live options: **Metropolitan Bank at 2.5 mi** (250 E 18th St, Oakland — apply at `mycommunitycc.com/FROlvrV1uR72/business`) and **BAC Community Bank at 17.6 mi** (Concord — apply at `mycommunitycc.com/2f497f80fb2c/business/`).
- **Metropolitan Bank is TCM, definitively** — the Elan/mbonlineportal.com lead was a dead domain with no DNS record.
- **Pinnacle Bank (Gilroy) and Oak Valley must be removed** from the TCM business-card list: Gilroy is TIB and never had the slug attributed to it; Oak Valley actively migrated off TCM to self-issuance.
- **Tri Counties Bank is a genuine new TCM find** at 8.9 mi and $9.9B in assets, but only for **personal** cards.
