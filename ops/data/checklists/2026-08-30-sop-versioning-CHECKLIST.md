# CHECKLIST — SOP versioning + checklist format refinement (8/30 late)
*Format per Alan's rule (refined 8/30): 🗣️ his exact quote · line break · 🤖 the AI's understanding beneath it, tied as one numbered pair. Verbatim source: [the full prompt](https://github.com/Awake999/awake/blob/claude/new-session-1ofk4w/ops/prompts/2026-08-30-sop-versioning-format-spec.md). Status: presented for confirm before execution.*

**1.** 🗣️ *"functionality first, right? Everything I say after this... functionality is most important"*

🤖 Standing priority: working function beats polish/ceremony in every deliverable.

**2.** 🗣️ *"I don't even see where the beginning of the run first started... I'm just going to assume that starts at a model line"*

🤖 Every protocol run opens with a visible 🏁 RUN-START line (model line first — confirmed good as-is).

**3.** 🗣️ *"Confirmation with the links... 'this is where your original wording was stored. This is where the checklist is stored,' and then the hyperlinks to both"*

🤖 Both links (verbatim prompt + checklist doc) appear at the top of every checklist response.

**4.** 🗣️ *"it makes me uneasy to see that there are actually no quotes here from what I said"*

🤖 Checklists must carry your exact words — a paraphrase-only checklist is a protocol violation.

**5.** 🗣️ *"put the quote of what I said and then underneath it maybe say, 'Your understanding of what that line meant'... tied together and have those physically in a document as well, too, that's hyperlinked. All this needs to be scan-friendly"*

🤖 THE NEW CHECKLIST FORMAT — quote → understanding pairs (this document is the first one), in the response AND in a linked file.

**6.** 🗣️ *"If you believe it will help and it'll not make things worse and not reduce from what was already done and said, that's good"*

🤖 My additions stay welcome, with a no-subtraction rule: they may never replace or shrink your words.

**7.** 🗣️ *"Number three is SOP confirmed integrated. That's good. You gave me a link to it, which is great."*

🤖 The confirm-with-link pattern is ratified; keep it.

**8.** 🗣️ *"one main SOP and then different lanes' SOPs or different departments' SOPs. That might be good. Factor that into the whole equation"*

🤖 SOP architecture: ONE main SOP (laws everyone inherits) + per-department SOPs (e.g. Design) that extend it, never contradict it.

**9.** 🗣️ *"all the SOPs, all the versions, are dated and saved into a folder... just so we can have a rollback"*

🤖 Every SOP version snapshotted into a history folder for rollback.

**10.** 🗣️ *"'Hey, save SOP' before any modifications are done... store that, date it, and version it. Store date, version number, and time as well, in a time zone"*

🤖 SAVE-BEFORE-MODIFY ritual: before ANY SOP edit, snapshot the current file named with date + time + timezone + version number.

**11.** 🗣️ *"store it in a folder, like 'history'"*

🤖 Folder: `ops/sop-history/` in the vault.

**12.** 🗣️ *"every time an SOP is created, dated, named, versioned, and stored in a backup folder... it's worth doubling up"*

🤖 Snapshot on CREATION too, not just before edits — deliberate redundancy.

**13.** 🗣️ *"in the beginning, there's a cross-check... 'The current SOP that I'm reading is this'... Does this align with the previous SOP's version that was stored most recently... before any changes"*

🤖 Pre-edit cross-check: current SOP must match the newest history snapshot before changes proceed; mismatch = stop and investigate.

**14.** 🗣️ *"Make sure the backup folder is read-only, so none of that stuff can be modified"*

🤖 History files marked read-only (chmod 444) + a policy line; honest limit: git itself can't hard-enforce read-only, but every historical version is also permanently recoverable from git commits — double protection.

**15.** 🗣️ *"store everything at the end of the process in the SOP as well"*

🤖 End of every protocol run: outcomes/refinements get written back into the SOP flow (and snapshotted).

**16.** 🗣️ *"that should apply not only for the main SOP but also for all continued SOPs in different departments"*

🤖 Versioning + history + cross-check rules bind ALL SOPs, main and departmental, current and future.
