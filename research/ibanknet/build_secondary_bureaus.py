#!/usr/bin/env python3
"""Phase 1: consolidate project evidence into 4-column verification-systems dataset."""
import csv, re, os

V6 = "/home/user/awake/research/v6/out/ews_chex_mapping.csv"
V7B = "/home/user/awake/research/v7/out/chex_socal_banks.csv"
V7C = "/home/user/awake/research/v7/out/chex_socal_cus.csv"
OUT = "/home/user/awake/research/ibanknet/out/secondary_bureaus.csv"

DOC_CHEX = "https://www.doctorofcredit.com/banks-credit-unions-dodont-pull-chexsystems/"
DOC_EWS = "https://www.doctorofcredit.com/banks-credit-unions-dodont-pull-early-warning-services/"

rows = {}  # name -> dict

def norm(s):
    return re.sub(r"\s+", " ", (s or "").strip())

def first_link(links, kw):
    """pick first link containing keyword, else first link, else em-dash"""
    parts = [p.strip() for p in re.split(r"[;|]", links or "") if p.strip() and p.strip() != "—"]
    for p in parts:
        if kw in p:
            return p
    return parts[0] if parts else "—"

def cell(summary, grade, date):
    summary = norm(summary)
    if not summary or summary in ("UNKNOWN", "N/M", "—"):
        return "UNKNOWN"
    g = norm(grade); d = norm(date)
    tail = "; ".join(x for x in (g, d) if x and x not in ("—", "(existing cell)"))
    return f"{summary} [{tail}]" if tail else summary

# ---------- Phase 1a: v6 ews_chex_mapping ----------
with open(V6, newline="", encoding="utf-8") as f:
    for r in csv.DictReader(f):
        name = norm(r["Institution"])
        if not name:
            continue
        grade = r["Evidence_grade"]
        date = r["DP_date"]
        links = r["Source_links"]
        chex_raw = norm(r["Existing_Chex_cell"])
        ews_raw = norm(r["Existing_EWS_cell"])
        chex_known = chex_raw not in ("", "N/M", "UNKNOWN") or norm(r["Chex_Pull"]) not in ("", "UNKNOWN")
        ews_known = ews_raw not in ("", "N/M", "UNKNOWN") or norm(r["EWS_Pull"]) not in ("", "UNKNOWN")
        chex_sum = chex_raw if chex_raw not in ("", "N/M") else (f"Pull: {norm(r['Chex_Pull'])}" if norm(r["Chex_Pull"]) not in ("", "UNKNOWN") else "UNKNOWN")
        ews_sum = ews_raw if ews_raw not in ("", "N/M") else (f"Pull: {norm(r['EWS_Pull'])}" if norm(r["EWS_Pull"]) not in ("", "UNKNOWN") else "UNKNOWN")
        # grade fallback: rows with UNKNOWN grade
        g = grade if norm(grade) not in ("", "UNKNOWN", "(existing cell)") else ("v6 existing cell" if (chex_known or ews_known) else "UNKNOWN")
        rows[name] = {
            "Institution": name,
            "ChexSystems": cell(chex_sum, g if chex_known else "", date if chex_known else ""),
            "Chex_link": first_link(links, "chexsystems") if chex_known else "—",
            "EWS": cell(ews_sum, g if ews_known else "", date if ews_known else ""),
            "EWS_link": first_link(links, "early-warning") if ews_known else "—",
            "LexisNexis_SageStream": "UNKNOWN",
            "LN_link": "—",
            "Other_secondary": "UNKNOWN",
            "Other_link": "—",
            "Notes": "v6 ews_chex_mapping. " + norm(r["Note"]),
        }

