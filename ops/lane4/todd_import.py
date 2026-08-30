# -*- coding: utf-8 -*-
"""LANE 4 — TASK 2: the ONE approved GHL write (Alan authorized 8/12, re-confirmed).
Executes TODD_GHL_IMPORT.md sections 1-7 against existing contact nIy2smghNYT9II3enmQv.
Idempotent by design: updates the existing contact + existing opportunity trnXkuLcYMuTg4iDg8za.
"""
import json, time, urllib.request, urllib.parse, urllib.error, pathlib, sys

HERE = pathlib.Path(__file__).resolve()
REPO = HERE.parent.parent.parent
ENVF = REPO.parent / "apw-intel" / ".env"
ENV = dict(l.split("=", 1) for l in ENVF.read_text().splitlines() if "=" in l and not l.startswith("#"))
TOKEN, LOC = ENV["GHL_TOKEN"].strip(), ENV["GHL_LOCATION"].strip()
BASE = "https://services.leadconnectorhq.com"
CID = "nIy2smghNYT9II3enmQv"          # Todd LoGuidice (matched by toddloguidice@gmail.com in the 8/30 pull)
OPP = "trnXkuLcYMuTg4iDg8za"          # his existing SCIO Pipeline opportunity
PIPE = "2JlgwyCzR7AnFqYK4MNu"         # SCIO Pipeline
STAGE_CLOSED = "bd4f455e-2cc5-40c0-8fc0-306a88d5fbde"  # 'Closed' stage
LOG = []

def api(method, path, body=None, version="2021-07-28"):
    url = BASE + path
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, method=method, headers={
        "Authorization": f"Bearer {TOKEN}", "Version": version,
        "Accept": "application/json", "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"})
    for attempt in range(5):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                out = json.loads(r.read().decode() or "{}")
                LOG.append({"call": f"{method} {path}", "ok": True, "resp": out})
                return out
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503, 504):
                time.sleep(2 ** attempt); continue
            err = {"call": f"{method} {path}", "ok": False, "code": e.code, "body": e.read().decode()[:500]}
            LOG.append(err); print("ERROR", err, flush=True); return err
        except Exception as ex:
            time.sleep(2 ** attempt)
    err = {"call": f"{method} {path}", "ok": False, "code": "retries_exhausted"}
    LOG.append(err); return err

# ---- §1 + §2: contact fields + tags (merge with existing tags) ----
existing_tags = ["name via lookup", "call booked scio"]
new_tags = ["client", "closed-won", "personal-guarantor", "mlcs-holdings", "referral",
            "prime-protocol", "no-phone-on-file", "zero-upfront-4pct"]
# NOTE: GHL has a phone for Todd (+14154245720) that the package thought was missing —
# keep it; drop the no-phone-on-file tag would deviate from the BRIEF, so apply as written
# but record the discrepancy in the report.
r1 = api("PUT", f"/contacts/{CID}", {
    "firstName": "Todd", "lastName": "LoGuidice",
    "email": "toddloguidice@gmail.com",
    "companyName": "MLCS Holdings",
    "source": "Referral - Matt L. (brother, co-owner MLCS Holdings)",
    "tags": sorted(set(existing_tags + new_tags)),
})
print("contact update:", "OK" if r1.get("contact") or r1.get("ok", True) and "code" not in r1 else r1, flush=True)

# ---- §3: opportunity -> Closed (won), $0 upfront / 4% success ----
r2 = api("PUT", f"/opportunities/{OPP}", {
    "pipelineId": PIPE, "pipelineStageId": STAGE_CLOSED,
    "status": "won", "monetaryValue": 0,
    "name": "Todd LoGuidice - $0 upfront / 4% success fee (household deal w/ Matt L.)",
})
print("opportunity update:", "OK" if "code" not in r2 else r2, flush=True)

