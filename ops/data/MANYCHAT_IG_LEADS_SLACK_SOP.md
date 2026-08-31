# 📲 IG LEADS → SLACK — ManyChat notification routing (register #123)
*2026-08-31 · Alan: "make sure that the [Many]chat window that's open right now gets routed to give us notifications in Slack under a new channel named IG Leads." Channel **#ig-leads** is CREATED (ID `C0BTTRX09UM`, public). Remaining work is click-work in ManyChat + one Slack webhook — neither is reachable from a cloud lane (no browser control on Alan's machine, and Slack app creation is admin-only in the UI).*

**🏁 RESULT WHEN DONE:** every new Instagram DM lead ManyChat captures posts instantly into **#ig-leads** with name, IG handle, what they asked, and the entry keyword/flow — so IG leads stop living only inside ManyChat.
**⏱ Timeline:** Step 0 Slack webhook (3 min, Alan) → Steps 1–3 ManyChat flow edit (10 min) → Step 4 test (2 min). ~15 minutes total, fully reversible (delete the action).

## STEP 0 — Slack incoming webhook for #ig-leads (Alan, one time, ~3 min)
1. https://api.slack.com/apps → **Create New App** → *From scratch* → name `APW IG Leads` → pick the APW workspace.
2. Left sidebar → **Incoming Webhooks** → toggle **On** → **Add New Webhook to Workspace** → choose **#ig-leads** → Allow.
3. Copy the `https://hooks.slack.com/services/...` URL. **Treat it as a password** — it goes ONLY into ManyChat and a local file on Alan's PC. Never into this repo, Notion, or a Slack message.
   *(If an `APW Call Outcomes` app already exists from the call-outcome build, reuse it: open it → Incoming Webhooks → Add New Webhook to Workspace → pick #ig-leads. One app can hold many webhooks, one per channel.)*

## STEP 1 — find the live IG flow in ManyChat (~2 min)
ManyChat → **Automation** → the Instagram flow that is currently capturing leads (the one behind the DM ads / comment-keyword). Open it and locate the step where the lead is *captured* — i.e. right after the user answers the qualifying question or their email/phone is stored. That is the notification point; earlier fires on tire-kickers, later loses drop-offs.

## STEP 2 — add the External Request action (~5 min)
1. In that flow, click **+** after the capture step → **Action** → **External Request** (ManyChat Pro feature; if the option is missing the account is on Free — upgrade or fall back to Step 5).
2. Method **POST** · Request URL = the Step-0 webhook URL.
3. **Headers:** `Content-Type: application/json`
4. **Body** (raw JSON) — insert each `{{...}}` via ManyChat's own merge-field picker, don't type them blind:
```json
{"text":"📸 *New IG lead* — {{first_name}} {{last_name}} (@{{ig_username}})\nAsked: {{last_input_text}}\nFlow: {{flow_name}} · Tags: {{tags}}\nEmail: {{email}} · Phone: {{phone}}"}
```
   Field names differ by account — use whatever the picker offers (e.g. `{{ig_username}}` may appear as `{{instagram_username}}`). Any field the picker doesn't have: delete that line rather than leaving a broken token.
5. Name the action `→ Slack #ig-leads`.

## STEP 3 — publish
Hit **Publish** on the flow. Unpublished edits never fire — this is the #1 reason a "built" ManyChat automation stays silent.

## STEP 4 — test before trusting (~2 min)
DM the IG account yourself (or use ManyChat's **Preview**) → run the flow to the capture step → confirm the message lands in **#ig-leads** with real values, not raw `{{tokens}}`. Raw tokens = the merge field doesn't exist on that account; fix in Step 2.4.

## STEP 5 — fallbacks if External Request isn't available
- **Zapier/Make:** ManyChat trigger *New Subscriber / Tag Added* → Slack *Send Channel Message* to #ig-leads. ~$0–20/mo, 10 min.
- **ManyChat → Google Sheet → Slack:** ManyChat's Google Sheets action appends the row; a Slack workflow watches the sheet. Slower (polling), free.
- **GHL bridge (preferred long-term):** if IG leads already flow into GHL, skip ManyChat entirely — a GHL workflow on `Tag Added = ig-lead` → Custom Webhook → the same Slack URL. Keeps all lead notifications on one rail with the call-outcome pings.

## Gotchas
- The webhook URL is a secret; if it leaks, regenerate it at api.slack.com and repaste into ManyChat.
- Invite whoever works IG leads into #ig-leads (Lynn, Carla) — an empty channel notifies nobody.
- ManyChat rate-limits External Requests on very high volume; at IG-DM scale this is irrelevant.
- Do NOT point this at #call-outcomes — different rail, different owner.
