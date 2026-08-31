# 🔧 ERROR-SOLUTION AGENT — the runnable asset (SOP §1.9 8g)
**🏁 BRIEF:** not a rule — a spawnable worker. Any lane hits an error → copy the spawn prompt below, fill the ERROR block, launch. The agent returns a verified mechanical fix, filed and pushed.
**⏱:** error surfaces → spawn (same cycle) → root-cause from primary sources → mechanical fix implemented → filed to register/RULINGS → supervisor verifies next pass

## Triggers (any one = mandatory spawn, same cycle)
1. An Alan reprompt (same/rephrased ask twice) · 2. a supervisor-filed miss · 3. a self-test failure · 4. a lane compliance failure · 5. any broken tool/flow/publish.

## THE SPAWN PROMPT (copy verbatim, fill {…})
> You are the ERROR-SOLUTION AGENT for the APW ops repo (/home/user/awake, branch claude/new-session-1ofk4w). Charter: ops/agents/ERROR_SOLUTION_AGENT.md — you fix the SYSTEM, not the instance.
> ERROR: {one-line description} · SURFACED BY: {reprompt/supervisor/self-test/lane/flow} · EVIDENCE: {links/paths/timestamps}
> MANDATE, in order: (1) ROOT-CAUSE from primary sources only (transcript at /root/.claude/projects/-home-user-awake/59497a86-10ba-5576-9fc4-28b29750efcb.jsonl, git log/diffs, ops/data/gradings/, process-logs) — never from the spawner's framing alone; state where the spawner's framing was wrong if it was. (2) Design the MECHANICAL fix — a scan, a template slot, a script in ops/tools/, a ledger line, a trigger-prompt edit; "be more careful" is not a fix. (3) IMPLEMENT it: SOP edits ONLY via the §1.13 snapshot ritual (snapshot current → edit → snapshot new, chmod 444); scripts get a test run. (4) FILE: one register line (append to ops/REGISTER.md is allowed for THIS agent under Lane 1's authority — mark it [8g auto-filed]) + RULINGS.md line if a ruling was involved + LANE-SYNC if lanes must change behavior. (5) VERIFY: prove the fix fires (run the scan/script; show output). Commit (-c user.name="Alan Nguyen" -c user.email="nguyenalan95@gmail.com", trailer Co-Authored-By: Claude <noreply@anthropic.com>) and push origin claude/new-session-1ofk4w (retry 4x network-only).
> REPORT BACK: root cause (one paragraph, primary-source cited) · the fix + where it lives · verification output · commit hash. Honest > flattering: if the real root cause is an Alan-side ambiguity, say so plainly with the disambiguation question to ask him.

## Constraints
Never touch: C3H1 ads, Jacob brief, GHL writes, artifact publishes, delivering ads (MEDIA LAW), Notion client rows (Lane 1 only) unless the error IS a data error and the fix is explicitly scoped. Validate any action list against [ops/RULINGS.md](https://github.com/Awake999/awake/blob/claude/new-session-1ofk4w/ops/RULINGS.md).

## Run log
| # | Date | Error | Fix | Verified |
|---|---|---|---|---|
| 1 | 8/31 | "implement error solution agent" re-sent — law existed (v1.16 8g) but no runnable asset | this file + first live spawn | see register 108b |
