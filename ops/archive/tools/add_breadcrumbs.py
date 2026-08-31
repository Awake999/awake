#!/usr/bin/env python3
"""Breadcrumb pass — puts a 🧭 navigation line at the top of every archive file
so a human can always click backwards (file → its index → its category → Start Here).

Per Alan's SOP directive (2026-08-30): "Every navigation leads into another category,
which leads into a subcategory, which all have clickable links that are able to go
backwards and forwards."

Idempotent: files that already contain a "> 🧭" line are skipped, so it runs at the
end of every archiving session and only touches new files. Raw originals untouched.

Usage:  python3 ops/archive/tools/add_breadcrumbs.py
"""
import os, re, glob

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
MARK = "> 🧭"

def crumb_for(relpath):
    """Return the breadcrumb markdown for a file, or None if it shouldn't get one."""
    parts = relpath.split(os.sep)
    d = os.path.dirname(relpath)
    def rel(target):
        return os.path.relpath(target, d).replace(os.sep, "/")
    home = f"[Start Here]({rel('START-HERE.md')}) · [Archive home]({rel('README.md')})"
    if parts[0] == "calls" and len(parts) == 4:            # calls/<platform>/<call-folder>/<file>
        platform = parts[1]
        return f"{MARK} {home} · [Calls hub]({rel('calls/README.md')}) · **[⬆ back to {platform.capitalize()} index]({rel(f'calls/{platform}/INDEX.md')})**"
    if parts[0] == "slack" and parts[1] == "channels" and len(parts) == 4:
        return f"{MARK} {home} · [Slack hub]({rel('slack/README.md')}) · **[⬆ back to channel index]({rel('slack/channels/INDEX.md')})**"
    if parts[0] == "slack" and parts[1] == "audio" and parts[2] == "files":
        return f"{MARK} {home} · [Slack hub]({rel('slack/README.md')}) · **[⬆ back to audio inventory]({rel('slack/audio/README.md')})**"
    if parts[0] == "people" and parts[-1] != "README.md":
        return f"{MARK} {home} · **[⬆ back to People index]({rel('people/README.md')})**"
    if relpath in ("people/README.md", "ghl/README.md", "slack/audio/README.md", "SYNC.md", "SOP-formatting.md"):
        return f"{MARK} {home}"
    return None

def main():
    changed = 0
    for path in glob.glob(os.path.join(ROOT, "**", "*.md"), recursive=True):
        rel = os.path.relpath(path, ROOT)
        if os.sep + "tools" + os.sep in path:
            continue
        crumb = crumb_for(rel)
        if crumb is None:
            continue
        txt = open(path, encoding="utf-8").read()
        if MARK in txt:
            continue
        lines = txt.split("\n")
        # insert after the H1 (first line starting with '# '), else at the very top
        at = next((i + 1 for i, l in enumerate(lines) if l.startswith("# ")), 0)
        lines[at:at] = ["", crumb]
        open(path, "w", encoding="utf-8").write("\n".join(lines))
        changed += 1
    print(f"breadcrumbs added to {changed} files")

if __name__ == "__main__":
    main()
