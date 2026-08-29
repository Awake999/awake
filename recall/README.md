# Business comms recall

A workspace for answering questions about what was said inside the company —
who committed to what, when a decision was made, what a client was told.

Sources: **Fathom** (meeting recordings/transcripts) and **Slack**. Gmail,
Notion, Trello, Google Calendar and Zoom are connected to the session but are
not yet part of this system.

## Start here, in a new chat

1. Read `CLAUDE.md` at the repo root — the operating rules, especially the
   coverage-reporting requirement.
2. Read `recall/tools/fetch-transcripts.md` — how to get transcripts, and the
   one trap that has already caused a wrong answer.
3. Check `recall/findings/` — the question may already be answered.
4. Check `recall/index/` — if the window is already enumerated, you have your
   denominator for free.

## Layout

```
recall/
├── README.md                 you are here
├── index/                    what meetings exist, per window, with coverage status
├── findings/                 answered questions, with citations and scope
└── tools/
    ├── fetch-transcripts.md  procedure + the search_meetings trap
    ├── scan_transcripts.py   keyword scan with context
    └── scan_by_speaker.py    turns spoken BY a person — the decisive query
```

## The one thing that matters most

**`mcp__Fathom__search_meetings` does not search transcripts.** It reads titles
and AI summaries only.

On 2026-08-29 this produced a confirmed false negative: a search of 71 meetings
for "Saturday" returned zero hits, while the relevant exchange sat verbatim in a
transcript whose AI summary simply did not mention it. The first answer was
wrong. Full write-up: `recall/findings/2026-08-29-carla-saturday.md`.

If the question is *"did someone say X"*, you must read transcripts. There is no
shortcut and no full-text search.

## Standard workflow for a "did X say Y" question

```bash
# 1. Enumerate the window and record the count — this is your denominator.
#    mcp__Fathom__list_meetings(created_after=..., max_pages=12)

# 2. Dedupe: the same call appears once per recorder.

# 3. Pull transcripts (pass url= for clickable timestamp deep links).
#    Large ones auto-persist to disk; small ones come back inline and must be
#    read in the response — track those separately or you will under-scan.

# 4. Cache them locally (gitignored).
mkdir -p archive/transcripts
cp ~/.claude/projects/*/tool-results/*.{txt,json} archive/transcripts/ 2>/dev/null

# 5. Run all three scans — they answer different questions.
python3 recall/tools/scan_transcripts.py --dir archive/transcripts saturday weekend
python3 recall/tools/scan_by_speaker.py  --dir archive/transcripts --speaker Carla saturday weekend
python3 recall/tools/scan_by_speaker.py  --dir archive/transcripts --speaker Carla --invert --mentions saturday weekend
```

Scan 2 answers "did they say it". Scan 3 catches someone *else* putting words in
their mouth — which is exactly what happened in the Carla case, where the belief
traced to Alan's own hedged message rather than anything Carla said.

## Slack

`from:<@USERID>` with **no keyword** is the strongest bound on "did X ever say
this" — it spans public channels, private channels, DMs and group DMs visible to
the account. Results paginate at 20; page to the end before claiming
completeness. Semantic search is available, so keyword-only queries miss
paraphrases.

## Writing a finding

One file per answered question in `recall/findings/`, named
`YYYY-MM-DD-short-slug.md`. It must contain:

- the answer, stated plainly up front
- the decisive evidence, quoted, with permalinks or `?timestamp=` deep links
- contradicting or complicating evidence, not omitted
- **coverage**: what was searched, how deep, and what was not
- any process lesson, especially if an earlier answer was wrong

A finding without a coverage section is not finished.

## Privacy

`archive/` is gitignored and must stay that way. Raw transcripts contain
consumer credit account numbers, client addresses, identity-theft case detail,
employee compensation and termination discussions, and credential references.
Fathom is the system of record and already stores them durably with its own
access controls; copying them into git adds exposure and no durability.

Findings and the index are safe to commit because they are metadata plus
narrowly quoted excerpts. Keep it that way — quote what the answer needs, not
whole passages, and never paste client account numbers or addresses into a
finding.
