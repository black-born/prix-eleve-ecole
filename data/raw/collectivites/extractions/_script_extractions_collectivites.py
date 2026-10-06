# -*- coding: utf-8 -*-
"""
Extractions dérivées de l'axe « Collectivités territoriales » (consulté le 2026-10-04).
Lit UNIQUEMENT les fichiers bruts du dossier parent (data/raw/collectivites/) et écrit des CSV dérivés dans extractions/.
Aucun fichier brut n'est modifié. Montants en millions d'euros courants (M€) sauf mention contraire.

Usage : python _script_extractions_collectivites.py   (depuis n'importe quel répertoire)
"""
import os
import numpy as np
import pandas as pd
import openpyxl

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.dirname(HERE)
OUT = HERE


def raw(name):
    return os.path.join(RAW, name)


# ---------------------------------------------------------------------------
# A. DGCL, Les collectivités locales en chiffres 2026, fichier 4F (ventilation fonctionnelle, comptes de gestion 2025)
# ---------------------------------------------------------------------------
def extract_dgcl_4f():
    wb = openpyxl.load_workbook(raw('DGCL_CLC2026_4F_Ventilation_fonctionnelle_CG25.xlsx'), data_only=True)
    rows = []
    # F1-F4 : colonnes B,C,D = 2025 (fonct., invest., total) ; P,Q,R = 2024 (N-1)
    # F5 et F6 : colonnes B,C,D = 2025 ; M,N,O = 2024
    specs = {
        'F1 Comm': ('Communes >= 3 500 hab. (Paris inclus), budgets principaux', 'BCD', 'PQR'),
        'F2 GFP': ('GFP ayant au moins une commune >= 3 500 hab. (Métropole de Lyon incluse), budgets principaux', 'BCD', 'PQR'),
        'F3 Dept': ('Départements, budgets principaux', 'BCD', 'PQR'),
        'F4 Reg+CTU': ('Régions et CTU, budgets principaux', 'BCD', 'PQR'),
        'F5 Ens': ('Ensemble collectivités et GFP dans le champ, budgets principaux', 'BCD', 'MNO'),
        'F6 BA et Synd': ('F6a budgets annexes (lignes 5-19) / F6b syndicats (lignes 27-41), selon code activité', 'BCD', 'MNO'),
    }
    # lignes retenues (vérifiées une à une le 2026-10-04) : fonction « Enseignement, formation et apprentissage » et ses
    # sous-fonctions, « Transports scolaires », totaux et hors-champ
    rows_keep = {
        'F1 Comm': [16, 17, 18, 19, 20, 21, 22, 54, 65, 66, 67],
        'F2 GFP': [16, 17, 18, 19, 20, 21, 22, 54, 65, 66, 67],
        'F3 Dept': [13, 14, 15, 16, 17, 18, 53, 65, 66],
        'F4 Reg+CTU': [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 42, 61, 62],
        'F5 Ens': [11, 12, 13, 14, 15, 16, 37, 47, 48, 49],
        'F6 BA et Synd': [8, 16, 18, 30, 38, 40],
    }
    for sheet, (champ, c25, c24) in specs.items():
        ws = wb[sheet]
        for r in rows_keep[sheet]:
            lab = ws.cell(r, 1).value
            if not isinstance(lab, str):
                continue
            def v(col):
                x = ws[f'{col}{r}'].value
                return round(float(x), 3) if isinstance(x, (int, float)) else None
            sub = ''
            if sheet == 'F6 BA et Synd':
                sub = 'F6a budgets annexes' if r < 25 else 'F6b syndicats'
            rows.append({
                'tableau': sheet, 'sous_tableau': sub, 'champ': champ, 'ligne': r, 'libelle': lab.strip(),
                'fonct_2025': v(c25[0]), 'invest_2025': v(c25[1]), 'total_2025': v(c25[2]),
                'fonct_2024': v(c24[0]), 'invest_2024': v(c24[1]), 'total_2024': v(c24[2]),
                'cellules_2025': f'{c25[0]}{r}:{c25[2]}{r}', 'cellules_2024': f'{c24[0]}{r}:{c24[2]}{r}',
            })
    df = pd.DataFrame(rows)
    df.to_csv(os.path.join(OUT, 'DGCL_4F_enseignement_transport_2024_2025.csv'), sep=';', index=False, encoding='utf-8-sig')
    return df