# ---------- Phase 1b: v7 chex_socal_banks (business-account angle) ----------
with open(V7B, newline="", encoding="utf-8") as f:
    for r in csv.DictReader(f):
        name = norm(r["Bank"])
        if not name:
            continue
        date = r["DP_dates"]; links = r["Source_links"]
        chex = norm(r["Chex_consumer(+grade)"])
        chexb = norm(r["Chex_BUSINESS(+grade)"])
        ews = norm(r["EWS_consumer"]); ewsb = norm(r["EWS_BUSINESS"])
        chex_cell = f"Consumer: {chex} | BUSINESS: {chexb} [{norm(date)}]"
        ews_cell = f"Consumer: {ews} | BUSINESS: {ewsb} [{norm(date)}]"
        # name harmonization with v6
        key = name
        alias = {
            "California Bank & Trust (div. of Zions Bancorporation)": "California Bank & Trust",
            "City National Bank (LA)": "City National Bank",
            "Western Alliance Bank (incl. Torrey Pines Bank div.)": "Western Alliance Bank",
            "IDB Bank (Israel Discount Bank of New York)": "Israel Discount Bank of New York (IDB)",
        }
        key = alias.get(name, name)
        base = rows.get(key, {
            "Institution": key, "LexisNexis_SageStream": "UNKNOWN", "LN_link": "—",
            "Other_secondary": "UNKNOWN", "Other_link": "—", "Notes": "",
        })
        base["Institution"] = key
        base["ChexSystems"] = chex_cell
        base["Chex_link"] = first_link(links, "")
        base["EWS"] = ews_cell
        base["EWS_link"] = first_link(links, "early-warning")
        base["Notes"] = ("v7 chex_socal_banks (business angle). " + norm(r.get("Verdict_tier", "")) + ". " + base.get("Notes", "")).strip()
        rows[key] = base

# ---------- Phase 1c: v7 chex_socal_cus ----------
with open(V7C, newline="", encoding="utf-8") as f:
    for r in csv.DictReader(f):
        name = norm(r["Institution"])
        if not name:
            continue
        date = r["DP_dates"]; links = r["Source_links"]
        chex = norm(r["Chex_membership"]); chexb = norm(r["Chex_BUSINESS"])
        ews = norm(r["EWS_membership"]); ewsb = norm(r["EWS_BUSINESS"])
        alias = {
            "Firefighters First CU": "Firefighters First Credit Union",
            "Logix Federal Credit Union": "Logix Federal Credit Union",
            "CommunityAmerica CU (ex-UNIFY)": "CommunityAmerica Credit Union (ex-UNIFY)",
            "AdelFi (Christian Community CU)": "Christian Community Credit Union (AdelFi)",
            "BCU (Baxter Credit Union)": "Baxter Credit Union (BCU)",
            "Wescom Credit Union": "Wescom Credit Union",
            "SchoolsFirst FCU": "SchoolsFirst Federal Credit Union",
        }
        key = alias.get(name, name)
        base = rows.get(key, {
            "Institution": key, "LexisNexis_SageStream": "UNKNOWN", "LN_link": "—",
            "Other_secondary": "UNKNOWN", "Other_link": "—", "Notes": "",
        })
        base["Institution"] = key
        base["ChexSystems"] = f"Membership: {chex} | BUSINESS: {chexb} [{norm(date)}]"
        base["Chex_link"] = first_link(links, "")
        base["EWS"] = f"Membership: {ews} | BUSINESS: {ewsb} [{norm(date)}]"
        base["EWS_link"] = first_link(links, "early-warning")
        base["Notes"] = ("v7 chex_socal_cus. " + norm(r.get("Verdict_tier", "")) + ". " + base.get("Notes", "")).strip()
        rows[key] = base

# ---------- Phase 1d: secondary-bureau facts from project docs ----------
def upd(name, **kw):
    base = rows.get(name)
    if base is None:
        base = {"Institution": name, "ChexSystems": "UNKNOWN", "Chex_link": "—",
                "EWS": "UNKNOWN", "EWS_link": "—", "LexisNexis_SageStream": "UNKNOWN",
                "LN_link": "—", "Other_secondary": "UNKNOWN", "Other_link": "—", "Notes": ""}
        rows[name] = base
    for k, v in kw.items():
        if k == "Notes":
            base["Notes"] = (v + " " + base.get("Notes", "")).strip()
        else:
            base[k] = v

