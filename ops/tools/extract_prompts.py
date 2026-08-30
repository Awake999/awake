#!/usr/bin/env python3
"""Extract Alan's verbatim user prompts from a Claude session JSONL into readable markdown.
Sustainable rule: rerun after archiving any session transcript. Usage:
  python3 ops/tools/extract_prompts.py <session.jsonl> >> ops/prompts/ALL_PROMPTS_FULL.md
"""
import json, sys

def texts(content):
    if isinstance(content, str):
        yield content
    elif isinstance(content, list):
        for b in content:
            if isinstance(b, dict) and b.get("type") == "text":
                yield b.get("text", "")

def is_noise(t):
    t = t.strip()
    return (not t or t.startswith("<system-reminder>") or t.startswith("[SYSTEM NOTIFICATION")
            or t.startswith("<local-command-caveat>") or t.startswith("<command-name>")
            or t.startswith("Caveat:") or t.startswith("<task-notification"))

def main(path):
    print("# ALL PROMPTS — Alan, verbatim, chronological\n")
    print(f"*Extracted from `{path.split('/')[-1]}` by ops/tools/extract_prompts.py. "
          "Originals govern over every summary (VERBATIM LAW).*\n")
    n = 0
    for line in open(path, encoding="utf-8", errors="replace"):
        try:
            e = json.loads(line)
        except Exception:
            continue
        if e.get("type") != "user":
            continue
        msg = e.get("message") or {}
        if msg.get("role") != "user":
            continue
        content = msg.get("content")
        # skip tool results (list items carrying tool_use_id)
        if isinstance(content, list) and any(isinstance(b, dict) and b.get("tool_use_id") for b in content):
            continue
        body = "\n".join(t for t in texts(content) if not is_noise(t)).strip()
        if not body:
            continue
        n += 1
        ts = e.get("timestamp", "")
        print(f"\n---\n\n## Prompt {n}" + (f" · {ts}" if ts else "") + "\n")
        print(body)
    print(f"\n\n*— {n} prompts extracted —*", file=sys.stderr)

if __name__ == "__main__":
    main(sys.argv[1])
