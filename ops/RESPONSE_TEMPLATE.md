# 📐 RESPONSE TEMPLATE — every Alan-facing reply is built by filling THIS skeleton
*The mechanical fix for "we created the SOP but didn't follow it": a reply isn't written from memory, it's this file filled in. Skipping a slot = visible hole. [SOP §1.9](https://github.com/Awake999/awake/blob/claude/new-session-1ofk4w/ops/SOP.md) is the law; this is the tool that makes it automatic.*

```
🏁 RUN START · Model: <model> · <effort> (session-verified) · rerun needed? <no/yes+why>
📜 [Your words, stored verbatim](<prompt file link>) · ✅ [This checklist as a file](<checklist file link>)

## Your words → my understanding
1. 🗣️ *"<exact quote>"*
   - 🤖 <understanding>
...one pair per ask, nothing grouped...

## My additions (help-only, nothing subtracted)
- <suggestion(s)>

## Tokens/effort (raw → plan → options)
<session used/remaining · est. cost of this run · Sonnet-eligible? per ops/data/TOKEN_SEGMENTATION.md>

<IF not yet approved: ask-to-execute question. IF executing: what got done, with links.>

## ⏱️ Progress
micro <bar+%> · macro <bar+%, register count>

---
📋 SOP check: model ✓ · links ✓ · checklist ✓ · additions ✓ · tokens ✓ · scorecard→[run grade ↗](<grade file>) · buttons ✓ · [SOP](https://github.com/Awake999/awake/blob/claude/new-session-1ofk4w/ops/SOP.md)
<AskUserQuestion buttons — live replies. Scheduled runs: "Reply with any of: ..." line>

**🎚️ NEXT: <model> · <effort> — <5-word reason>**   ← THE LAST LINE, ALWAYS
```

**Hard rules baked in:** the reply text ships in the SAME turn as the last tool call (8d) · fill EVERY slot or write "n/a — why" · micro replies still carry line 1 and the footer.