# ---------------------------------------------------------------------------
# B. DGFiP, balances comptables présentation croisée nature-fonction 2025 (export agrégé API)
# ---------------------------------------------------------------------------
def load_dgfip():
    df = pd.read_csv(raw('DGFiP_balances_nature-fonction_2025_fonction2_et_81_agrege_API.csv'), sep=';', encoding='utf-8-sig',
                     dtype={'ctype': str, 'cstyp': str, 'cacti': str, 'cbudg': str, 'fonction': str, 'compte': str})
    for c in ['obnetdeb', 'obnetcre', 'oobdeb', 'oobcre']:
        df[c] = df[c].fillna(0.0)
    # opérations réelles = opérations budgétaires nettes - opérations d'ordre budgétaires
    df['deb'] = df.obnetdeb - df.oobdeb
    df['cre'] = df.obnetcre - df.oobcre
    # budgets votés par fonction : codes « 90 » (investissement) / « 93 » (fonctionnement) + code fonctionnel
    df['f'] = [x[2:] if (x.startswith('90') or x.startswith('93')) else x for x in df.fonction]

    def nature(c):
        if c.startswith('6'):
            if c.startswith(('675', '676', '68')):
                return 'exclu_ordre'
            if c.startswith('66'):
                return 'F_charges_financieres'
            if c.startswith(('621', '631', '633', '64')):
                return 'F_personnel'
            if c[:2] in ('60', '61', '62'):
                return 'F_achats_charges_externes'
            if c.startswith(('655', '657', '651', '652', '656')):
                return 'F_interventions'
            return 'F_autres'
        if c.startswith('204'):
            return 'I_subventions_equipement_versees'
        if c[:2] in ('20', '21', '23'):
            return 'I_equipement'
        if c[:2] in ('26', '27'):
            return 'exclu' if c.startswith(('269', '2768', '279')) else 'I_autres'
        if c.startswith('102'):
            return 'exclu' if c.startswith(('10229', '1027')) else 'I_autres'
        if c.startswith('13'):
            return 'exclu' if c.startswith('139') else 'I_autres'
        if c[:3] in ('454', '455', '456', '458') or c.startswith('481'):
            return 'I_autres'
        return 'hors_depense'
    df['nature'] = df.compte.map(nature)

    def montant(r):
        n = r.nature
        if n.startswith('F_'):
            return r.deb - r.cre          # débit net (définition DGCL)
        if n == 'I_equipement':
            # débit 20 (hors 204), 21, 23 - crédit 236, 237, 238 (définition DGCL)
            return r.deb - (r.cre if r.compte[:3] in ('236', '237', '238') else 0.0)
        if n in ('I_subventions_equipement_versees', 'I_autres'):
            return r.deb
        return np.nan
    df['montant'] = df.apply(montant, axis=1)
    grp = {'Commune': 'Communes (y.c. Paris)', 'PARIS': 'Communes (y.c. Paris)', 'GFP': 'GFP (y.c. Métropole de Lyon, EPT)',
           'ML': 'GFP (y.c. Métropole de Lyon, EPT)', 'EPT': 'GFP (y.c. Métropole de Lyon, EPT)', 'DEPT': 'Départements',
           'REG': 'Régions et CTU', 'CTU': 'Régions et CTU', 'EPL': 'Établissements publics locaux', 'SYND': 'Syndicats'}
    df['niveau'] = df.categ.map(grp)

    def sousfonction(f):
        if f.startswith('81'):
            return '81 Transports scolaires'
        lab3 = {'211': '211 Écoles maternelles', '212': '212 Écoles primaires', '213': '213 Classes regroupées',
                '221': '221 Collèges', '222': '222 Lycées publics', '223': '223 Lycées privés',
                '281': '281 Hébergement et restauration scolaires', '282': '282 Sport scolaire', '283': '283 Médecine scolaire',
                '284': '284 Classes de découverte', '288': '288 Autres services annexes'}
        lab2 = {'20': '20 Services communs', '21': '21 Premier degré (non ventilé)', '22': '22 Second degré (non ventilé)',
                '23': '23 Enseignement supérieur', '24': '24 Cités scolaires', '25': '25 Formation professionnelle',
                '26': '26 Apprentissage', '27': '27 Formation sanitaire et sociale', '28': '28 Services périscolaires et annexes (non ventilé)',
                '29': '29 Sécurité'}
        if f[:3] in lab3:
            return lab3[f[:3]]
        if f[:2] in lab2:
            return lab2[f[:2]]
        return '2 Enseignement (non ventilé)'
    df['sous_fonction'] = df.f.map(sousfonction)
    return df


