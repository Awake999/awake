# EWS / ChexSystems Mapping Report — v6 (EWS-CHEX agent)

Date: 2026-06-10 · Scope: top-60 Rec Rank + all N/M rows of `v5_funding_table.csv` (213 rows mapped) · ADD-ONLY: existing cells preserved in columns 3–4 of the CSV; new determinations in columns 5–8.

Output: `out/ews_chex_mapping.csv` — 213 rows; **57 rows with a Chex or EWS determination; 29 rows carry NEW or UPGRADED data vs the existing table cells.**

## 1. Method

1. **Parsed local DoC docs.** `docs_D5.md` (cleaned DoC ChexSystems pull list, page updated 2025-08-07, + EWS appendix) was used as the primary Chex lookup. `docs_D3.md` (raw scrape of DoC "Do/Don't Pull Early Warning Services", page dated 2016-10-21 with 227 comments through **2026-05-22**) supplied EWS pull AND report DPs — the comment stream is far richer than the page body. `docs_D4.md` is base64-image scaffolding (comment avatars) with no usable text and was discarded.
2. **Key comment DPs mined from D3** (all on https://www.doctorofcredit.com/banks-credit-unions-dodont-pull-early-warning-services/):
   - **Dealgamer 2026-05-22 (#2326911)** — three lists from a fresh EWS report pull: (a) *reports ACH transactions*: Citizens, Ally, Amex Checking, BofA, Bethpage, BMO, CapOne (incl. balance "at all times"), Citibank, Delta Community, Fifth Third, First Horizon, Chase (incl. balance), E*Trade, Navy Fed, PNC (incl. balance), Regions, Synovus, TD, Truist (incl. balance), US Bank, Wells Fargo (incl. balance), Wings; (b) *does an EWS inquiry*: Truist, Navy Fed, Fifth Third, Regions, BofA, Wells, Delta Community, Citi (incl. Retail), SoFi, LendingClub (GIACT), **US Bank & Elan**, Schwab (GIACT), PNC, Amex, Chase, TBK, Discover; (c) ***doesn't report and no inquiry***: Seacoast, Robinhood, Chartway, Chime, Bask, Relay, Current, SouthState, Varo, CIT, Union B&T, Trustco, Sunward, Canyon View, **Skyla**, PSECU, **Baxter Credit Union**, **Grasshopper**, **Community America**, Addition Financial, Onpath, Revolut, et al.
   - **Gadget 2022-11-20 (#1492418)** — banks that REPORT new accounts/activity to EWS: incl. **First Citizens, MidFirst, TIAA (EverBank), Comerica**, BMO Harris, M&T, Huntington, Desert Financial, Fidelity, Mountain America, VyStar.
   - **Davis 2021-05-26 (#1196492)** — banks that PULLED his EWS: **Wescom (sav+chk), LBS Financial, Orange County CU, Comerica, First Foundation**, Chase (pers+biz), KeyBank, Citibank, CapOne, HSBC, US Bank, Navy Fed, PNC, CFG.
   - **Ampersand 2018-08-15 (#629661)** — CCCU/AdelFi opened with NO EWS inquiry; **Jay 2018-08-10 (#628472)** — PNC in-branch denial letter citing EWS; **Gadget 2022-12-26 (#1518872)** — "other than PNC, there are not many EWS-sensitive banks"; **CGID 2016-10-21 (#308348)** — Tech CU pulls only Chex, not EWS; **CB 2024-03-27 (#1820901)** — Truist hit EWS twice for one app; TD reports w/o inquiry.
3. **Fetched the DoC ChexSystems inquiry-sensitivity page** (https://www.doctorofcredit.com/banks-credit-unions-chexsystems-inquiry-sensitive/, fetched 2026-06-10) — resolved many CA rows in one shot: Fremont Bank, SAFE CU, CU SoCal, Bank of Hope, Hanmi, Patelco, Wescom, Provident CU, California CU, Premier America, HomeStreet, First Tech, MidFirst, Valley National, NYCB/Flagstar.
4. **Targeted web searches** (2026-06-10) for top-60 institutions not covered: America First CU (Crediful, updated 2025-10-21 — pulls), Kinecta (own dispute form PDF + myFICO 6588582 — pulls & reports), Tri Counties (own FAQ — VERIFIED soft Chex inquiry), Patelco (American Banker 2004 vendor adoption — VERIFIED), East West (Crediful — pulls), Logix (secondary sites — pulls, lenient), Cathay (one weak undated forum no-Chex claim). No-data after search: Firefighters First, First Bank (MO), Redwood CU, Enterprise B&T, Citizens Business Bank, Preferred Bank, F&M Long Beach, Montecito, Mission Valley, and the small SoCal business banks (HCN, American Plus, Infinity, GBC, Mega, Home Bank of CA, Icon, Community West, FFB) → **UNKNOWN, never guessed**.
5. **Grading:** VERIFIED = bank's own disclosure/document or vendor-adoption press; DOC-LIST = DoC crowd lists; COMMUNITY-DP = dated forum/comment data point; UNKNOWN = no evidence.

## 2. Gold list (no Chex AND no EWS at opening)

**Strict gold (evidence on both axes): none in the table.** No institution we map has positive evidence of *both* no-Chex and no-EWS. Honest tiering instead:

| Tier | Institution (rank) | Evidence | Gap |
|---|---|---|---|
| Gold candidate | **Baxter CU / BCU (71)** | EWS: no report + no inquiry (DoC comment 2026-05-22, #2326911) | Chex unknown — one verification call from Diamond tier |
| Gold candidate | **Skyla CU (79)** | EWS: no report + no inquiry (same 2026-05-22 DP) | Chex unknown |
| Gold candidate (weak) | **Cathay Bank (49)** | One undated forum claim of no Chex (bankinusa.com) | EWS unknown; claim weak — verify in branch |
| EWS-clean, Chex via legacy | **CommunityAmerica (27)** | EWS: no report + no inquiry (2026-05-22) | legacy UNIFY pulled Chex ×5 (not sensitive) |
| Chex-free but EWS-heavy (NOT gold) | Chase (1), BofA (2), Wells (3) | DoC Chex no-pull | all pull AND report to EWS incl. balances (2026-05-22) — they spend EWS budget, not Chex budget |

Diamond/Platinum build note: the table's many tiny SoCal business banks (Mega, GBC, Home Bank of CA, Icon, Beach Cities, etc.) are UNKNOWN — absence of data is **not** evidence of no-pull; manual-onboarding banks often run QualiFile quietly. Each needs one banker question: "Do you screen deposit applicants through ChexSystems or Early Warning?"

## 3. Notable flips / conflicts vs existing cells

- **BMO (9):** existing EWS cell = N/M → **reports ACH to EWS** (2026-05-22 DP; also Gadget 2022 list; D5 appendix "EWS in addition to Chex"). No EWS-inquiry DP. Chex yes but NOT inquiry-sensitive.
- **First Citizens (18):** EWS N/M → **reports to EWS** (Gadget 2022-11-20). Chex-tolerant until ~32 inquiries/12mo.
- **MidFirst (38):** EWS N/M → **reports to EWS**; Chex confirmed SENSITIVE (denied 7/12).
- **EverBank (83):** EWS N/M → **reports to EWS** (as TIAA, Gadget 2022-11-20).
- **Comerica (48):** N/M both → Chex pull (not sensitive, 80+/24 OK) + **EWS pull AND report** (2021/2022/2024 DPs).
- **Wescom (146), LBS Financial (159), Orange County's CU (35):** N/M EWS → **EWS pull** DPs (Davis 2021-05-26) — SoCal CUs that hit BOTH bureaus.
- **CU SoCal (152):** N/M → **most Chex-inquiry-sensitive find of the run: denied at 3 inquiries/6 months.**
- **Fremont Bank (23):** N/M → Chex pull + sensitive (declined 10/12).
- **Bank of Hope (107):** N/M → Chex pull + sensitive ("they want less than 5"/12mo).
- **PNC (5):** confirms project-log "EWS-not-Chex" — in-branch EWS denial letter DP + Gadget calling PNC the main EWS-sensitive bank; Chex DPs mixed (8y/23n). The binding constraint at PNC is the **EWS** inquiry count, which **cannot be frozen**.
- **Grasshopper:** no newer Chex DPs found (D5 shows 1-yes/1-no); project-log flip (now pulls) stands. EWS-clean per 2026-05-22 DP.
- **Banner (39), California CU (24), Premier America (15):** re-verified; existing sensitive/auto-deny cells stand (no newer contradicting DPs).
- **City National Bank (41):** Chex DPs exist but possibly contaminated by City National Bank WV (commenter: "CNB WV pulls Chex, no EWS") — flagged ambiguous.
- **Pinnacle Bank Gilroy (126), CIBC Trust (176), SBI California (76):** DoC entries likely refer to same-named other institutions — flagged, not blindly applied.

## 4. Sequencing strategy (Chex/EWS throttle management)

1. **Open the Chex-sensitive accounts FIRST, while the Chex file is empty:** CU SoCal (3/6mo limit — first or never), Premier America (3/90d), Bank of Hope (<5/12), MidFirst (7/12), Fremont (10/12), California CU, Patelco, Provident CU, SAFE CU, Wescom, Banner (QualiFile auto-deny). One sequencing window supports roughly 2–3 of these before thresholds start tripping; prioritize by funding value.
2. **Middle of sequence — Chex-pullers that tolerate inquiries:** Comerica (80+/24 OK), Hanmi (10+/12 OK), Axos (50+/12 OK), Tech CU (25+/12 OK), US Bank, BMO, Citi (approves with frozen Chex), Tri Counties (soft Chex), State Bank of India, City National. These barely consume risk.
3. **Open the EWS-only big banks LAST or anytime:** Chase, BofA, Wells Fargo don't touch Chex; their EWS inquiries land on a register most banks don't deny on — **except PNC**. Open PNC *before* stacking Chase/BofA/Wells/Citi EWS inquiries (EWS keeps ~1 year of inquiries and **cannot be frozen**).
4. **Freeze strategy:** a ChexSystems security freeze blocks pulls at Chex-only banks — some auto-deny on frozen file, but Citi approves frozen (2026 DPs) and Andrews-type approvals exist; thaw selectively for the sensitive openings in step 1. The freeze does **nothing** at EWS banks (Chase/BofA/Wells/PNC/US Bank/Citi/Amex/CapOne/Truist). MyIDCare monitors EWS (imperfectly), not Chex.
5. **Business vs personal:** several DPs show business accounts behaving differently — Chase biz no-pull (×4), Truist biz in-branch skipped Chex (existing cell), Citizens biz often skips owner Chex, BMO biz reports to *business* Chex (separate file, 2024-05-05 #1840439). Where funding needs a deposit account, prefer the business-account path at these.
6. **EWS-clean parking:** Baxter/BCU, Skyla, CommunityAmerica (and Grasshopper for biz) leave no EWS footprint — use them for operating/landing accounts mid-sequence without spending either budget (confirm BCU/Skyla Chex first).

## 5. Source index

- DoC ChexSystems pull list (page updated 2025-08-07, via docs_D5.md): https://www.doctorofcredit.com/banks-credit-unions-dodont-pull-chexsystems/
- DoC EWS pull list + comments through 2026-05-22 (docs_D3.md): https://www.doctorofcredit.com/banks-credit-unions-dodont-pull-early-warning-services/
- DoC Chex inquiry-sensitive list (fetched 2026-06-10): https://www.doctorofcredit.com/banks-credit-unions-chexsystems-inquiry-sensitive/
- Tri Counties Bank FAQ (fetched 2026-06-10): https://www.tcbk.com/personal/online-accounts-personal
- Kinecta consumer-reporting dispute form (ChexSystems named): https://www.kinecta.org/Kinecta/media/Kinecta/Forms/Fraud%20and%20Theft%20and%20Dispute%20Forms/consumer_credit_reporting_dispute.pdf
- Crediful: America First CU (upd. 2025-10-21): https://www.crediful.com/chexsystems/america-first-credit-union/ · East West Bank: https://www.crediful.com/chexsystems/east-west-bank/
- American Banker (2004, Patelco adopts ChexSystems): https://www.americanbanker.com/news/authentication-patelco-chooses-chexsystems-to-combat-id-fraud
- myFICO "CUs that pull ChexSystems for membership" (Kinecta DP): https://ficoforums.myfico.com/t5/Personal-Finance/CU-s-that-pull-ChexSystems-for-membership-IME/td-p/6588582
- TheCreditPeople (Logix, undated/weak): https://www.thecreditpeople.com/bureaus/which-credit-unions-really-do-not-use-chexsystems
- bankinusa forum (Cathay, undated/weak): http://bankinusa.com/answer/does-anyone-know-any-non-chexsystems-banks-in-los-angeles-ca-399/

Integrity notes: every determination in the CSV carries grade + date + link; UNKNOWN means no evidence found — nothing inferred from absence. DoC sens-page header shows "Last Updated March 29, 2016" but contains DPs from 2020s institutions (Lili, Current, Laurel Road), i.e., it is continuously maintained; treat individual thresholds as undated crowd DPs.