upd("U.S. Bank (direct)",
    LexisNexis_SageStream="Yes — soft-pulls SageStream (now LexisNexis Risk Solutions); can DENY on it; freeze before applying [COMMUNITY-DP/project-fact; 2026-06]",
    LN_link="https://ficoforums.myfico.com/t5/Business-Credit/ (Triple Cash DPs; v7 funding table row 'U.S. Bank')",
    Other_secondary="ARS (Advanced Resolution Services, CBC/Innovis affiliate) — soft-pulled alongside SageStream; can deny [COMMUNITY-DP/project-fact; 2026-06]",
    Other_link="/home/user/awake/research/v7/deliverables/ca_business_credit_funding_v7_funding_table.csv",
    Notes="PROJECT FACT: freeze SageStream+ARS before US Bank apps (soft-pulled, can deny).")

upd("Regions Bank",
    LexisNexis_SageStream="Yes — ONLINE applications pull LexisNexis (frozen LN file => denial, DP 2022-02-27); in-BRANCH opening did NOT pull [COMMUNITY-DP; 2022-02-27]",
    LN_link=DOC_EWS + "#comment-1339779",
    Notes="No CA retail footprint; row included for LexisNexis evidence. DoC commenter Gadget: 'a lot of banks pull LexisNexis, at least with online opening.'")

upd("Charles Schwab Bank",
    EWS="Yes — EWS inquiries appear as 'CHARLES SCHWAB via GIACT SERVICES' (mostly external-account linking, not always new-account screening) [COMMUNITY-DP; 2022-2025 DPs]",
    EWS_link=DOC_EWS,
    Other_secondary="GIACT Services (Refinitiv/LSEG gDNA) — account-linking verification rail that posts EWS inquiries [COMMUNITY-DP]",
    Other_link=DOC_EWS,
    Notes="On DoC EWS list; multiple report DPs in docs_D3 (Nov 2022-Apr 2025 editions). Major CA branch presence.")

upd("Banner Bank",
    Other_secondary="QualiFile (ChexSystems/FIS scoring product) — auto-deny, no manual override [COMMUNITY-DP; 2026-01-27]",
    Other_link="https://www.doctorofcredit.com/banks-credit-unions-dodont-pull-chexsystems/",
    Notes="QualiFile is the Chex-based decision engine; recorded under Other for product-level visibility.")

upd("Chime (fintech)",
    ChexSystems="No — does not pull Chex (DoC don't-pull list) [DOC-LIST; 2025-08-07]",
    Chex_link=DOC_CHEX,
    EWS="No — 'doesn't report and no inquiry' (Dealgamer EWS-clean list) [COMMUNITY-DP; 2026-05-22]",
    EWS_link=DOC_EWS + "#comment-2326911",
    Notes="SF-HQ fintech (Bancorp/Stride partner banks).")

upd("Varo Bank, N.A.",
    EWS="No — on Dealgamer 'doesn't report and no inquiry' list; older DPs show 'VARO MONEY via GIACT SYSTEMS' linking inquiries only [COMMUNITY-DP; 2026-05-22]",
    EWS_link=DOC_EWS + "#comment-2326911",
    Other_secondary="GIACT Systems (linking verification) [COMMUNITY-DP]",
    Other_link=DOC_EWS,
    Notes="SF-HQ national bank charter fintech.")

upd("SoFi Bank, N.A.",
    EWS="Yes — does an inquiry (Dealgamer 2026-05-22 list; 'SOFI LENDING CORP via GIACT SERVICES' DPs) [COMMUNITY-DP; 2026-05-22]",
    EWS_link=DOC_EWS + "#comment-2326911",
    Other_secondary="GIACT Services (linking/verification rail) [COMMUNITY-DP]",
    Other_link=DOC_EWS,
    Notes="SF-HQ national bank. EWS inquiries on open + GIACT on linking.")