# ---- §4 + §5 + §6: notes (oldest first so the timeline reads chronologically) ----
notes = [
"""ROLE - WHAT TODD ACTUALLY IS (import 8/30 from TODD_GHL_IMPORT.md):
Todd is the credit half of a two-person structure. He co-owns MLCS Holdings (Delaware entity, foreign-filed CA) with his brother Matt L. and acts as PERSONAL GUARANTOR on the entity's funding while Matt's credit is in repair. His credit is the asset being underwritten. He is not a lead - he is a guarantor who became a client through the household deal. Business role: 85% owner as stated on the 7/31 applications (fathom.video/calls/769061378). Fee structure: $0 up front, 4% performance fee payable ONLY on successful funding, from the new funds. Agreement signed: Matt 7/2, Todd countersigned 7/31 (SendLink 'Todd - Matt - APW_Program_Agreement_v3 signed'). Terms source: fathom.video/calls/732157346.""",
"""TIMELINE 2026-06-30: Credit optimization + funding strategy set for Todd. Plan: apply for a 0% interest business card ($5-25K) from a no-seasoning bank; Matt to run the 'nuke' method to remove 4 hard inquiries across all three bureaus (4-day target). Evidence: fathom.video/calls/730356996""",
"""TIMELINE 2026-07-01: Agreement finalized: $0 down, 4% success fee. Strategy: Equifax-only and TransUnion-only cards, then inquiry removal to enable more applications. Evidence: fathom.video/calls/732157346""",
"""TIMELINE 2026-07-01: BLOCKER worked live: funding stalled pending a physical Social Security card. Online SSA application required in-person verification (next appt Aug 2026); resolved same call by submitting via ID.me after the standard portal failed to send a code. Emergency-appointment path also opened citing hardship. Evidence: fathom.video/calls/732184668""",
"""TIMELINE 2026-07-02: Matt signs the joint APW Program Agreement v3 ('Matthew Signed' email). Evidence: support@ mailbox""",
"""TIMELINE 2026-07-03: Entity strategy decided: foreign file the existing Delaware entity (MLCS Holdings) in Oakland using a vetted virtual address (vs. Matt buying a separate aged CO LLC as an SPV). Evidence: fathom.video/calls/734613825""",
"""TIMELINE 2026-07-14: MLCS profile optimization for a $300K goal. CRITICAL: a $20 Delaware public-record pull revealed an $85,000 franchise tax assessment - must be corrected by the filing agent (Harvard Business Services) before applying. Evidence: fathom.video/calls/747196033""",
"""TIMELINE 2026-07-31: Two business card applications submitted: Mechanics Bank (TransUnion pull, 12-mo 0% APR) and First Foundation Bank (Equifax pull, 6-mo 0% APR). Stated annual revenue $1.6M to preserve a future $150K no-doc LOC option; Todd listed as 85% owner to leverage his personal credit. Evidence: fathom.video/calls/769061378""",
"""TIMELINE 2026-07-31: Todd countersigns the joint program agreement. Evidence: support@ mailbox (SendLink)""",
"""TIMELINE 2026-08-03: Forwards MLCS Holdings application #6301694 (from Gabrielle McGillvery, cardassets.com) and flags a First Foundation Bank query as unrecognized. Evidence: Gmail thread 19fc806c7df95559""",
"""TIMELINE 2026-08-10: RESOLVED - the 'unrecognized' First Foundation query was their OWN 7/31 application. Not fraud. No dispute needed. Evidence: fathom.video/calls/769061378 confirms the 7/31 EQ-pull application""",
"""DOCUMENTS (links; import 8/30):
- Todd - 3B tri-bureau credit report: https://drive.google.com/file/d/1jf4Gdb1KHygSDnafLXaWFg-paPTFzQYh/view
- MLCS CA SOS filing B4841-0906 (Articles): https://drive.google.com/file/d/17BXlGHdvCXHcPN6GUe3ehBNFCWpHyVii/view
- MLCS Holdings application #6301694: Gmail thread 19fc806c7df95559 (8/3)
- Joint signed agreement (Todd + Matt, v3): SendLink in support@ mailbox - PDF never downloaded; do this
- Client Drive folder (all files): https://drive.google.com/drive/folders/1uGJxCdkv8VJAf7L4Bw1bRA3nuW0B-qe2""",
]
for n in notes:
    rn = api("POST", f"/contacts/{CID}/notes", {"body": n})
    print("note:", "OK" if "code" not in rn else rn, flush=True)
    time.sleep(0.2)

# ---- §7: open items as tasks ----
tasks = [
("RED: Obtain Government ID for Todd (personal guarantor on live application)",
 "No Government ID on file for the personal guarantor on a live application. Highest-priority missing document across the entire client base - the PG is who the lender pursues. Request and file."),
("RED: Confirm/verify phone number on file",
 "Import package found no phone anywhere in Notion/Fathom/support@. GHL has +14154245720 on this contact - verify it is current and reachable; every touch currently routes through Matt."),
("ORANGE: Verify $85,000 Delaware franchise tax assessment corrected (MLCS)",
 "Must be corrected by Harvard Business Services before further applications. Status unverified since 7/14."),
("ORANGE: Populate Score Band from the 3B report",
 "Score Band reads Unknown despite the 3B tri-bureau report being on file - open it and populate; it is the number the guarantee rests on."),
("YELLOW: Close Prime Protocol gaps (EIN letter, operating agreement, bank statements, tax return, income proof)",
 "No EIN letter (status asserted, not evidenced), no operating agreement (material where two owners share an entity and only one guarantees), no personal/business bank statements (3 months each required), no tax return, no income proof - Income Range reads Unknown for the guarantor."),
("YELLOW: Record outcome of application #6301694",
 "MLCS Holdings application #6301694 has no recorded outcome."),
("DECISION for Alan: should a guarantor carry his own commercial terms?",
 "Whether a guarantor should carry his own commercial terms at all is an open question for Alan - Closed Won with no Deal Value is currently correct but unusual."),
]
for title, body in tasks:
    rt = api("POST", f"/contacts/{CID}/tasks", {
        "title": title, "body": body, "dueDate": "2026-09-05T17:00:00Z", "completed": False})
    print("task:", "OK" if "code" not in rt else rt, flush=True)
    time.sleep(0.2)

out = REPO / "ops" / "lane4" / "todd_import_log.json"
out.write_text(json.dumps(LOG, indent=1, default=str), encoding="utf-8")
print("CONTACT_ID:", CID)
print("log ->", out)
