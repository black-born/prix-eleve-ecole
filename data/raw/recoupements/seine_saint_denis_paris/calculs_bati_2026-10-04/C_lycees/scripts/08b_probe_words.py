# -*- coding: utf-8 -*-
"""Positions des mots (UAI et montants) sur la page 7 de CR 2025-030 RAP, pour vérifier l'alignement des lignes."""
import sys
import pdfplumber

sys.stdout.reconfigure(encoding='utf-8')
W = 'C:/Users/chret/AppData/Local/Temp/claude/c--Users-chret-Documents-EtatEcole/5b29c961-d5a9-4d19-af60-f12e126ef8ef/scratchpad/analyse_bati/C_lycees/'
pdf = pdfplumber.open(W + 'raw/IDF_CR2025-030RAP.pdf')
page = pdf.pages[6]
words = page.extract_words()
rows = {}
for w in words:
    if w['top'] < 180:
        continue
    key = round(w['top'])
    rows.setdefault(key, []).append((round(w['x0']), w['text']))
for k in sorted(rows)[:60]:
    print(k, rows[k])
# lignes horizontales du tableau
hl = sorted(set(round(l['top']) for l in page.lines if abs(l['top'] - l['bottom']) < 1))
print('lignes horizontales:', hl[:40])
rects = sorted(set(round(r['top']) for r in page.rects))
print('rects top:', rects[:60])
