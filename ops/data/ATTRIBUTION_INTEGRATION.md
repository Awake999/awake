# GHL -> Notion Attribution Integration - Ascend Prime Wealth
*Run: 2026-08-30 (UTC) | Executor: cloud attribution agent | Target: Notion data source `collection://5614ffa0-e3d0-40cb-ae64-b32ec52e288c` (Clients & Leads, 83 rows)*

**TLDR:** 79 of 83 Notion rows confidently matched to GHL contacts and enriched (all writes verified by post-write re-query, 0 mismatches). 1 row skipped as pre-linked (Todd L.), 1 skipped as ambiguous (Robert M. - 4 duplicate GHL records), 2 unmatched (Stefan, Bryan (RE dev) - no candidate in the GHL export). 73/83 rows now carry a Verified attribution label (72 Verified (GHL UTM) written this run + 1 pre-existing Verified (Ad ID)). 27 GHL contacts with UTM/ad data are absent from Notion.

**Sources (evidence base):**
- `/home/user/awake/ops/archive/ghl/2026-08-30/contacts_2026-08-30.csv` (259 contacts)
- `/home/user/awake/ops/archive/ghl/2026-08-30/speed_to_lead_2026-08-30.csv` (minutesToFirstTouch per contactId)
- `/home/user/awake/ops/archive/ghl/2026-08-30/raw/contacts.json` (authoritative; used once, for Kevin C.)
- Notion rows read via view `view://11413082-5683-4ee2-86e4-240763c048d6` (SQL quota was exhausted; view-mode fallback per brief)

**Write policy applied (ops/SOP.md + brief):** only EMPTY fields written; sole exception = Attribution Confidence upgraded from empty/Missing/Derived to Verified (GHL UTM) when the GHL contact carries utm_source or ad_id; no Verified value ever downgraded; no Notes/stage/new-row writes; GHL untouched.

## 1. Match table (79 rows written + 1 pre-linked)

Speed to Lead = `minutesToFirstTouch` from speed_to_lead CSV, rounded to 1 decimal. GHL Link = `https://app.gohighlevel.com/v2/location/WFkoNzKa9J9PxhngsLfl/contacts/detail/<id>`.

