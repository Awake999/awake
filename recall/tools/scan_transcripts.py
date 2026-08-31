#!/usr/bin/env python3
"""
Keyword scan across cached Fathom transcripts, with surrounding context.

Fathom has NO full-text transcript search. `search_meetings` reads only titles
and AI summaries, so anything said in a call but absent from its summary is
invisible to it. This script is the substitute: fetch transcripts to disk, then
grep them here.

Usage:
    python3 scan_transcripts.py --dir <transcript_dir> saturday weekend sunday
    python3 scan_transcripts.py --dir . --context 400 "work.*weekend"

Each argument after the flags is a regex, OR'd together, case-insensitive.

Handles both shapes the Fathom MCP writes to disk:
  - plain .txt transcript dumps
  - .json arrays of {"type": "text", "text": "..."} blocks
"""
import argparse
import glob
import json
import os
import re
import sys


def load(path):
    """Return transcript text from a .txt or .json tool-result file."""
    raw = open(path, encoding="utf-8", errors="replace").read()
    try:
        parsed = json.loads(raw)
        if isinstance(parsed, list):
            return "\n".join(
                b.get("text", "") for b in parsed if isinstance(b, dict)
            )
    except (json.JSONDecodeError, ValueError):
        pass
    return raw


TURN = re.compile(r"\[\d+:\d+(?::\d+)?\]\(https://fathom\.video/calls/\d+\?timestamp=\d+\)")


def call_id(text):
    m = re.search(r"fathom\.video/calls/(\d+)", text)
    return m.group(1) if m else "unknown"


def is_transcript(text):
    """True only for a real single-meeting transcript.

    Guards against scanning our own scan output, notes, or any other file that
    happens to quote transcript excerpts. Such a file cites several different
    call IDs; a genuine transcript cites exactly one.
    """
    ids = set(re.findall(r"fathom\.video/calls/(\d+)", text))
    return len(ids) == 1 and len(TURN.findall(text)) >= 5


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("keywords", nargs="+", help="regex patterns, OR'd")
    ap.add_argument("--dir", default=".", help="directory of cached transcripts")
    ap.add_argument("--context", type=int, default=280,
                    help="characters of context each side of a hit")
    args = ap.parse_args()

    pattern = re.compile("|".join(args.keywords), re.I)

    files = sorted(
        glob.glob(os.path.join(args.dir, "*.json"))
        + glob.glob(os.path.join(args.dir, "*.txt"))
    )
    if not files:
        sys.exit(f"No transcripts found in {args.dir!r}")

    scanned = hits = 0
    for path in files:
        text = load(path)
        if not is_transcript(text):
            continue  # not a transcript (notes, scan output, etc.)
        scanned += 1
        found = list(pattern.finditer(text))
        if not found:
            continue
        print(f"\n===== call {call_id(text)}  ({os.path.basename(path)})"
              f"  — {len(found)} hit(s) =====")
        for m in found:
            hits += 1
            s = max(0, m.start() - args.context)
            e = min(len(text), m.end() + args.context)
            print(f"\n  [{m.group(0)}]")
            print("  " + text[s:e].replace("\n", " ").strip())

    print(f"\n---\nScanned {scanned} transcript(s); {hits} hit(s).")
    if not hits:
        print("No matches. State this result WITH the scope that produced it.")


if __name__ == "__main__":
    main()