def perimetre(niveau, sf):
    """Périmètre « scolaire » retenu pour chaque niveau (hypothèse documentée dans NOTES.md)."""
    code = sf.split(' ')[0]
    if code.startswith('81'):
        return 'transport scolaire'
    if code in ('23', '25', '26', '27'):
        return 'hors scolaire (supérieur, formation pro., apprentissage, sanitaire et social)'
    if niveau in ('Communes (y.c. Paris)', 'GFP (y.c. Métropole de Lyon, EPT)'):
        if code.startswith('21') or code.startswith('28') or code in ('20', '29', '2'):
            return 'écoles (1er degré)'
        return 'collèges-lycées (cas particuliers : Paris, Métropole de Lyon)'
    if niveau == 'Départements':
        if code.startswith('21'):
            return 'écoles (1er degré)'
        return 'collèges'
    if niveau == 'Régions et CTU':
        if code.startswith('21'):
            return 'écoles (1er degré)'
        if code == '221':
            return 'collèges (CTU : Corse, Guyane, Martinique)'
        return 'lycées'
    return 'non classé (EPL, syndicats)'


def poste(compte, sf):
    """Postes détaillés (libellés M57 : OFGL_nomenclature_M57_2025_libelles_comptes.csv)."""
    c = compte
    if c.startswith(('621', '631', '633', '64')):
        return 'Personnel (621, 631, 633, 64)'
    if c.startswith(('60611', '60612', '60613', '60621', '60622')):
        return 'Énergie et fluides (6061x, 60621-60622)'
    if c.startswith(('60623', '6042', '611')):
        return 'Alimentation, prestations de services et contrats (60623, 6042, 611)'
    if c.startswith(('6152', '6156', '6283')):
        return 'Entretien, maintenance, nettoyage (6152x, 6156, 6283)'
    if c.startswith('6067'):
        return 'Fournitures scolaires (6067)'
    if c.startswith(('655111', '655121')):
        return 'Dotations de fonctionnement aux établissements publics (655111 collèges, 655121 lycées)'
    if c.startswith(('655112', '655122')):
        return 'Dotations de fonctionnement aux établissements privés sous contrat (655112, 655122)'
    if c in ('65511', '65512'):
        return 'Dotations de fonctionnement collèges/lycées non subdivisées (65511, 65512)'
    if c.startswith('657364'):
        return 'Subventions aux caisses des écoles (657364)'
    if c.startswith('6558'):
        return 'Autres contributions obligatoires (6558 : forfait écoles privées, frais de scolarité intercommunaux)'
    if c.startswith(('6573', '6574', '655', '656', '651', '652', '657')):
        return 'Autres subventions et participations (65x)'
    if c[:2] in ('60', '61', '62'):
        return 'Autres achats et charges externes (60-62)'
    if c.startswith('6'):
        return 'Autres charges de fonctionnement'
    if c.startswith(('2313', '2312', '2314', '2315', '2318', '2135', '2131', '21312', '217', '2317', '238', '236', '237', '2324')):
        return 'Constructions, rénovations, grosses réparations, mises à disposition, avances (231x, 2131x, 2135x, 217x, 2317, 236-238)'
    if c.startswith(('2183', '2184', '2188', '2157', '2158', '2154', '2182', '2185', '2181', '215')):
        return 'Équipement : informatique, mobilier, matériel (218x, 215x)'
    if c.startswith(('203', '205', '208', '201')):
        return 'Études, logiciels, incorporels (20 hors 204)'
    if c.startswith('204'):
        return "Subventions d'équipement versées (204)"
    if c[:2] in ('21', '23'):
        return 'Autres immobilisations (21, 23)'
    return 'Autres investissements (13, 26, 27, 45x, 481)'


