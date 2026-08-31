#!/usr/bin/env python3
"""
Speaker-attributed scan: find turns spoken BY a named person that match a regex.

This is the decisive tool for "did X actually SAY this?" questions. A plain
keyword grep answers "was this topic discussed near X's name", which is a much
weaker claim and routinely produces false positives — someone else raising the
topic, or the person merely being mentioned.

Usage:
    python3 scan_by_speaker.py --dir <dir> --speaker Carla saturday weekend
    python3 scan_by_speaker.py --dir . --speaker "Alan" --invert deadline

    --invert   report turns by everyone EXCEPT the named speaker
    --mentions also require the speaker's name inside the matched turn
               (use with --invert to find "someone else talking about X")

Fathom transcript turn format:
    [MM:SS](https://fathom.video/calls/<id>?timestamp=<secs>) Speaker Name: text
"""
import argparse
import glob
import json
import os
import re
import sys

TURN = re.compile(
    r"\[(\d+:\d+(?::\d+)?)\]"
    r"\((https://fathom\.video/calls/\d+\?timestamp=\d+)\)"
    r"\s*([^:\n]{1,48}?):\s*"
)


def load(path):
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


def turns(text):
    """Yield (timestamp_label, deep_link, speaker, body) for each turn."""
    marks = list(TURN.finditer(text))
    for i, m in enumerate(marks):
        end = marks[i + 1].start() if i + 1 < len(marks) else len(text)
        yield m.group(1), m.group(2), m.group(3).strip(), text[m.end():end]


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
    ap.add_argument("--dir", default=".")
    ap.add_argument("--speaker", required=True,
                    help="substring of the speaker name, e.g. 'Carla'")
    ap.add_argument("--invert", action="store_true",
                    help="report turns by everyone EXCEPT --speaker")
    ap.add_argument("--mentions", action="store_true",
                    help="also require --speaker's name inside the turn body")
    ap.add_argument("--chars", type=int, default=700)
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
            continue
        scanned += 1
        for label, link, speaker, body in turns(text):
            is_target = args.speaker.lower() in speaker.lower()
            if is_target == args.invert:
                continue
            if not pattern.search(body):
                continue
            if args.mentions and args.speaker.lower() not in body.lower():
                continue
            hits += 1
            print(f"\n### [{label}] {speaker}\n    {link}")
            print("    " + body.strip()[:args.chars].replace("\n", " "))

    who = f"NOT {args.speaker}" if args.invert else args.speaker
    print(f"\n---\nScanned {scanned} transcript(s); "
          f"{hits} matching turn(s) spoken by {who}.")
    if not hits:
        print("No matches. Report this WITH the scope that produced it: "
              "which transcripts, which date window, which patterns.")


if __name__ == "__main__":
    main()
