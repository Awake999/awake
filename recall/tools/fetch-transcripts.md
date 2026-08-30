# Fetching Fathom transcripts into a local cache

The scan tools in this directory operate on transcripts cached on disk. This is
how to get them there, and why the obvious shortcut does not work.

## The trap (read this first)

`mcp__Fathom__search_meetings` searches **titles and AI summaries only**. It
never touches transcript text.

This has already produced one confirmed false negative in this workspace: a
relevant exchange existed verbatim in a transcript, but was absent from that
same meeting's AI summary, so a summary-level search returned zero hits and the
first answer given was wrong. See
`recall/findings/2026-08-29-carla-saturday.md`.

**A summary-level search is not evidence of absence.** If the question is "did
someone say X", you must read transcripts.

## Procedure

### 1. Enumerate the window

```
mcp__Fathom__list_meetings(created_after="2026-08-21T00:00:00Z", max_pages=12)
```

Returns `recording_id`, title, date, recorder, and sometimes
`calendar_invitees`. Record the full list before reading anything — the meeting
count is the denominator of every coverage claim you will later make.

### 2. Dedupe

The same call appears once per recorder, as separate `recording_id`s. Adjacent
IDs on the same date with the same title are the tell; confirm by comparing the
first minute of dialogue. Deduping typically removes 10–15% of the list.

### 3. Triage, but do not trust the triage

Set aside external prospect/client sales calls if the question is internal.
**Say that you did.** Everything else gets read.

### 4. Pull transcripts

```
mcp__Fathom__get_meeting_transcript(recording_id=<id>, url=<url>)
```

Passing `url` yields clickable `?timestamp=` deep links in the output — always
pass it, so findings can be cited to the second.

Transcripts over ~45KB auto-persist to a file under
`~/.claude/projects/<project>/tool-results/` and the tool returns the path
instead of the content. **This is the good path** — it keeps context free and
makes the transcript greppable. Smaller ones come back inline and must be read
in the response.

> Because inline transcripts never touch disk, the disk-based scanners below
> will not see them. Track which ones came back inline and account for them
> separately, or you will silently under-scan.

### 5. Copy the cache somewhere stable

```bash
mkdir -p archive/transcripts
cp ~/.claude/projects/*/tool-results/*.txt \
   ~/.claude/projects/*/tool-results/*.json archive/transcripts/ 2>/dev/null
```

`archive/` is gitignored. See "Archiving" below.

### 6. Scan

```bash
# every mention of a topic, with context
python3 recall/tools/scan_transcripts.py --dir archive/transcripts \
    saturday weekend sunday

# only turns actually SPOKEN BY a person — the decisive query
python3 recall/tools/scan_by_speaker.py --dir archive/transcripts \
    --speaker Carla saturday weekend sunday

# someone ELSE talking about that person
python3 recall/tools/scan_by_speaker.py --dir archive/transcripts \
    --speaker Carla --invert --mentions saturday weekend
```

Run all three. They answer different questions, and conflating them is how a
"nobody said that" conclusion goes wrong.

## Archiving: the scratch cache vs. the real archive

`/archive/` at the repo root is gitignored deliberately. It is a **per-session
scratch cache** — raw tool output, kept only so the scanners have something to
grep — and it is not the archive of record.

The repo's durable, committed archive is **`ops/archive/`** (Lane 3,
append-only, per the lane law in `CLAUDE.md`). If a call belongs in the
permanent record, it goes there through Lane 3's process, not by committing this
scratch directory.

**Check `ops/archive/calls/fathom/INDEX.md` before fetching anything** — the
call may already be archived, which saves a fetch and gives you a curated
transcript alongside the raw original.

Whichever store you are in, treat raw transcripts as sensitive. They routinely
contain:

- consumer credit account numbers and partial identifiers
- client full names with home addresses
- identity-theft and SSN case detail
- employee compensation, performance, and termination discussions
- references to credentials and login procedures

Anything committed becomes effectively permanent — rewriting history across
clones is not a real remedy. So quote narrowly in findings, and never paste
account numbers or home addresses into a summary document.

**What `recall/` persists** is the *index* (which meetings exist, and how much
of each window was actually read), the *method* (these scripts), and the
*findings* (what was concluded, with citations). Those are what die with an
ephemeral container.
