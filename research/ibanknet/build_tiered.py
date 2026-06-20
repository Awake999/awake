#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""TIER-BUILD: SoCal Self-UW Tiered (no-Chex/no-EWS) workbook."""
import csv, re, os, sys

BASE = '/home/user/awake/research'
OUT  = BASE + '/ibanknet/out'
DELV = BASE + '/ibanknet/deliverables'
V6   = BASE + '/v6/out'
V7   = BASE + '/v7/out'

def rd(path):
    with open(path, encoding='utf-8-sig') as f:
        return list(csv.DictReader(f))

# ---------- name normalization ----------
STOP = {'national','association','na','federal','credit','union','bank','trust',
        'company','co','the','of','and','&','fcu','cu','f','sb','na','n','inc',
        'banking','financial','savings'}
def norm(s):
    s = (s or '').lower()
    s = s.replace('&',' and ')
    s = re.sub(r"[^a-z0-9 ]", ' ', s)
    toks = [t for t in s.split() if t and t not in STOP]
    return ' '.join(toks)

def keyset(s):
    return set(norm(s).split())

def match(a, b):
    """loose match between two institution names (conservative to avoid false twins)"""
    ka, kb = keyset(a), keyset(b)
    if not ka or not kb: return False
    na, nb = norm(a), norm(b)
    if na == nb: return True
    inter = ka & kb
    smaller = ka if len(ka) <= len(kb) else kb
    GENERIC = {'america','first','community','pacific','western','valley',
               'united','american','central','citizens','peoples','golden',
               'sun','state','city','heritage','premier','liberty','national'}
    # whole normalized-string containment (e.g. 'city national' in 'city national bank')
    # but NOT when the smaller name is a single generic token
    if na and nb and ((' '+na+' ' in ' '+nb+' ') or (' '+nb+' ' in ' '+na+' ')):
        sm_str = na if len(na) <= len(nb) else nb
        if not (len(sm_str.split()) == 1 and sm_str in GENERIC):
            return True
    # the smaller name's tokens must be (almost) fully contained in the larger
    if smaller and inter == smaller and len(smaller) >= 1:
        # single-token names: require it be a distinctive token (not generic geography)
        if len(smaller) == 1:
            tok = next(iter(smaller))
            if tok in GENERIC:
                return False
        return True
    if len(inter) >= 2 and len(inter) >= min(len(ka),len(kb)):
        return True
    return False

def find_row(name, rows, namecol, city=None, citycol=None):
    """find best matching row in rows for name (optionally constrain by city)"""
    cands = [r for r in rows if match(name, r.get(namecol,''))]
    if not cands: return None
    if len(cands) == 1: return cands[0]
    if city and citycol:
        for c in cands:
            if norm(city) and norm(city) in norm(c.get(citycol,'')):
                return c
    # pick highest token overlap
    cands.sort(key=lambda r: len(keyset(name) & keyset(r.get(namecol,''))), reverse=True)
    return cands[0]

# ---------- load main deposits ----------
dep = rd(DELV + '/iBankNet_CA_Deposits_v2.csv')

# self-UW + biz card YES
def is_self(r):
    return r['Underwriter'].strip().upper() == 'SELF'
def has_card(r):
    return r['Biz card?'].strip().upper().startswith('YES')

main_set = [r for r in dep if is_self(r) and has_card(r)]

# Special-case: Commercial Bank of California (prompt names as Tier-1 candidate,
# business sections have no consumer-report clause; v2 marks card NO but include per instruction)
cbc = [r for r in dep if 'commercial bank of california' in r['Institution'].lower()]
if cbc and cbc[0] not in main_set:
    main_set.append(cbc[0])

print('Self-UW+card (incl CBC special-case):', len(main_set))

# ---------- county census ----------
fdic = rd(V6 + '/fdic_sod_census_6cty_2025.csv')
ncua = rd(V6 + '/ncua_cu_census_6cty.csv')

CTY_COLS = [('Branches_LA','Los Angeles'),('Branches_SB','San Bernardino'),
            ('Branches_Riv','Riverside'),('Branches_OC','Orange'),
            ('Branches_Ventura','Ventura'),('Branches_SD','San Diego')]
