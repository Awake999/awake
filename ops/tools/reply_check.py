#!/usr/bin/env python3
"""reply_check.py — the literal pre-send scan (SOP v1.20 §8j).

Four inspections in a row recommended mechanizing this and four times it was
logged instead of built. This is the build. Run it on a DRAFTED reply before
sending; it greps for the actual strings, so nothing can be certified from memory.

    python3 ops/tools/reply_check.py draft.md            # file
    python3 ops/tools/reply_check.py - < draft.md        # stdin
    python3 ops/tools/reply_check.py draft.md --new-prompt   # Alan sent a new prompt this turn

Exit 0 = ships. Exit 1 = does not ship. FLOOR failures are fatal; CONDITIONAL
failures are fatal unless the reply prints an explicit "n/a — reason".
"""
import sys, re

def main():
    args = [a for a in sys.argv[1:]]
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