def extract_dgfip(df):
    d = df[df.nature.str.startswith(('F_', 'I_')) & (df.nature != 'F_charges_financieres')].copy()
    d['section'] = np.where(d.nature.str.startswith('F_'), 'fonctionnement', 'investissement')
    d['budget'] = d.cbudg.map({'1': 'budget principal', '2': 'budget principal rattaché', '3': 'budget annexe'})
    d['perimetre'] = [perimetre(n, s) for n, s in zip(d.niveau, d.sous_fonction)]
    d['poste'] = [poste(c, s) for c, s in zip(d.compte, d.sous_fonction)]
    # B1. niveau x budget x sous-fonction x nature
    b1 = d.groupby(['niveau', 'budget', 'perimetre', 'sous_fonction', 'section', 'nature'], dropna=False).montant.sum().div(1e6).round(3).reset_index()
    b1 = b1.rename(columns={'montant': 'montant_M€'})
    b1.to_csv(os.path.join(OUT, 'DGFiP_2025_enseignement_niveau_sousfonction_nature.csv'), sep=';', index=False, encoding='utf-8-sig')
    # B2. postes clés, budgets principaux
    bp = d[d.cbudg == '1']
    b2 = bp.groupby(['niveau', 'perimetre', 'section', 'poste']).montant.sum().div(1e6).round(1).reset_index()
    b2 = b2.rename(columns={'montant': 'montant_M€'})
    b2.to_csv(os.path.join(OUT, 'DGFiP_2025_enseignement_postes_cles_budgets_principaux.csv'), sep=';', index=False, encoding='utf-8-sig')
    # B3. synthèse par niveau x périmètre (budgets principaux)
    b3 = bp.pivot_table(index=['niveau', 'perimetre'], columns='section', values='montant', aggfunc='sum').fillna(0).div(1e6).round(1)
    b3['total'] = b3.sum(axis=1)
    b3.reset_index().to_csv(os.path.join(OUT, 'DGFiP_2025_enseignement_synthese_niveau_perimetre_BP.csv'), sep=';', index=False, encoding='utf-8-sig')
    # B4. sous-fonction 281 restauration (toutes natures) par niveau
    return d, b1, b2, b3


# ---------------------------------------------------------------------------
# C. Couverture de la comptabilité fonctionnelle des communes et dépense par élève du public (2025)
# ---------------------------------------------------------------------------
def insee_code(nd, ins):
    if nd.startswith('1'):          # DROM : 101 Guadeloupe, 102 Guyane, 103 Martinique, 104 La Réunion, 106 Mayotte
        return '97' + ins
    return nd[1:] + ins             # 001 -> 01 ; 02A -> 2A


def norm_commune(c):
    if not isinstance(c, str):
        return c
    if c.startswith('751') and len(c) == 5:
        return '75056'   # arrondissements de Paris
    if c.startswith('6938'):
        return '69123'   # Lyon
    if c.startswith('132') and len(c) == 5:
        return '13055'   # Marseille
    return c


