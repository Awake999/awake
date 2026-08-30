# Verifiable Booking Roster - Ascend Prime Wealth (audit as of 2026-08-30)

**Purpose:** per-name evidence behind every claimed booking, so each person can be checked individually against the disputed "37-odd bookings / 15 showed" figure.

**Sources (read-only):** Slack `#alan-nguyen-booked-calls` (full history, Mar 24-Aug 30) + `#alan-nguyen-booked-calls-medical`; Fathom full recording list (complete - earliest client recording 2026-06-21); Notion Comms Log (96 rows) and Clients & Leads (74 rows) via SQL.

**How to read "Showed?":**
- **SHOWED - VERIFIED** = a Fathom recording of the actual call exists (link given) and, where Notion has notes, they agree.
- **Showed - secondary** = Notion records the show (team-session review) but Fathom has no named recording.
- **No-show / cancelled** = affirmative evidence (Notion notes; in most cases the named Fathom recording is a voicemail-only call attempt - see Discrepancies #1).
- **Unknown** = no recording found. This is NOT proof of no-show: Fathom verifiably missed real calls (Johnny S. 7/20, Myla M. 7/31, Pedro's recovered call, Carla-hosted Zooms before ~8/17), and everything before 6/21 predates Fathom entirely.
- Entry path is labeled **explicit** only where Notion states it; otherwise **derived** from the alert (full form data = Opt-In Form funnel; blank form = likely Direct Booked link).

## Booking events (one row per GHL booking alert), chronological

| # | Name | Alert date | Booked slot | Entry path | Showed? | Evidence / notes |
|---|------|-----------|-------------|-----------|---------|------------------|
| 1 | Clint Losch | 2026-03-25 | Mar 27, 11:00 AM | internal | Excluded | Test booking by SCIO (Clint, 'SCIO' business, x-reaction). Excluded. |
| 2 | Sari Gupta | 2026-04-23 | Apr 24, 2:30 PM | Opt-In Form (derived; old form w/ revenue) | Unknown | Pre-Fathom era (no recordings exist before 6/21). No show/no-show evidence either way. |
| 3 | Sari Gupta | 2026-04-24 | Apr 25, 4:00 PM | Opt-In Form (derived) | Unknown | Reschedule of 4/24 slot. Pre-Fathom; unknown. |
| 4 | Clint Losch | 2026-04-25 | Apr 25, 8:00 PM | internal | Excluded | Test booking ('Test' business, test.com). Excluded. |
| 5 | Abayomi Sokoya | 2026-04-26 | Apr 29, 1:00 PM | Opt-In Form (derived) | Unknown | Pre-Fathom; unknown. In Notion (Booked Call). |
| 6 | Kevin Phillip Cherry | 2026-04-27 | Apr 30, 6:00 PM | Opt-In Form (derived) | Unknown | Pre-Fathom; unknown. In Notion (Kevin C.). |
| 7 | Jennifer Losch | 2026-04-30 | Apr 30, 10:00 PM | Direct/unknown (derived - form mostly blank) | Unknown | Pre-Fathom. x-reaction on alert; Notion stage Unqualified (likely related to Clint Losch - same surname). Unknown. |
| 8 | Donnie Burnes | 2026-06-20 | Jun 22, 4:15 PM | Opt-In Form (derived; old format, partial) | Unknown | No recording 6/22. Unknown. |
| 9 | Lonnie Goodwin | 2026-06-20 | Jun 21, 6:00 PM | Opt-In Form (derived; old format) | SHOWED - VERIFIED | https://fathom.video/calls/718619432 - 'Lonnie Goodwin \| Guarenteed Funding' 6/21. Notion: Showed (real intake, golf-cart biz). |
| 10 | Dance Kelley | 2026-06-21 | Jun 22, 4:00 PM | Opt-In Form (derived; partial) - via medical channel misroute | Unknown | No recording. In Notion (Booked Call). Unknown. |
| 11 | VALENTINO Graham | 2026-06-21 | Jun 24, 5:00 PM | Opt-In Form (derived; partial) - via medical channel misroute | Unknown | No recording 6/24. Unknown (he books again 7/10). |
| 12 | Matthew LoGuidice | 2026-06-24 | Jun 25, 1:00 PM PT | Opt-In Form (derived - full form) | SHOWED - VERIFIED | https://fathom.video/calls/723857619 - 'Matthew LoGuidice \| Guaranteed Funding' 6/25. Notion: Closed Won (Matt L.). |
| 13 | Yasantha Lion | 2026-06-24 | Jun 27, 3:15 PM PT | Opt-In Form (derived - full form) | No-show / cancelled | Notion: NO-SHOW; recording https://fathom.video/calls/726399183 is Alan alone - 'client never joined... I don't think it was real'. |
| 14 | Leo DeOrnellas | 2026-06-25 | Jun 26, 3:15 PM CT | Opt-In Form (derived - full form) | Unknown | No 6/26 recording. Unknown (Leo verifiably shows 7/28; Closed Won). |
| 15 | Milad Keshavarz | 2026-06-25 | Jun 27, 4:30 PM PT | Opt-In Form (derived; partial) | Unknown | No recording. Unknown. |
| 16 | Tests Test | 2026-06-25 | Jun 28, 3:00 PM | internal | Excluded | Test booking in medical channel. Excluded. |
| 17 | Ed Choi | 2026-06-27 | Jun 29, 1:00 PM PT | Opt-In Form (derived; partial) | SHOWED - VERIFIED | https://fathom.video/calls/726927356 (+ https://fathom.video/calls/728838119) - 'Ed Choi \| Guaranteed Funding' 6/29. Notion: Closed Won ($2,000 on 7/1). |
| 18 | Luis Rosa | 2026-06-27 | Jun 29, 5:00 PM ET | Opt-In Form (derived; partial) | No-show / cancelled | Notion: NO-SHOW; recording https://fathom.video/calls/726976750 is outbound voicemail only. |
| 19 | Marcos Madrid | 2026-06-28 | Jun 30, 12:00 AM ET | Opt-In Form (derived - full form) | No-show / cancelled | Notion: NO-SHOW; recording https://fathom.video/calls/727159826 is voicemail w/ reschedule offer (possible timezone error). |
| 20 | Cordero Galloway | 2026-06-29 | Jun 30, 5:00 PM ET | Opt-In Form (derived - full form) | No-show / cancelled | Notion: NO-SHOW; recording https://fathom.video/calls/728410420 captured only Alan on an unrelated PNC call - client never joined. |
| 21 | Ed Choi | 2026-06-29 | Jun 30, 4:00 PM PT | Opt-In Form (derived; partial) | SHOWED - VERIFIED | https://fathom.video/calls/728895030 - 'Ed Choi \| Guaranteed Funding' 6/30 (2nd call). |
| 22 | George Jones | 2026-06-30 | Jul 1, 3:00 PM CT | Opt-In Form (derived - full form) | SHOWED - VERIFIED | https://fathom.video/calls/730407363 - 'George Jones \| Guaranteed Funding' 7/1. Notion: Offer Made. |
| 23 | James Bradley | 2026-06-30 | Jul 1, 6:00 PM CT | Opt-In Form (derived - full form) | Unknown | No recording. Unknown. |
| 24 | Ric Inting | 2026-07-01 | Jul 3, 2:00 PM PT | Opt-In Form (derived - full form) | Unknown | No recording. Unknown. |
| 25 | David Butler | 2026-07-03 | Jul 7, 12:00 AM ET | Opt-In Form (derived - full form) | No-show / cancelled | Notion Comms Log + Clients: NO-SHOW; recording https://fathom.video/calls/734668074 is voicemail only, no conversation. |
| 26 | Jose Reinoso | 2026-07-05 | Jul 6, 4:00 PM (TZ 'SST') | Opt-In Form (derived; partial) | Unknown | No recording; x-reaction on alert. Unknown. |
| 27 | Whitney Young | 2026-07-05 | Jul 7, 5:30 PM CT | Opt-In Form (derived - full form; cardell57@) | SHOWED - VERIFIED | https://fathom.video/calls/735878820 - 'Whitney Young \| Guaranteed Funding' 7/7. |
| 28 | Michael Romano | 2026-07-06 | Jul 7, 11:15 PM CT | Opt-In Form (derived - full form) | Unknown | No recording. Unknown. |
| 29 | Ran Day | 2026-07-06 | Jul 7, 8:00 PM PT | Opt-In Form (derived - full form) | Unknown | CONFLICT/unresolved: recording https://fathom.video/calls/737121220 ('Ran Day \| Guaranteed Funding', dated 7/8 UTC) exists, but Notion stage = No-Show and his other named recording (7/16) is proven voicemail-only. Not counted as verified. |
| 30 | Test Test | 2026-07-06 | Jul 9, 9:15 PM PT | internal | Excluded | Test booking (echoimd@ test contact). Excluded. |
| 31 | Test Test | 2026-07-06 | Jul 9, 8:15 PM PT | internal | Excluded | Test booking. Excluded. |
| 32 | Testing 1 Testing 2 | 2026-07-06 | Jul 9, 7:15 PM PT | internal | Excluded | Test booking (diviner369@ test contact). Excluded. |
| 33 | Eliel Ntakirutimana | 2026-07-07 | Jul 8, 9:00 PM CT | Opt-In Form (derived; partial) | No-show / cancelled | Notion: NO-SHOW; recording https://fathom.video/calls/739002213 is voicemail only (possible timezone error). |
| 34 | Gunjan Patel | 2026-07-07 | Jul 8, 11:30 PM ET | Opt-In Form (derived - full form) | Unknown | No recording near 7/8. Unknown (Gunjan verifiably shows 7/31; 'Booked x5 Jul' per Notion). |
| 35 | Jillian Peralta | 2026-07-07 | Jul 8, 1:00 PM (TZ '-12') | Opt-In Form (derived - full form) | SHOWED - VERIFIED | https://fathom.video/calls/739063325 - 'Jillian Peralta \| Guaranteed Funding' (recorded 7/9 UTC = 7/8 evening PT). Notion: Closed Won (Jill P.). |
| 36 | Kesavan Rajendran | 2026-07-07 | Jul 8, 6:30 PM ET | Opt-In Form (derived - full form) | Unknown | No recording. Unknown. |
| 37 | Ronrecus Goodwin | 2026-07-07 | Jul 8, 4:00 PM ET | Opt-In Form (derived - full form) | Unknown | No recording. Unknown. |
| 38 | Whitney Young | 2026-07-07 | Jul 10, 6:30 PM CT | Opt-In Form (derived - full form; cardell57@) | Unknown | Real-contact booking of the 7/10 slot; no 7/10 recording. Unknown. |
| 39 | Whitney Young (diviner369@) | 2026-07-07 | Jul 10, 6:30 PM CT | suspect test | Excluded | 3 near-identical alerts 7/7 (18:05, 20:19, 20:34) under diviner369@gmail.com / (951) 376-2395 - same contact used by 'Testing 1 Testing 2' on 7/6. Suspected test/dup of Whitney's slot; excluded (labeled derived). |
| 40 | Whitney Young (diviner369@) | 2026-07-07 | Jul 10, 6:30 PM PT | suspect test | Excluded | See above; excluded. |
| 41 | Whitney Young (diviner369@) | 2026-07-07 | Jul 10, 6:30 PM CT | suspect test | Excluded | See above; excluded. |
| 42 | Lynn Neves | 2026-07-08 | Jul 11, 11:15 PM ET | internal | Excluded | Alan's own appointment setter; Notion-verified non-lead internal/test booking. Excluded. |
| 43 | Jill Peralta | 2026-07-09 | Jul 10, 3:30 PM PT | Opt-In Form (derived - full form) | SHOWED - VERIFIED | https://fathom.video/calls/741969838 - 'Jill Peralta \| Strategy & Consulting' 7/10. |
| 44 | VALENTINO Graham | 2026-07-10 | Jul 10, 8:00 PM PT | Opt-In Form (derived - full form) | No-show / cancelled | Notion: NO-SHOW; recording https://fathom.video/calls/742588509 - client never joined; outbound call hit unconfigured voicemail box. |
| 45 | VALENTINO Graham | 2026-07-10 | Jul 11, 3:00 PM PT | Opt-In Form (derived - full form) | Unknown | Double-book 1 min apart under a 2nd phone number ('merge in GHL' per Notion). No 7/11-slot show evidence. Unknown. |
| 46 | Ashwini Anand | 2026-07-11 | Jul 14, 11:45 PM ET | Opt-In Form (derived; partial) | Unknown | No recording near 7/14 (question/zzz reactions). Unknown (she verifiably shows 7/28 & 7/29). |
| 47 | Nia Becker | 2026-07-11 | Jul 14, 3:00 PM CT | Opt-In Form (derived; partial) | Unknown | No recording. Unknown. |
| 48 | Allen Sims | 2026-07-12 | Jul 15, 9:00 PM CT | Opt-In Form (derived - full form) | Unknown | No 7/15 recording. Unknown (he verifiably shows 7/27). |
| 49 | Fabio Cristilli | 2026-07-12 | Jul 14, 9:00 PM ET | Opt-In Form (derived; partial) | No-show / cancelled | Notion: NO-SHOW; recording https://fathom.video/calls/745440890 is voicemail confirming no-show. |
| 50 | Flavio Palalon | 2026-07-12 | Jul 15, 3:00 PM CT | Opt-In Form (derived - full form) | No-show / cancelled | Notion: NO-SHOW; recording https://fathom.video/calls/746607495 is voicemail w/ reschedule info. |
| 51 | Zacherly Sheets | 2026-07-12 | Jul 15, 9:00 PM ET | Opt-In Form (derived - full form) | Unknown | No 7/15 recording. Unknown (shows 7/31). |
| 52 | Ran Day | 2026-07-13 | Jul 16, 1:00 PM PT | Opt-In Form (derived - full form) | No-show / cancelled | Notion: NO-SHOW; recording https://fathom.video/calls/747882935 is Alan calling at appt time, Ran never joined, voicemail left. |
| 53 | Charlie Murphy | 2026-07-14 | Jul 15, 7:00 PM ET | Opt-In Form (derived - full form) | Unknown | No recording. Unknown. |
| 54 | Ghani Ayesh | 2026-07-14 | Jul 14, 7:00 PM PT | Opt-In Form (derived - full form) | SHOWED - VERIFIED | https://fathom.video/calls/746607489 - 'Ghani Ayesh \| Guaranteed Funding' (7/15 UTC). Notion: Showed. (Note: later formally requested data deletion 7/15.) |
| 55 | Whitney Young | 2026-07-14 | Jul 16, 4:00 PM CT | Opt-In Form (derived - full form) | SHOWED - VERIFIED | https://fathom.video/calls/747882934 - 'Whitney Young \| Guaranteed Funding' 7/16 (2nd show). Notion: Offer Made. |
| 56 | Drandre Google Todd | 2026-07-15 | Jul 16, 7:30 PM PT | Opt-In Form (derived - full form) | Unknown | No recording. Unknown. |
| 57 | Drandre Google Todd | 2026-07-15 | Jul 18, 3:00 PM PT | Opt-In Form (derived - full form) | Unknown | Rebooked to 7/18; no recording. Unknown. |
| 58 | Johnny Smith III | 2026-07-17 | Jul 20, 9:00 PM CT | Opt-In Form (derived - full form) | Showed - secondary evidence | Notion: SHOWED - call reviewed in 7/20 Fathom team session (https://fathom.video/calls/754023963), but no named client recording. Secondary evidence only. |
| 59 | Vernon Love | 2026-07-17 | Jul 20, 6:00 PM PT | Opt-In Form (derived - full form) | Unknown | No recording. Unknown. |
| 60 | Andrew Williams | 2026-07-19 | Jul 22, 2:30 PM PT | Opt-In Form (derived; partial) | Unknown | No recording. Unknown. |
| 61 | Armand Armstrong | 2026-07-19 | Jul 23, 12:15 AM ET | Opt-In Form (derived - full form) | Unknown | No recording. Unknown. |
| 62 | Jose Andres De La Fuente Castano | 2026-07-19 | Jul 21, 3:15 PM CT | Opt-In Form (derived - full form) | Unknown | No recording. Unknown. |
| 63 | Ken'Bre Mann | 2026-07-20 | Jul 21, 9:00 PM ET | Opt-In Form (derived; partial) | Unknown | No recording. Unknown. |
| 64 | Rico Rice | 2026-07-20 | Jul 21, 4:15 PM CT | mis-booking | Excluded | MIS-BOOKING: alert under Rico Rice's contact but was actually Allen Sims (Lynn's Slack messages 7/21 + Notion Comms Log). Excluded; superseded by Allen Sims 7/22 row. |
| 65 | Allen Sims | 2026-07-21 | Jul 22, 7:00 PM CT | Opt-In Form (derived - full form) | Unknown | Reschedule of the mis-booked 7/21 slot (alert still carried Rico's contact). No 7/22 recording. Unknown. |
| 66 | Johnny Smith III | 2026-07-22 | Jul 23, 8:30 PM CT | Opt-In Form (derived - full form) | Unknown | 2nd booking (different email - icloud). No recording. Unknown. |
| 67 | Allen Sims | 2026-07-23 | Jul 27, 6:00 PM CT | Opt-In Form (derived - full form) | SHOWED - VERIFIED | https://fathom.video/calls/759494613 - 'Allen Sims \| Guaranteed Funding' 7/27. Notion: Showed. |
| 68 | Ashwini Anand | 2026-07-23 | Jul 28, 4:00 PM ET | Opt-In Form (derived; partial) | SHOWED - VERIFIED | https://fathom.video/calls/762499930 - 'Ashwini Anand \| Guaranteed Funding' 7/28. Notion: Offer Made. |
| 69 | Ken'Bre Mann | 2026-07-23 | Jul 27, 5:00 PM ET | Opt-In Form (derived; partial) | Unknown | No recording. Unknown. |
| 70 | Patrick O | 2026-07-23 | Jul 27, 9:00 PM ET | Opt-In Form (derived - full form) | No-show / cancelled | Notion: CANCELLED - misread automated email's 'reservation not yet booked' disclaimer (fixable system issue). Debrief https://fathom.video/calls/764531452. |
| 71 | Leo De Ornellas | 2026-07-24 | Jul 27, 5:00 PM CT | Opt-In Form (derived - full form) | Unknown | No 7/27 recording; superseded by 7/28 rebooking. Unknown. |
| 72 | Patrick O | 2026-07-26 | Jul 28, 7:00 PM ET | Opt-In Form (derived - full form) | No-show / cancelled | 2nd booking, same cancellation episode per Notion ('Booked x2'). Reheat candidate. |
| 73 | Bryon Cooper | 2026-07-27 | Jul 28, 12:00 AM ET | Opt-In Form (derived - full form) | Unknown | No recording. Unknown. |
| 74 | Jill Peralta | 2026-07-27 | Jul 29, 6:00 PM PT | Opt-In Form (derived - full form) | Unknown | No 7/29-slot recording. She is an active Closed-Won client w/ coaching sessions recorded 7/28 (https://fathom.video/calls/761220510) - slot itself unverified. |
| 75 | Leo De Ornellas | 2026-07-27 | Jul 28, 5:00 PM CT | Opt-In Form (derived - full form) | SHOWED - VERIFIED | https://fathom.video/calls/762747396 - 'Leo De Ornellas \| Guaranteed Funding' 7/28. Notion: Closed Won. |
| 76 | Ashwini Anand | 2026-07-28 | Jul 29, 7:00 PM ET | Opt-In Form (derived; partial) | SHOWED - VERIFIED | https://fathom.video/calls/764436554 - 'Ashwini Anand \| Onboarding & Action Session' 7/29 (2nd show). |
| 77 | Gunjan Patel | 2026-07-28 | Jul 28, 11:45 PM ET | Opt-In Form (derived - full form) | Unknown | Same-day booking; no recording. Unknown. |
| 78 | Robert Schechner | 2026-07-28 | Jul 29, 11:30 PM ET | Opt-In Form (derived - full form) | Unknown | No recording. Unknown. |
| 79 | Gunjan Patel | 2026-07-29 | Jul 30, 10:00 PM ET | Opt-In Form (derived - full form) | Unknown | No recording; superseded by 7/31 rebooking. Unknown. |
| 80 | Kesavan Rajendran | 2026-07-29 | Jul 30, 11:30 PM ET | Opt-In Form (derived - full form) | Unknown | 2nd booking. No recording. Unknown. |
| 81 | Rena Sookra | 2026-07-29 | Aug 3, 12:00 AM ET | Opt-In Form (derived - full form) | Unknown | No recording. Unknown. |
| 82 | Zacherly Sheets | 2026-07-29 | Jul 30, 7:00 PM ET | Opt-In Form (derived - full form) | Unknown | No 7/30 recording; superseded by 7/31 rebooking. Unknown. |
| 83 | Chris Bowers | 2026-07-30 | Aug 1, 11:00 PM CT | Opt-In Form (derived; partial) | Unknown | No 8/1 recording. Unknown (he shows 8/4 & 8/6). |
| 84 | Gunjan Patel | 2026-07-30 | Jul 31, 9:00 PM ET | Opt-In Form (derived - full form) | SHOWED - VERIFIED | https://fathom.video/calls/767888047 - 'Gunjan Patel \| Funding Strategy Session' (8/1 UTC = 7/31 9pm ET). Notion: Showed, HOT. |
| 85 | Myla Maheedhar | 2026-07-30 | Jul 31, 9:00 PM CT | Opt-In Form (derived - full form) | Showed - secondary evidence | Notion: SHOWED ~7/31 - call reviewed in Fathom team session (https://fathom.video/calls/768849661); no named client recording. Secondary evidence only. |
| 86 | Zacherly Sheets | 2026-07-30 | Jul 31, 7:30 PM ET | Opt-In Form (derived - full form) | SHOWED - VERIFIED | https://fathom.video/calls/766265132 - 'Zacherly Sheets \| Guaranteed Funding' 7/31. Notion: Closed Lost. |
| 87 | Carmen Meridith | 2026-07-31 | Aug 1, 3:00 PM MT | Opt-In Form (derived; partial) | SHOWED - VERIFIED | https://fathom.video/calls/768936830 - 'Carmen Meridith \| Credit & Funding Consultation' 8/1. Notion: Showed. |
| 88 | Gunjan Patel | 2026-07-31 | Aug 4, 4:00 PM ET | Opt-In Form (derived - full form) | Unknown | 5th July booking; no 8/4 recording (already showed 7/31). Unknown. |
| 89 | Leo De Ornellas | 2026-07-31 | Aug 1, 2:30 PM CT | Opt-In Form (derived - full form) | Unknown | Post-show follow-up booking; no 8/1 recording. Unknown. |
| 90 | Antonio Jenkins | 2026-08-01 | Aug 5, 7:00 PM CT | Opt-In Form (derived - full form) | Unknown | No recording. Unknown. |
| 91 | Chris Bowers | 2026-08-01 | Aug 3, 8:00 PM CT | Opt-In Form (derived; partial) | Unknown | No 8/3 recording; superseded by 8/4 rebooking. Unknown. |
| 92 | Leo De Ornellas | 2026-08-01 | Aug 4, 4:45 PM CT | Opt-In Form (derived - full form) | Unknown | No 8/4 recording. Unknown. |
| 93 | Trent Hamilton | 2026-08-02 | Aug 3, 11:00 PM ET | Opt-In Form (derived - full form) | Unknown | No recording. Unknown. |
| 94 | Chris Bowers | 2026-08-03 | Aug 4, 8:00 PM CT | Opt-In Form (derived; partial) | SHOWED - VERIFIED | https://fathom.video/calls/768297031 - 'Chris Bowers \| Guaranteed Funding' 8/4. Notion: 'SHOWED x2 (8/4, 8/7)'. |
| 95 | Chris Bowers | 2026-08-03 | Aug 6, 9:00 PM CT | Opt-In Form (derived; partial) | SHOWED - VERIFIED | https://fathom.video/calls/771447748 - 'Chris Bowers \| Guaranteed Funding' (8/7 UTC = 8/6 9pm CT). Notion: Showed; then PAUSED - Nurture. |
| 96 | JOE STLOUIS | 2026-08-03 | Aug 4, 9:00 PM ET | Opt-In Form (derived - full form) | Unknown | No 8/4 recording; superseded by 8/7 rebooking. Unknown. |
| 97 | Shamar Samuel | 2026-08-03 | Aug 6, 12:15 AM ET | Opt-In Form (derived - full form) | Unknown | No recording. Unknown. |
| 98 | JOE STLOUIS | 2026-08-04 | Aug 7, 1:15 PM ET | Opt-In Form (derived - full form) | SHOWED - VERIFIED | https://fathom.video/calls/775117203 - 'JOE STLOUIS \| Funding Strategy Session' 8/7. Notion: Offer Made. |
| 99 | Jack Kates | 2026-08-04 | Aug 5, 12:00 AM ET | Opt-In Form (derived - full form) | Unknown | No recording. Unknown. |
| 100 | Whitney Young | 2026-08-04 | Aug 5, 8:30 PM CT | Opt-In Form (derived - full form) | Unknown | No 8/5 recording (already showed twice). Unknown. |
| 101 | Desi Harmon Sr | 2026-08-05 | Aug 8, 6:30 PM ET | Opt-In Form (derived - full form) | Unknown | No recording. Unknown. |
| 102 | Pradeep Bhatia | 2026-08-05 | Aug 7, 3:00 PM PT | Opt-In Form (derived - full form) | SHOWED - VERIFIED | https://fathom.video/calls/775117204 - 'Pradeep Bhatia \| Guaranteed Funding' 8/7. Notion: Offer Made. |
| 103 | Jennifer Ulloa | 2026-08-06 | Aug 7, 4:00 PM ET | Opt-In Form (derived - full form) | SHOWED - VERIFIED | https://fathom.video/calls/775643888 - 'Jennifer Ulloa \| Guaranteed Funding' 8/7. Notion: Closed Lost. |
| 104 | P Reddy P | 2026-08-06 | Aug 10, 3:00 PM CT | Opt-In Form (derived - full form) | SHOWED - VERIFIED | https://fathom.video/calls/777298604 - 'P Reddy P \| Guaranteed Funding' 8/10. Notion: Showed (Meta engineer, Ridiit). |
| 105 | Jennifer Ulloa | 2026-08-07 | Aug 18, 6:00 PM ET | Opt-In Form (derived - full form) | Unknown | Follow-up booking; no 8/18 recording. Unknown. |
| 106 | Jesse Hopcus | 2026-08-07 | Aug 10, 9:00 PM PT | Opt-In Form (derived - full form) | Unknown | No recording. Unknown. LAST booking alert imported into Notion Comms Log. |
| 107 | Leo DeOrnellas | 2026-08-07 | Aug 10, 5:00 PM CT | Opt-In Form (derived - full form) | Unknown | No 8/10 recording (active Closed-Won client by then). Unknown. |
| 108 | Behnad Zandi | 2026-08-12 | Aug 12, 5:00 PM PT | Opt-In Form (derived - full form: $1M+, 800+, $250K+, LLC) | Unknown | No recording. NOT in Notion Clients & Leads at all. Unknown. |
| 109 | Connor Robertson | 2026-08-12 | Aug 13, 4:00 PM ET | Opt-In Form (explicit - Notion Entry Path) | Unknown | No 8/13 recording; he rebooks next day for 8/17. Unknown (likely reschedule). |
| 110 | Yeshaya Dank | 2026-08-12 | Aug 13, 8:00 PM ET | Opt-In Form (derived - full form) | SHOWED - VERIFIED | https://fathom.video/calls/783351348 - 'Yeshaya Dank \| Guaranteed Funding' (8/14 UTC = 8/13 8pm ET). Notion: Offer Made. |
| 111 | Connor Robertson | 2026-08-13 | Aug 17, 5:00 PM ET | Opt-In Form (explicit - Notion Entry Path) | SHOWED - VERIFIED | https://fathom.video/calls/788222126 - 'Connor Robertson \| Guaranteed Funding' 8/17. Notion: Showed. (Contradicts the working assumption that Fathom missed this call.) |
| 112 | Ms Terry | 2026-08-13 | Aug 13, 10:30 PM CT | Opt-In Form (derived - full form: $1M+, 720-749) | Unknown | No recording. NOT in Notion Clients & Leads. Unknown. |
| 113 | Stephen Greco | 2026-08-13 | Aug 17, 5:00 PM CT | Opt-In Form (derived - full form) | Unknown | No recording. NOT in Notion Clients & Leads. Unknown. |
| 114 | Yeshaya Dank | 2026-08-14 | Aug 27, 12:30 PM ET | Opt-In Form (derived - full form) | SHOWED - VERIFIED | https://fathom.video/calls/799338949 - 'Yeshaya Dank \| $1M-$1.5M - Dank SPV - Funding' 8/27 (2nd show). |
| 115 | Pedro Perez Grizzle | 2026-08-15 | Aug 18, 7:00 PM ET | Opt-In Form (derived - full form) | No-show / cancelled | Notion: NO-SHOW at the 7pm slot (joined an old auto-sent Zoom link - fixable system issue), RECOVERED same evening: https://fathom.video/calls/790045529. Slot itself = no-show. |
| 116 | George Truesdale | 2026-08-16 | Aug 17, 11:00 PM ET | Opt-In Form (derived - full form) | Unknown | No recording. NOT in Notion Clients & Leads. Unknown. |
| 117 | Tarlochan Singh | 2026-08-16 | Aug 17, 10:00 PM ET | Opt-In Form (derived - full form) | Unknown | No recording. NOT in Notion Clients & Leads. Unknown. |
| 118 | Connor Robertson | 2026-08-17 | Sep 1, 4:00 PM ET | Opt-In Form (explicit - Notion Entry Path) | Pending | Appointment is after 2026-08-30 (audit date) - outcome pending, must not count either way. |
| 119 | Michael Moore | 2026-08-17 | Aug 17, 4:00 PM (TZ '-12') | Opt-In Form (derived; partial) | Unknown | Odd timezone value; no matching recording. Unknown. |
| 120 | Tarlochan Singh | 2026-08-17 | Aug 20, 12:15 AM ET | Opt-In Form (derived - full form) | Unknown | Double-book (3 min before the 8/19 booking below). No recording. NOT in Notion. Unknown. |
| 121 | Tarlochan Singh | 2026-08-17 | Aug 19, 9:30 PM ET | Opt-In Form (derived - full form) | Unknown | No recording. NOT in Notion. Unknown. |
| 122 | Karl Krummenacher | 2026-08-18 | Aug 20, 3:00 PM MT | Referral (explicit - Notion Entry Path; form partial) | SHOWED - VERIFIED | https://fathom.video/calls/791088813 - 'Karl Krummenacher \| Guaranteed Funding' 8/20. Notion: Offer Made (Modern Thyroid Clinic). |
| 123 | Michael Moore | 2026-08-20 | Aug 20, 10:00 PM ET | Opt-In Form (derived; partial) | SHOWED - VERIFIED | https://fathom.video/calls/791826979 - 'Michael Moore \| Guaranteed Funding' 8/20. Notion (Michael M., wellness ctr): 'SHOWED + STRATEGY PROPOSED 8/20' - same recording URL. |
| 124 | Nick Samara | 2026-08-20 | Aug 20, 7:00 PM ET | Opt-In Form (derived - full form) | Unknown | No 8/20 recording. Unknown (he verifiably shows 8/25 & 8/26). |
| 125 | Ed McCullough | 2026-08-21 | Aug 24, 1:00 PM PT | Opt-In Form (derived; partial) | Unknown | No recording. NOT in Notion Clients & Leads. Unknown. |
| 126 | Michael Moore | 2026-08-21 | Aug 25, 9:00 PM ET | Opt-In Form (derived; partial) | SHOWED - VERIFIED | https://fathom.video/calls/795906439 - 'Michael Moore \| Guaranteed Funding' (Fathom lists 8/26 = 8/25 9pm ET in UTC). Date-conversion match; noted as such. |
| 127 | Nick Samara | 2026-08-21 | Aug 25, 6:00 PM ET | Opt-In Form (derived - full form) | SHOWED - VERIFIED | https://fathom.video/calls/795906442 - 'Nick Samara \| Guaranteed Funding' 8/25. Notion: Closed Won. |
| 128 | David Shepherd | 2026-08-22 | Aug 24, 11:00 PM ET | Opt-In Form (derived - full form) | Unknown | No recording. NOT in Notion Clients & Leads. Unknown. |
| 129 | Lee McEachin Jr | 2026-08-23 | Aug 24, 7:00 PM ET | Opt-In Form (derived - full form) | Unknown | No recording. NOT in Notion Clients & Leads. Unknown. |
| 130 | Robert Morawitz | 2026-08-23 | Aug 25, 5:00 PM PT | Opt-In Form (derived - full form) | Unknown | First of a 3-booking reschedule chain (8/25 - 8/26 - 8/27); final slot verifiably shows 8/27. This slot: unknown. |
| 131 | Tessa Ndille | 2026-08-23 | Aug 24, 5:00 PM ET | Opt-In Form (derived; partial) | Unknown | No recording. NOT in Notion Clients & Leads. Unknown. |
| 132 | Chris Bowers | 2026-08-24 | Aug 25, 6:00 PM CT | Opt-In Form (derived; partial) | Unknown | 4th+ booking; no 8/25 recording (Notion: Nurture/paused since 8/7). Unknown. |
| 133 | Chris Mclean | 2026-08-25 | Aug 26, 8:15 PM ET | Direct Booked Call (derived - form blank) | SHOWED - VERIFIED | https://fathom.video/calls/798638035 - 'Chris Mclean \| Guaranteed Funding' (8/27 UTC = 8/26 8:15pm ET). Notion: Showed, credit-optimization consult. |
| 134 | Michael Moore | 2026-08-25 | Aug 27, 8:00 PM ET | Opt-In Form (derived; partial) | Unknown | No recording matching 8/27 slot. Unknown. |
| 135 | Nick Samara | 2026-08-25 | Aug 25, 3:00 PM ET | Opt-In Form (derived - full form) | Unknown | Alert arrived 8:10pm ET for a 3:00pm ET same-day slot (retroactive/reschedule artifact). Unknown; his 6pm slot that day is verified. |
| 136 | Robert Morawitz | 2026-08-25 | Aug 26, 4:00 PM PT | Opt-In Form (derived - full form) | Unknown | Middle of reschedule chain; superseded by 8/27 booking. Unknown. |
| 137 | Lee McEachin Jr | 2026-08-26 | Aug 27, 7:00 PM ET | Opt-In Form (derived - full form) | Unknown | 2nd booking. No recording. NOT in Notion Clients & Leads. Unknown. |
| 138 | Nick Samara | 2026-08-26 | Aug 26, 3:00 PM ET | Opt-In Form (derived - full form) | SHOWED - VERIFIED | https://fathom.video/calls/799338953 - 'Nick Samara \| Strategic Consulting - Funding' 8/26 (2nd show). |
| 139 | Robert Morawitz | 2026-08-26 | Aug 27, 1:00 PM PT | Opt-In Form (derived - full form) | SHOWED - VERIFIED | https://fathom.video/calls/798787726 - 'Robert Morawitz \| Guaranteed Funding' 8/27. Notion: Offer Made. |
| 140 | Todd LoGuidice | 2026-08-26 | Aug 26, 3:00 PM PT | Referral (explicit - Notion; form blank = direct-booked) | SHOWED - VERIFIED | https://fathom.video/calls/800283407 - 'Todd LoGuidice \| Funding Execution' 8/26. Notion: Closed Won. Brother of Closed-Won client Matt LoGuidice. |

## Summary

- **Booking events (real leads, tests/internal/mis-bookings excluded):** 129  (11 excluded rows are shown in the table for completeness)
- **Unique people booked:** 79
- **Showed - VERIFIED with a Fathom recording:** 34 events, across 26 unique people
- **Showed - secondary evidence only (Notion):** 2 events (Johnny Smith III, Myla Maheedhar)
- **No-show / cancelled with affirmative evidence:** 13 events; people with no-shows and no show ever: 12 (Cordero Galloway, David Butler, Eliel Ntakirutimana, Fabio Cristilli, Flavio Palalon, Luis Rosa, Marcos Madrid, Patrick O, Pedro Perez Grizzle, Ran Day, VALENTINO Graham, Yasantha Lion)
- **Unknown (no evidence either way):** 79 events; people never resolved either way: 39
- **Pending (future appt):** 1 (Connor R. 9/1 - already showed 8/17)

### Honest show-rate range
- **Per booking event** (n=128 resolvable events): floor 34/128 = **27%** (verified only) up to ceiling 115/128 = **90%** (if every unknown had showed). True value is between; many unknowns are same-person reschedule-chain slots, which deflates the per-event floor.
- **Per unique person** (n=79): **26** people have at least one Fathom-verified show = **33%** floor; adding secondary-evidence shows: 28 (35%); ceiling if every unresolved person showed: **85%**. Only 12 people are affirmatively no-show/cancelled-and-never-showed.

## Discrepancies vs the claimed "37-odd bookings, 15 showed"

1. **"15 showed" is contradicted by primary evidence.** 34 booking events have a Fathom recording of the call itself, covering 26 distinct people - more than double 15 on either measure - plus 2 more shows documented in Notion team reviews. Every one is individually clickable in the table above.
2. **"37-odd bookings" does not match any natural window.** The Slack channels contain 140 booking alerts total (129 after removing tests/internal/mis-bookings), covering 79 unique people (Mar-Aug). July alone produced ~45 lead booking events. If "37" was meant as unique July-era leads it is still low; the number's basis should be stated before it is used.
3. **Fathom title-match is NOT proof of a show - 10 named recordings are voicemail-only no-show attempts** (Fabio C., David B., Eliel N., Luis R., Marcos M., Cordero G., Valentino G., Yasantha L., Flavio P., Ran D. 7/16 - links in table). A naive count of named Fathom recordings would overstate shows; this audit excludes them from the verified column. Conversely, Fathom missed real shows (Johnny S. 7/20, Myla M. 7/31 - documented only via team-review sessions; Pedro's recovered 8/18 call sits in an untitled impromptu recording).
4. **The working assumption that Fathom missed Connor R.'s 8/17 call is wrong** - the recording exists: https://fathom.video/calls/788222126 ('Connor Robertson | Guaranteed Funding', 8/17).
5. **Notion Comms Log stops importing booking alerts at 2026-08-08** (last: Jesse Hopcus). All 33 lead booking alerts from 8/12-8/26 (Behnad Z. through Todd L.) are absent from the Comms Log.
6. **9 recently-booked people are missing from Notion Clients & Leads entirely** (all booked 8/12-8/26): Behnad Zandi, Ms Terry, Stephen Greco, Tarlochan Singh (x3 bookings), George Truesdale, Ed McCullough, David Shepherd, Lee McEachin Jr (x2), Tessa Ndille. Anyone auditing from Notion alone would undercount bookings by these 12 events.
7. **One verified show has NO booking alert at all:** 'Bryan (RE dev)' - Notion: SHOWED 8/8 via impromptu recording https://fathom.video/calls/777749171, "not in Slack ledger... RE-VERIFIED". Bookings made outside GHL (referrals, direct Zoom) never hit the alert channel, so the channel undercounts real calls (Karl K. and Todd L. are referrals that did get alerts; Bryan did not).
8. **Channel plumbing issues bracket the data:** the medical channel mis-routed W2 alerts on 6/21 (Valentino G., Dance Kelley), a mis-booking landed under Rico Rice's contact on 7/20 (actually Allen Sims), and 3 suspected test alerts reused the 'Testing 1 Testing 2' contact under Whitney Young's name on 7/7. All are flagged, not silently dropped.
9. **Pre-Fathom era (Mar 25-Apr 30, 7 alerts, 5 real people)** can never be verified by recording; those 6 lead events sit permanently in Unknown.

## Caveats
- "Unknown" must never be reported as "no-show": Fathom coverage is provably incomplete (see Discrepancy #3/#7; Carla-hosted Zoom calls before ~8/17 were not recorded to Alan's Fathom).
- Date matches across timezones: a few verified links show a Fathom date one day after the booked slot because Fathom lists UTC (e.g. Yeshaya 8/13 -> rec dated 8/14; Chris Bowers 8/6 -> 8/7; Michael Moore 8/25 -> 8/26; Gunjan 7/31 -> 8/1; Ghani 7/14 -> 7/15; Chris Mclean 8/26 -> 8/27; Jillian 7/8 -> 7/9). Each is noted in its row.
- Entry path is mostly **derived** (from form completeness); only Connor R. (Opt-In Form), Karl K. (Referral) and Todd L. (Referral) are explicit in Notion.
- Nothing was written to Slack or Notion; this file is the only output.
