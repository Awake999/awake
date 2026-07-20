# Card Assets Bank Search — Working Checklist

Shared source of truth so we stay on the same page. Updated 2026-07-20.

## THE MISSION (what we're supposed to be doing)

Find banks in the **Southern California area (LA + Orange County)** that issue
**business credit cards underwritten by Card Assets** (agent issuer known to pull
**Equifax**). Output a list ranked **most → least deposits**, with for each bank:
name, business product name, application link, whether you can apply online, and
any other apply details. Purpose: apply for business credit against the Equifax
profile — legitimate, honest applications as the real business.

## SOURCES I WAS ASKED TO CHECK

- [x] **Our existing lists / Google Sheets** (SoCal deposit workbook) — USED as the candidate list + deposit rankings
- [ ] **iBankNet.com** — NOT freshly searched this session (relied on prior workbook export instead)
- [ ] **FDIC.gov (BankFind)** — NOT searched. This is the authoritative census; biggest gap
- [ ] **Bank Branch Locator** — NOT searched (misses out-of-area banks with LA/OC branches)
- [ ] **ICBA directory** — NOT searched (community-bank census = Card Assets' natural base)

## WHAT I ACTUALLY DID

- [x] Pulled 50 candidate institutions from the existing SoCal deposit workbook
- [x] Live-checked all 50 for the Card Assets tell (34 banks + 16 credit unions)
- [x] Confirmed the Card Assets fingerprint (thecardservicescenter.com, 24-7cardaccess.com,
      cardaccount.net, 5 Mastercard product names, issuer = First Arkansas Bank & Trust)
- [x] **CONFIRMED: First Foundation Bank** (Irvine, $8.78B) — live app at index/0350
- [x] **LIKELY: Partners Bank of California** (Mission Viejo, $482M) — needs a call to confirm
- [x] Flagged 2 call-to-confirm (Genesis Bank, Beach Cities Commercial)
- [x] Mapped every other institution to its real underwriter (Elan / Synchrony / TCM / Visa / none)
- [x] Wrote deliverable `socal-card-assets-banks.md`, committed, opened PR #1

## WHAT'S NOT DONE (the gaps)

- [ ] Build the COMPLETE SoCal bank universe from FDIC BankFind (est. 30–60 banks never checked)
- [ ] Add out-of-area banks with LA/OC branches (Bank Branch Locator)
- [ ] Add ICBA community-bank members
- [ ] Refresh deposits from a current source (workbook is the 2026-06-10 sweep)
- [ ] Reverse-enumerate Card Assets `index/####` client numbers, filter to SoCal (highest yield)
- [ ] Verify every newly-found bank + merge into the ranked deliverable

## THE PLAN (phased)

**Phase 1 — Build the full universe** (effort: low; pure retrieval)
1. FDIC BankFind: all banks HQ'd or branched in LA + Orange County → names + deposits
2. Cross-check Bank Branch Locator (out-of-area branches) + ICBA (community banks)
3. Diff against the 50 already checked → "never-checked" list

**Phase 2 — Reverse enumeration** (effort: medium; highest yield)
4. Walk `app.thecardservicescenter.com/SelectionBusiness/index/####`, harvest which FI
   each resolves to, keep SoCal hits (finds Card Assets clients directly)

**Phase 3 — Verify + merge** (effort: low–medium; fan-out pattern-match)
5. Live-check each never-checked bank + each Phase 2 SoCal hit for the tells
6. Update ranked list (deposits, product, link, apply-online), push to PR #1

## OPEN DECISIONS FOR YOU

- [ ] Approve the plan / reorder phases?
- [ ] Effort level (my rec: **medium** for the run; researchers can go low individually)
- [ ] Start with Phase 2 (fastest signal) or Phase 1 (completeness first)?
