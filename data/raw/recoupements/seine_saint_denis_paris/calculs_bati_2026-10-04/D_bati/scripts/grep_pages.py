# -*- coding: utf-8 -*-
"""Recherche de termes dans les textes extraits (pdftotext -layout) avec numéro de page PDF.

Usage : python grep_pages.py <fichier.txt> <regex> [contexte_lignes]
Sortie : pour chaque occurrence, « p. <page PDF> | l. <ligne> » puis le contexte.
Le numéro de page est celui du PDF (1 = première page du fichier), obtenu en
comptant les sauts de page (\f) insérés par pdftotext.
"""
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

path, pattern = sys.argv[1], sys.argv[2]
ctx = int(sys.argv[3]) if len(sys.argv) > 3 else 2
rx = re.compile(pattern, re.IGNORECASE)

with open(path, encoding="utf-8", errors="replace") as fh:
    text = fh.read()

pages = text.split("\f")
seen = set()
for pno, page in enumerate(pages, start=1):
    lines = page.split("\n")
    for i, line in enumerate(lines):
        if rx.search(line):
            lo, hi = max(0, i - ctx), min(len(lines), i + ctx + 1)
            key = (pno, lo)
            if key in seen:
                continue
            seen.add(key)
            print(f"=== p. {pno} | l. {i+1}")
            for j in range(lo, hi):
                print("   " + lines[j].rstrip())