PRIMARY = {'Los Angeles','Orange','San Bernardino','Riverside'}
SOCAL_HQ_CITIES = None  # we rely on county census + HQ city heuristic

def n_int(v):
    try: return int(float(str(v).replace(',','').strip()))
    except: return 0

def census_for(name, city, is_cu):
    src = ncua if is_cu else fdic
    nc = 'Credit_Union' if is_cu else 'Institution'
    row = find_row(name, src, nc, city, 'HQ_City')
    if not row:
        # try the other census (some CUs mis-typed)
        other = fdic if is_cu else ncua
        onc = 'Institution' if is_cu else 'Credit_Union'
        row = find_row(name, other, onc, city, 'HQ_City')
        if row: nc = onc
    return row, nc

# SoCal HQ cities (from SoCal counties) — fallback set for HQ-based confirmation
SOCAL_CITY_MAP = {
 'los angeles':'Los Angeles','glendale':'Los Angeles','hollywood':'Los Angeles',
 'manhattan beach':'Los Angeles','torrance':'Los Angeles','san dimas':'Los Angeles',
 'glendora':'Los Angeles','montclair':'San Bernardino','valencia':'Los Angeles',
 'chatsworth':'Los Angeles','irvine':'Orange','santa ana':'Orange',
 'huntington beach':'Orange','riverside':'Riverside','ventura':'Ventura',
 'san diego':'San Diego','el centro':'Imperial','santa barbara':'Santa Barbara',
}

def socal_info(name, city, is_cu):
    row, nc = census_for(name, city, is_cu)
    counties = []
    branch_counts = {}
    if row:
        for col, cty in CTY_COLS:
            cnt = n_int(row.get(col,0))
            if cnt > 0:
                counties.append(cty); branch_counts[cty]=cnt
        # parse Counties col too
        cstr = row.get('Counties','') or ''
        for col, cty in CTY_COLS:
            if cty.lower() in cstr.lower() and cty not in counties:
                counties.append(cty)
    hq_city = (row.get('HQ_City') if row else city) or city
    hq_state = (row.get('HQ_State') if row else '')  # unknown if no census row
    # HQ-based fallback
    hq_cty = SOCAL_CITY_MAP.get(norm_city(city))
    if not counties and hq_cty:
        counties = [hq_cty]
    socal = len(counties) > 0
    return socal, counties, branch_counts, hq_city, hq_state, row

def norm_city(c):
    return (c or '').strip().lower()

# ---------- geo branch cities ----------
geo_lb = rd(V7 + '/geo_longbeach.csv')
geo_ft = rd(V7 + '/geo_fontana.csv')
def branch_cities_for(name):
    cities = set()
    for g in geo_lb + geo_ft:
        if match(name, g.get('Institution','')):
            addr = g.get('Nearest_branch_address','')
            m = re.search(r',\s*([A-Za-z .]+),\s*CA', addr)
            if m: cities.add(m.group(1).strip())
    return list(cities)[:3]

# ---------- Chex/EWS ----------
sec = rd(OUT + '/secondary_bureaus.csv')
dchex = rd(OUT + '/deep_chex_results_1.csv') + rd(OUT + '/deep_chex_results_2.csv')

def classify_chex(text):
    """map a chex/ews finding string to NO/YES/UNKNOWN + grade.
    Honest rules: inquiry-side pulls => YES; verified own-doc absence => NO;
    furnish-on-closure-only (no inquiry evidence) => UNKNOWN inquiry-side;
    'uses-but-lenient' => still YES."""
    raw = (text or '')
    t = raw.lower()
    if not t.strip():
        return 'UNKNOWN', 'UNKNOWN'
    # furnish-on-closure-only -> inquiry-side UNKNOWN (do NOT count as pull or clean)
    if 'furnishes' in t or 'furnish' in t:
        if 'inquiry-side unknown' in t or 'inquiry side unknown' in t or 'closure' in t or 'closures' in t:
            return 'UNKNOWN', 'VERIFIED-own-doc'
    # explicit lean-no / likely-no / verified absence (own doc) -> NO
    if 'lean-no' in t or 'likely-no' in t or 'verified-absence' in t or 'verified absence' in t \
       or 'not-named' in t or 'no mention' in t or "does not" in t or "doesn't" in t or "don't" in t:
        g = 'VERIFIED-own-doc' if ('own doc' in t or 'own-doc' in t or 'not-named' in t or 'no mention' in t or 'verified' in t) else 'COMMUNITY-DP'
        return 'NO', g
    # YES / pulls / uses (incl lenient) -> YES
    if re.search(r'\byes\b', t) or 'pulls' in t or ' uses ' in t or 'verified own deposit' in t \
       or 'is used' in t or 'is conducted' in t:
        if 'verified' in t or 'own deposit' in t or 'own-doc' in t:
            return 'YES', 'VERIFIED-own-doc'
        return 'YES', 'COMMUNITY-DP'
    if 'weak' in t or 'generic' in t or 'generic-cra' in t:
        return 'UNKNOWN', 'CONSUMER-PROXY'
    return 'UNKNOWN', 'UNKNOWN'

