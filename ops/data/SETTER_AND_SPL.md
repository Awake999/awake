# 📞 SETTER DATA + SPEED TO LEAD — the real numbers (register #130)
*2026-09-01 · Alan: "show me all the setter data and the SPL." Built from raw GHL: [contacts](https://github.com/Awake999/awake/blob/claude/new-session-1ofk4w/ops/archive/ghl/2026-08-30/contacts_2026-08-30.csv) (tags) · [speed_to_lead](https://github.com/Awake999/awake/blob/claude/new-session-1ofk4w/ops/archive/ghl/2026-08-30/speed_to_lead_2026-08-30.csv) · [call logs](https://github.com/Awake999/awake/tree/claude/new-session-1ofk4w/ops/archive/ghl/2026-08-30/raw) (durations). Window = the 38 hand-checked ad leads, Jul 28–Aug 26.*

## ⚠️ CORRECTION FIRST — the "speed to lead ≤1 min" number was wrong
Earlier reports (mine included) said **36 of 38 were first-touched within a minute**. That came from the `speed_to_lead` export, and it is **not a touch at all**: all 38 rows read `minutesToFirstTouch = 0.0` with `firstOutboundType = TYPE_ACTIVITY_OPPORTUNITY` — that is GHL stamping the *opportunity record being created*, not anyone contacting the lead. **Nobody was contacted in under a minute. The metric was measuring itself.**

## ⏱ THE REAL SPEED TO LEAD — first human dial
| | |
|---|---|
| Leads ever dialed | **38 of 38** — every lead was worked |
| **Median time to first dial** | **13.2 hours** |
| Dialed within 1 hour | **9 of 38 (24%)** |
| Dialed within 24 hours | 28 of 38 (74%) |
| Total dials placed | **285** (median 7 per lead) |

## 📊 WHAT ACTUALLY MOVES THE SHOW RATE (booked cohort = 29, showed = 9)
| Cut | n | Showed | Rate |
|---|---|---|---|
| Dialed **1–12 hours** after opt-in | 8 | 4 | **50%** ← the sweet spot |
| Dialed 12–24 hours | 6 | 2 | 33% |
| Dialed within 1 hour | 7 | 2 | 29% |
| Dialed **after 24 hours** | 8 | 1 | **12%** ← the killer |
| **Connected at least once (60s+)** | 21 | 8 | **38%** |
| **Never connected** | 8 | 1 | **12%** |
| Connected 3+ times | 7 | 3 | 43% |
| Has a `triaged` tag | 16 | 7 | **44%** |
| No `triaged` tag | 13 | 2 | **15%** |

**Read it plainly:** speed alone is not the lever — **connection is**. Sub-hour dials show 29%, but 1–12 hour dials show 50%; what separates them is whether anyone ever got the lead on the phone. Waiting past 24 hours is the one thing that reliably kills the booking (12%).

## 🏷 SETTER TAG COVERAGE — the instrument is half-used
| Tag | On the 38 | Note |
|---|---|---|
| `0 - no answer` | 21 | most-used tag |
| `0 lynn - triaged` / `0 apw triaged - yes` | 16 | the useful one — 44% show rate |
| `1 - connected` | 13 | but **21 leads actually connected** — 8 connections never got tagged |
| `0 - unresponsive` | 10 | |
| **`0 lynn - spl - yes`** | **4** | ⚠️ the SPL tag is effectively unused — 10 uses across the entire 259-contact book |
| `1 - qualified` | 3 | Behnad, Jennifer, P Reddy — and **all three turned out unqualified** |

**Tag hygiene problems, named:**
- **9 leads carry `0 - no answer` but the call log shows a real connection** — Robert Schechner, Trent Hamilton, **Jack Kates (7 connections)**, **Connor Robertson (3)**, Ms Terry, John Mazzocchi, Tarlochan Singh, Nick Samara, **Chris Bowers (6)**. The tags understate the work done.
- **`lynn - spl - yes` on 3 booked leads → 0 shows.** As a metric it currently predicts nothing because almost nobody applies it.
- **Karl Krummenacher — the only qualified lead in the window — carries zero setter tags.** The best outcome of the month is invisible to the setter instrument.
- 8 leads got **3 dials or fewer**: Marko Sakren, Jennifer Ulloa, Desi Harmon Sr, Jesse Hopcus, Yeshaya Dank, Stephen Greco, Ed McCullough, David Shepherd. (Jennifer, Jesse and Yeshaya still showed — few dials but real connections.)

## 👤 BOOKED LEADS — every one, sorted by how fast a human dialed
| | Person | 1st dial | Dials | Connected | Setter tags [V] |
|---|---|---|---|---|---|
| ❌ [Stephen Greco](https://app.gohighlevel.com/v2/location/WFkoNzKa9J9PxhngsLfl/contacts/detail/FWmJO9pOj3dI7eFlCUtO) | 0.0h | 2 | **2** | `0 lynn - spl - yes` `0 lynn - triaged` `1 - connected` |
| ❌ [Myla Maheedhar](https://app.gohighlevel.com/v2/location/WFkoNzKa9J9PxhngsLfl/contacts/detail/hDKXjL3QDuda9XfRT7lv) | 0.0h | 9 | **1** | `0 lynn - spl - yes` `1 - connected` `0 lynn - triaged` `0 no show` |
| ❌ [Robert Schechner](https://app.gohighlevel.com/v2/location/WFkoNzKa9J9PxhngsLfl/contacts/detail/VD04ZTrHJvQACmuby8KF) | 0.0h | 9 | **1** | `0 lynn - spl - yes` `0 - no answer` `1 - connected` `0 lynn - triaged` `0 no show` |
| ✅ [Karl Krummenacher](https://app.gohighlevel.com/v2/location/WFkoNzKa9J9PxhngsLfl/contacts/detail/H4aNUi4T4zClFs5EAJtP) | 0.0h | 7 | **1** | *(none)* |
| ✅ [Pradeep Bhatia](https://app.gohighlevel.com/v2/location/WFkoNzKa9J9PxhngsLfl/contacts/detail/wc452MDflzJUVSOT6JPy) | 0.0h | 8 | **4** | `1 - connected` `0 apw triaged - yes` `1 - triage to call booked` `1 unqualified` `2 - closer follow up` |
| ❌ [Rena Sookra](https://app.gohighlevel.com/v2/location/WFkoNzKa9J9PxhngsLfl/contacts/detail/4vDzMOYAL1dcuAqGyIIU) | 0.0h | 13 | **0** | `0 - no answer` `0 - unresponsive` `0 no show` |
| ❌ [Shamar Samuel](https://app.gohighlevel.com/v2/location/WFkoNzKa9J9PxhngsLfl/contacts/detail/WuRw9EKIbfcPuGnrVKgk) | 0.0h | 13 | **0** | `0 - no credit report` `0 - no answer` `0 no show` `0 - unresponsive` |
| ❌ [Jack Kates](https://app.gohighlevel.com/v2/location/WFkoNzKa9J9PxhngsLfl/contacts/detail/4a8QdzeBed4mRo97Z4vx) | 1.2h | 17 | **7** | `0 - no answer` `0 no show` `1 - connected` `0 - unresponsive` `4 - reschedule` |
| ✅ [Nick Samara](https://app.gohighlevel.com/v2/location/WFkoNzKa9J9PxhngsLfl/contacts/detail/lgswJD9fKGfqmRic0iul) | 1.9h | 9 | **1** | `0 - no answer` `0 no show` `0 lynn - triaged` |
| ✅ [Jennifer Ulloa](https://app.gohighlevel.com/v2/location/WFkoNzKa9J9PxhngsLfl/contacts/detail/Beb6LGrnKnPPmF9B1MpW) | 5.0h | 2 | **1** | `0 lynn - triaged` `1 - responsive` `1 - qualified` `1 - connected` `2 - closer follow up` |
| ❌ [Ms Terry](https://app.gohighlevel.com/v2/location/WFkoNzKa9J9PxhngsLfl/contacts/detail/xsHo2g1QTQgecx5OV6S4) | 6.0h | 11 | **1** | `0 - no answer` `0 - unresponsive` `2 - hung up` |
| ❌ [Ed McCullough](https://app.gohighlevel.com/v2/location/WFkoNzKa9J9PxhngsLfl/contacts/detail/NYiNc0yWNWvHUsoxZMGU) | 7.8h | 2 | **0** | `0 - no answer` |
| ✅ [Michael Moore](https://app.gohighlevel.com/v2/location/WFkoNzKa9J9PxhngsLfl/contacts/detail/lCa8gYSSfhlb1YyszdrK) | 10.6h | 10 | **4** | `0 lynn - triaged` `1 - connected` |
| ✅ [P Reddy P](https://app.gohighlevel.com/v2/location/WFkoNzKa9J9PxhngsLfl/contacts/detail/8Ermg0m5C1JDmvAb808b) | 11.1h | 4 | **0** | `0 lynn - triaged` `1 - connected` `1 - qualified` |
| ❌ [Antonio Jenkins](https://app.gohighlevel.com/v2/location/WFkoNzKa9J9PxhngsLfl/contacts/detail/LWR0IetKviApaOvTmBxK) | 11.5h | 6 | **1** | `0 lynn - triaged` |
| ❌ [Behnad Zandi](https://app.gohighlevel.com/v2/location/WFkoNzKa9J9PxhngsLfl/contacts/detail/Dg9fyJ621iCphlIRa0vm) | 14.5h | 6 | **2** | `0 lynn - triaged` `1 - connected` `1 - qualified` `3 - not interested` |
| ✅ [Chris Bowers](https://app.gohighlevel.com/v2/location/WFkoNzKa9J9PxhngsLfl/contacts/detail/S80lc8JjJ7284xzdh1Wi) | 16.4h | 17 | **6** | `0 lynn - triaged` `0 - no answer` |
| ✅ [Yeshaya Dank](https://app.gohighlevel.com/v2/location/WFkoNzKa9J9PxhngsLfl/contacts/detail/5CRpCl0usJYwUCcw0D79) | 16.5h | 1 | **1** | `0 lynn - triaged` `1 - connected` |
| ❌ [Tessa Ndille](https://app.gohighlevel.com/v2/location/WFkoNzKa9J9PxhngsLfl/contacts/detail/SoJGlleiyOTlQFwfH4Jk) | 16.6h | 7 | **0** | `0 - no answer` |
| ❌ [Trent Hamilton](https://app.gohighlevel.com/v2/location/WFkoNzKa9J9PxhngsLfl/contacts/detail/nsrxMsSnOMHdr1iOkUdj) | 19.3h | 11 | **1** | `0 - no answer` `0 no show` `0 - unresponsive` |
| ❌ [George Truesdale](https://app.gohighlevel.com/v2/location/WFkoNzKa9J9PxhngsLfl/contacts/detail/8JvItcgAZPOFGsFVbbA2) | 22.9h | 10 | **0** | `0 - no answer` `0 - unresponsive` `2 - hung up` |
| ❌ [Tarlochan Singh](https://app.gohighlevel.com/v2/location/WFkoNzKa9J9PxhngsLfl/contacts/detail/x5E8IABgpkEyDiOs5TZd) | 25.6h | 7 | **1** | `0 - no answer` `0 no show` `0 lynn - triaged` |
| ❌ [Robert Morawitz](https://app.gohighlevel.com/v2/location/WFkoNzKa9J9PxhngsLfl/contacts/detail/Ek6fa6SLTvUfIlCNhsGk) | 25.7h | 14 | **8** | `0 lynn - triaged` |
| ❌ [Lee McEachin Jr](https://app.gohighlevel.com/v2/location/WFkoNzKa9J9PxhngsLfl/contacts/detail/wIxJeo4piIN0qghQiY2m) | 26.1h | 7 | **3** | `0 lynn - triaged` |
| ❌ [Desi Harmon Sr](https://app.gohighlevel.com/v2/location/WFkoNzKa9J9PxhngsLfl/contacts/detail/3pJWW8qMPiZkyWokyH7g) | 39.7h | 3 | **0** | `0 no show` |
| ❌ [Pedro Perez Grizzle](https://app.gohighlevel.com/v2/location/WFkoNzKa9J9PxhngsLfl/contacts/detail/5IxjeWvQ0aW8onfhZ9xM) | 45.1h | 7 | **2** | `1 - connected` |
| ❌ [Connor Robertson](https://app.gohighlevel.com/v2/location/WFkoNzKa9J9PxhngsLfl/contacts/detail/aUuP9CfKdLFG1bSqVban) | 54.9h | 7 | **3** | `0 - no answer` `0 lynn - triaged` `1 - connected` |
| ❌ [David Shepherd](https://app.gohighlevel.com/v2/location/WFkoNzKa9J9PxhngsLfl/contacts/detail/F2fA9NZW88pSwL3P6JbE) | 58.3h | 2 | **0** | `0 - no answer` |
| ✅ [Jesse Hopcus](https://app.gohighlevel.com/v2/location/WFkoNzKa9J9PxhngsLfl/contacts/detail/SG3f3PsV3sJaJRS34v21) | 72.3h | 3 | **1** | `0 - no credit report` `0 - unqualified` |

## 📥 NEVER BOOKED — the 9
| Person | 1st dial | Dials | Connected | Setter tags [V] |
|---|---|---|---|---|
| [Javaris Johnson](https://app.gohighlevel.com/v2/location/WFkoNzKa9J9PxhngsLfl/contacts/detail/1LpdOmQr5SLXuS3blGHs) | 0.0h | 8 | 0 | `0 lynn - spl - yes` `0 - no answer` `0 - unresponsive` |
| [Marko Sakren](https://app.gohighlevel.com/v2/location/WFkoNzKa9J9PxhngsLfl/contacts/detail/zPHKP5SyzqpnJxn5gCz9) | 0.5h | 2 | 0 | *(none)* |
| [John Mazzocchi](https://app.gohighlevel.com/v2/location/WFkoNzKa9J9PxhngsLfl/contacts/detail/yWBoytMEygPZXSyvplHl) | 4.1h | 10 | 1 | `0 - no answer` |
| [LeRoy McCall](https://app.gohighlevel.com/v2/location/WFkoNzKa9J9PxhngsLfl/contacts/detail/9kRWME9TdBvPTZiixBiX) | 11.8h | 6 | 0 | `0 - no answer` `1 - connected` `0 - unresponsive` |
| [HERMAN ROGERS](https://app.gohighlevel.com/v2/location/WFkoNzKa9J9PxhngsLfl/contacts/detail/RYHu2KExLZOScp0ori3t) | 13.2h | 9 | 0 | `0 - no answer` |
| [Fernando De Pieri](https://app.gohighlevel.com/v2/location/WFkoNzKa9J9PxhngsLfl/contacts/detail/jypnYW0kj5700hD8azMk) | 15.7h | 4 | 0 | `0 - no answer` |
| [Njjnn Of](https://app.gohighlevel.com/v2/location/WFkoNzKa9J9PxhngsLfl/contacts/detail/dI21IaM4rp5cDTR8VK3T) | 17.3h | 6 | 0 | `0 - no answer` `0 - unresponsive` |
| [Natalia Rumbuc](https://app.gohighlevel.com/v2/location/WFkoNzKa9J9PxhngsLfl/contacts/detail/XWpYlTI8Ar1QnwizNVuA) | 34.7h | 11 | 0 | `0 - no answer` `0 - unresponsive` |
| [Noel Rivera](https://app.gohighlevel.com/v2/location/WFkoNzKa9J9PxhngsLfl/contacts/detail/Rxrtsgt3VREGPivwS6RE) | 70.6h | 5 | 0 | `2 - hung up` |

## What to fix (in order)
1. **Kill the fake SPL metric.** `minutesToFirstTouch` measures an opportunity stamp. Real speed to lead = time to first *dial*; median is 13.2 hours, and past 24h the show rate collapses to 12%. Track the dial.
2. **Target the 1–12 hour window with an actual connection**, not a sub-minute robot text. Connection is the variable that doubles the show rate (38% vs 12%).
3. **Tag on the outcome, not the attempt** — 8 real connections went untagged and the one qualified lead has no tags at all. The Sep-1 fields (Setter Verdict, Triage Date, Outcome) exist to end this.
4. **`1 - qualified` at setter stage is currently 0-for-3.** Either define it against the money/credit bar or stop using it — it is misleading the pipeline.