| Notion client | GHL contact id | GHL name (CSV) | Match method | Fields written |
|---|---|---|---|---|
| Lee M. | `wIxJeo4piIN0qghQiY2m` | Lee McEachin Jr | name (first + last initial) | GHL Contact ID, GHL Link, Email, Phone, Ad ID, Speed to Lead (min), Attribution Confidence |
| Ms Terry | `xsHo2g1QTQgecx5OV6S4` | Ms Terry | name (first + last initial) | GHL Contact ID, GHL Link, Email, Phone, Ad ID, Speed to Lead (min), Attribution Confidence |
| Tessa N. | `SoJGlleiyOTlQFwfH4Jk` | Tessa Ndille | name (first + last initial) | GHL Contact ID, GHL Link, Email, Phone, Ad ID, Speed to Lead (min), Attribution Confidence |
| Stephen G. | `FWmJO9pOj3dI7eFlCUtO` | Stephen Greco | name (first + last initial) | GHL Contact ID, GHL Link, Email, Phone, Ad ID, Speed to Lead (min), Attribution Confidence |
| Tarlochan S. | `x5E8IABgpkEyDiOs5TZd` | Tarlochan Singh | name (first + last initial) | GHL Contact ID, GHL Link, Email, Phone, Ad ID, Speed to Lead (min), Attribution Confidence |
| Ed McC. | `NYiNc0yWNWvHUsoxZMGU` | Ed McCullough | name (first + last initial) | GHL Contact ID, GHL Link, Email, Phone, Ad ID, Speed to Lead (min), Attribution Confidence |
| Behnad Z. | `Dg9fyJ621iCphlIRa0vm` | Behnad Zandi | name (first + last initial) | GHL Contact ID, GHL Link, Email, Phone, Ad ID, Speed to Lead (min), Attribution Confidence |
| George T. | `8JvItcgAZPOFGsFVbbA2` | George Truesdale | name (first + last initial) | GHL Contact ID, GHL Link, Email, Phone, Ad ID, Speed to Lead (min), Attribution Confidence |
| David S. | `F2fA9NZW88pSwL3P6JbE` | David Shepherd | name (first + last initial) | GHL Contact ID, GHL Link, Email, Phone, Ad ID, Speed to Lead (min), Attribution Confidence |
| Chris M. | `paixz1K5D8j4RuZNbWxO` | Chris Mclean (Matthew Referral) | name (first + last initial) | GHL Contact ID, GHL Link, Email, Phone, Speed to Lead (min), Entry Path |
| Nick S. (ExtremeFunMI) | `lgswJD9fKGfqmRic0iul` | Nick Samara | name (first + last initial) | GHL Contact ID, GHL Link, Email, Phone, Ad ID, Speed to Lead (min), Attribution Confidence, Entry Path |
| Michael M. (wellness ctr) | `lCa8gYSSfhlb1YyszdrK` | Michael Moore | name (first + last initial) | GHL Contact ID, GHL Link, Email, Phone, Ad ID, Speed to Lead (min), Attribution Confidence, Entry Path |
| Pedro (CDL) | `5IxjeWvQ0aW8onfhZ9xM` | Pedro Perez grizzle | phone digits | GHL Contact ID, GHL Link, Email, Ad ID, Speed to Lead (min), Attribution Confidence, Entry Path |
| Connor R. | `aUuP9CfKdLFG1bSqVban` | Connor Robertson | name (first + last initial) | GHL Contact ID, GHL Link, Email, Phone, Speed to Lead (min), Attribution Confidence |
| Yeshaya D. | `5CRpCl0usJYwUCcw0D79` | Yeshaya Dank | name (first + last initial) | GHL Contact ID, GHL Link, Email, Phone, Ad ID, Speed to Lead (min), Attribution Confidence, Entry Path |
| Karl K. (Modern Thyroid Clinic) | `H4aNUi4T4zClFs5EAJtP` | Karl Krummenacher | name (first + last initial) | GHL Contact ID, GHL Link, Email, Phone, Speed to Lead (min), Attribution Confidence |
| Dance K. | `hWwKJSGLIySWfFfGvgbG` | Dance Kelley | email exact | GHL Contact ID, GHL Link, Phone, Speed to Lead (min), Attribution Confidence, Entry Path |
| Trent H. | `nsrxMsSnOMHdr1iOkUdj` | Trent Hamilton | email exact | GHL Contact ID, GHL Link, Speed to Lead (min), Attribution Confidence, Entry Path |
| P Reddy P. | `8Ermg0m5C1JDmvAb808b` | P reddy P | email exact | GHL Contact ID, GHL Link, Speed to Lead (min), Attribution Confidence, Entry Path |
| Antonio J. | `LWR0IetKviApaOvTmBxK` | Antonio Jenkins | email exact | GHL Contact ID, GHL Link, Speed to Lead (min), Attribution Confidence, Entry Path |
| Jesse H. | `SG3f3PsV3sJaJRS34v21` | Jesse Hopcus | email exact | GHL Contact ID, GHL Link, Speed to Lead (min), Attribution Confidence, Entry Path |
| Desi H. | `3pJWW8qMPiZkyWokyH7g` | Desi Harmon Sr | email exact | GHL Contact ID, GHL Link, Speed to Lead (min), Attribution Confidence, Entry Path |
| Michael R. | `uRfz5N6q6qWWmJnI8g3P` | Michael Romano | email exact | GHL Contact ID, GHL Link, Speed to Lead (min), Entry Path |
| Jack K. | `4a8QdzeBed4mRo97Z4vx` | Jack Kates | email exact | GHL Contact ID, GHL Link, Speed to Lead (min), Attribution Confidence, Entry Path |
| Shamar S. | `WuRw9EKIbfcPuGnrVKgk` | Shamar Samuel | email exact | GHL Contact ID, GHL Link, Speed to Lead (min), Attribution Confidence, Entry Path |
| Pradeep B. | `wc452MDflzJUVSOT6JPy` | Pradeep Bhatia | email exact | GHL Contact ID, GHL Link, Speed to Lead (min), Attribution Confidence, Entry Path |
| Carmen M. | `rMXnEsp1c2F7gjZJxU8R` | Carmen Meridith | email exact | GHL Contact ID, GHL Link, Speed to Lead (min), Entry Path |
| Jennifer U. | `Beb6LGrnKnPPmF9B1MpW` | Jennifer Ulloa | email exact | GHL Contact ID, GHL Link, Speed to Lead (min), Attribution Confidence, Entry Path |
| Joe S. | `qqUfALv2TDyD73i9Nj20` | JOE STLOUIS | email exact | GHL Contact ID, GHL Link, Speed to Lead (min), Attribution Confidence, Entry Path |
| Fabio C. | `2EOi7W1AewSnUX5uzMen` | Fabio Cristilli | email exact | GHL Contact ID, GHL Link, Speed to Lead (min), Attribution Confidence, Entry Path |
| Ed C. | `6ynM2oi6T5jDOGrz7IFU` | Ed Choi | email exact | GHL Contact ID, GHL Link, Speed to Lead (min) |
| Lynn N. | `nbD9xUmvOTmXLpRQybEf` | Lynn Neves | email exact | GHL Contact ID, GHL Link, Speed to Lead (min), Entry Path |
| Donnie B. | `TRNF2tS64ZYzfupQ8wxA` | Donnie Burnes | name (first + last initial) | GHL Contact ID, GHL Link, Email, Phone, Speed to Lead (min), Attribution Confidence, Entry Path |
| Yasantha L. | `Bh9gDHCfPWz3bbgCf3qY` | Yasantha Lion | email exact | GHL Contact ID, GHL Link, Speed to Lead (min), Attribution Confidence, Entry Path |
| Ric I. | `VElSiTMnV9Wyx4uKfMu8` | Ric Inting | email exact | GHL Contact ID, GHL Link, Speed to Lead (min), Attribution Confidence, Entry Path |
| Eliel N. | `Ummc2b5oHIcRkLoHCGQL` | Eliel Nataki | email exact | GHL Contact ID, GHL Link, Speed to Lead (min), Attribution Confidence, Entry Path |
| Nia B. | `Cpw3HApQspTN95MOrX6E` | Nia Becker | email exact | GHL Contact ID, GHL Link, Speed to Lead (min), Attribution Confidence, Entry Path |
| Luis R. | `jB334pthMJOVWrBQV5n4` | Luis Rosa | email exact | GHL Contact ID, GHL Link, Speed to Lead (min), Attribution Confidence, Entry Path |
| Sari G. | `mMWCfpUes68WBLo0PHYw` | Sari Gupta | name (first + last initial) | GHL Contact ID, GHL Link, Email, Phone, Speed to Lead (min), Attribution Confidence, Entry Path |
| David B. | `dIe0wr70voH4byEdM43W` | David Butler | email exact | GHL Contact ID, GHL Link, Speed to Lead (min), Attribution Confidence, Entry Path |
| Cordero G. | `Kuo6f1crB8zBDDzhj1MS` | Cordero Galloway | email exact | GHL Contact ID, GHL Link, Speed to Lead (min), Attribution Confidence, Entry Path |
| Marcos M. | `66AvsZJcPX5PSVpRKl04` | Marcos Madrid | email exact | GHL Contact ID, GHL Link, Speed to Lead (min), Attribution Confidence, Entry Path |
| Lonnie G. | `Oq3JZG51pbuX876O74uR` | Lonnie Goodwin | name (first + last initial) | GHL Contact ID, GHL Link, Email, Phone, Speed to Lead (min), Attribution Confidence, Entry Path |
| Jose R. | `lNlFbE1OnyNybL7uSTW7` | Jose Reinoso | email exact | GHL Contact ID, GHL Link, Speed to Lead (min), Attribution Confidence, Entry Path |
| Jennifer L. | `V9CMDGMhvaGasRH7TPHy` | Jennifer Losch | email exact | GHL Contact ID, GHL Link, Speed to Lead (min), Entry Path |
| Flavio P. | `5GIpPqhKqpPovI7NRTaY` | Flavio Palalon | email exact | GHL Contact ID, GHL Link, Speed to Lead (min), Attribution Confidence, Entry Path |
| Milad K. | `Op9dVw0zNovHRET8GjwN` | Milad Keshavarz | email exact | GHL Contact ID, GHL Link, Speed to Lead (min), Attribution Confidence, Entry Path |
| Ronrecus G. | `6T9lJgPwh81u5dKDkyW1` | Ronrecus Goodwin | email exact | GHL Contact ID, GHL Link, Speed to Lead (min), Attribution Confidence, Entry Path |
| Valentino G. | `nSM6AnWwsM2efc7tNKCU` | VALENTINO Graham | email exact | GHL Contact ID, GHL Link, Speed to Lead (min), Attribution Confidence, Entry Path |
| James B. | `s6ECUffAvOuTu70PJMkI` | James Bradley | email exact | GHL Contact ID, GHL Link, Speed to Lead (min), Attribution Confidence, Entry Path |
| George J. | `cevmJmqpYRU1mSyUp3qk` | George Jones | email exact | GHL Contact ID, GHL Link, Speed to Lead (min), Attribution Confidence, Entry Path |
| Ran D. | `LSM1pOSvq93xQBAo3YHt` | Ran day | email exact | GHL Contact ID, GHL Link, Speed to Lead (min), Attribution Confidence, Entry Path |
| Abayomi S. | `zzzVGlcWC8GMovsS2lWT` | Abayomi Sokoya | name (first + last initial) | GHL Contact ID, GHL Link, Email, Phone, Speed to Lead (min), Attribution Confidence, Entry Path |
| Myla M. | `hDKXjL3QDuda9XfRT7lv` | myla maheedhar myla maheedhar | email exact | GHL Contact ID, GHL Link, Speed to Lead (min), Attribution Confidence, Entry Path |
| Robert S. | `VD04ZTrHJvQACmuby8KF` | Robert Schechner | email exact | GHL Contact ID, GHL Link, Speed to Lead (min), Attribution Confidence, Entry Path |
| Patrick O. | `Kby40q23X5P2LGEQ8vbE` | Patrick O | email exact | GHL Contact ID, GHL Link, Speed to Lead (min), Attribution Confidence, Entry Path |
| Whitney Y. | `8GShcGD1WsuniLQbAjaW` | Whitney Young | email exact | GHL Contact ID, GHL Link, Speed to Lead (min), Attribution Confidence, Entry Path |
| Bryon C. | `dAOsTTKWYRjwoGpPL3jX` | Bryon Cooper | email exact | GHL Contact ID, GHL Link, Speed to Lead (min), Attribution Confidence, Entry Path |
| Johnny S. | `74UFJU4WP3UHwvEmbsfs` | Johnny Smith III (not preferred contact) | email exact | GHL Contact ID, GHL Link, Speed to Lead (min), Attribution Confidence, Entry Path |
| Ashwini A. | `zyX9EScR9ZWtKT9aQJiF` | Ashwini Anand | email exact | GHL Contact ID, GHL Link, Speed to Lead (min), Attribution Confidence, Entry Path |
| Rena S. | `4vDzMOYAL1dcuAqGyIIU` | Rena Sookra | email exact | GHL Contact ID, GHL Link, Speed to Lead (min), Attribution Confidence, Entry Path |
| Vernon L. | `vqxDjaVWNphy3yQ7AklO` | Vernon Love | email exact | GHL Contact ID, GHL Link, Speed to Lead (min), Attribution Confidence, Entry Path |
| Zacherly S. | `41WVU1osEDCIgZrwkrWS` | Zacherly Sheets | email exact | GHL Contact ID, GHL Link, Speed to Lead (min), Attribution Confidence, Entry Path |
| Leo D. | `lVBxwQne0uiiXkoParUN` | Leo DeOrnellas | email exact | GHL Contact ID, GHL Link, Speed to Lead (min), Attribution Confidence, Entry Path |
| Allen S. | `xhFYrmZPiE4XORDQsoIg` | Allen Sims | email exact | GHL Contact ID, GHL Link, Speed to Lead (min), Attribution Confidence, Entry Path |
| Charlie M. | `zGnj3RjjrjIjLU2RUZhp` | Charlie Murphy | email exact | GHL Contact ID, GHL Link, Speed to Lead (min), Attribution Confidence, Entry Path |
| Andrew W. | `436Us3RE6kK0Hvto2AyK` | Andrew Williams | phone digits | GHL Contact ID, GHL Link, Email, Speed to Lead (min), Attribution Confidence, Entry Path |
| Kesavan R. | `stZFzTokXZRnDDbKcVqr` | Kesavan Rajendran | email exact | GHL Contact ID, GHL Link, Speed to Lead (min), Attribution Confidence, Entry Path |
| Rico R. | `vEDk6s6HDayHYKB8cFtX` | Rico Rice | name (first + last initial) | GHL Contact ID, GHL Link, Email, Phone, Speed to Lead (min), Attribution Confidence, Entry Path |
| Chris B. | `S80lc8JjJ7284xzdh1Wi` | Chris Bowers | email exact | GHL Contact ID, GHL Link, Speed to Lead (min), Attribution Confidence, Entry Path |
| Gunjan P. | `adjVc3JxuFAAIJsBxuCP` | Gunjan Patel | email exact | GHL Contact ID, GHL Link, Speed to Lead (min), Attribution Confidence, Entry Path |
| Ghani A. | `WoHz0xgeLpnhHgJcU5zw` | Ghani Ayesh | email exact | GHL Contact ID, GHL Link, Speed to Lead (min), Attribution Confidence, Entry Path |
| Jose D. | `luUmj2bF4ydVn6pE75v9` | Jose Andres De la fuente castano | email exact | GHL Contact ID, GHL Link, Speed to Lead (min), Attribution Confidence, Entry Path |
| Jill P. | `ZtcBu49xnqBtxlP9W9aU` | Jill Peralta | email exact | GHL Contact ID, GHL Link, Speed to Lead (min), Entry Path |
| Drandre T. | `cHTCRTPTWC29egGMfEc1` | Drandre Google Todd | email exact | GHL Contact ID, GHL Link, Speed to Lead (min), Attribution Confidence, Entry Path |
| Armand A. | `a4zzB27B1HK8gma8Hk2I` | Armand Armstrong | email exact | GHL Contact ID, GHL Link, Speed to Lead (min), Attribution Confidence, Entry Path |
| Ken'Bre M. | `jvpxNdbOqAHUN0dmxMFA` | Ken’Bre Mann | email exact | GHL Contact ID, GHL Link, Speed to Lead (min), Attribution Confidence, Entry Path |
| Matt L. | `A0Jy0hg4FTHyN5d6fDvP` | Matthew LoGuidice | email exact | GHL Contact ID, GHL Link, Speed to Lead (min), Attribution Confidence, Entry Path |
| Kevin C. | `ReAJ7RtVXSDE7rf61fD6` | KevinpCherry205 Kevin Phillip Cherry | name via raw JSON (lastNameRaw "Kevin Phillip Cherry") | GHL Contact ID, GHL Link, Email, Phone, Speed to Lead (min), Attribution Confidence, Entry Path |
| Todd L. | `nIy2smghNYT9II3enmQv` | (pre-existing) | skipped per brief - GHL Contact ID already present | none |

