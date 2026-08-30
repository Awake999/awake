# SYNC — operating this archive from many devices and many chats at once, without ever losing data

The archive is a git repo. Git is what makes "multiple devices + multiple simultaneous Claude chats" safe: every copy is a full backup, history is permanent, and nothing merged is ever silently destroyed. These rules keep it that way.

## The five rules (for every human and every Claude lane)

1. **Pull before you start, push when you stop.** `git pull` at the start of a work session, `git push` after each batch. Small frequent commits — commits ARE the backup.
2. **Append-only.** Never rewrite or delete an existing archive file. Corrections and updates go in a NEW dated file next to the original (e.g. `meta-update-2026-09-02.md`). The only sanctioned in-place edits are flipping `no → yes` in an INDEX row and adding rows to inventory tables.
3. **Never force-push. Never `--force`, never `push -f`, never rebase shared history.** If git refuses your push, the answer is `git pull` then push again — not force.
4. **Coexistence on conflict.** If two copies of the same file ever collide (a real merge conflict, or "this file already exists with different content"): KEEP BOTH. Rename the incoming one with a suffix — `filename--variant-YYYY-MM-DD.md` — commit both, and add one line at the top of each pointing to its sibling. Never pick a winner by deleting; a human can reconcile later with both versions intact.
5. **Lanes own separate paths.** Parallel chats never write to the same folder: archive lane → `ops/archive/**`; data-ops lane → `ops/data`, `ops/checklists`, `ops/sops`; dashboard lane → `ops/dashboard`; each lane's own dated file in `ops/process-log/`. Slack exports are one file per channel per month and call folders are keyed by recording ID precisely so that simultaneous work almost never touches the same file.

## Setting up a new device (once per device)

```
git clone https://github.com/Awake999/awake.git
```

Then, for Obsidian on that device: Open folder as vault → select the `awake` folder. Optional but recommended: install the community plugin **Obsidian Git** and set it to auto-pull/auto-push every 10–15 minutes — then the vault syncs itself and rule 1 is automatic.

## Daily use on any device

- Before reading/working: `git pull` (or let Obsidian Git do it).
- After adding anything: commit with a plain-English message and `git push`.
- If push is rejected: `git pull` (git will merge cleanly because lanes touch different files), then `git push` again.

## Why nothing can be lost

- Every device's clone is a complete copy of every version of every file ever committed.
- GitHub (private) holds the same complete history in the cloud.
- Git never discards a committed version — even "changed" files keep every prior version retrievable (`git log -- path/to/file`).
- The rules above remove the only two real risks: force-pushes (rule 3) and overwrite-instead-of-coexist habits (rules 2 and 4).
