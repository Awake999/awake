# Verification-Systems Dataset — iBankNet-CA (secondary bureaus)

Built 2026-06-12 by SECONDARY-BUREAUS agent. Companion CSV: `secondary_bureaus.csv` (230 institutions, one row each).
Generator: `/home/user/awake/research/ibanknet/build_secondary_bureaus.py` (re-runnable).

## Scheme

Four separate determinations per institution, each cell = finding + [grade; date], with a link column per cell:

| Column | Covers |
|---|---|
| ChexSystems | Chex pulls/reports, incl. QualiFile (a ChexSystems/FIS scoring product) |
| EWS | Early Warning Services inquiries/reporting |
| LexisNexis_SageStream | LexisNexis Risk Solutions, incl. SageStream (ex-ID Analytics/IDA, absorbed into LexisNexis) |
| Other_secondary | Anything else named: ARS, Innovis, TeleCheck/Certegy, Clarity, GIACT, Equifax-at-join, etc. |

Grades: **VERIFIED** (institution's own disclosure names the vendor) > **DOC-LIST** (Doctor of Credit resource page/article) > **COMMUNITY-DP** (forum/comment datapoints) > **Generic-CRA-clause (vendor unnamed)** (own agreement authorizes consumer-report checks but names nobody — distinct, useful signal) > **VERIFIED-absence** (own full agreement read; vendor not named) > **UNKNOWN** (never guessed).

## Counts (230 rows)

| Column | Known (any grade) | UNKNOWN |
|---|---|---|
| ChexSystems | 92 (incl. 12+ VERIFIED-own-doc, ~41 DOC-LIST, 2 Generic-CRA-only) | 138 |
| EWS | 61 | 169 |
| LexisNexis_SageStream | 6 | 224 |
| Other_secondary | 6 | 224 |

Sources consolidated: v6 `ews_chex_mapping.csv` (213 rows), v7 `chex_socal_banks.csv` (16, business-account angle), v7 `chex_socal_cus.csv` (19 CUs/fintechs), v6 `docs_D3-D5` DoC dumps, v7 deliverables; plus a 2026-06-12 targeted web sweep (East West, Cathay, Mechanics, Golden 1, SchoolsFirst, Axos, Pacific Premier, Westamerica, Umpqua/Columbia, CalCoast, plus LexisNexis/SageStream checks).

## Notable LexisNexis / other-vendor findings

1. **SYSTEMIC — QualiFile embeds LexisNexis.** Per DoC: banks using the Chex **QualiFile score** indirectly pull **LexisNexis**; a frozen LexisNexis file produces an "abnormal Chex score" and the bank auto-declines "citing frozen Chex." Practical rule: before applying anywhere known/suspected to use a Chex *score* (vs. raw report) — e.g. **Banner Bank** (QualiFile auto-deny, no override) — make sure LexisNexis is THAWED, the opposite of the U.S. Bank playbook.
2. **U.S. Bank** — soft-pulls **SageStream (now LexisNexis Risk Solutions) + ARS (Advanced Resolution Services, CBC/Innovis-affiliated, Independence OH)** on credit apps; they only add deny-reasons, so freeze both first (DoC article since 2015; project fact reconfirmed 2026-06). Approves when those reports are frozen/unavailable.
3. **Bank of America** — uses **SageStream "Credit Optics"** score data in credit decisions (DoC 2016-08-08); unlikely to deny solely for a frozen SageStream unless traditional file is thin.
4. **Regions Bank** — **online** applications pull LexisNexis (frozen LN ⇒ denial DP 2022-02-27); **in-branch** opening did not pull. DoC commenter: "a lot of banks pull LexisNexis, at least with online opening" — generalizes to most online openers via identity-verification rails.
5. **GIACT Services (Refinitiv/LSEG)** — posts EWS inquiries as "<bank> via GIACT SERVICES" for external-account **linking** (Schwab, SoFi, LendingClub, Upgrade, Varo, Webull, PayNearMe, Ingo, Personal Capital DPs in docs_D3). Not new-account screening — don't misread these on an EWS report.
6. **Certegy** — appears on EWS reports via **Target RedCard** ("TARGET via CERTEGY WELLS"); merchant-side check-risk CRA, not seen as a CA bank account-opening screen.
7. **Golden 1 CU** — hard **Equifax** pull just to join (recorded under Other), plus Chex inquiry-sensitive.
8. **No CA institution found naming Innovis, TeleCheck, or Clarity** in any deposit disclosure or DP reviewed (TeleCheck/Certegy are merchant-side; Innovis appears only via the ARS affiliation).

## Phase 2 upgrades (new vs. Phase 1)

- **Mechanics Bank** — Chex **VERIFIED** own Personal Account Agreement (doc dated 2026-03-23): "new accounts are subject to verification through ChexSystems... may be declined based in whole or in part." EWS/LN not named (20-pg read).
- **SchoolsFirst FCU** — Chex **VERIFIED** own product pages: "ChexSystems verification... required" (Free Checking, Investment Checking, Liquid Advantage MM).
- **Axos Bank** — Chex upgraded to **VERIFIED** own FAQ: cannot process application with Chex freeze in place — personal **and business**.
- **Golden 1 CU** — Chex Yes + inquiry-sensitive (DOC-LIST).
- **East West Bank** — own 60-pg Deposit Agreement (eff. 2024-06-01): **Generic-CRA-clause** ("check or credit reporting agency", vendor unnamed); Chex Yes stands via Crediful.
- **Cathay Bank** — own 40-pg consumer+business agreement: **Generic-CRA-clause** (§50 "Use of Consumer Reporting Agencies", vendor unnamed). Still a high-value verify-by-phone target (weak forum claim of NO Chex).
- **Pacific Premier, Westamerica, Umpqua (Columbia), California Coast CU** — searched 2026-06-12, nothing public naming a vendor: all four columns UNKNOWN.

## Caveats

- LexisNexis "Not named in own agreement [VERIFIED-absence]" ≠ no LexisNexis use: identity-verification pulls usually live outside deposit agreements (see systemic finding #1 and #4).
- v6/v7 inherited grades and DP dates are preserved inside each cell; name-twin warnings (City National WV, Citizens RI, Pinnacle TN, SBI NY, SunWest FCU AZ) carried through in Notes.
- Other_secondary for U.S. Bank/BofA/Golden 1 records credit-side bureau use, flagged as such — kept per the 4-column scheme since these soft pulls can deny.
