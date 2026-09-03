# 📋 CHECKLIST SOP — how a two-person review is built (verbatim · linked · counted)
*v1.1 · 2026-09-03 · Owner: Lane 1 · Binding on every "review X and Y" / "both perspectives" / "what does X want" request. Register #170. Lives under SOP v1.21 as a domain SOP; Law 0 and RULING #24 (evidence law) apply in full.*

## 0. The standard in one line
**Nothing on the page is a paraphrase. Every point is a quote, with a one-tap link to the second it was said, and a count of how many times it was said.** Interpretation is allowed only in a section labelled as interpretation, and it must cite the quotes it rests on.

## 1. Sources — before anything is written
1. **Enumerate every recording the two people share.** `find_person` on each name, `recorded_by: anyone`. Do not stop at the calls one of them recorded — *"we've had meetings hosted by others too."* Log the total (e.g. "64 meetings with Carla").
2. **Classify each call:** (a) 1:1 between the two, (b) small group where they negotiate with each other, (c) large group where one of them speaks to the room. Read (a) and (b) in full. For (c), read every segment in which either of them addresses the other, with ±1 segment of context, and say so.
3. **Read means read.** Pull the transcript, read it end-to-end (chunked if long), and only then quote. A summary from the recorder's AI is never a source.
4. **Archive first, analyse second.** Every transcript read lands in `ops/archive/calls/fathom/<date>--<slug>--<id>/transcript.md` + `meta.md` (Vault law §8k). Group calls read partially get `meta.md` with the segments read named.
5. **State what was not read**, by count, in the page header.

## 2. Extraction — how each point is captured
Every point on the page is a row with **six fields**, no exceptions:

| Field | Rule |
|---|---|
| **ID** | `C#` (person 1), `A#` (person 2), `S#` (shared/structural) |
| **Point** | One sentence, present tense, in plain words |
| **Quote** | Verbatim, in *italics*, ≤ 40 words. Trim with "…", never rewrite |
| **Link** | `[Mon DD h:mm:ss](https://fathom.video/calls/<id>?timestamp=<sec>)` — the second the quote starts |
| **Count** | How many separate calls the same point was raised in, with the other links listed |
| **Type** | `spoken` · `owned` (self-criticism) · `shipped` / `given` (verifiable output) · `blocked` (named obstacle) · `unspoken` (see §4) |

Rules for the Quote field: the speaker's own words only; if two people say the same thing, quote both; if the transcript is garbled, quote what is there and mark `[transcript garbled]`.

## 3. Counting — "how many times" is data, not colour
- A theme's **count** is the number of *distinct calls* in which it appears, not the number of sentences.
- Every count carries every link. "Said 3×" with one link is a violation.
- Counts drive the order of the checklist: highest-count points first within each person's list.
- A point said once by one person and never again is still listed; its count is 1 and that is informative.

## 4. Desires and wishes — spoken and unspoken
Each person gets a **Desires** table with two halves:

**Spoken** — they said it. Quote + link + count. Examples: "I want to be closing as soon as possible."

**Unspoken** — they did not say it, but the record supports it. This is the only place interpretation is permitted, and each row must carry:
1. the inference in one sentence,
2. **at least two quotes** (with links) that ground it,
3. a **confidence label**: `strong` (both people's words point the same way, or the person said it to a third party), `moderate` (pattern across ≥3 calls), `weak` (single strong signal),
4. a one-line **disconfirmer** — what they said that cuts against it, if anything.

An unspoken desire with one quote and no disconfirmer is not allowed on the page.

## 5. Page order (fixed)
1. Source table (every call, link, length, who, read-in-full / segments-read)
2. TL;DR — ≤ 5 findings, each with a link
3. Person 1 — spoken points · owned · shipped · blocked · **Desires (spoken / unspoken)** · honest read
4. Person 2 — same
5. Unified plan — every requirement from both Desires tables must map to a numbered plan item; an unmet requirement is listed as unmet, not omitted
6. **The checklist** — C / A / S rows in the six-field format, counts descending
7. Method note — what was read, what was not, and the date

## 6. Pre-send check (script it)
Before the page ships, `python3 ops/tools/reply_check.py --review <file>` (built 2026-09-03, same commit as this SOP) verifies:
- every C/A row has all six fields, an italic verbatim quote ≤ 40 words, and a recognised Type;
- every link matches `fathom.video/calls/\d+\?timestamp=\d+`;
- every count ≥ 2 lists ≥ 2 links;
- every `unspoken` row has ≥ 2 quote links and a confidence label;
- every S row cites the C/A rows it rests on;
- the page header states the not-read count;
- no malformed fathom link anywhere on the page.
Exit 0 = ships. The method note records the run.

## 7. What this SOP forbids
- Quoting the recorder's AI summary as if it were the speaker.
- Paraphrasing a person's position without the quote beside it.
- Reporting a count without every link.
- Listing an "unspoken" desire that rests on one quote.
- Presenting interpretation outside the labelled sections.
- Shipping the page without archiving the transcripts it rests on.
