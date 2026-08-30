# CALL-OUTCOME PING AUTOMATION — the plan (register #78)
*2026-08-30 · Lane 1 · Replaces the #-announcements "please update statuses" approach (Alan: "not really helpful"). Status: PLANNED, awaiting Alan's pick of Option A/B/C + ping target.*

## The problem it kills
109 of 144 GHL appointments sat at "confirmed" forever because nobody ever set showed/no-show after the call ([evidence](https://github.com/Awake999/awake/blob/claude/new-session-1ofk4w/ops/archive/ghl/2026-08-30/GHL_PULL_SUMMARY.md), register #64). Asking people to remember via an announcement = discipline-dependent = will decay. The fix is a machine that asks THEM, every time, 5 minutes after every call, with a one-tap answer.

## The loop (all options share this shape)
1. **Trigger** — appointment end time passes in GHL (calendar is already the booking truth).
2. **Ping** — Slack message to the closer (and/or Alan): *"Your 2:00 pm with Jane D. just ended — what happened?"*
3. **One-tap answer** — Showed–Closed ✅ · Showed–Follow-up 📞 · No-Show ❌ · Rescheduled 🔁 · Cancelled 🚫
4. **Auto-write** — GHL appointment status + a tag + a contact note get set with zero typing; our nightly pull then syncs it to Notion/dashboard automatically.

## Option A — 100% inside GHL (RECOMMENDED: no new vendors, no code to babysit)
- GHL **Workflow**, trigger: *Appointment Status = confirmed* + wait until *appointment end time + 15 min*.
- Action: **Slack ping via incoming webhook** (GHL "Custom Webhook" action → Slack webhook URL posts to a `#call-outcomes` channel or DM).
- The ping carries **5 GHL trigger links** (one per outcome). Trigger links are native GHL: each click fires its own workflow → sets the tag (`outcome-showed-closed`, `outcome-noshow`, …), writes a contact note with timestamp, and updates the appointment via the workflow's appointment action.
- Effort: ~45 min of clicking in the GHL UI. Zero monthly cost. Survives forever.
- Limit to verify in-UI: whether the workflow can flip the *appointment* status itself or only tag the contact (tags alone still give us the truth — our pull reads tags fine; statuses can be batch-corrected weekly from tags).

## Option B — Slack-native form (prettiest answer UX)
- Same GHL trigger → webhook → **Slack Workflow Builder** form (dropdown: outcome, optional note box).
- Form submission → webhook back to GHL (inbound webhook trigger, paid GHL feature on some plans) or to a tiny Zapier/Make step that calls the GHL API to tag.
- Effort: ~1.5 h, may add a $0–20/mo Zapier/Make dependency. Only worth it if the team hates link-taps.

## Option C — pre-filled landing page (Alan's "landing page" idea, native GHL)
- Ping contains ONE link to a **GHL survey/form pre-filled with the contact** (GHL forms accept URL-prefill of contact fields).
- Closer picks the outcome from a dropdown, hits submit → form-submitted workflow sets tag + note + status.
- Effort: ~1 h. Best when one tap isn't enough (e.g. also capture "no-close reason" and "next step" in the same screen — feeds register #8/#16/#24 forward-only fields).

## Recommendation
**A now, C as phase 2.** A gets the status truth flowing Monday with nothing new to maintain. C later adds the qualification/no-close-reason fields on the same submit, which the Sep-1 forward-only protocol needs anyway.

## Build constraints (binding)
- GHL is READ-ONLY for agents except approved writes → the workflow build happens **in the GHL UI**: Lane 4 browser session with Alan present, or Carla/Lynn following a click-by-click SOP that Lane 1 writes.
- Slack webhook creation needs workspace admin (Alan, 2 min, one time).
- Nothing here edits ads, contacts en masse, or anything delivering. Fully reversible (delete the workflow).

## Who gets pinged (Alan to pick)
The closer who owned the calendar slot (DM) · a shared `#call-outcomes` channel (visible accountability) · both + Alan CC'd. Channel is the recommended default: misses are publicly visible, which is the enforcement.