Notes on individual matches:
- **Kevin C.** - CSV name fields are garbled (`first=KevinpCherry205`, `last=Kevin Phillip Cherry`); raw `contacts.json` (authoritative) shows `lastNameRaw: "Kevin Phillip Cherry"`, email kevinpcherry0@gmail.com - unique Kevin C. in the export, so matched.
- **Johnny S.** - matched by exact email (johnnysmithiii@icloud.com -> `74UFJU4WP3UHwvEmbsfs`, GHL-labeled "(not preferred contact)"). A second GHL record for the same person exists (`Cskmn3RVKsKAC2zOoxuB`, johnnysmithiii@me.com, dateAdded 2026-07-17). Email-exact wins per rule 1; duplicate flagged for GHL cleanup (no GHL write made).
- **Jill P.** - matched by email; already carried Ad ID `120249661985200556` + "Verified (Ad ID)" in Notion. GHL shows ad_id `120251505193840556` for her contact (`ZtcBu49xnqBtxlP9W9aU`). DISCREPANCY logged, nothing overwritten (Verified never downgraded, non-empty Ad ID never touched). Only empty fields filled (GHL Contact ID, GHL Link, Speed to Lead 0.0, Entry Path Opt-In Form).

Entry Path mapping used (only into EMPTY Entry Path): GHL source `Application` / `Application W2/Business Owner` -> Opt-In Form; `Funding Consultation - Calendar - ...` -> Direct Booked Call (Chris M., Lynn N.). Sources `Upload`, `A2P`, `Scheduling Form + Credit Score`, blank -> left empty (not clear enough). Ed C. (source blank) got no Entry Path.

