# The APW SOP in plain English
**What every rule actually means, why it exists, and what "done right" looks like.**
Source of truth: [ops/SOP.md](../SOP.md) v1.21 · rulings: [ops/RULINGS.md](../RULINGS.md) · template: [ops/RESPONSE_TEMPLATE.md](../RESPONSE_TEMPLATE.md). This page explains those files. It does not replace them.

## TLDR — the whole SOP in six sentences
1. Repeat back every single thing I asked, in my own words, before you do anything.
2. Prove every claim with a link and a date, or label it unknown.
3. Keep the raw original next to any summary you write.
4. Save everything to GitHub, and say where you saved it.
5. Tell me which model wrote the reply and what it cost.
6. End with numbered options I can answer with one number.

---

## Part 1 — Law 0: never miss anything
This is the law that outranks all the others. It exists because the expensive failure was never a wrong answer. It was an ask that quietly vanished.

| The rule | In plain English | What good looks like | What failure looks like |
|---|---|---|---|
| **Parse gate** | Before working, break my message into a numbered list. Every clause counts as its own item. | A message with three sentences becomes three numbered lines. | Answering "the gist" of a long message and dropping the second half. |
| **Nothing drops** | If you did not do one of them, print "NOT DONE — because X". | A visible line admitting the gap. | Silence on item 4, hoping nobody counts. |
| **Reprompt = failure** | If I have to ask twice, your first answer was wrong. Compare it to my literal words, name what you missed, fix only that. | "You asked for X, I delivered Y, here is X." | Re-delivering the same thing in a new font. |
| **No grouping** | One line per item. Never "17–22", never "etc.", never "and 5 others". | Six rows for six items. | One row saying "items 17–22: various". |
| **Do then check** | Do not tick a box for work you have not actually done yet. | Checkboxes that match reality. | A tidy checklist of things that do not exist. |
| **Literal first** | Give me exactly what I asked for, in the shape I asked for it. Your improvements come after, in their own section. | The deliverable, then "My additions". | A better idea instead of the thing I asked for. |
| **Self-audit** | Before sending, re-read my message and count. | The count matches. | Sending, then discovering the gap. |

## Part 2 — the eight laws, one at a time

**1. Checklist.** Every ask gets quoted back in my exact words before work starts. *Why:* quoting is the only proof you read it rather than guessed at it. *Done right:* a 🗣️ line with my words and a 🤖 line with your reading of them.

**2. Evidence.** Every claim carries a clickable link, the date, and the window you searched. *Why:* a number without a source cannot be checked, and an unverifiable number is worse than no number. *Done right:* "3 calls booked [link, Sep 9, searched Sep 1–9]". *The trap:* not finding something is not proof it does not exist. Say "not found in X" and name X.

**3. Verbatim.** My original words beat any summary of them, including your own. *Why:* summaries drift. The prompt is the contract.

**4. Tandem.** Every summary sits next to the raw original. *Why:* so I can check your reading against the source without going hunting.

**5. Truth.** Label everything verified, derived, or unknown. Never guess. Corrections get appended and dated, never quietly swapped in. *Why:* one invented number poisons every number beside it.

**6. Clickable.** Every reference in something a human reads is a real https link. *Why:* a file path I cannot click is homework.

**7. Options.** End with numbered next steps I can answer with one number. Never re-ask permission for work I already ordered. *Why:* momentum. Asking "shall I?" about work already ordered wastes a whole round trip.

**8. Scan-ready.** TLDR first, tables over paragraphs, state visible at a glance. *Why:* these get read on a phone between calls.

## Part 3 — the loop you run on every prompt
1. **Parse** — split my message into numbered asks.
2. **Present** — show me that list inside the reply.
3. **Store** — save it and say where. GitHub (`Awake999/awake`) is the spine.
4. **Add** — a "My additions" section with your suggestions, kept separate from my ask.
5. **Disclose** — which model, what effort, what it cost, what is left.
6. **Execute** — on my confirm, or straight away when I already ordered it.
7. **Scorecard** — one row per ask: done, %, quality, why, improvement, link, before→after.
8. **Close** — options, timeline, progress, final line.

## Part 4 — the floor (the four things that must be on every reply)
| # | The slot | Why it exists |
|---|---|---|
| 1 | Model line in the body | So I know whether a weak model wrote something that needed a strong one. |
| 2 | Token line with the word "remaining" | So I can see a long session running out of room before it does. |
| 3 | 🔘 OPTIONS numbered list | So my next move is one keystroke. |
| 4 | Bold 🎚️ NEXT line, absolutely last | So the recommended model and effort for the next step is always in the same place. |

## Part 5 — the rulings that catch people out
- **#23 Info first.** The answer comes before the process talk. Never open with "here is how I will approach this".
- **#24 Numbers carry their list.** "12 leads" must come with the 12 names.
- **#27 A digest is a top-3, not a roster.** This one was learned the hard way. A daily summary that lists three people is not a list of everyone being monitored. Never write "X is not covered" because X is missing from a summary. Missing from a summary means unknown.
- **#28 A percentage with an unknown denominator** gets labelled as such. "57% activity" is a digest headline, not a measure of productivity.
- **#30 Vault law.** Nothing counts as delivered until it is in GitHub and mirrored somewhere I can reach it. If a surface is unreachable, that becomes a named task, not a silent gap.
- **Media law.** Never edit a live, delivering ad.

## Part 6 — how to use this with each tool
| Tool | What to do | File |
|---|---|---|
| **Claude Code, this repo** | Nothing. It auto-loads. Type `/apw-ops-protocol`. | `.claude/skills/apw-ops-protocol/SKILL.md` |
| **Claude Code, any other repo** | Copy the skill folder into `~/.claude/skills/`. | `skills-export/claude/apw-ops-protocol/` |
| **claude.ai or Desktop** | Settings → Capabilities → Skills → upload the zip. | `skills-export/apw-skills-claude.zip` |
| **GPT-6, easiest route** | Paste one file into Instructions. Upload nothing. | `skills-export/gpt/APW_SOP_GPT6_ONE_FILE.md` |
| **GPT-6, full route** | Paste the instructions file, upload the four knowledge files. | `gpt/APW_OPS_PROTOCOL.instructions.md` + `gpt/knowledge/` |
| **ChatGPT global settings** | Paste the short version (fits the 1,500-character box). | `gpt/APW_OPS_PROTOCOL.custom-instructions-1500.md` |

## Part 7 — how to tell in ten seconds whether a reply followed the SOP
Read the reply bottom-up. If the last line is not a bold 🎚️ NEXT line, it failed. If there are no numbered options above it, it failed. If no line contains the word "remaining", it failed. If your own words are not quoted near the top, it failed. In this repo, `python3 ops/tools/reply_check.py <file>` runs exactly those checks for you.

## Keeping this honest
Edit the source files only (`ops/SOP.md`, `ops/RULINGS.md`, `ops/RESPONSE_TEMPLATE.md`, the skill files), then run `python3 ops/tools/skills_export.py`. This page and the GPT exports are regenerated from them.
