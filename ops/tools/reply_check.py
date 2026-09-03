#!/usr/bin/env python3
"""reply_check.py — the literal pre-send scan (SOP v1.20 §8j).

Four inspections in a row recommended mechanizing this and four times it was
logged instead of built. This is the build. Run it on a DRAFTED reply before
sending; it greps for the actual strings, so nothing can be certified from memory.

    python3 ops/tools/reply_check.py draft.md            # file
    python3 ops/tools/reply_check.py - < draft.md        # stdin
    python3 ops/tools/reply_check.py draft.md --new-prompt   # Alan sent a new prompt this turn
    python3 ops/tools/reply_check.py --review ops/data/X_REVIEW.md   # two-person review page (CHECKLIST SOP §6)

Exit 0 = ships. Exit 1 = does not ship. FLOOR failures are fatal; CONDITIONAL
failures are fatal unless the reply prints an explicit "n/a — reason".
"""
import sys, re

# ---------------------------------------------------------------------------
# --review : ops/sops/RELATIONSHIP_REVIEW_CHECKLIST_SOP.md §6
# Verifies a two-person review page row by row. Grep-level, no judgement.
# ---------------------------------------------------------------------------
FATHOM = r'https://fathom\.video/calls/\d+\?timestamp=\d+'
CONF = ('strong', 'moderate', 'weak')
TYPES = ('spoken', 'owned', 'shipped', 'given', 'blocked', 'unspoken')

def _cells(line):
    return [c.strip() for c in line.strip().strip('|').split('|')]

def review(text):
    fails = []
    rows = {'six': 0, 'unspoken': 0, 'structural': 0}
    for ln, line in enumerate(text.splitlines(), 1):
        if not line.startswith('| '):
            continue
        cells = _cells(line)
        rid = cells[0]
        # --- six-field rows: C#, A# (checklist) ---
        if re.fullmatch(r'[CA]\d+', rid):
            rows['six'] += 1
            if len(cells) != 6:
                fails.append(f'L{ln} {rid}: {len(cells)} fields, need 6'); continue
            _, point, quote, link, count, typ = cells
            if not point: fails.append(f'L{ln} {rid}: empty Point')
            if not re.search(r'\*".+"\*', quote): fails.append(f'L{ln} {rid}: Quote not an italic verbatim quote')
            if len(re.sub(r'[^\w\s]', '', quote).split()) > 45: fails.append(f'L{ln} {rid}: Quote > 40 words')
            if not re.search(FATHOM, link): fails.append(f'L{ln} {rid}: Link is not fathom.video/calls/<id>?timestamp=<sec>')
            m = re.match(r'\**(\d+)', count)
            if not m: fails.append(f'L{ln} {rid}: Count does not start with a number')
            else:
                n = int(m.group(1))
                links = len(re.findall(FATHOM, link)) + len(re.findall(FATHOM, count))
                if links < n: fails.append(f'L{ln} {rid}: Count {n} but only {links} link(s) — every count carries every link')
            if re.split(r'[^a-z]', typ.strip('*').lower())[0] not in TYPES: fails.append(f'L{ln} {rid}: Type "{typ}" not in {TYPES}')
        # --- unspoken rows: CU#, AU# ---
        elif re.fullmatch(r'[CA]U\d+', rid):
            rows['unspoken'] += 1
            if len(cells) != 5:
                fails.append(f'L{ln} {rid}: {len(cells)} fields, need 5 (ID·Inference·Quotes·Confidence·Disconfirmer)'); continue
            _, inf, quotes, conf, dis = cells
            nq = len(re.findall(FATHOM, quotes))
            if nq < 2: fails.append(f'L{ln} {rid}: unspoken row has {nq} quote link(s), needs ≥2')
            if re.split(r'[^a-z]', conf.strip('*').lower())[0] not in CONF: fails.append(f'L{ln} {rid}: confidence "{conf}" not strong/moderate/weak')
            if len(dis) < 5: fails.append(f'L{ln} {rid}: disconfirmer missing')
        # --- structural rows: S# must rest on named C/A rows or a link ---
        elif re.fullmatch(r'S\d+', rid):
            rows['structural'] += 1
            rest = ' '.join(cells[1:])
            if not (re.search(r'\b[CA]U?\d+\b', rest) or re.search(FATHOM, rest)):
                fails.append(f'L{ln} {rid}: structural row cites no C/A row and no link')
    # --- header must state what was not read ---
    head = '\n'.join(text.splitlines()[:12])
    if not re.search(r'\d+\s+(calls?\s+)?not\b|\bnot read\b', head, re.I):
        fails.append('header does not state the not-read count')
    # --- any fathom link without a timestamp inside a quote row is already caught; also flag malformed links anywhere ---
    bad = [u for u in re.findall(r'https://fathom\.video/calls/[^\s)\]]+', text)
           if not re.fullmatch(r'https://fathom\.video/calls/\d+(\?timestamp=\d+)?', u)]
    if bad: fails.append(f'{len(bad)} malformed fathom link(s): {bad[:3]}')
    print(f"rows checked: {rows['six']} six-field · {rows['unspoken']} unspoken · {rows['structural']} structural")
    for f in fails: print('FAIL  ' + f)
    print('-' * 60)
    if fails:
        print(f'DOES NOT SHIP — {len(fails)} failure(s).'); return 1
    print('SHIPS — every row quoted, linked, counted; unspoken rows grounded; header states not-read.'); return 0