## 2. Unmatched Notion rows (2)

| Notion client | Reason |
|---|---|
| Stefan (`3c15bb1ffef481139b64f9b6f6e38f5e`) | No email/phone in Notion; no GHL contact with first name starting "Stefan" in the 259-contact export |
| Bryan (RE dev) (`3b75bb1ffef4812fb11ad477dfe02b9d`) | No email/phone in Notion; no GHL contact with first name starting "Bryan" in the export |

## 3. Ambiguous matches skipped (1)

| Notion client | Candidates (all GHL ids) | Why skipped |
|---|---|---|
| Robert M. (`3c95bb1ffef481c8bf6cf87b5915c6e7`) | `CDax69Bvm2YttP8b6lax` (Robert morawitz), `jxxK6fePUjOv4Aisa6vG` (Robert Morawitz v2), `aPvVoQKnmYksX4nIpD2U` (Robert Morawitz (Secondary Phone)), `Ek6fa6SLTvUfIlCNhsGk` (Robert Morawitz) | 4 duplicate GHL records for the same surname; Notion row has no email/phone to disambiguate which record is canonical. SOP: never guess -> skipped. Recommend GHL dedupe, then re-run. |

## 4. Attribution summary (feeds Ad Scoreboard)

Post-write state of all 83 rows (re-queried from Notion after writes; 0 mismatches vs plan):