def extract_couverture():
    dep = {}
    for kind, fname in [('fonct', 'DGFiP_balances_nature-fonction_2025_communes_ecoles_fonct_par_commune_API.csv'),
                        ('invest', 'DGFiP_balances_nature-fonction_2025_communes_ecoles_invest_par_commune_API.csv')]:
        f = pd.read_csv(raw(fname), sep=';', dtype={'ndept': str, 'insee': str, 'siren': str}, encoding='utf-8-sig')
        for c in ['obnetdeb', 'obnetcre', 'oobdeb', 'oobcre']:
            f[c] = f[c].fillna(0)
        f['code'] = [insee_code(a, b) for a, b in zip(f.ndept, f.insee)]
        f['m'] = (f.obnetdeb - f.oobdeb) - (f.obnetcre - f.oobcre) if kind == 'fonct' else (f.obnetdeb - f.oobdeb)
        dep[kind] = f.groupby('code').m.sum()
    dep = pd.DataFrame(dep).fillna(0)
    dep['total'] = dep.fonct + dep.invest
    e = pd.read_csv(raw('MEN_effectifs_par_ecole_rentrees2024-2025_extrait_API.csv'), sep=';', dtype={'numero_ecole': str}, encoding='utf-8-sig')
    e['annee'] = e.rentree_scolaire.astype(str).str[:4].astype(int)
    a = pd.read_csv(raw('MEN_annuaire_education_ecoles_UAI_commune_extrait_API.csv'), sep=';', dtype=str, encoding='utf-8-sig')
    a = a.drop_duplicates('identifiant_de_l_etablissement').set_index('identifiant_de_l_etablissement')
    e['code'] = e.numero_ecole.map(a.code_commune).map(norm_commune)
    pub = e[e.secteur.str.upper().str.startswith('PUBLIC')]
    tot_rentree = pub.groupby('annee').nombre_total_eleves.sum()
    non_app = pub[pub.code.isna()].groupby('annee').nombre_total_eleves.sum()
    pc = pub.dropna(subset=['code']).pivot_table(index='code', columns='annee', values='nombre_total_eleves', aggfunc='sum').fillna(0)
    pc['civil2025'] = 2 / 3 * pc[2024] + 1 / 3 * pc[2025]
    pc['couverte'] = pc.index.isin(dep.index[dep.fonct > 0])
    tot = pc.civil2025.sum()
    cov = pc.loc[pc.couverte, 'civil2025'].sum()
    j = dep.join(pc[['civil2025']], how='left').fillna({'civil2025': 0})
    jc = j[j.civil2025 > 0]
    res = [
        ('Élèves des écoles publiques, rentrée 2024 (jeu fr-en-ecoles-effectifs-nb_classes)', tot_rentree.get(2024)),
        ('Élèves des écoles publiques, rentrée 2025', tot_rentree.get(2025)),
        ('dont non appariés à une commune (UAI absente de l annuaire actuel), rentrée 2024', non_app.get(2024, 0)),
        ('dont non appariés, rentrée 2025', non_app.get(2025, 0)),
        ('Élèves du public appariés, année civile 2025 (2/3 R2024 + 1/3 R2025)', tot),
        ('dont dans des communes à comptabilité fonctionnelle (fonction 20/21/28/29 > 0 en 2025)', cov),
        ('Part des élèves du public couverts par la comptabilité fonctionnelle', cov / tot),
        ('Nombre de communes ayant au moins une école publique', len(pc)),
        ('dont communes couvertes', int(pc.couverte.sum())),
        ('Dépense écoles des communes couvertes, fonctionnement, M€', dep.fonct.sum() / 1e6),
        ('Dépense écoles des communes couvertes, investissement (20, 21, 23), M€', dep.invest.sum() / 1e6),
        ('Dépense écoles des communes couvertes, total, M€', dep.total.sum() / 1e6),
        ('Dépense moyenne par élève du public (communes couvertes), total, €', jc.total.sum() / cov),
        ('Dépense moyenne par élève du public (communes couvertes), fonctionnement, €', jc.fonct.sum() / cov),
        ('Dépense moyenne par élève du public (communes couvertes), investissement, €', jc.invest.sum() / cov),
        ('Médiane communale de la dépense par élève du public, total, €', (jc.total / jc.civil2025).median()),
        ('Médiane communale de la dépense par élève du public, fonctionnement, €', (jc.fonct / jc.civil2025).median()),
        ('Élèves du public dans des communes non couvertes (année civile 2025)', tot - cov),
        ('Communes non couvertes ayant une école publique', int((~pc.couverte).sum())),
        ('Extrapolation type OFGL (total couvert / part couverte), M€', dep.total.sum() / (cov / tot) / 1e6),
    ]
    bins = [0, 100, 200, 300, 500, 1000, 2000, 5000, 1e9]
    jc = jc.assign(classe=pd.cut(jc.civil2025, bins, right=False))
    g = jc.groupby('classe', observed=True).agg(nb_communes=('total', 'size'), eleves=('civil2025', 'sum'), depense=('total', 'sum'), fonct=('fonct', 'sum'))
    for cl, r in g.iterrows():
        res.append((f'Communes couvertes {cl} élèves publics : nb communes | élèves | dépense M€ | € par élève (total) | € par élève (fonct.)',
                    f"{int(r.nb_communes)} | {round(r.eleves)} | {round(r.depense / 1e6, 1)} | {round(r.depense / r.eleves)} | {round(r.fonct / r.eleves)}"))
    unc = pc[~pc.couverte]
    gu = unc.groupby(pd.cut(unc.civil2025, bins, right=False), observed=True).civil2025.agg(['size', 'sum'])
    for cl, r in gu.iterrows():
        res.append((f'Communes NON couvertes {cl} élèves publics : nb communes | élèves', f"{int(r['size'])} | {round(r['sum'])}"))
    out = pd.DataFrame(res, columns=['indicateur', 'valeur'])
    out.to_csv(os.path.join(OUT, 'DGFiP_MEN_2025_communes_couverture_et_depense_par_eleve.csv'), sep=';', index=False, encoding='utf-8-sig')
    return out


