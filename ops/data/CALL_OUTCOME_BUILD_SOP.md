# CALL-OUTCOME AUTOMATION — click-by-click build SOP (Option A, register #78)
*2026-08-30 · Lane 1 · Alan ruled: Option A now, ping → #call-outcomes channel (created 8/30, ID C0BTJL3BPPX). Builder: Lane 4 browser session with Alan present, OR Carla/Lynn following this doc verbatim. ~45 min. Everything reversible (delete the workflows).*

## What you're building (one sentence)
15 min after every appointment ends, Slack #call-outcomes gets: *"[Closer]'s call with [Contact] just ended — what happened?"* with 5 tap-links; one tap makes GHL tag the contact, write a dated note, and set the outcome — zero typing.

## STEP 0 — Slack incoming webhook (Alan, one time, ~3 min)
1. Go to https://api.slack.com/apps → **Create New App** → From scratch → name `APW Call Outcomes`, pick the APW workspace.
2. Left sidebar → **Incoming Webhooks** → toggle ON → **Add New Webhook to Workspace** → choose channel **#call-outcomes** → Allow.
3. Copy the webhook URL (`https://hooks.slack.com/services/...`). Treat it like a password: store it ONLY in GHL's webhook step and in a local file on Alan's PC — never in the repo, Notion, or a Slack message.

## STEP 1 — five trigger links (GHL, ~5 min)
GHL location **Prismatic** → **Marketing → Trigger Links → + Add Link**. Create five; URL for all five can be `https://ascendprimewealth.com` (the click is the data; the destination is cosmetic — a "logged ✅" page can come later):
| Link name | will set tag |
|---|---|
| Outcome — Showed, Closed | `outcome-showed-closed` |
| Outcome — Showed, Follow-up | `outcome-showed-followup` |
| Outcome — No-Show | `outcome-noshow` |
| Outcome — Rescheduled | `outcome-rescheduled` |
| Outcome — Cancelled | `outcome-cancelled` |

## STEP 2 — five tiny "record it" workflows (~15 min)
**Automation → Workflows → + Create (start from scratch)**, one per outcome. Example for No-Show (repeat the pattern ×5):
1. Trigger: **Trigger Link Clicked** → filter: link = *Outcome — No-Show*.
2. Action **Add Contact Tag** → `outcome-noshow`.
3. Action **Add Note** → `Outcome logged via #call-outcomes ping: NO-SHOW ({{right_now.date}} {{right_now.time}})`.
4. If your workflow action list has an **Appointment** action that can set status → set appointment status = **no_show** (likewise: showed→showed, cancelled→cancelled, rescheduled leave status and add tag only). If the action doesn't exist on this plan, skip — the TAG is the truth; weekly batch-correction reads tags (see Step 5).
5. Name it `Outcome ← No-Show`, publish.

## STEP 3 — the ping workflow (~15 min)
One more workflow, `Ping → call outcome`:
1. Trigger: **Customer Booked Appointment** (or "Appointment Status = confirmed"), calendar filter: the sales calendars only.
2. Step: **Wait → Event/Appointment Time → until 15 minutes AFTER end time** (GHL wait supports appointment-time anchors).
3. Step: **Custom Webhook** → POST → the Step-0 Slack URL → Content-Type `application/json` → body:
```json
{"text":"📞 *{{appointment.title}}* — {{contact.name}} ({{contact.phone}}) with *{{appointment.user.name}}* just ended.\nWhat happened? Tap one:\n✅ Showed–Closed: {{trigger_link.showed_closed}}\n📞 Showed–Follow-up: {{trigger_link.showed_followup}}\n❌ No-Show: {{trigger_link.noshow}}\n🔁 Rescheduled: {{trigger_link.rescheduled}}\n🚫 Cancelled: {{trigger_link.cancelled}}"}
```
   Insert each trigger link via the **custom-values picker** (Trigger Links section) — do NOT paste the raw URL; the merge-field version generates a per-contact link so the tap maps to the right person. Field names in the picker may differ slightly from the above — use the picker's own tokens.
4. Publish.

## STEP 4 — test before trusting (~5 min)
1. Book a dummy appointment on a sales calendar for 5 min from now with a TEST contact (not a client).
2. Wait for it to end +15 min → confirm the #call-outcomes ping arrives with the contact's name and 5 links.
3. Tap **No-Show** → confirm on the TEST contact: tag `outcome-noshow` + the note appear.
4. Delete the test contact/appointment.

## STEP 5 — how it reaches the dashboard (already built, nothing to do)
The nightly GHL pull reads tags + statuses; outcomes flow into the roster audit, Stage History, and the live board automatically. If Step-2.4's appointment action didn't exist, the weekly pull batch-maps tags → statuses instead — same truth either way.

## Gotchas
- Trigger-link taps are counted once per contact per link — a re-tap on a different link later still fires that link's workflow, so a wrong tap is correctable by tapping the right one (both tags land; latest note wins; flag for human if two conflicting outcome tags on one appointment day).
- Closers must be IN #call-outcomes (invite Lynn, Carla, and any closer — 1 min).
- The webhook URL is a secret. If it leaks, regenerate it at api.slack.com and paste the new one into the workflow.
