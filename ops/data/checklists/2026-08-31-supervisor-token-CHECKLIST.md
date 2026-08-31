# CHECKLIST — supervisor + token optimization + compliance gap (8/31)
*🗣️ Alan's exact words → 🤖 indented beneath. Source: [the full prompt](https://github.com/Awake999/awake/blob/claude/new-session-1ofk4w/ops/prompts/2026-08-31-supervisor-token-spec.md). Alan: "Let's work together... Turn this into a system."*

1. 🗣️ *"Make sure this is all updated into the SOP"*
   - 🤖 Confirmed — grade-file redesign + brief/timeline landed as SOP v1.5; this run ships v1.6.
2. 🗣️ *"figure out why there are some communication issues with the SOP, with this Claude version versus the local version. Even though I keep pointing it to it"*
   - 🤖 Diagnosed [V]: the SOP auto-loads only when a session STARTS inside the repo folder (CLAUDE.md is the loader). A local chat opened elsewhere or on a stale clone never loads it; mid-chat pointing is weaker than start-time loading. Fix = §1.12 bootstrap ritual (open in repo → git pull → read CLAUDE.md → confirm SOP version).
3. 🗣️ *"Is there not a part in the SOP where, at the very end, you're then giving me buttons?... token usages, the effort levels, or the modes"*
   - 🤖 Yes — all already law (§1.9 steps 5, 8). The failure was execution, not missing rules — see item 6.
4. 🗣️ *"go back and check what we are actually missing... 1. Identify. 2. Resolve. 3. Execute."*
   - 🤖 Audited every §1.9 step against recent replies: rules complete; compliance broke at (a) turn segmentation cutting closing replies, (b) replies written from memory instead of a template. Both resolved mechanically (items 6–7), executed this run.
5. 🗣️ *"Add to the SOP some type of token optimization... token tracking all the way through... sub-analysis and micro-analysis for each different task... These could all be done with Sonnet... export them out into a file"*
   - 🤖 §1.11 TOKEN OPTIMIZATION added + the segmentation file: 8 recurring task types classified Sonnet-eligible with a ready paste-brief for a Sonnet-only chat; 4 classified Fable-required; tracking rule on every reply/cycle/grade.
6. 🗣️ *"you did not even use your own SOP. Help me identify why... we just created it and then we did not succeed in executing it"*
   - 🤖 Honest root cause: (1) turn breaks — the harness sometimes ends a work turn at a tool call, so the composed closing never renders (the buttons you never saw existed as intent, not output); (2) memory-based compliance — rules on disk don't force themselves into a reply written freehand. A rule can't fix a mechanism problem; a TOOL can.
7. 🗣️ *"Implement some type of agent... a trainer or someone over our shoulder or a coach... Supervisors... manager"*
   - 🤖 Built two layers (§1.9 8e): PREVENTION = every reply is the RESPONSE_TEMPLATE filled in (skipped step = visible hole); INSPECTION = every mastery cycle spawns a SUPERVISOR agent that reads the actual transcript, grades each reply slot-by-slot vs §1.9, and auto-files misses to the register. Coach before, inspector after.
8. 🗣️ *"Turn this into a system so we do not lose it... always successful... not going back in circles"*
   - 🤖 All of it on disk (SOP v1.6 + template + segmentation + CLAUDE.md loader), inherited by every session at start, inspected every cycle — memory-proof, compaction-proof.
