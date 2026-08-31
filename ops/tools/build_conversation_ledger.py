#!/usr/bin/env python3
"""Build the human-readable conversation ledger from a raw session JSONL.
Output: ops/archive/conversation/ — README + 000-INDEX.md + exchanges/NNN-*.md
Each exchange file: the user's prompt VERBATIM (open) + collapsible AI thinking + collapsible AI output.
The raw JSONL stays the no-word-lost master; tool calls/results live only there."""
import json, os, re, sys, html

SRC = sys.argv[1] if len(sys.argv) > 1 else 'ops/prompts/transcripts/session-59497a86-full.jsonl'
OUT = 'ops/archive/conversation'
EX = os.path.join(OUT, 'exchanges')
os.makedirs(EX, exist_ok=True)

def clean_user(content):
    """Return user-visible text, or None if this isn't a real user message."""
    if isinstance(content, str):
        txt = content
    elif isinstance(content, list):
        parts = [b.get('text','') for b in content if isinstance(b,dict) and b.get('type')=='text']
        if not parts: return None
        txt = '\n'.join(parts)
    else:
        return None
    txt = re.sub(r'<system-reminder>.*?</system-reminder>', '', txt, flags=re.S)
    txt = txt.strip()
    if not txt: return None
    if txt.startswith('[Request interrupted') or txt.startswith('Caveat:'): return None
    if txt.startswith('<local-command') or txt.startswith('<command-name>'): return None
    if txt.startswith('<task-notification') or txt.startswith('[SYSTEM NOTIFICATION'): return None
    if txt.startswith('This session is being continued'): return None
    if txt.startswith('Continue from where you left off'): return None
    return txt

events = []  # (ts, kind, text)
with open(SRC) as fh:
    for line in fh:
        try: d = json.loads(line)
        except Exception: continue
        t, ts = d.get('type'), d.get('timestamp','')
        if t == 'user':
            txt = clean_user(d.get('message',{}).get('content'))
            if txt: events.append((ts,'user',txt))
        elif t == 'assistant':
            for b in (d.get('message',{}).get('content') or []):
                if not isinstance(b,dict): continue
                if b.get('type') == 'thinking' and b.get('thinking','').strip():
                    events.append((ts,'think',b['thinking'].strip()))
                elif b.get('type') == 'text' and b.get('text','').strip():
                    events.append((ts,'out',b['text'].strip()))

# group into exchanges: each user event opens a new exchange
exchanges, cur = [], None
for ts,kind,txt in events:
    if kind == 'user':
        cur = {'ts':ts,'prompt':txt,'think':[],'out':[]}
        exchanges.append(cur)
    elif cur is not None:
        cur['think' if kind=='think' else 'out'].append((ts,txt))

def fname(i, ts):
    stamp = re.sub(r'[-:]','',ts[:16]).replace('T','-')
    return f"{i:03d}-user-prompt-{stamp}Z.md"

def det(summary, items):
    if not items: return ''
    body = '\n\n---\n\n'.join(f"*{ts[11:19]}Z*\n\n{txt}" for ts,txt in items)
    return f"<details><summary>{summary}</summary>\n\n{body}\n\n</details>\n"

index = ["# 🗂️ CONVERSATION INDEX — every exchange, chronological",
 "*All times UTC (Z). One row per user prompt; click through for the full exchange (prompt verbatim + collapsible 🧠 thinking + 🤖 output). The raw master (tool calls included, zero words lost): [session JSONL](../../prompts/transcripts/session-59497a86-full.jsonl).*",
 "", "| # | Date | Time (UTC) | The prompt begins… | Open |", "|---|---|---|---|---|"]
for i,e in enumerate(exchanges,1):
    fn = fname(i, e['ts'])
    snippet = ' '.join(e['prompt'].split())[:90].replace('|','·')
    with open(os.path.join(EX,fn),'w') as f:
        f.write(f"# Exchange {i:03d} · {e['ts'][:10]} {e['ts'][11:19]} UTC\n")
        f.write(f"*[← index](../000-INDEX.md) · prev {max(i-1,1):03d} · next {i+1:03d} · 🗣️ = user's exact words · 🧠 = AI thinking · 🤖 = AI output*\n\n")
        f.write(f"## 🗣️ User prompt (verbatim)\n\n{e['prompt']}\n\n")
        f.write(det(f"🧠 AI thinking — {len(e['think'])} block(s), expand to read", e['think']))
        f.write('\n')
        f.write(det(f"🤖 AI output — {len(e['out'])} message(s), expand to read", e['out']))
    index.append(f"| {i:03d} | {e['ts'][:10]} | {e['ts'][11:19]} | {snippet}… | [open](exchanges/{fn}) |")
with open(os.path.join(OUT,'000-INDEX.md'),'w') as f: f.write('\n'.join(index)+'\n')
print(f"exchanges: {len(exchanges)} · thinking blocks: {sum(len(e['think']) for e in exchanges)} · output blocks: {sum(len(e['out']) for e in exchanges)}")
