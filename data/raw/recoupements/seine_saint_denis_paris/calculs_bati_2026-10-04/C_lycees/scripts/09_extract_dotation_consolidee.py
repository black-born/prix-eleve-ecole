# -*- coding: utf-8 -*-
"""Extraction de l'annexe 1 au rapport CR 2025-030 (Région Île-de-France, conseil régional du 24/09/2025) :
« Financement régional du fonctionnement des EPLE - Dotation de fonctionnement consolidée » 2016 et 2026, par établissement.
Source : https://www.iledefrance.fr/actes/deliberations/CR2025-030RAP.pdf (pages 7 à 13 du PDF).
Périmètre (note de l'annexe) : 2016 = DGFL + énergie + CTO-CEO votés en 2016 ; 2026 = DGFL + dotation internat + CTO-CEO
proposés pour 2026 + demandes budgétaires 2026 pour l'énergie et les EPI (sous réserve du vote du budget 2026).
Méthode : pdfplumber ; lignes reconstituées à partir de la position verticale des mots (l'extraction « layout » de pdftotext
décale les montants de certaines lignes) ; montant = concaténation des fragments numériques des colonnes 2016 (x ~ 425-495)
et 2026 (x ~ 495-560). Les lignes « Total » délimitent les sections : EPLE, CMR (cités mixtes régionales), CMD (cités
mixtes départementales), puis « lycées actifs en 2026 et absents de la liste régionale en 2016 ».
Sortie : resultats/dotation_consolidee_2016_2026_par_UAI.csv ; contrôle des totaux publiés.
"""
import re
import sys
import pdfplumber
import pandas as pd

sys.stdout.reconfigure(encoding='utf-8')
W = 'C:/Users/chret/AppData/Local/Temp/claude/c--Users-chret-Documents-EtatEcole/5b29c961-d5a9-4d19-af60-f12e126ef8ef/scratchpad/analyse_bati/C_lycees/'
pdf = pdfplumber.open(W + 'raw/IDF_CR2025-030RAP.pdf')

UAI_RE = re.compile(r'^\d{7}[A-Z]$')
NUM_RE = re.compile(r'^\d+$')


def montant(ws, x0, x1):
    s = ''.join(w['text'] for w in sorted(ws, key=lambda w: w['x0']) if x0 <= w['x0'] < x1 and NUM_RE.match(w['text']))
    return int(s) if s else None


rows, totaux = [], []
section = 'EPLE'
for pno in range(6, 13):
    page = pdf.pages[pno]
    words = page.extract_words()
    lines = {}
    for w in words:
        lines.setdefault(round(w['top']), []).append(w)
    for y in sorted(lines):
        ws = lines[y]
        texts = [w['text'] for w in ws]
        if 'Total' in texts or 'TOTAL' in texts:
            label = ' '.join(w['text'] for w in sorted(ws, key=lambda w: w['x0']) if w['x0'] < 420)
            # les montants d'une ligne « Total » peuvent être sur la ligne suivante (Total CMD)
            nxt = [w for yy in lines if 0 < yy - y <= 3 for w in lines[yy]]
            totaux.append({'page_pdf': pno + 1, 'libelle': label, 'v2016': montant(ws + nxt, 425, 495), 'v2026': montant(ws + nxt, 495, 560)})
            if 'EPLE' in texts:
                section = 'CMR'
            elif 'CMR' in texts:
                section = 'CMD'
            elif 'CMD' in texts:
                section = 'apres_CMD'
            elif 'général' in texts:
                section = 'nouveaux_2026'
            continue
        if 'absents' in texts:
            section = 'nouveaux_2026'
        uai = [w for w in ws if UAI_RE.match(w['text']) and w['x0'] < 80]
        if not uai:
            # ligne fusionnée : deux UAI (lycée général et lycée professionnel) pour un seul montant
            v16, v26 = montant(ws, 425, 495), montant(ws, 495, 560)
            if v26 is not None and 'Total' not in texts and 'CONSOLIDEE' not in texts:
                us = [w['text'] for yy in lines if abs(yy - y) <= 6 for w in lines[yy] if UAI_RE.match(w['text']) and w['x0'] < 80]
                if us:
                    rows.append({'page_pdf': pno + 1, 'section': section, 'uai': '+'.join(sorted(us)),
                                 'patronyme': ' '.join(w['text'] for w in sorted(ws, key=lambda w: w['x0']) if 85 <= w['x0'] < 220),
                                 'commune': ' '.join(w['text'] for w in sorted(ws, key=lambda w: w['x0']) if 220 <= w['x0'] < 340),
                                 'type_lycee': ' '.join(w['text'] for w in ws if 340 <= w['x0'] < 400),
                                 'dotation_consolidee_2016': v16, 'dotation_consolidee_2026': v26})
            continue
        if not any(425 <= w['x0'] < 560 and NUM_RE.match(w['text']) for w in ws):
            continue  # UAI d'une ligne fusionnée, traitée avec la ligne des montants
        u = uai[0]
        near = [w for yy in lines if abs(yy - y) < 8 for w in lines[yy] if 85 <= w['x0'] < 220]
        patro = ' '.join(w['text'] for w in sorted(near, key=lambda w: (round(w['top']), w['x0'])))
        rows.append({'page_pdf': pno + 1, 'section': section, 'uai': u['text'], 'patronyme': patro,
                     'commune': ' '.join(w['text'] for w in sorted(ws, key=lambda w: w['x0']) if 220 <= w['x0'] < 340),
                     'type_lycee': ' '.join(w['text'] for w in ws if 340 <= w['x0'] < 400),
                     'dotation_consolidee_2016': montant(ws, 425, 495),
                     'dotation_consolidee_2026': montant(ws, 495, 560)})

d = pd.DataFrame(rows)
t = pd.DataFrame(totaux)
print(t.to_string())
print(d.shape, d['uai'].nunique())
print(d.groupby('section')[['dotation_consolidee_2016', 'dotation_consolidee_2026']].agg(['sum', 'count']))
print('dup UAI:', d[d['uai'].duplicated(keep=False)])
d['dep'] = d['uai'].str[1:3]
d.to_csv(W + 'resultats/dotation_consolidee_2016_2026_par_UAI.csv', sep=';', index=False, encoding='utf-8-sig')
t.to_csv(W + 'resultats/dotation_consolidee_2016_2026_totaux_publies.csv', sep=';', index=False, encoding='utf-8-sig')
print(d.groupby(['dep'])[['dotation_consolidee_2016', 'dotation_consolidee_2026']].agg(['sum', 'count']))