| Attribution Confidence | Rows |
|---|---|
| Verified (GHL UTM) - written this run | 72 |
| Verified (Ad ID) - pre-existing (Jill P.) | 1 |
| Missing (remaining) | 2 (Robert M. - ambiguous; Chris M. - matched but GHL has no utm/ad_id) |
| Empty (no UTM evidence or unmatched) | 8 (Ed C., Lynn N., Michael R., Carmen M., Jennifer L. - matched, no utm; Todd L.; Stefan; Bryan (RE dev)) |

**=> 73 of 83 rows now carry a Verified attribution label** (was 1 before this run).

Ad IDs on matched contacts (GHL ad_id, ground truth from contacts CSV; 13 written to Notion this run, Jill P.'s pre-existing Notion value differs - see section 1 note):

| ad_id | Leads (matched Notion rows) | Rows |
|---|---|---|
| `120251505193840556` | 9 | Lee M., Ms Terry, Stephen G., Behnad Z., George T., David S., Pedro (CDL), Yeshaya D., Jill P. |
| `120251505168610556` | 3 | Tessa N., Ed McC., Michael M. (wellness ctr) |
| `120251505193860556` | 1 | Tarlochan S. |
| `120251505193870556` | 1 | Nick S. (ExtremeFunMI) |

62 matched rows are Verified via utm_source only (utm_source fb/ig/an/th present, no ad_id captured in GHL) - ad-level attribution for those requires the fbclid/attribution raws or GHL ad reporting, not available in the CSV ad_id column.

## 5. GHL contacts with UTM/ad data NOT in Notion (27)

100 of 259 GHL contacts carry utm_source and/or ad_id; 73 are matched to Notion rows (incl. Todd L.); **27 are not in the tracker at all** - possible missing leads. Sorted newest first (dateAdded from contacts CSV):

| GHL id | Name | dateAdded | ad_id |
|---|---|---|---|
| `jypnYW0kj5700hD8azMk` | Fernando De pieri | 2026-08-27 | `120251505193840556` |
| `Ek6fa6SLTvUfIlCNhsGk` | Robert Morawitz | 2026-08-23 | `120251505193840556` |
| `1LpdOmQr5SLXuS3blGHs` | Javaris johnson | 2026-08-20 | `120251505168610556` |
| `dI21IaM4rp5cDTR8VK3T` | Njjnn Of (test-like name) | 2026-08-17 | `120251505193870556` |
| `Rxrtsgt3VREGPivwS6RE` | Noel Rivera | 2026-08-15 | `120251505193840556` |
| `yWBoytMEygPZXSyvplHl` | John Mazzocchi | 2026-08-14 | `120251505193840556` |
| `RYHu2KExLZOScp0ori3t` | HERMAN ROGERS | 2026-08-13 | `120251505193850556` |
| `XWpYlTI8Ar1QnwizNVuA` | Natalia Rumbuc | 2026-08-09 | - |
| `zPHKP5SyzqpnJxn5gCz9` | Marko Sakren | 2026-07-30 | - |
| `9kRWME9TdBvPTZiixBiX` | LeRoy McCall | 2026-07-29 | - |
| `p3IDzIDqWJFugwvIVB7K` | ddddddd dwww (test record) | 2026-07-28 | - |
| `13y5SqYNb2v9MawqscKn` | Kevin-Vincent Ryan | 2026-07-19 | - |
| `Cskmn3RVKsKAC2zOoxuB` | Johnny Smith III (duplicate of matched contact) | 2026-07-17 | - |
| `qhf0fk5vxiDdS6N1zgoH` | Arlene Lorica | 2026-07-16 | - |
| `8yrGAVf67eYPOgTk2ERr` | Meckdad Morsy | 2026-07-14 | - |
| `2T9Pi7t8bMqTjqBy5Yqb` | Jonathan Leighton | 2026-07-13 | - |
| `e4k4mZQTMf6208sd0kej` | Lance Mullins | 2026-07-08 | - |
| `TH2PlxBlMhdFI5OvtBh7` | Ray Stephens | 2026-07-04 | - |
| `yhNMZqeotx5NKu82nTYA` | Tony Powell | 2026-07-03 | - |
| `4IDuyT5fDv0z92dp4rU4` | Dummy Lilsloot (test record) | 2026-07-01 | - |
| `ss0FiOGMInClC93VRTkI` | Mark Gold | 2026-06-30 | - |
| `3AlCi32X1HaAUZy5YdXz` | BROKEN GHL GLITCH (test record) | 2026-06-27 | - |
| `uPZo7Qevay8jtW69aI92` | Ee Loong Chaw | 2026-06-23 | - |
| `IZO4y3SK0tY6PVQPDfas` | Kenneth Parker | 2026-06-21 | - |
| `tH5dfLY7k8I17yZmD1Is` | john lee | 2026-06-21 | - |
| `NVnHhbYRhe1gHea689Jj` | Sara Mosleh | 2026-04-23 | - |
| `6i0aEfZysP9R3WfFPF7g` | Ricky Wriden | 2026-04-13 | - |

**Notable real-looking leads with ad_id and NO tracker row (highest priority):** Fernando De pieri (08-27), Javaris johnson (08-20), Noel Rivera (08-15), John Mazzocchi (08-14), HERMAN ROGERS (08-13). 4 entries look like test/glitch records (marked). Robert Morawitz `Ek6fa6SLTvUfIlCNhsGk` likely belongs to the ambiguous Notion row Robert M. (section 3). Johnny Smith III `Cskmn3RVKsKAC2zOoxuB` is a duplicate of an already-matched contact.

## Verification
- Post-write re-query of the full 83-row view: GHL Contact ID filled on 80 rows (79 written + Todd L.), GHL Link 80, Speed to Lead 79, Ad ID 14 (13 written + Jill P. pre-existing), Attribution = 72 Verified (GHL UTM) / 1 Verified (Ad ID) / 2 Missing / 8 empty. Field-by-field comparison of all 79 planned writes vs live Notion values: **0 mismatches**.
- No writes to GHL, Slack, or any other system. No Notes, stage, or new-row edits.
