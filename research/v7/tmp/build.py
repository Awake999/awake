import json, csv

rows=json.load(open("/home/user/awake/research/v7/tmp/branches_geo.json"))
fdic=json.load(open("/home/user/awake/research/v7/tmp/fdic_fin.json"))
ncua=json.load(open("/home/user/awake/research/v7/tmp/ncua_fin.json"))
w8=[r for r in rows if r.get("dist") is not None and r["dist"]<=8.0]
SHARED={("NCUA","W S S C"),("NCUA","COLLEGEDALE")}

best={}; cnt={}
for r in w8:
    k=(r["src"],r["inst"])
    if k in SHARED: continue
    cnt[k]=cnt.get(k,0)+1
    if k not in best or r["dist"]<best[k]["dist"]: best[k]=r

# display names, v6 flag, found_by, notes
META={
 "Wells Fargo Bank, National Association":("Wells Fargo Bank, N.A.","Yes (Wells Fargo)","SOD+OSM+web",""),
 "JPMorgan Chase Bank, National Association":("JPMorgan Chase Bank, N.A.","Yes (Chase)","SOD+OSM+web",""),
 "U.S. Bank National Association":("U.S. Bank, N.A.","Yes (U.S. Bank)","SOD+OSM+web",""),
 "Bank of America, National Association":("Bank of America, N.A.","Yes","SOD+OSM+web",""),
 "Citibank, National Association":("Citibank, N.A.","Yes (Citi)","SOD+OSM",""),
 "Citizens Business Bank":("Citizens Business Bank","Yes","SOD+OSM","HQ Ontario CA - hometown Inland Empire business bank"),
 "HomeStreet Bank":("Mechanics Bank (ex-HomeStreet)","Yes (both names)","SOD","HomeStreet merged into Mechanics Bank 2025; SOD 2025 still lists HomeStreet. Financials = Mechanics Bank (CERT 1768)"),
 "Comerica Bank":("Fifth Third Bank, N.A. (ex-Comerica)","Yes (both names)","SOD+OSM","Comerica acquired by Fifth Third (closed 2026; FDIC CERT 983 now inactive). Financials = Fifth Third (CERT 6672)"),
 "Banner Bank":("Banner Bank","Yes","SOD+web",""),
 "Chino Commercial Bank, N.A.":("Chino Commercial Bank, N.A.","Yes","SOD+web","Community business bank"),
 "BMO Bank National Association":("BMO Bank, N.A.","Yes (BMO Bank)","SOD+OSM+web","OSM still tagged as Bank of the West"),
 "Banc of California":("Banc of California","Yes","SOD+web",""),
 "East West Bank":("East West Bank","Yes","SOD",""),
 "Cathay Bank":("Cathay Bank","Yes","SOD",""),
 "City National Bank":("City National Bank","Yes","SOD",""),
 "ARROWHEAD":("Arrowhead Credit Union","Yes","NCUA+OSM+web",""),
 "CREDIT UNION OF SOUTHERN CA, A":("Credit Union of Southern California","Yes (CU SoCal)","NCUA+OSM",""),
 "FONTANA":("Fontana Federal Credit Union","No","NCUA+OSM","Small local CU, HQ Fontana"),
 "INLAND VALLEY":("Inland Valley Federal Credit Union","No","NCUA+OSM","HQ Fontana"),
 "THINKWISE":("Thinkwise Credit Union","No","NCUA+OSM",""),
 "ALTA VISTA":("Alta Vista Credit Union","No","NCUA+OSM",""),
 "CHAFFEY":("Chaffey Federal Credit Union","No","NCUA+OSM",""),
 "SCHOOLSFIRST":("SchoolsFirst Federal Credit Union","Yes","NCUA+OSM",""),
 "CAHP":("CAHP Credit Union","Yes","NCUA+OSM",""),
 "WESCOM CENTRAL":("Wescom Credit Union","Yes (Wescom)","NCUA+OSM",""),
 "NAVY FEDERAL CREDIT UNION":("Navy Federal Credit Union","No","NCUA",""),
 "RIZE":("Rize Credit Union (ex-SCE FCU)","No","NCUA+OSM","OSM still tagged SCE Federal Credit Union"),
}

