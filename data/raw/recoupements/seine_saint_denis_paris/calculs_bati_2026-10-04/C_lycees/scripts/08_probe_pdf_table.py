# -*- coding: utf-8 -*-
"""Sonde de la structure du tableau « Dotation de fonctionnement consolidée 2016 / 2026 » (CR 2025-030, annexe 1 au rapport)."""
import sys
import pdfplumber

sys.stdout.reconfigure(encoding='utf-8')
W = 'C:/Users/chret/AppData/Local/Temp/claude/c--Users-chret-Documents-EtatEcole/5b29c961-d5a9-4d19-af60-f12e126ef8ef/scratchpad/analyse_bati/C_lycees/'
pdf = pdfplumber.open(W + 'raw/IDF_CR2025-030RAP.pdf')
print(len(pdf.pages))
for pno in [6]:
    page = pdf.pages[pno]
    print('== page', pno + 1, page.width, page.height)
    tables = page.extract_tables()
    print('n tables', len(tables))
    for t in tables[:1]:
        for row in t[:25]:
            print(row)
    words = page.extract_words(keep_blank_chars=False, use_text_flow=False)
    for w in words[:80]:
        print(round(w['x0'], 1), round(w['top'], 1), w['text'])
