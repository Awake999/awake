# Bureau Pulls for Business Card / Business LOC Applications (California) — v7

Date: 2026-06-11. Companion data: `bureau_pulls.csv` (same directory).

**Honesty note:** business-card bureau DPs are scarce. Most public datapoints are consumer-card pulls (labeled CONSUMER-PROXY) or aggregate issuer behavior. Where no data exists the verdict is NO-DATA and the action is "ask at application." myFICO forums block direct fetching (HTTP 403), so myFICO evidence below comes from search-indexed thread content; spot-verify before relying on it.

## Mentor's 14 — verdict table

| Institution | Mentor claim | Verdict | Evidence grade | What we found |
|---|---|---|---|---|
| PNC | Experian | AGREES-WEAKLY | CONSUMER-PROXY | WalletHub: cards lean Experian (anecdotal); EQ for deposit products. Consistent with our prior soft-EQ-then-EX-hard-outlier pattern. No CA biz DP. |
| Sunwest Bank | Experian | CONFLICTS (stale) | MENTOR-ONLY | Current card = Torpago-powered "Visionary" commercial card (launched ~2023). Old Elan program (source of the 2015 EX trace) is dead. Mentor's EX claim is legacy data about a product that no longer exists. |
| Tustin Community Bank | Experian | CONFLICTS (no product) | VERIFIED (product absence) | tustin.bank lists only business/professional/CRE loans + cash mgmt. No card product live — confirms our prior DP. Claim untestable. |
| First Citizens Bank | Equifax | AGREES-WEAKLY | COMMUNITY-DP | myFICO ($20k biz CC approval thread): FCB employee says they pull all three for personal — matches our "all-3-blend/EQ" prior. EQ plausible as part of tri-merge. Warning: most search results conflate with Citizens Bank (RI). |
| KeyBank | Equifax | AGREES | CONSUMER-PROXY | Aggregators consistently report KeyBank usually pulls Equifax. No biz-specific CA DP. |
| California Credit Union | Equifax | NO-DATA | MENTOR-ONLY | Nothing public found. Generic note: CA CU shared platforms often TU, which would cut against EQ — unverified. |
| First Western Trust | Equifax | CONFLICTS (Elan = variable) | COMMUNITY-DP | Elan-issued (our prior DP). Elan pulls EX/EQ/TU variably, sometimes multiple bureaus per app — a fixed "EQ" claim is not supportable. |
| Banner Bank | TransUnion | NO-DATA | MENTOR-ONLY | Banner self-issues (not Elan; Banner FCU is a different entity). Zero bureau DPs found. |
| Valley Bank (Valley National) | TransUnion | CONFLICTS (Elan = variable) | COMMUNITY-DP | valley.com card pages run on Elan's mycardapply/cardmanager platform — Elan issuance confirmed; bureau is Elan's variable choice, not fixed TU. |
| BMO | TransUnion | AGREES | COMMUNITY-DP | FairFigure lists BMO biz card TU-only; myFICO BMO business LOC approval DP cites TU FICO8; consumer DPs also TU. Strongest corroboration of the 14. |
| Western Alliance Bank | TransUnion | NO-DATA | MENTOR-ONLY | In-house biz/commercial Visa; zero bureau DPs found. |
| WaFd Bank | TransUnion | NO-DATA | MENTOR-ONLY | No bureau DP; card FAQ silent. Could not confirm or deny the 6/30 application pause from public pages — re-check after 6/30. |
| Los Angeles FCU | TransUnion | NO-DATA | MENTOR-ONLY | Nothing new; our prior TU-membership / EX-card conflict stands. Pull-test candidate. |
| California Bank & Trust | BRANCH VERIFY | AGREES (verify) | UNKNOWN | Confirmed the information vacuum: the bureau question is asked but never answered publicly (Zions/myFICO). Branch verify is correct. |

Scorecard: 4 AGREE (1 strong: BMO), 4 CONFLICT (Sunwest stale-product, Tustin no-product, FWT + Valley Elan-variable), 5 NO-DATA, 1 verify-as-instructed (CB&T).

## Strongest new finds

1. **Elan cluster is bigger than known.** Cathay Bank, Hanmi Bank, and Bank of Hope card programs are Elan-issued (creditor/issuer = Elan Financial Services on their card pages); Valley Bank confirmed via Elan's mycardapply platform; First Western Trust already known. For ALL of these, the bureau is Elan's per-application choice (EX/EQ/TU, sometimes multiple) — any single-bureau claim is unreliable. East West Bank likely fits the pattern but was not explicitly confirmed.
2. **Sunwest's program changed hands.** The card is now a Torpago-powered commercial card (2023+), so the mentor's EX claim — which traces to the dead 2015 Elan program — is stale on two generations of product.
3. **Chase in CA = Experian, high confidence.** DoC state chart CA row: Experian 44 DPs vs Equifax 11, TU 1 (mostly consumer, but Chase CS says biz cards also lean EX).
4. **BMO TU corroborated for business** (FairFigure biz-card list + myFICO business LOC DP) — the single best-supported mentor claim.
5. **Kinecta EX corroborated; SDCCU EX supported** (membership-pull proxy); Premier America EX×2 stands unchallenged.

## Second-priority quick table

| Institution | Best evidence (CA) | Grade |
|---|---|---|
| Chase Ink | Experian (44/56 CA DPs) | COMMUNITY-DP |
| Amex business | Experian | COMMUNITY-DP |
| Bank of America biz | Experian typical | CONSUMER-PROXY |
| Wells Fargo biz | EX or TU (state-dep.) | CONSUMER-PROXY |
| U.S. Bank biz | TU most common (state-dep.) | CONSUMER-PROXY |
| FNBO Business Edition | Experian (HP-CLI DP) | COMMUNITY-DP |
| UMB | EQ or TU (mixed DPs) | COMMUNITY-DP |
| Kinecta | Experian | COMMUNITY-DP |
| SDCCU | Experian (membership proxy) | COMMUNITY-DP |
| Premier America | Experian (prior ×2) | COMMUNITY-DP (prior) |
| Cathay / Hanmi / Bank of Hope | Elan-issued → variable | VERIFIED issuer / variable bureau |
| East West | likely Elan — verify | UNKNOWN |
| Enterprise B&T, Comerica, Stanford FCU, Valley Strong, Wescom, BCU, Skyla | none found | UNKNOWN — ask at application |

## Recommended actions
- **Use as-is:** BMO (TU), Chase Ink (EX), Amex (EX), Kinecta (EX), FNBO (EX).
- **Ask banker / branch verify:** CB&T, Western Alliance, Banner, KeyBank biz, First Citizens (tri-merge vs single), PNC, Sunwest (Torpago underwriting), all UNKNOWNs.
- **Pull-test candidates:** LAFCU (cheap membership pull resolves the TU/EX conflict), any Elan program (accept bureau roulette).
- **Re-check after 2026-06-30:** WaFd.
