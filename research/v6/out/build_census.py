import csv, re, difflib
from collections import defaultdict

BASE='/home/user/awake/research/v6/out/cr202603/'
COUNTIES=['Los Angeles','San Bernardino','Riverside','Orange','Ventura','San Diego']
ABBR={'Los Angeles':'LA','San Bernardino':'SB','Riverside':'Riv','Orange':'OC','Ventura':'Ventura','San Diego':'SD'}
PRIO4={'Los Angeles','San Bernardino','Riverside','Orange'}

# 1. Branch data
cu_counties=defaultdict(lambda: defaultdict(int))
with open(BASE+'Credit Union Branch Information.txt',encoding='latin-1') as f:
    for row in csv.DictReader(f):
        if row['PhysicalAddressStateCode']=='CA' and row['PhysicalAddressCountyName2'] in COUNTIES:
            cu_counties[row['CU_NUMBER']][row['PhysicalAddressCountyName2']]+=1

# 2. FOICU (HQ)
hq={}
with open(BASE+'FOICU.txt',encoding='latin-1') as f:
    for row in csv.DictReader(f):
        hq[row['CU_NUMBER']]=(row['CU_NAME'],row['CITY'],row['STATE'])

# 3. FS220 assets
assets={}
with open(BASE+'FS220.txt',encoding='latin-1') as f:
    r=csv.DictReader(f)
    acol=[c for c in r.fieldnames if c.upper()=='ACCT_010'][0]
    for row in r:
        try: assets[row['CU_NUMBER']]=int(float(row[acol]))
        except: pass

# 4. v5 universe
def norm(s):
    s=s.upper()
    s=re.sub(r'\b(FEDERAL|CREDIT|UNION|FCU|CU|THE)\b','',s)
    s=re.sub(r'[^A-Z0-9]','',s)
    return s

v5_charters={}; 
with open('/home/user/awake/research/v6/v5_ncua_census.csv') as f:
    for row in csv.DictReader(f):
        v5_charters[row['CU#'].strip()]=row['Credit Union'].strip()

v5_names=[l.strip() for l in open('/home/user/awake/research/v6/v5_all_institution_names.txt') if l.strip()]
v5_norm={norm(n):n for n in v5_names}

rows=[]
for cu,cnts in cu_counties.items():
    name,city,state=hq.get(cu,('?','?','?'))
    a=assets.get(cu,'')
    bl={c:cnts.get(c,0) for c in COUNTIES}
    tot=sum(bl.values())
    counties_present=[ABBR[c] for c in COUNTIES if bl[c]>0]
    prio='PRIORITY-4CTY' if any(cnts.get(c,0)>0 for c in PRIO4) else 'OUTLIER'
    oos='Y' if state!='CA' else ''
    # v5 match
    if cu in v5_charters:
        status='IN_V5'; note=f'charter match: {v5_charters[cu]}'
    else:
        nn=norm(name)
        if nn and nn in v5_norm:
            status='IN_V5'; note=f'name match: {v5_norm[nn]}'
        else:
            close=difflib.get_close_matches(nn,[k for k in v5_norm if k],n=1,cutoff=0.82) if nn else []
            # also try charter-name fuzzy against v5 census names
            close2=difflib.get_close_matches(nn,[norm(v) for v in v5_charters.values()],n=1,cutoff=0.82) if nn else []
            if close:
                status='POSSIBLE_MATCH'; note=f'~ {v5_norm[close[0]]}'
            elif close2:
                cand=[v for v in v5_charters.values() if norm(v)==close2[0]][0]
                status='POSSIBLE_MATCH'; note=f'~ v5 census: {cand}'
            else:
                status='NEW_GAP'
                note='Ventura/SD only (outlier counties, not in v5 4-cty scope)' if prio=='OUTLIER' else ''
    rows.append(dict(charter=cu,name=name,city=city.title(),state=state,assets=a,oos=oos,
        bl=bl,tot=tot,counties='+'.join(counties_present),prio=prio,status=status,note=note))

rows.sort(key=lambda r:(-(r['assets'] or 0)))
SRC='https://ncua.gov/files/publications/analysis/call-report-data-2026-03.zip'
with open('/home/user/awake/research/v6/out/ncua_cu_census_6cty.csv','w',newline='') as f:
    w=csv.writer(f)
    w.writerow(['Charter#','Credit_Union','HQ_City','HQ_State','Assets_$','OOS_HQ_with_SoCal_branches',
        'Branches_LA','Branches_SB','Branches_Riv','Branches_OC','Branches_Ventura','Branches_SD',
        'Total_6cty','Counties','Priority','v5_status','Match_note','Source_link'])
    for r in rows:
        w.writerow([r['charter'],r['name'],r['city'],r['state'],r['assets'],r['oos'],
            r['bl']['Los Angeles'],r['bl']['San Bernardino'],r['bl']['Riverside'],r['bl']['Orange'],
            r['bl']['Ventura'],r['bl']['San Diego'],r['tot'],r['counties'],r['prio'],r['status'],r['note'],SRC])

# stats
from collections import Counter
print('Total CUs:',len(rows))
print('4-cty CUs:',sum(1 for r in rows if r['prio']=='PRIORITY-4CTY'))
for c in COUNTIES: print(f'{c}: CUs={sum(1 for r in rows if r["bl"][c]>0)} branches={sum(r["bl"][c] for r in rows)}')
print(Counter(r['status'] for r in rows))
print('OOS HQ:',sum(1 for r in rows if r['oos']))
print()
print('NEW_GAP top 20 by assets:')
for r in [x for x in rows if x['status']=='NEW_GAP'][:20]:
    print(f"  {r['charter']:>6} {r['name'][:42]:42} {r['state']} ${r['assets']:>14,} {r['counties']} [{r['prio']}]")
print()
print('POSSIBLE_MATCH:')
for r in [x for x in rows if x['status']=='POSSIBLE_MATCH']:
    print(f"  {r['charter']:>6} {r['name'][:42]:42} {r['note']}")
