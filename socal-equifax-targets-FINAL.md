# SoCal Equifax / Card Assets Targets — FINAL (2026-07-20)

Lawful public-record research: SoCal banks offering business credit cards, identifying
Equifax-pull lanes. Card Assets = agent issuer whose clients all pull Equifax.
Method: full enumeration of the Card Assets platform + FDIC BankFind universe + bureau checks.

## CONFIRMED / LEAD CARD ASSETS (EQUIFAX) LANES — LA/OC
| Bank | CA Index | Deposits | Application | Status |
|------|----------|---------:|-------------|--------|
| First Foundation Bank (Irvine) | 0350 | $8.78B | app.thecardservicescenter.com/SelectionBusiness/index/0350 | CONFIRMED live. ⚠️ Merged into Sunflower Bank 4/1/26 — legacy lane may migrate; apply before it closes |
| Hanmi Bank (Los Angeles) | 0092 | $6.80B | app.thecardservicescenter.com/SelectionBusiness/index/0092 | NEW LEAD. Application page is live (active I-Accept/Continue). BUT Hanmi's current marketed business cards route to Synchrony (mycardapply.com/synindex) and mentor intel marked Hanmi=Elan. Likely a legacy Card Assets program still reachable. CALL Hanmi business banking to confirm 0092 still originates before relying on it. If live, it pulls Equifax. |

## CALIFORNIA CARD ASSETS — CENTRAL COAST (widen-scope only)
| Bank | CA Index | Note |
|------|----------|------|
| Santa Barbara Community Bank | 2002 | Division of Ojai Community Bank (Santa Barbara) |
| Ojai Community Bank | 2250 | Ventura County |

## DEFINITIVE NEGATIVE
Full Card Assets platform enumerated twice (75 client institutions nationally). Cross-checked
vs FDIC's complete LA/OC HQ universe (53 banks). The ONLY LA/OC Card Assets/Equifax lanes are
**Hanmi (0092)** and **First Foundation (0350)**. All other LA/OC banks use Elan / TCM /
Synchrony / self-issued Visa, or offer no business card.

## FDIC LA/OC UNIVERSE — 18 BANKS NOT IN PRIOR SWEEPS (none are Card Assets)
CTBC Bank Corp USA ($4.5B), Mizrahi Tefahot Bank ($4.4B), State Bank of India CA ($1.19B),
Malaga Bank FSB ($941M), EverTrust Bank ($840M), American Plus Bank ($717M), First Commercial
Bank USA ($670M), Mission Valley Bank ($632M), New OMNI Bank ($371M), Community Commerce Bank
($312M), American Continental Bank ($311M), Universal Bank ($279M), First Credit Bank ($258M),
United Pacific Bank ($153M), Bank of Whittier ($131M); OC: First American Trust FSB ($7.8B),
Liberty Bank NA, California International Bank, Capital Bank & Trust.
→ Optional next step: check whether any self-underwrites a card that pulls Equifax (rare —
   self-UW SoCal skews Experian/TransUnion: LAFCU=TU, Kinecta=EX).

## BUREAU REALITY (Phase C)
Equifax is uncommon among SoCal self-underwriters. Confirmed: LAFCU = TransUnion only;
Kinecta MyPro = Experian. This is why Card Assets (guaranteed Equifax) is the primary clean
EQ lane in the region.

## METHOD NOTES (reproducible)
- Card Assets client = live page at app.thecardservicescenter.com/SelectionBusiness/index/####
- Each index loads a bank-specific logo at cdn2.thecardservicescenter.com/images/CUE/Logos/<ts>.png
- Enumerate indexes 1..2300, extract logo, OCR (tesseract) → bank name; filter to CA.
- FDIC universe: api.fdic.gov/banks/institutions?filters=STALP:CA AND ACTIVE:1 AND COUNTY:"Los Angeles"|"Orange"
- Coverage caveat: sweeps resolved 72–75 readable logos; some index ranges returned blank.
  CA set stable across two independent sweeps.

## NEXT STEPS
1. Call Hanmi business banking — confirm index/0092 Card Assets program is still live (highest value).
2. First Foundation index/0350 — apply before Sunflower migration if pursuing.
3. Optional: self-underwrite bureau check on the 18 new FDIC banks.
