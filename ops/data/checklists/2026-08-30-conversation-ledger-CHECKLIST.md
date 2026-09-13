# CHECKLIST — conversation ledger + SOP-compliance footer (8/30 late night)
*🗣️ = Alan's exact words · 🤖 = the AI's understanding. Source: [the full prompt](https://github.com/Awake999/awake/blob/claude/new-session-1ofk4w/ops/prompts/2026-08-30-conversation-ledger-spec.md). Alan pre-authorized execution ("let's execute").*

**1.** 🗣️ *"we want stored data for everything... organized with pointers, URL links... pointing to different sections of the folders and how to navigate"*

🤖 Every stored surface carries clickable navigation to its neighbors — no orphan files.

**2.** 🗣️ *"All the user prompts in the timelines and the dates and the times... The AI responses... all records of AI thinking relative to that as well"*

🤖 A conversation ledger with all three layers, timestamped, chronological.

**3.** 🗣️ *"user prompts, AI thinking, and AI output, all expandable and collapsible"*

🤖 Exchange files use click-to-expand sections (GitHub-native) — prompt open, AI layers collapsed.

**4.** 🗣️ *"fully saved without missing one word somewhere in the files"*

🤖 The raw session JSONL (every word incl. tool calls) is the master; the ledger is the readable layer on top.

**5.** 🗣️ *"If I'm training a new employee... so easy that they don't even need training... instructions for that on the landing page... a brand-new, vanilla person with no experience"*

🤖 A README landing page: 3 icons, 3 clicks, zero code knowledge assumed.

**6.** 🗣️ *"the original prompts and the original chronological order as the main thing. As a separate, additional folder within that same space"*

🤖 ops/prompts/ (originals) stays the main thing; ops/archive/conversation/ is the organized companion folder.

**7.** 🗣️ *"number them, like 1, 2, 3... then the title... and then the date and the time... the very first thing is easily synchronizable"*

🤖 Filenames: NNN-user-prompt-YYYYMMDD-HHMMZ.md — number first for cross-referencing, then title, date, time.

**8.** 🗣️ *"the SOPs are not even being followed, even in these micro responses... at the end, you're supposed to say what the effort level is"*

🤖 Miss admitted and logged: recent micro replies dropped the model/effort line. Rule hardened: EVERY reply carries it, no size exception.

**9.** 🗣️ *"a quick, easy checklist saying, 'OK, hey, this is the SOP. We followed all these steps... check, check, check, boom'... collapsible... or just a link... we don't want to bloat everything"*

🤖 New standard footer: one compact SOP-compliance line (checks + links to SOP/checklist) at the end of every reply — expandable detail lives one click away.

**10.** 🗣️ *"where's the SOP? Where's the checklist?"*

🤖 Always answerable in one glance: the footer links both, every time.

**11.** 🗣️ *"We don't want to lose data, but we also want things to be efficient... with the means to go more advanced where necessary and to verify"*

🤖 Raw = complete, surface = lean, links = the bridge. That's the whole design rule.
