# Ad Forensics — what changed, when, and did it break the ads (2026-08-30)
*Alan's ask, verbatim: "our ads are doing fine up until this past month, and they were horrible... I did have Claude change something, so backtrack the date... see if there's any type of synchronicity there."*

## VERDICT (scan-ready)
**YES — strong synchronicity, mechanism confirmed, sole-cause NOT proven.**
On **Aug 10**, the creative on **all 12 active ads** was replaced (Meta activity log: 12 × "Ad updated" old_creative→new_creative, actor "Alan Nguyen" — the identity the Claude connector acts under; new creatives carry machine-generated `2026-08-10-<hash>` names). This was the 8/10 Claude-session Meta-URL/UTM work. Effect per Meta's own log: every ad went Active → Pending Process → Pending Review → re-Activated, and **learning was reset** — the log stamps `last_learning_exit` ≈ Aug 4, i.e. the ads had JUST stabilized out of learning six days before the swap.

## The performance series (weekly, both active campaigns; source: Meta insights 7/28–8/30)
| Week | Prof/BizOwners CTR / CPC | Medical v2 CTR / CPC |
|---|---|---|
| Jul 28–Aug 3 (launch/learning) | 2.43% / $6.02 | 1.84% / $15.97 |
| **Aug 4–10 (out of learning — BEST week)** | **2.75% / $5.84** | **2.17% / $11.77** |
| **Aug 11–17 (first week after the 8/10 swap)** | 2.38% / $6.18 | **1.70% / $16.59 (worst week, CPC +41%)** |
| Aug 18–24 | 2.00% / $7.20 (+23% vs peak) | 2.28% / $9.20 (recovered) |
| Aug 25–30 | 2.28% / $6.36 | 2.01% / $13.18 |

Both campaigns peaked in exactly the week before the swap and degraded in exactly the week after. Medical v2 took the harder hit and stayed choppy; Prof/BizOwners partially recovered.

## Honest boundaries [labels]
- [V] The 8/10 all-ads creative swap happened, reset learning, and forced re-review — Meta's log, not inference.
- [V] The best-to-worst inflection lands on the swap week for both campaigns.
- [D] NOT proven as sole cause: creative fatigue, auction seasonality, and Medical v2's pre-existing high CPL are live alternatives; Prof/BizOwners' later recovery cuts against a permanent break.
- [V] The trade the 8/10 change bought: the UTMs from that swap are WHY attribution now works — 100 contacts with utm_source, 73/83 tracker rows Verified, 21 lost leads recovered. Cost: one learning reset at the worst possible moment.

## MEDIA LAW (adopted, SOP-bound, per Alan: "find an alternative way... without breaking the ads")
**Never edit the creative/URL of a DELIVERING ad again — no exceptions.** Tracking parameters ride at CREATION TIME only: Sep 1 A/B new ads (Jacob tags the DM arm; SCIO arm gets params at build), and any future change ships as a NEW ad added beside the running one, original untouched until the new one exits learning.
