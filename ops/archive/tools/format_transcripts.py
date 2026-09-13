#!/usr/bin/env python3
"""Archive formatting pass — makes every transcript human + AI friendly simultaneously.

Per Alan's SOP directive (2026-08-30): no giant blocks of text; easy to navigate;
verbatim content NEVER altered. This tool only ADDS structure:
  1. a chapter heading every CHAPTER_SECONDS of meeting time
  2. a clickable table of contents under the file header
  3. files larger than SPLIT_BYTES are split into transcript-part-N.md files,
     and transcript.md becomes the index (header + parts + full chapter TOC)

Idempotent: files carrying the FORMAT_MARK are skipped, so it can run on every
archiving pass ("constant updates"). Raw originals (transcript-raw.*) are never touched.

Usage:  python3 ops/archive/tools/format_transcripts.py [archive_root]
"""
import os, re, sys, glob

CHAPTER_SECONDS = 600          # one chapter per 10 minutes of meeting time
SPLIT_BYTES = 150_000          # files bigger than this get split into parts
PART_TARGET = 110_000          # aim for parts around this size
FORMAT_MARK = "<!-- formatted: chapters-v1 -->"

TS_PATTERNS = [
    re.compile(r'^\*\*[^*]+\*\* \[(\d+):(\d{2}):(\d{2})\]'),     # Zoom: **Name** [HH:MM:SS]
    re.compile(r'^\[(\d+):(\d{2}):(\d{2})(?:\.\d+)?\]'),          # Zoom VTT: [HH:MM:SS.mmm] / Fathom [H:MM:SS](url)
    re.compile(r'^\[(\d+):(\d{2})\]\(http'),                     # Fathom: [MM:SS](url)
    re.compile(r'^\*\*[^*|]+ \| (\d+):(\d{2})(?::(\d{2}))?\*\*'),# Krisp: **Name | MM:SS**
    re.compile(r'^\[(\d+):(\d{2})\] '),                          # audio: [MM:SS] text
]

def line_ts(line):
    for i, pat in enumerate(TS_PATTERNS):
        m = pat.match(line)
        if not m:
            continue
        g = [x for x in m.groups() if x is not None]
        if len(g) == 3:                                           # HH:MM:SS
            return int(g[0]) * 3600 + int(g[1]) * 60 + int(g[2])
        return int(g[0]) * 60 + int(g[1])                         # MM:SS
    return None

def fmt(sec):
    if sec >= 3600:
        return f"{sec // 3600}:{sec % 3600 // 60:02d}:{sec % 60:02d}"
    return f"{sec // 60:02d}:{sec % 60:02d}"

def slug(text):
    s = text.lower()
    s = re.sub(r'[^\w\s-]', '', s)
    return re.sub(r'[\s]+', '-', s.strip())

def chapterize(body_lines):
    """Insert chapter headings; returns (new_lines, chapters=[(title, line_idx)]).
    A timestamp going backwards means a new recording segment — chapter resets there too."""
    out, chapters = [], []
    n, boundary, prev = 0, 0, -1
    for line in body_lines:
        ts = line_ts(line)
        if ts is not None and (ts >= boundary or ts < prev - 300):
            n += 1
            start = ts - (ts % CHAPTER_SECONDS) if ts >= boundary else ts
            title = f"Chapter {n} ({fmt(start)} to {fmt(start + CHAPTER_SECONDS)})"
            out.append("")
            out.append(f"## {title}")
            out.append("")
            chapters.append((title, len(out) - 2))
            boundary = start + CHAPTER_SECONDS
        if ts is not None:
            prev = ts
        out.append(line)
    return out, chapters

def process(path):
    txt = open(path, encoding="utf-8").read()
    if FORMAT_MARK in txt:
        return "skip"
    lines = txt.split("\n")
    # header = up to and including the first '---' rule; body = the rest
    try:
        sep = next(i for i, l in enumerate(lines) if l.strip() == "---")
    except StopIteration:
        sep = 0
    header, body = lines[: sep + 1], lines[sep + 1 :]
    if sum(1 for l in body if line_ts(l) is not None) < 12:
        return "no-ts"                                            # nothing to chapter
    body, chapters = chapterize(body)
    if len(chapters) < 2:
        return "short"
    toc = ["", FORMAT_MARK, "", "### Contents", ""]
    size = len(txt.encode())
    if size <= SPLIT_BYTES:
        toc += [f"- [{t}](#{slug(t)})" for t, _ in chapters]
        open(path, "w", encoding="utf-8").write("\n".join(header + toc + [""] + body) + "\n")
        return f"chaptered ({len(chapters)} chapters)"
    # --- split into parts ---
    folder, name = os.path.split(path)
    stem = name[: -len(".md")]
    parts, cur, cur_size, cur_ch = [], [], 0, []
    ch_bounds = [idx for _, idx in chapters] + [len(body)]
    for k, (title, idx) in enumerate(chapters):
        seg = body[(0 if k == 0 else idx) : ch_bounds[k + 1]]   # part 1 keeps any preamble
        seg_size = len("\n".join(seg).encode())
        if cur and cur_size + seg_size > PART_TARGET:
            parts.append((cur, cur_ch)); cur, cur_size, cur_ch = [], 0, []
        cur += seg; cur_size += seg_size; cur_ch.append(title)
    if cur:
        parts.append((cur, cur_ch))
    total = len(parts)
    for pn, (seg, chs) in enumerate(parts, 1):
        pname = f"{stem}-part-{pn}.md"
        phead = [f"# {stem} — Part {pn} of {total}", "",
                 f"Split per the formatting SOP for navigability — content verbatim, order preserved. Index: [{name}]({name}). Raw original untouched beside it.",
                 "", FORMAT_MARK, "", "---"]
        open(os.path.join(folder, pname), "w", encoding="utf-8").write("\n".join(phead + seg) + "\n")
    idx_toc = ["", FORMAT_MARK, "",
               f"**This transcript is split into {total} parts for navigability (content verbatim, nothing removed).**", "",
               "### Parts & chapters", ""]
    for pn, (seg, chs) in enumerate(parts, 1):
        pname = f"{stem}-part-{pn}.md"
        idx_toc.append(f"- **[Part {pn}]({pname})**")
        idx_toc += [f"  - [{t}]({pname}#{slug(t)})" for t in chs]
    open(path, "w", encoding="utf-8").write("\n".join(header + idx_toc) + "\n")
    return f"SPLIT into {total} parts ({len(chapters)} chapters)"

def main():
    root = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), "..")
    targets = sorted(glob.glob(os.path.join(root, "calls", "**", "transcript.md"), recursive=True)) + \
              sorted(glob.glob(os.path.join(root, "slack", "audio", "files", "*.transcript.md")))
    for p in targets:
        r = process(p)
        if r not in ("skip",):
            print(f"{r:35s} {os.path.relpath(p, root)}")

if __name__ == "__main__":
    main()