# ---------- Phase 2: targeted web sweep 2026-06-12 ----------
upd("East West Bank",
    ChexSystems="Yes — Crediful: uses Chex to screen checking applicants; own Deposit Agreement (eff. 2024-06-01) 'New Account Verification' = generic 'check or credit reporting agency', vendor UNNAMED [COMMUNITY-DP (Crediful) + Generic-CRA-clause (own doc); 2026-06-12]",
    Chex_link="https://www.crediful.com/chexsystems/east-west-bank/",
    EWS="Generic-CRA-clause (vendor unnamed) — own Deposit Agreement names no EWS; 0 'Early Warning' hits in 60-pg doc [VERIFIED-absence; 2026-06-12]",
    EWS_link="https://www.eastwestbank.com/content/dam/ewb-dotcom/docs/terms-and-conditions/Deposit_Account_Agreement.pdf",
    LexisNexis_SageStream="Not named in own 60-pg Deposit Agreement [VERIFIED-absence; 2026-06-12] — inquiry-side UNKNOWN",
    LN_link="https://www.eastwestbank.com/content/dam/ewb-dotcom/docs/terms-and-conditions/Deposit_Account_Agreement.pdf",
    Notes="P2: agreement quote: 'We may use a third-party service to verify and obtain information regarding your previous banking relationships... credit information from a check or credit reporting agency'.")

upd("Cathay Bank",
    ChexSystems="Generic-CRA-clause (vendor unnamed) — own Deposit Account Agreement (consumer+business) sec.50 'Use of Consumer Reporting Agencies': 'third party services to verify... previous banking relationships'; ChexSystems never named; one weak undated forum claim of NO Chex stands [VERIFIED-absence (own doc) + weak COMMUNITY-DP; 2026-06-12]",
    Chex_link="https://www.cathaybank.com/documents/personal/digital-account-opening/deposit-account-agreement.pdf",
    EWS="Generic-CRA-clause (vendor unnamed) — 0 EWS hits in 40-pg agreement [VERIFIED-absence; 2026-06-12]",
    EWS_link="https://www.cathaybank.com/documents/personal/digital-account-opening/deposit-account-agreement.pdf",
    LexisNexis_SageStream="Not named in own agreement [VERIFIED-absence; 2026-06-12] — inquiry-side UNKNOWN",
    LN_link="https://www.cathaybank.com/documents/personal/digital-account-opening/deposit-account-agreement.pdf",
    Notes="P2: also sec.14 'Consent to Gather Information' = generic credit-reporting-agency authorization. High-value verification call target.")

upd("Golden 1 Credit Union",
    ChexSystems="Yes — pulls Chex and is INQUIRY-SENSITIVE ('signing up for lots of bank bonuses => struggle to be approved for membership') [DOC-LIST; 2026-06-12 search]",
    Chex_link="https://www.doctorofcredit.com/banks-credit-unions-chexsystems-inquiry-sensitive/",
    Other_secondary="Equifax HARD pull just to join (credit bureau, noted for completeness) [COMMUNITY-DP; 2026-06-12]",
    Other_link="https://www.doctorofcredit.com/banks-credit-unions-dodont-pull-chexsystems/",
    Notes="P2 UPGRADE vs UNKNOWN. Non-CA join requires Financial Fitness Association ($5).")

upd("SchoolsFirst Federal Credit Union",
    ChexSystems="Yes — VERIFIED own product pages: 'ChexSystems verification and $25 minimum opening deposit required' (Free Checking, Investment Checking; Liquid Advantage MM = Chex + $2,000) [VERIFIED (own site); 2026-06-12]",
    Chex_link="https://www.schoolsfirstfcu.org/products/checking-savings/checking/free-checking/",
    EWS="No screening evidence — only Zelle (EWS-owned product) infrastructure on site [searched 2026-06-12; UNKNOWN]",
    EWS_link="—",
    Notes="P2 UPGRADE vs UNKNOWN — own-site VERIFIED Chex. Education FOM gate still applies.")

