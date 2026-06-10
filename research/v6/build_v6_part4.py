#!/usr/bin/env python3
"""v6 Part 4: CSV export (task 11) + SELF-CHECK (task 12)."""
import csv, openpyxl

BASE = '/home/user/awake/research/v6'
V6 = f'{BASE}/deliverables/ca_business_credit_funding_v6.xlsx'
V5 = f'{BASE}/ca_business_credit_funding_v5.xlsx'
OUTCSV = f'{BASE}/deliverables/ca_business_credit_funding_v6_funding_table.csv'

# ---------------- TASK 11: export Funding Table CSV
wb6 = openpyxl.load_workbook(V6)
ft = wb6['Funding Table']
with open(OUTCSV, 'w', newline='') as f:
    w = csv.writer(f)
    for row in ft.iter_rows(min_row=1, max_row=ft.max_row, max_col=36):
        w.writerow(['' if c.value is None else str(c.value) for c in row])
print(f'Exported {OUTCSV}: {ft.max_row} rows x 36 cols')

# ---------------- TASK 12: self-check
wb5 = openpyxl.load_workbook(V5)
violations = []
print('\n===== SELF-CHECK =====')

# (a) every v5 tab preserved, row counts not reduced
print('(a) v5 tab preservation:')
for name in wb5.sheetnames:
    if name not in wb6.sheetnames:
        violations.append(f'TAB MISSING: {name}')
        print(f'  ✗ {name}: MISSING'); continue
    r5, r6 = wb5[name].max_row, wb6[name].max_row
    ok = r6 >= r5
    print(f'  {"✓" if ok else "✗"} {name}: v5 {r5} rows -> v6 {r6} rows')
    if not ok:
        violations.append(f'ROWS LOST in {name}: {r5}->{r6}')

# (b) cell-by-cell add-only audit on ALL v5 tabs
def is_nm(v):
    s = ('' if v is None else str(v)).strip()
    return s in ('', 'N/M', '—', '-', '–') or s.startswith('N/M')

print('(b) cell-by-cell add-only audit (identical | strict-append | allowed N/M-overwrite):')
tot = ident = app = nmover = 0
for name in wb5.sheetnames:
    ws5, ws6 = wb5[name], wb6[name]
    for r in range(1, ws5.max_row + 1):
        for c in range(1, ws5.max_column + 1):
            v5v, v6v = ws5.cell(r, c).value, ws6.cell(r, c).value
            if v5v is None and v6v is None:
                continue
            tot += 1
            s5 = '' if v5v is None else str(v5v)
            s6 = '' if v6v is None else str(v6v)
            if s5 == s6:
                ident += 1
            elif s6.startswith(s5) and ' ‖ v6 2026-06-10: ' in s6:
                app += 1
            elif is_nm(v5v):
                nmover += 1
            else:
                violations.append(f'{name}!{ws5.cell(r,c).coordinate}: OLD={s5[:80]!r} NEW={s6[:80]!r}')
print(f'  cells compared: {tot} | identical: {ident} | strict-appends: {app} | allowed N/M-overwrites: {nmover}')
print(f'  VIOLATIONS: {len(violations)}')
for v in violations[:20]:
    print('   ✗', v)

# (c) new tab row counts vs source CSVs
print('(c) new dump tabs vs source CSVs:')
import os
pairs = [('FDIC SOD 6cty 2025', 'out/fdic_sod_census_6cty_2025.csv'),
         ('NCUA CU 6cty 2026Q1', 'out/ncua_cu_census_6cty.csv'),
         ('EWS-Chex Map v6', 'out/ews_chex_mapping.csv'),
         ('ibanknet CA 2026Q1', 'out/ibanknet_ca_institutions.csv')]
for tab, path in pairs:
    src = len(list(csv.reader(open(f'{BASE}/{path}'))))
    got = wb6[tab].max_row
    ok = src == got
    print(f'  {"✓" if ok else "✗"} {tab}: source {src} rows == tab {got} rows')
    if not ok:
        violations.append(f'ROWCOUNT {tab}: {src} vs {got}')

# extras: funding-table structural checks
ft5 = wb5['Funding Table']
print('(extras) Funding Table:')
print(f'  v5 data rows: {ft5.max_row-1} -> v6 data rows: {ft.max_row-1} (added {ft.max_row-ft5.max_row})')
print(f'  freeze panes: {ft.freeze_panes} (v5: {ft5.freeze_panes}) | autofilter: {ft.auto_filter.ref}')
ranks = [str(ft.cell(r, 1).value) for r in range(215, ft.max_row + 1)]
print(f'  new Rec Ranks: {ranks[0]}..{ranks[-1]} contiguous={ranks == [str(i) for i in range(214, 214+len(ranks))]}')
newmark = sum(1 for r in range(215, ft.max_row + 1) if str(ft.cell(r, 35).value).startswith('NEW v6 2026-06-10'))
print(f'  new rows with NEW-v6 Confidence/Date marker: {newmark}/{len(ranks)}')

print('\nRESULT:', 'PASS — fully add-only' if not violations else f'{len(violations)} VIOLATIONS — FIX REQUIRED')