recs=[]
for k,v in best.items():
    src,inst=k
    disp,v6,found,note=META.get(inst,(inst.title(),"No",src,""))
    if src=="SOD":
        c=str(v["cert"])
        fin=fdic[c]
        if inst=="HomeStreet Bank":
            am,dm=21403986/1000,18251541/1000; cert="1768 (was 32489)"; hq="Walnut Creek, CA"
        elif inst=="Comerica Bank":
            am,dm=296118000/1000,240416000/1000; cert="6672 (was 983)"; hq="Cincinnati, OH"
        else:
            am,dm=fin["ASSET"]/1000,fin["DEP"]/1000; cert=c; hq=f"{fin['CITY']}, {fin['STALP']}"
        typ="Bank"
    else:
        c=str(v["cert"]); f2=ncua["fin"][c]; nm=ncua["names"][c]
        am,dm=float(f2["assets"])/1e6,float(f2["shares_dep"])/1e6
        cert=c; hq=f"{nm[1].title().strip()}, {nm[2]}"; typ="Credit Union"
    recs.append({"disp":disp,"typ":typ,"addr":f"{v['addr']}, {v['city']}, CA {v['zip']}",
        "dist":v["dist"],"cert":cert,"hq":hq,"am":am,"dm":dm,"n":cnt[k],
        "v6":v6,"found":found,"note":note})
recs.sort(key=lambda r:r["dist"])

def money(m):
    return f"${m/1e6:.2f}T" if m>=1e6 else (f"${m/1e3:.1f}B" if m>=1e3 else f"${m:.0f}M")

with open("/home/user/awake/research/v7/out/geo_fontana.csv","w",newline="") as f:
    w=csv.writer(f)
    w.writerow(["Rank_by_distance","Institution","Type","Nearest_branch_address","Distance_miles",
        "CERT_or_Charter","HQ_City_State","Total_Assets_$M","Total_Deposits_$M","Branches_within_8mi",
        "In_v6_table","Found_by","Source_links","Notes"])
    SRC={"SOD":"https://banks.data.fdic.gov/api/sod (YEAR:2025)","NCUA":"https://ncua.gov Call Report 2026-03 branch file"}
    for i,r in enumerate(recs,1):
        links=[]
        if "SOD" in r["found"]: links.append("banks.data.fdic.gov/api/sod 2025; banks.data.fdic.gov/api/institutions")
        if "NCUA" in r["found"]: links.append("ncua.gov call-report-data-2026-03 (branch file + FS220)")
        if "OSM" in r["found"]: links.append("overpass-api amenity=bank r=12.9km")
        w.writerow([i,r["disp"],r["typ"],r["addr"],r["dist"],r["cert"],r["hq"],
            round(r["am"],1),round(r["dm"],1),r["n"],r["v6"],r["found"],"; ".join(links),r["note"]])
print("CSV:",len(recs),"institutions")

# 8-15 mi notables
far={}
for r in rows:
    if r.get("dist") and 8.0<r["dist"]<=15.0:
        k=r["inst"]
        if any(k==kk[1] for kk in best): continue
        if k in ("W S S C","COLLEGEDALE"): continue
        if k not in far or r["dist"]<far[k]["dist"]: far[k]=r
farl=sorted(far.values(),key=lambda x:x["dist"])

