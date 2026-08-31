#!/usr/bin/env python3
"""Render a DM's raw-pageN.txt captures into one chronological export.md.

Raw pages are newest-first as returned by the Slack API; this tool reads every
raw-page*.txt in a DM folder, strips each page's capture-metadata header
(everything before the first message line), reverses the message order, and
writes export.md with a header + the messages oldest-first, VERBATIM (content
lines are never altered). Raw pages are never modified (RAW-ORIGINALS law).

Usage: python3 ops/archive/tools/render_dm.py ops/archive/slack/dms/<person>/ "Title line"
Idempotent: overwrites export.md (a pure rendering of the raws) on each run.
"""
import sys, os, re, glob

MSG_RE = re.compile(r'^(.+?) <([^>]+)>: ')

def page_messages(path):
    """Split a raw page into message blocks, in file (newest-first) order."""
    lines = open(path, encoding='utf-8').read().split('\n')
    # skip metadata header: everything before the first line matching MSG_RE
    start = next((i for i, l in enumerate(lines) if MSG_RE.match(l)), None)
    if start is None:
        return []
    blocks, cur = [], []
    for l in lines[start:]:
        if MSG_RE.match(l) and cur:
            blocks.append('\n'.join(cur).rstrip())
            cur = [l]
        else:
            cur.append(l)
    if cur:
        blocks.append('\n'.join(cur).rstrip())
    return blocks

def main():
    folder = sys.argv[1].rstrip('/')
    title = sys.argv[2] if len(sys.argv) > 2 else os.path.basename(folder)
    pages = sorted(glob.glob(os.path.join(folder, 'raw-page*.txt')),
                   key=lambda p: int(re.search(r'raw-page(\d+)', p).group(1)))
    # pages are newest-first, and within each page messages are newest-first:
    # chronological order = reversed(concat(pages)) 
    all_blocks = []
    for p in pages:
        all_blocks.extend(page_messages(p))
    all_blocks.reverse()
    hdr = (f'# {title}\n\n'
           f'Rendered chronologically (oldest first) from {len(pages)} verbatim raw pages '
           f'([raw-page1.txt](raw-page1.txt) …) by tools/render_dm.py. '
           f'Message content is untouched; only the order is reversed for reading.\n\n---\n\n')
    out = os.path.join(folder, 'export.md')
    open(out, 'w', encoding='utf-8').write(hdr + '\n\n'.join(all_blocks) + '\n')
    print(f'{out}: {len(all_blocks)} messages from {len(pages)} pages')

if __name__ == '__main__':
    main()
