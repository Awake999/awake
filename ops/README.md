# APW Ops Vault

Permanent, Obsidian-compatible storage for Ascend Prime Wealth operations — so context is **pointed to, not re-derived**. Every Claude session updates this vault: prompts, decisions, process, and data snapshots.

## Map

| Folder | Contents |
|---|---|
| `checklists/` | Master checklists (mirrors of the Notion originals) |
| `sops/` | SOP mirrors — qualification standard, dispute doctrine |
| `dashboard/` | The APW Command Board HTML (live-capable when published as a claude.ai artifact) |
| `process-log/` | Per-session log: what was decided, built, and why |
| `data/` | Pointer map to every system of record (Notion IDs, Drive files, key recordings) |

## Systems of record

- **Notion** = editable truth (Clients & Leads is the master lead table; edits there flow to the live dashboard)
- **This repo** = permanence + pointers
- **Fathom/Krisp** = call evidence
- **GHL** = booking/contact ground truth (pull is local-only — see the runbook pointer in `data/`)