def _refers_prior(t):
    t = (t or '').lower()
    return ('no change' in t or 'prior stands' in t or 'prior' in t and 'no new' in t
            or 'no new' in t or 'stands' in t and 'prior' in t)

def chex_ews_for(name, city, deprow=None):
    """returns (chex_status, chex_grade, chex_note, ews_status, ews_grade, ews_note, src)"""
    dr = find_row(name, dchex, 'Institution')
    sr = find_row(name, sec, 'Institution')
    # prior cells: secondary then deposits v2
    pc = (sr.get('ChexSystems','') if sr else '') or (deprow.get('ChexSystems','') if deprow else '')
    pe = (sr.get('EWS','') if sr else '') or (deprow.get('EWS','') if deprow else '')
    if deprow:
        if not (sr and sr.get('ChexSystems','').strip()): pc = deprow.get('ChexSystems','') or pc
        if not (sr and sr.get('EWS','').strip()): pe = deprow.get('EWS','') or pe
    if dr:
        cf = dr.get('New_Chex_finding','')
        ef = dr.get('New_EWS_finding','')
        if _refers_prior(cf) and pc.strip(): cf = pc
        if _refers_prior(ef) and pe.strip(): ef = pe
        cs, cg = classify_chex(cf)
        es, eg = classify_chex(ef)
        src = (dr.get('Source_links','') or (sr.get('Chex_link','') if sr else ''))
        return cs, cg, cf, es, eg, ef, src
    if sr:
        cf = sr.get('ChexSystems',''); ef = sr.get('EWS','')
        cs, cg = classify_chex(cf); es, eg = classify_chex(ef)
        src = (sr.get('Chex_link','') or '') + ' ' + (sr.get('EWS_link','') or '')
        return cs, cg, cf, es, eg, ef, src.strip()
    # fall back to deposits v2 cell
    if deprow and (deprow.get('ChexSystems','').strip() or deprow.get('EWS','').strip()):
        cf = deprow.get('ChexSystems',''); ef = deprow.get('EWS','')
        cs, cg = classify_chex(cf); es, eg = classify_chex(ef)
        return cs, cg, cf, es, eg, ef, ''
    return 'UNKNOWN','UNKNOWN','', 'UNKNOWN','UNKNOWN','', ''

# ---------- Bureau (hard pull) ----------
dbur = rd(OUT+'/deep_bureau_results_1.csv')+rd(OUT+'/deep_bureau_results_2.csv')+rd(OUT+'/deep_bureau_results_3.csv')
rerun = []
for i in range(1,6):
    rerun += rd(OUT+f'/rerun_bureau_results_{i}.csv')

def bureau_for(name, city):
    rr = find_row(name, rerun, 'Institution')
    if rr and str(rr.get('Upgrade','')).strip().upper().startswith('YES'):
        return rr.get('New_bureau_finding',''), rr.get('New_grade',''), rr.get('Source_links',''), rr.get('DP_dates','')
    if rr:
        return rr.get('New_bureau_finding','') or rr.get('Old_bureau',''), rr.get('New_grade','') or rr.get('Old_grade',''), rr.get('Source_links',''), rr.get('DP_dates','')
    db = find_row(name, dbur, 'Institution')
    if db:
        return db.get('Bureau_finding',''), db.get('Evidence_grade',''), db.get('Source_links',''), db.get('DP_dates','')
    return '', '', '', ''