def main():
    args = [a for a in sys.argv[1:]]
    if '--review' in args:
        files = [a for a in args if not a.startswith('--')]
        return review(open(files[0], encoding='utf-8').read())
    new_prompt = '--new-prompt' in args
    args = [a for a in args if not a.startswith('--')]
    src = args[0] if args else '-'
    text = sys.stdin.read() if src == '-' else open(src, encoding='utf-8').read()
    lines = [l for l in text.strip().splitlines() if l.strip()]
    last = lines[-1] if lines else ''

    checks = []   # (tier, name, passed, hint)

    # ---- FLOOR (SOP v1.19 §8i) — never bends ----
    # 1. model identity, and it must appear somewhere OTHER than the final line
    #    (inspection #5: slots 1 and 4 were satisfied by the same string)
    body = '\n'.join(lines[:-1])
    model_re = r'(Opus|Sonnet|Haiku|Fable)\s*\d'
    checks.append(('FLOOR', 'model identity stated in the body (not only the final line)',
                   bool(re.search(model_re, body, re.I)),
                   'put the serving model in the run-header or token line, not just the 🎚️ line'))
    # 2. token disclosure INCLUDING remaining budget
    # scan EVERY "token" occurrence, not just the first — a table header named
    # "Tokens" was shadowing the real disclosure line (found by the script's own
    # first live run, 2026-09-02)
    toks = [m.group(0).lower() for m in re.finditer(r'[Tt]okens?.{0,120}', text, re.S)]
    checks.append(('FLOOR', 'token line includes remaining budget',
                   any('remaining' in t for t in toks),
                   'write: **Tokens:** ~NK this run · ~N.NM session remaining'))
    # 3. options mirrored in text
    checks.append(('FLOOR', '🔘 OPTIONS list mirrored in text',
                   '🔘' in text and bool(re.search(r'^\s*\**\s*1[\.\)]', text, re.M)),
                   'add a 🔘 OPTIONS block with numbered forward choices'))
    # 4. bold 🎚️ line is the absolute last line
    checks.append(('FLOOR', '🎚️ model+effort line is the last line',
                   last.strip().startswith('**🎚️') or last.strip().startswith('🎚️'),
                   'nothing may follow the 🎚️ line'))

    # ---- CONDITIONAL — must appear, or print "n/a — reason" ----
    na = lambda kw: bool(re.search(kw + r'[^\n]{0,60}n/a\s*[—-]', text, re.I))
    if new_prompt:
        pair = ('🗣️' in text and '🤖' in text)
        checks.append(('COND', 'verbatim 🗣️ quote → 🤖 understanding pair',
                       pair or na('checklist'),
                       'quote Alan verbatim, then indent your understanding'))
    add = re.search(r'(my additions|additions)', text, re.I)
    checks.append(('COND', '"My additions" section present or explicitly n/a',
                   bool(add) or na('additions'),
                   'add "## My additions" or print "My additions: n/a — reason"'))
    # ---- EVIDENCE (rulings #24) ----
    has_num = bool(re.search(r'\b\d{2,}\b', text))
    has_link = 'http' in text
    checks.append(('EVID', 'claims carry at least one link when numbers are present',
                   (not has_num) or has_link,
                   'ruling #24: counts ship with names + a link to primary proof'))

    width = max(len(n) for _, n, _, _ in checks)
    fatal = 0
    for tier, name, ok, hint in checks:
        mark = 'PASS' if ok else 'FAIL'
        print(f"[{tier:5}] {mark}  {name.ljust(width)}" + ('' if ok else f"\n           ↳ {hint}"))
        if not ok:
            fatal += 1
    print('-' * 60)
    if fatal:
        print(f"DOES NOT SHIP — {fatal} failure(s). Fix, then re-run.")
        return 1
    print("SHIPS — floor intact, conditionals accounted for.")
    return 0

if __name__ == '__main__':
    sys.exit(main())