upd("Mechanics Bank",
    ChexSystems="Yes — VERIFIED own Personal Account Agreement (doc dated 2026-03-23): 'new accounts are subject to verification through ChexSystems (the Reporting Agency) and may be declined based in whole or in part on information obtained in a report' [VERIFIED (own doc); 2026-06-12]",
    Chex_link="https://www.mechanicsbank.com/contentassets/9e0348bebd2b44b2a8fa059267bcab78/1200-personal-account-agreement-disclosure-mkt10000-v3-final-mkt-copy.pdf",
    EWS="Not named in own 20-pg Personal Account Agreement [VERIFIED-absence; 2026-06-12] — inquiry-side UNKNOWN",
    EWS_link="https://www.mechanicsbank.com/contentassets/9e0348bebd2b44b2a8fa059267bcab78/1200-personal-account-agreement-disclosure-mkt10000-v3-final-mkt-copy.pdf",
    LexisNexis_SageStream="Not named in own agreement [VERIFIED-absence; 2026-06-12]",
    LN_link="https://www.mechanicsbank.com/contentassets/9e0348bebd2b44b2a8fa059267bcab78/1200-personal-account-agreement-disclosure-mkt10000-v3-final-mkt-copy.pdf",
    Notes="P2 UPGRADE vs UNKNOWN. Also reports to 'credit bureaus, including ChexSystems' on unpaid balances.")

upd("Axos Bank",
    ChexSystems="Yes — UPGRADE to VERIFIED: own support FAQ: 'Axos will not be able to process or approve your application with a ChexSystems freeze in place' — applies to PERSONAL and BUSINESS accounts; DoC: 6 DPs, NOT inquiry-sensitive (approved 50+/12mo) [VERIFIED (own FAQ) + DOC-LIST; 2026-06-12]",
    Chex_link="https://www.axosbank.com/business/support/faqs",
    Notes="P2 UPGRADE: Chex freeze = hard blocker incl. business banking.")

upd("Bank of America",
    LexisNexis_SageStream="Yes — uses SageStream 'Credit Optics' score data for CREDIT decisions (cards/loans); 'extremely unlikely to deny for frozen SageStream' unless thin traditional file [DOC-LIST; article 2016-08-08]",
    LN_link="https://www.doctorofcredit.com/bank-america-now-uses-sagestream-credit-optics-score-data-credit-decisions/",
    Notes="P2: SageStream usage is credit-side, not deposit-screening; recorded per 4-column scheme.")

upd("U.S. Bank (direct)",
    Notes="P2: DoC article 'Two Credit Bureaus You Should Freeze Before You Apply For A U.S Bank Credit Card' (2015-05-26, since updated): SageStream (ex-IDA, now LexisNexis Risk Solutions) + ARS (Advanced Resolution Services, 5005 Rockside Rd, Independence OH); US Bank still approves when reports frozen/unavailable. Grade upgraded to DOC-LIST. https://www.doctorofcredit.com/two-credit-bureaus-you-should-freeze-before-you-apply-for-a-u-s-bank-credit-card/")

for nm in ("Pacific Premier Bank", "Westamerica Bank", "Umpqua Bank (Columbia)", "California Coast Credit Union"):
    upd(nm, Notes="P2: web-searched 2026-06-12 — no public deposit agreement naming a vendor and no DoC/forum DPs found; all four columns remain UNKNOWN (never guess).")

# systemic QualiFile-LexisNexis linkage note
for nm, base in rows.items():
    pass  # documented in secondary_bureaus.md instead of per-row spam
upd("Banner Bank",
    Notes="SYSTEMIC (DoC): banks using the Chex QualiFile SCORE indirectly pull LexisNexis — frozen LexisNexis => abnormal Chex score => auto-decline 'citing frozen Chex'. Directly relevant to Banner's QualiFile auto-deny.")

# ---------- write ----------
FIELDS = ["Institution", "ChexSystems", "Chex_link", "EWS", "EWS_link",
          "LexisNexis_SageStream", "LN_link", "Other_secondary", "Other_link", "Notes"]
with open(OUT, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=FIELDS)
    w.writeheader()
    for name in sorted(rows):
        w.writerow({k: rows[name].get(k, "—") for k in FIELDS})
print(f"wrote {len(rows)} rows -> {OUT}")