md=open("/home/user/awake/research/v7/out/geo_fontana.md","w")
md.write(f"""# Geo Census: Banks & Credit Unions near 6614 Tokay Avenue, Fontana, CA

**Anchor point:** 6614 Tokay Ave, Fontana, CA — geocoded to **34.13320, -117.45615** (ZIP **92336**, North Fontana).
Both the US Census geocoder (TIGER match, 6500-6798 block) and OSM Nominatim agree on this point.
*Note: the briefing's approximation (34.087, -117.463, ZIP 92335) is ~3.2 mi south of the verified rooftop location; all distances below use the verified geocode.*

**Method:** FDIC Summary of Deposits 2025 (San Bernardino + Riverside + Los Angeles county extracts) and the NCUA 2026-03 call-report branch file were filtered to {len(rows)} branches in 20 surrounding cities, batch-geocoded with the US Census geocoder (Nominatim fallback), and ranked by haversine distance. An organic pass (OSM Overpass `amenity=bank` within 12.9 km — 49 hits — plus web searches) was merged in for cross-checking. Bank assets/deposits from the FDIC institutions API (ASSET/DEP); credit union figures from NCUA FS220 ACCT_010 (total assets) and ACCT_018 (total shares & deposits), cycle 2026-03.

**Result: {len(recs)} institutions with a branch within 8.0 miles** ({sum(1 for r in recs if r['typ']=='Bank')} banks, {sum(1 for r in recs if r['typ']=='Credit Union')} credit unions; {sum(r['n'] for r in recs)} branch locations).

| # | Institution | Type | Nearest branch | Mi | CERT/Charter | HQ | Assets | Deposits | Br<=8mi | In v6 table | Found by |
|---|---|---|---|---|---|---|---|---|---|---|---|
""")
for i,r in enumerate(recs,1):
    md.write(f"| {i} | {r['disp']} | {r['typ']} | {r['addr']} | {r['dist']} | {r['cert']} | {r['hq']} | {money(r['am'])} | {money(r['dm'])} | {r['n']} | {r['v6']} | {r['found']} |\n")

md.write("""
## Organic-pass reconciliation (OSM + web vs. regulatory files)
- The organic pass produced **zero net-new active institutions** — every OSM/web hit within 8 mi mapped to a SOD or NCUA record. It did catch **3 stale/renamed entries**:
  - **"Bank of the West" (OSM, 8311 Haven Ave)** -> now **BMO Bank** (SOD confirms).
  - **"SCE Federal Credit Union" (OSM, 975 N Haven Ave, Ontario)** -> rebranded **Rize Credit Union** (NCUA confirms).
  - **"Mission Oaks National Bank" (OSM, 800 Ferrari Ln, Ontario)** -> **defunct** — FDIC CERT 57021 inactive since 2014-05-03. Excluded.
- Regulatory-vs-org successor fixes: **Comerica** (CERT 983 now inactive; acquired by **Fifth Third**, financials swapped to CERT 6672) and **HomeStreet** (merged into **Mechanics Bank**, CERT 1768).
- **Excluded as not-own-branches:** WSSC FCU and Collegedale CU both list "CO-OP Shared Branching" sites at 9692 Haven Ave, Rancho Cucamonga (7.8 mi) — co-op service-center listings, not proprietary branches.
- Regulatory-only finds the organic pass missed: Navy Federal CU (Ontario), East West Bank, Cathay Bank, City National Bank, Banc of California, HomeStreet/Mechanics, Banner Bank, Chino Commercial Bank (last two surfaced by web search but not OSM).

## Notables 8-15 miles (nearest branch per institution)
""")
for r in farl:
    md.write(f"- **{r['inst'].title() if r['src']=='NCUA' else r['inst']}** ({'CU' if r['src']=='NCUA' else 'Bank'}) — {r['addr']}, {r['city']} — {r['dist']} mi\n")
md.write("""
## Sources
- FDIC Summary of Deposits 2025: local extracts /home/user/awake/research/v6/out/sod_2025_{San_Bernardino,Riverside,Los_Angeles}.json (banks.data.fdic.gov/api/sod)
- FDIC institutions API (ASSET/DEP, $000s): banks.data.fdic.gov/api/institutions
- NCUA call report 2026-03: /home/user/awake/research/v6/out/cr202603/ (branch file, FOICU, FS220 ACCT_010/ACCT_018)
- US Census geocoder (Public_AR_Current benchmark, batch + oneline); OSM Nominatim fallback
- OSM Overpass API: amenity=bank around:12875m of 34.133203,-117.456149 (49 elements)
- Web: usbranches.bmo.com/ca/fontana; locations.bannerbank.com/ca/rancho-cucamonga; business.fontanachamber.org (Chino Commercial Bank); bancofcal.com/location/rancho-cucamonga; businessbranch.chase.com; arrowheadcu.org
- v6 cross-check: /home/user/awake/research/v6/deliverables/ca_business_credit_funding_v6_funding_table.csv (col 3 "Bank")
""")
md.close()
print("MD written.", len(farl),"notables 8-15mi")
for i,r in enumerate(recs[:15],1): print(i, r["disp"], r["dist"])
