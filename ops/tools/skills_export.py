#!/usr/bin/env python3
"""Regenerate ops/skills-export/ from the live sources and zip the Claude skills for upload."""
import pathlib, shutil, zipfile
R = pathlib.Path(__file__).resolve().parents[2]; E = R/"ops/skills-export"
pairs = {
 "claude/apw-ops-protocol/SKILL.md": ".claude/skills/apw-ops-protocol/SKILL.md",
 "claude/apw-ops-protocol/reference/SOP.md": "ops/SOP.md",
 "claude/apw-ops-protocol/reference/RULINGS.md": "ops/RULINGS.md",
 "claude/apw-ops-protocol/reference/RESPONSE_TEMPLATE.md": "ops/RESPONSE_TEMPLATE.md",
 "claude/apw-ops-protocol/reference/LANE_COMPLIANCE_TEST.md": "ops/LANE_COMPLIANCE_TEST.md",
 "claude/client-testimonials/SKILL.md": ".claude/skills/client-testimonials/SKILL.md",
 "claude/client-testimonials/CLIENT_TESTIMONIALS_SOP.md": "ops/sops/CLIENT_TESTIMONIALS_SOP.md",
 "gpt/knowledge/SOP.md": "ops/SOP.md", "gpt/knowledge/RULINGS.md": "ops/RULINGS.md",
 "gpt/knowledge/RESPONSE_TEMPLATE.md": "ops/RESPONSE_TEMPLATE.md",
 "gpt/knowledge/CLIENT_TESTIMONIALS_SOP.md": "ops/sops/CLIENT_TESTIMONIALS_SOP.md",
}
for dst, src in pairs.items():
    (E/dst).parent.mkdir(parents=True, exist_ok=True); shutil.copy(R/src, E/dst)
for f in ("gpt/APW_OPS_PROTOCOL.instructions.md", "gpt/CLIENT_TESTIMONIALS.instructions.md"):
    n = len((E/f).read_text()); print(f, n, "chars", "OK" if n <= 8000 else "OVER GPT 8000 LIMIT")
with zipfile.ZipFile(E/"apw-skills-claude.zip", "w", zipfile.ZIP_DEFLATED) as z:
    for p in sorted((E/"claude").rglob("*")):
        if p.is_file(): z.write(p, p.relative_to(E/"claude"))
print("zip:", E/"apw-skills-claude.zip")