# ---------- No-doc ----------
nodoc = rd(OUT+'/nodoc_dps_1.csv')+rd(OUT+'/nodoc_dps_2.csv')
GRADE_RANK = {'VERIFIED-OWN-DOC':5,'VERIFIED-OWN-PAGE':5,'COMMUNITY-DP':4,
              'CONSUMER-PROXY':3,'RAIL-INFERENCE':2,'UNKNOWN':1,'':0}
def grank(g):
    return GRADE_RANK.get((g or '').upper().replace(' ','-').split(';')[0].strip(), 1)

def _nodoc_status(dt, docs):
    low = (dt + ' ' + docs).lower()
    if 'none-found' in (dt or '').lower(): return 'unknown'
    if 'app-only' in low or 'no-doc' in low or 'no doc' in low or 'no financ' in low \
       or 'no tax' in low or 'instant' in low or 'no documents' in low:
        return 'YES'
    if 'recon' in low or 'app +' in low or 'app+' in low or 'limited' in low or 'partial' in low:
        return 'partial'
    if 'tax return' in low or 'financials required' in low or 'full doc' in low or '2 year' in low:
        return 'NO'
    if 'not stated' in low or not low.strip():
        return 'unknown'
    return 'partial'

ST_RANK = {'YES':4,'partial':3,'NO':2,'unknown':1}
def nodoc_for(name, city):
    cands = [r for r in nodoc if match(name, r.get('Institution',''))]
    if not cands:
        return 'unknown','UNKNOWN','',''
    best = None; best_key=(-1,-1)
    for r in cands:
        st = _nodoc_status(r.get('DP_type',''), r.get('Docs_required',''))
        key = (ST_RANK.get(st,0), grank(r.get('Evidence_grade','')))
        if key > best_key:
            best_key = key; best = (st, r)
    st, r = best
    note = f"{r.get('DP_type','')}; {r.get('Amount','')}; {r.get('Docs_required','')}".strip()
    return st, r.get('Evidence_grade','UNKNOWN'), note[:180], r.get('Source_link','')
print('loaders ready')

# ============================================================
# RECORD ASSEMBLY + TIERING
# ============================================================
def est_limit(deprow):
    t = (deprow.get('Terms','') or '')
    m = re.search(r'\$[\d,]+K?', t)
    return m.group(0) if m else ''

# explicit own-doc overrides per prompt (verified absence => likely-NO)
CHEX_OVERRIDE = {
  'commercial bank of california': ('NO','VERIFIED-own-doc','Own business deposit sections name no consumer-report clause / no ChexSystems/QualiFile [VERIFIED-absence own-doc 2026-06-11]'),
  'beneficial state bank': ('NO','VERIFIED-own-doc','Own Personal + BUSINESS Deposit Agreements name NO Chex/QualiFile/EWS; generic credit-verification clause only [VERIFIED-absence own-doc 2026-06-11]'),
}
EWS_OVERRIDE = {
  'commercial bank of california': ('NO','VERIFIED-own-doc','No Early Warning language in own business sections [VERIFIED-absence own-doc]'),
  'beneficial state bank': ('NO','VERIFIED-own-doc','0 "Early Warning" hits in both own agreements [VERIFIED-absence own-doc]'),
}

def is_online_national(deprow):
    t = (deprow.get('Type','') or '').lower()
    return 'online' in t and 'branch' not in t

