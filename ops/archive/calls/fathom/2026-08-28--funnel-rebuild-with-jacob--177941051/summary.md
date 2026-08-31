# Summary — Funnel rebuild with Jacob, Sep 1 A/B (Fathom call 801234866)

> 🧭 [Start Here](../../../START-HERE.md) · [Archive home](../../../README.md) · [Calls hub](../../README.md) · **[⬆ back to Fathom index](../INDEX.md)**

> **Companion to `transcript.md` — never a replacement.** The verbatim original in this folder is the source of truth; this AI summary is for fast orientation only.

## Meeting Purpose
Refine lead generation and DM setting processes to improve call quality.

## Key Takeaways
- **New Ad Strategy:** Replace static ads with video creatives using the "Other People's Money" (OPM) angle; A/B test against native Instagram Lead Forms to increase lead volume and quality before the "Cash Cabin" event.
- **Tighter DM Qualification:** Stricter triage script in DMs — "time to start" question at the top, firm 30-day funding timeline to filter non-serious leads.
- **Enhanced Lead Nurturing:** Boost show rates with a personalized pre-call Loom per lead and a consolidated VSL funnel that pre-handles objections.
- **Automated Performance Dashboard:** Real-time dashboard in Claude Code pulling GoHighLevel + Meta Ads data to identify and fix funnel bottlenecks.

## Topics
### Problem: Low-Quality Leads & Calls
- Current campaigns yield low-quality leads (maxed-out cards, near bankruptcy). DM setting is too lenient — unqualified prospects book calls.

### Solution 1: New Ad Strategy
- Video creatives (messaging dictates targeting; low-production single-cut is fine), OPM angle (proven winner for a similar client).
- A/B test with native Instagram Lead Forms — cheap leads, in-app pre-qualification logic; setters must call within 2 minutes of submission.

### Solution 2: Tighter DM Qualification Script
- Triage: (1) How much funding do you need? (2) Timeline — firm 30-day cutoff, longer → send a resource and move on; (3) What have you tried? (4) How will you deploy it? (infer industry for personalization); (5) Approximate credit score?
- Booking: binary time slots ("Thursday 3 PM or 4 PM?") instead of a calendar link; manually enter booked leads into GoHighLevel to trigger automations.

### Solution 3: Enhanced Lead Nurturing
- Personalized pre-call Loom per booked lead: confirm appointment, drop Zoom link, ask an industry-based engagement question. A response signals higher intent.
- New post-booking funnel: VSL → "what to do next" (ICS file, email check) → Q&A videos → video testimonials → picture testimonials.
- Call policy: immediately cancel and reschedule calls taken from a car.

### Solution 4: Automated Performance Dashboard
- Data sources: GoHighLevel (Private Integration Token — pipeline, show rates, closed deals), Meta Ads Developer App API (spend, CPM, CTR), PostHog pixel on VSL/confirmation pages (page conversion).
- Features: real-time metrics, pipeline visualization booked→won, green/yellow/red benchmarks.
- Claude Code workflow: /handoff and /resume to keep project context across chats.

## Next Steps
- **Alan:** film 5–10 OPM video creatives over the weekend; launch ads Monday Sep 1 to build the GHL contact list (~250) before Cash Cabin.
- **Jacob:** send OPM ad scripts; send the Claude Code dashboard prompt and the updated /handoff skill.
- **All:** meet Monday Sep 1, 10 AM PST to launch the new campaigns.
