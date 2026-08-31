# CHECKLIST — format + grading + limitations refinement (8/30 ~23:50)
*🗣️ Alan's exact words → 🤖 indented beneath, same column every line. Source: [the full prompt](https://github.com/Awake999/awake/blob/claude/new-session-1ofk4w/ops/prompts/2026-08-30-format-grading-refinement-spec.md).*

1. 🗣️ *"it did not do a line break... the bot head line is in a different place every single time. I need it to be in the same place... press Shift+Enter to drop it down one line, and I press Tab to indent it in"*
   - 🤖 Checklist format fixed: the 🤖 line is an indented sub-bullet under the quote — same column, every item, chat and files alike.
2. 🗣️ *"whenever something says like ops/prompts/blah... that should be a hyperlink... always the case for everything in the SOP"*
   - 🤖 SOP swept — every bare path is now a clickable link; rule enforced everywhere going forward.
3. 🗣️ *"There has to be a way to approach the thinking layer... I could copy-paste it manually if I want to, but I don't want to. I want to be part of the process and storage and growth"*
   - 🤖 Raw thinking is stored EMPTY by the platform (verified, unfixable from our side). Automatic replacement: a labeled 🧠 REASONING DIGEST written into every run's grade file — zero manual work for Alan; if the platform ever exposes thinking, the ledger auto-includes it.
4. 🗣️ *"we want this to be live for the other ones too, because the other lanes right now keep missing the whole checklist thing"*
   - 🤖 Lanes inherit via root CLAUDE.md at session start + LANE-SYNC; idle cloud lanes pick it up on their next pull (honest limit: can't force an idle container from here).
5. 🗣️ *"You're missing it too: you didn't respond with the buttons... Where are all those things?"*
   - 🤖 Miss logged (95b): turn breaks ate the closing reply. Hard rule now: no turn ends on a commit — the reply with buttons/footer is composed in the same turn.
6. 🗣️ *"at the very end there should be a link to this run's... execution, graded side by side against the actual SOP"*
   - 🤖 Every reply footer now links the run's grade file.
7. 🗣️ *"in that grading there should be an SOP saying, 'How do we approach the grading?'... did / did not / percentage / quality / why / link / before and after"*
   - 🤖 Grading SOP created with exactly those elements + the grade scale.
8. 🗣️ *"we should not have to scan a table left to right... all vertical and mobile-optimized"*
   - 🤖 Grade files are vertical stacks — thumb-scroll, no wide tables.
9. 🗣️ *"Reason why it didn't follow through the first time... what the limitations are and how to resolve those things effectively automatically"*
   - 🤖 Plain LIMITATIONS section in the grade file: 4 root causes, each with its automatic fix, so it stops recurring.