def assemble(deprow):
    nm = deprow['Institution']
    city = deprow['City']
    is_cu = 'credit union' in (deprow.get('Type','') or '').lower()
    socal, counties, bcounts, hqc, hqs, crow = socal_info(nm, city, is_cu)
    bcities = branch_cities_for(nm)
    cities = []
    if hqc: cities.append(hqc.strip())
    for c in bcities:
        if c not in cities: cities.append(c)
    cities = cities[:4]
    cs,cg,cn,es,eg,en,csrc = chex_ews_for(nm, city, deprow)
    key = nm.lower().strip()
    for k,v in CHEX_OVERRIDE.items():
        if k in key: cs,cg,cn = v
    for k,v in EWS_OVERRIDE.items():
        if k in key: es,eg,en = v
    nst,ng,nn,nsrc = nodoc_for(nm, city)
    bf,bg,bsrc,bd = bureau_for(nm, city)
    rec = dict(
      institution=nm, website=deprow.get('Website',''), city=city,
      type=deprow.get('Type',''), is_cu=is_cu,
      socal=socal, counties=counties, bcounts=bcounts, cities=cities,
      hq_city=hqc, hq_state=hqs,
      deposits=deprow.get('Deposits',''),
      self_uw=('SELF' if deprow.get('Underwriter','').strip().upper()=='SELF' else deprow.get('Underwriter','')),
      uw_evidence=deprow.get('UW evidence',''),
      card='YES' if deprow.get('Biz card?','').strip().upper().startswith('YES') else deprow.get('Biz card?',''),
      card_link=deprow.get('Card link',''),
      apply=deprow.get('Apply',''), apply_link=deprow.get('Apply link',''),
      chex=cs, chex_grade=cg, chex_note=cn, chex_src=csrc,
      ews=es, ews_grade=eg, ews_note=en,
      nodoc=nst, nodoc_grade=ng, nodoc_note=nn, nodoc_src=nsrc,
      bureau=bf, bureau_grade=bg, bureau_src=bsrc, bureau_date=bd,
      est_limit=est_limit(deprow),
      sources=deprow.get('Sources',''),
    )
    # tier
    rec['tier'] = tier_of(rec)
    rec['online_national'] = is_online_national(deprow)
    rec['note'] = ''
    # CBC documented exception: no issued card product, kept as deposit-only no-Chex/EWS Tier-1
    if 'commercial bank of california' in key:
        rec['card'] = 'NO (deposit-only)'
        rec['note'] = 'Own site has NO issued business-card product (differentiates payment-processing from issuing). Kept in Tier 1 as a deposit-only verified no-Chex/no-EWS option — pair with a Tier-1/2 card from another row.'
    return rec

def tier_of(r):
    chex, ews, nodoc = r['chex'], r['ews'], r['nodoc']
    # Tier 3: pulls Chex AND/OR EWS confirmed
    if chex == 'YES' or ews == 'YES':
        return 3
    # Tier 1: Chex NO and EWS NO and no-doc YES/partial (or nodoc unknown w/ both clean -> still T1, flag)
    if chex == 'NO' and ews == 'NO':
        return 1
    # else (any UNKNOWN in chex/ews) -> Tier 2
    return 2

# build all records
records = [assemble(r) for r in main_set]

socal_recs = [r for r in records if r['socal']]
notsocal_recs = [r for r in records if not r['socal']]

# Re-tier honesty: Tier-1 requires SoCal too (all socal_recs already socal)
from collections import Counter
tcount = Counter(r['tier'] for r in socal_recs)
print('\\nSoCal tier counts:', dict(tcount))
print('Not-SoCal self-UW+card:', len(notsocal_recs))
for r in [x for x in socal_recs if x['tier']==1]:
    print('  T1:', r['institution'], '| nodoc=',r['nodoc'])

if __name__ == '__main__' and '--test' in sys.argv:
    for nm,cy,cu in [('Beneficial State Bank','Oakland',False),
                     ('COMMERCIAL BANK OF CALIFORNIA','Irvine',False),
                     ('CITY NATIONAL BANK','Los Angeles',False),
                     ('NUVISION FEDERAL CREDIT UNION','Huntington Beach',True),
                     ('BAY FEDERAL CREDIT UNION','Capitola',True),
                     ('MONTECITO BANK & TRUST','Santa Barbara',False),
                     ('Bank of America, National Association','Charlotte',False)]:
        socal,counties,bc,hqc,hqs,_ = socal_info(nm,cy,cu)
        dpr = next((r for r in dep if match(nm,r['Institution'])), None)
        cs,cg,cn,es,eg,en,csrc = chex_ews_for(nm,cy,dpr)
        nst,ng,nn,nsrc = nodoc_for(nm,cy)
        bf,bg,bsrc,bd = bureau_for(nm,cy)
        print(f'\\n{nm}\\n  SoCal={socal} counties={counties} hq={hqc},{hqs}')
        print(f'  Chex={cs}/{cg} EWS={es}/{eg}')
        print(f'  Nodoc={nst}/{ng}  Bureau={bf[:40]}/{bg}')
