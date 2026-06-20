#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import build_tiered as bt
from collections import Counter

recs = bt.socal_recs
ns   = bt.notsocal_recs

print('='*64)
print('SELF-CHECK — SoCal_SelfUW_Tiered_NoChex_v1')
print('='*64)

# tier counts
tc = Counter(r['tier'] for r in recs)
print(f'\nTIER COUNTS (SoCal main tab):  Tier1={tc.get(1,0)}  Tier2={tc.get(2,0)}  Tier3={tc.get(3,0)}  | total={len(recs)}')
print(f'NOT-SoCal (Tab 3): {len(ns)}')

# per county (T1+T2)
ctyc = Counter()
for r in recs:
    if r['tier'] in (1,2):
        for c in r['counties']: ctyc[c]+=1
print('\nCOUNTY COUNTS (Tier1+2):')
for c in ['Los Angeles','Orange','San Bernardino','Riverside','Ventura','San Diego']:
    print(f'   {c}: {ctyc.get(c,0)}')

# BUG ASSERTION: no green (Tier1) row with Chex=YES or EWS=YES
viol = [r for r in recs if r['tier']==1 and (r['chex']=='YES' or r['ews']=='YES')]
print(f'\n[ASSERT] zero green rows with Chex=YES or EWS=YES  ->  violations = {len(viol)}', '  PASS' if not viol else '  FAIL')
for v in viol: print('   VIOLATION:', v['institution'])

# Tier-1 invariants
print('\nTIER-1 MEMBERS (each must be: nodoc set, Chex=NO, EWS=NO, SoCal=YES):')
t1ok=True
for r in [x for x in recs if x['tier']==1]:
    ok = (r['chex']=='NO' and r['ews']=='NO' and r['socal'])
    nd = r['nodoc']  # may be unknown -> flagged
    flag = '' if nd in ('YES','partial') else ' [NO-DOC GAP — flagged]'
    t1ok = t1ok and ok
    print(f"   {r['institution']}: Chex={r['chex']} EWS={r['ews']} SoCal={r['socal']} nodoc={nd}{flag}  {'OK' if ok else 'BAD'}")
print(f'[ASSERT] every Tier-1 row Chex=NO & EWS=NO & SoCal=YES -> {"PASS" if t1ok else "FAIL"}')

# main-tab invariant: every row self-UW + card + SoCal (CBC = documented deposit-only exception)
def is_exception(r): return 'commercial bank of california' in r['institution'].lower()
bad_main = [r for r in recs if not is_exception(r) and not (r['self_uw'].upper().startswith('SELF') and r['card']=='YES' and r['socal'])]
exc = [r for r in recs if is_exception(r)]
print(f'\n[ASSERT] every main-tab row self-UW + card + SoCal (excl. documented exceptions) -> violations={len(bad_main)}', '  PASS' if not bad_main else '  FAIL')
for r in bad_main: print('   ', r['institution'], '| self_uw=',r['self_uw'],'card=',r['card'],'socal=',r['socal'])
for r in exc: print('   DOCUMENTED EXCEPTION (prompt-mandated Tier-1):', r['institution'], '|', r['card'], '— deposit-only no-Chex/EWS, flagged in workbook')

# website coverage
wc = sum(1 for r in recs if r['website'].startswith('http'))
print(f'\n[ASSERT] website hyperlink coverage (main tab): {wc}/{len(recs)} = {100*wc/len(recs):.0f}%')

# unmatched county (none silently dropped)
unm = [r['institution'] for r in recs if not r['counties']]
print(f'\nInstitutions on main tab with NO county match: {len(unm)}')
for u in unm: print('   ', u)

# list any self-UW+card institution whose SoCal status fell back to HQ-only (no census row)
print('\nNote: not-SoCal members (Tab 3):')
for r in sorted(ns, key=lambda x:-bt.n_int(x['deposits']))[:30]:
    why='online-national' if r['online_national'] else f"HQ {r['hq_city']},{r['hq_state']}"
    print(f"   {r['institution']}  ({why})")
print('\nDONE.')
