# Part de variance de la depense par eleve expliquee par chaque ligne (cov(ligne,total)/var(total), ponderee par eleves)
import sys, pandas as pd, numpy as np
sys.stdout.reconfigure(encoding='utf-8')
B1 = r"C:/Users/chret/Documents/EtatEcole/resultats/B1_depense_publique_par_etablissement_2025.csv"
df = pd.read_csv(B1, sep=';', encoding='utf-8-sig', dtype=str)
num = [c for c in df.columns if c not in ('uai','nom','degre','type','secteur','academie','code_departement','departement','commune','code_commune_norm','cle_commune','cle_departement','cle_region','ips')]
for c in num: df[c] = pd.to_numeric(df[c])
pub = df[df.secteur=='public']
lines = ['etat_enseignants','etat_remplacement_formation','etat_vie_scolaire','etat_pilotage_admin','etat_inclusion_sante_social','etat_activites_educatives','etat_aides_familles','etat_forfait_prive_internats','etat_soutien_administration','ct_ecoles','ct_colleges','ct_lycees','ct_transports']
def wcov(x, y, w):
    mx = np.average(x, weights=w); my = np.average(y, weights=w)
    return np.average((x-mx)*(y-my), weights=w)
for g, types in [('colleges',['collège']),('lycees',['lycée général et technologique','lycée polyvalent','lycée professionnel'])]:
    for d in ['93','75']:
        s = pub[pub.type.isin(types) & (pub.code_departement==d)].copy()
        w = s.eleves.values
        tot = (s.depense_publique/s.eleves).values
        vt = wcov(tot, tot, w)
        out = {}
        for c in lines + ['apu']:
            if c == 'apu':
                x = s.apu_par_eleve.values
            else:
                x = (s[c]/s.eleves).values
            out[c] = 100*wcov(x, tot, w)/vt
        print(g, d, {k: round(v,1) for k,v in out.items() if abs(v) > 0.05}, 'somme', round(sum(out.values()),1))
# cles uniformes
s = pub[pub.type=='collège']
for d in ['75','93']:
    x = s[s.code_departement==d]
    k = x.ct_colleges/x.eleves
    print('cle dep colleges', d, k.min(), k.max())