# ---------------------------------------------------------------------------
# D. DEPP : part des collectivités par niveau (NI 26.42) et financement final 2024p (RERS 2026)
# ---------------------------------------------------------------------------
def extract_depp():
    wb = openpyxl.load_workbook(raw('DEPP_NI_26-42_compte_education_2025_donnees.xlsx'), data_only=True)
    f4, f5, f6, f2 = wb['Figure 4'], wb['Figure 5'], wb['Figure 6'], wb['Figure 2']
    die1, die2 = f5['B32'].value, f5['B33'].value            # Md€
    ct1, ct2 = f4['B33'].value, f4['C33'].value              # % financement initial
    pe1, pe2 = f6['E31'].value, f6['E33'].value              # € par élève
    rows = [
        ('DIE premier degré 2025p, Md€', die1, 'NI 26.42 xlsx, Figure 5, B32'),
        ('DIE second degré (apprentissage compris) 2025p, Md€', die2, 'NI 26.42 xlsx, Figure 5, B33'),
        ('Part des collectivités territoriales, financement initial, premier degré 2025p, %', ct1, 'NI 26.42 xlsx, Figure 4, B33'),
        ('Part des collectivités territoriales, financement initial, second degré 2025p, %', ct2, 'NI 26.42 xlsx, Figure 4, C33'),
        ('Montant CT premier degré 2025p (calcul = part x DIE), M€', ct1 / 100 * die1 * 1000, 'calcul dérivé'),
        ('Montant CT second degré 2025p (calcul = part x DIE), M€', ct2 / 100 * die2 * 1000, 'calcul dérivé'),
        ('Dépense moyenne par élève premier degré 2025p, €', pe1, 'NI 26.42 xlsx, Figure 6, E31'),
        ('Dépense moyenne par élève second degré 2025p, €', pe2, 'NI 26.42 xlsx, Figure 6, E33'),
        ('Part CT par élève premier degré 2025p (calcul), €', pe1 * ct1 / 100, 'calcul dérivé'),
        ('Part CT par élève second degré 2025p (calcul), €', pe2 * ct2 / 100, 'calcul dérivé'),
        ('Part CT dans la DIE totale, financement initial 2025p, %', f2['C6'].value, 'NI 26.42 xlsx, Figure 2, C6'),
        ('dont communes, %', f2['C7'].value, 'NI 26.42 xlsx, Figure 2, C7'),
        ('dont départements, %', f2['C8'].value, 'NI 26.42 xlsx, Figure 2, C8'),
        ('dont régions, %', f2['C9'].value, 'NI 26.42 xlsx, Figure 2, C9'),
    ]
    f3b = wb['Figure 3bis']
    rows += [('Financement initial CT, DIE totale 2025p, M€ courants', f3b['F6'].value, 'NI 26.42 xlsx, Figure 3bis, F6'),
             ('Financement initial CT, DIE totale 2024 (définitif), M€ courants', f3b['E6'].value, 'NI 26.42 xlsx, Figure 3bis, E6')]
    tot = f3b['F6'].value
    for lab, cell in [('communes', 'C7'), ('départements', 'C8'), ('régions', 'C9')]:
        rows.append((f'Financement initial {lab} 2025p (calcul = part de la DIE x DIE), M€', f2[cell].value / 100 * f3b['F10'].value, 'calcul dérivé (Figure 2 x Figure 3bis F10)'))
    w2 = openpyxl.load_workbook(raw('DEPP_RERS2026_10-02_financement_DIE_donnees.xlsx'), data_only=True)['10.02 Tableau 4']
    for r, lab in [(8, 'Enseignement premier degré'), (9, 'Enseignement second degré'), (10, 'Enseignement supérieur'), (11, 'Enseignement extrascolaire'),
                   (13, 'Hébergement, restauration (tous niveaux)'), (14, 'Médecine scolaire'), (15, 'Orientation'), (16, 'Administration générale'),
                   (17, 'Transports scolaires'), (18, 'Fournitures et livres scolaires'), (20, 'Ensemble DIE')]:
        rows.append((f'CT, financement final 2024p, {lab}, M€', w2[f'F{r}'].value, f'RERS 2026 xlsx 10.02, onglet « 10.02 Tableau 4 », F{r}'))
    w4 = openpyxl.load_workbook(raw('DEPP_RERS2026_10-04_producteurs_education_donnees.xlsx'), data_only=True)['10.04 Tableau 2']
    for r, lab in [(9, 'Écoles maternelles et élémentaires publiques'), (10, 'Collèges et lycées publics'), (19, 'Écoles privées sous contrat'),
                   (20, 'Collèges et lycées privés sous contrat'), (15, "Centres d'enseignement spécial"), (14, 'Centres de formation artistique'), (31, 'Total producteurs')]:
        rows.append((f'CT, financement final 2024p des producteurs, {lab}, M€', w4[f'E{r}'].value, f'RERS 2026 xlsx 10.04, onglet « 10.04 Tableau 2 », E{r}'))
    out = pd.DataFrame(rows, columns=['indicateur', 'valeur', 'emplacement'])
    out.to_csv(os.path.join(OUT, 'DEPP_collectivites_parts_montants_par_niveau.csv'), sep=';', index=False, encoding='utf-8-sig')
    return out


