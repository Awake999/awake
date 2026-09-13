# 🗄️ SOP HISTORY — every version, dated, read-only, rollback-ready
*Alan's spec ([verbatim](https://github.com/Awake999/awake/blob/claude/new-session-1ofk4w/ops/prompts/2026-08-30-sop-versioning-format-spec.md)), executed 8/31 under the 100% directive.*

**🏁 BRIEF:** snapshot before every SOP change + at every SOP creation · files named `SOP-vX.X-date-timeTZ` · chmod read-only · git history = second permanent layer.
**⏱ Ritual:** 📸 snapshot current → 🔍 cross-check it matches the newest file here → ✏️ edit the live SOP → 📸 nothing else touched → 💾 commit both.

- **Read-only, two layers:** files here are chmod 444 (copy/reference only) AND every version is permanently recoverable from git commits — nothing here is ever losable or silently editable.
- **Pre-edit cross-check (mandatory):** before modifying any SOP, confirm the live file matches the newest snapshot; a mismatch = stop and investigate (someone edited without the ritual).
- **Applies to ALL SOPs** — the main [ops/SOP.md](https://github.com/Awake999/awake/blob/claude/new-session-1ofk4w/ops/SOP.md) and every department SOP (architecture: ONE main SOP all lanes inherit + department SOPs — Design, Sales, Dispute — that extend it, never contradict it; each gets a one-line pointer in the main SOP + front door when born).