def extract_recettes(df):
    """Recettes réelles rattachées à la fonction 2 « scolaire » (sous-fonctions 2, 20, 21x, 22x, 24, 28x, 29), budgets principaux :
    classe 7 (fonctionnement) et comptes 13 (subventions d'investissement reçues). Montant = crédit réel - débit réel."""
    lab = pd.read_csv(raw('OFGL_nomenclature_M57_2025_libelles_comptes.csv'), sep=';', dtype=str, encoding='utf-8-sig')
    lab = lab.drop_duplicates('numero_compte').set_index('numero_compte').libelle_compte
    r = df[(df.cbudg == '1') & (df.compte.str[:1].isin(['7']) | df.compte.str[:2].isin(['13']))].copy()
    r = r[r.f.str[:2].isin(['20', '21', '22', '24', '28', '29']) | (r.f == '2')]
    r['section'] = np.where(r.compte.str[:1] == '7', 'recettes de fonctionnement (classe 7)', "subventions d'investissement reçues (13)")
    r['recette'] = r.cre - r.deb
    g = r.groupby(['niveau', 'section', 'compte']).recette.sum().div(1e6).round(2).reset_index()
    g['libelle_M57'] = g.compte.map(lambda c: lab.get(c, ''))
    g = g.sort_values(['niveau', 'section', 'recette'], ascending=[True, True, False]).rename(columns={'recette': 'montant_M€'})
    g.to_csv(os.path.join(OUT, 'DGFiP_2025_enseignement_recettes_par_niveau_BP.csv'), sep=';', index=False, encoding='utf-8-sig')
    return g


if __name__ == '__main__':
    a = extract_dgcl_4f()
    df = load_dgfip()
    d, b1, b2, b3 = extract_dgfip(df)
    rr = extract_recettes(df)
    c = extract_couverture()
    dd = extract_depp()
    pd.set_option('display.width', 250)
    print(b3.to_string())
    print(c.to_string())
    print(dd.to_string())
