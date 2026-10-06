# Ecart Region Paris / 93 (dotation consolidee 2026 + operations directes 2021-2023) selon le denominateur
import sys, pandas as pd
sys.stdout.reconfigure(encoding='utf-8')
R = r"C:/Users/chret/AppData/Local/Temp/claude/c--Users-chret-Documents-EtatEcole/5b29c961-d5a9-4d19-af60-f12e126ef8ef/scratchpad/analyse_bati/C_lycees/resultats/"
dot = pd.read_csv(R+'dotation_consolidee_par_departement.csv', sep=';', dtype={'dep':str}, encoding='utf-8-sig').set_index('dep')
op = pd.read_csv(R+'affectations_2021_2023_par_departement.csv', sep=';', dtype={'dep':str}, encoding='utf-8-sig').set_index('dep')
for dep in ['75','93']:
    d = dot.loc[dep]; o = op.loc[dep]
    acc = d.EUR_par_eleve_accueilli + o.EUR_par_eleve_par_an_operations_directes
    pp = d.EUR_par_lyceen_postbac_inclus + o.EUR_par_lyceen_postbac_inclus_par_an_operations_directes
    pre = d.EUR_par_lyceen_prebac + o.EUR_par_lyceen_prebac_par_an_operations_directes
    print(dep, 'par eleve accueilli', round(acc), '| par lyceen pre+post (numerateur avec CMR)', round(pp), '| par lyceen pre-bac', round(pre), '| part de la dotation 2026 allant aux cites mixtes regionales', round(100*d.part_CMR_dans_dot2026,1), '%')
p, s = dot.loc['75'], dot.loc['93']
print('Ecart 93 - Paris : par eleve accueilli', round((s.EUR_par_eleve_accueilli + op.loc['93'].EUR_par_eleve_par_an_operations_directes) - (p.EUR_par_eleve_accueilli + op.loc['75'].EUR_par_eleve_par_an_operations_directes)))
print('Ecart 93 - Paris : par lyceen pre+post', round((s.EUR_par_lyceen_postbac_inclus + op.loc['93'].EUR_par_lyceen_postbac_inclus_par_an_operations_directes) - (p.EUR_par_lyceen_postbac_inclus + op.loc['75'].EUR_par_lyceen_postbac_inclus_par_an_operations_directes)))
print('Ecart 93 - Paris : par lyceen pre-bac', round((s.EUR_par_lyceen_prebac + op.loc['93'].EUR_par_lyceen_prebac_par_an_operations_directes) - (p.EUR_par_lyceen_prebac + op.loc['75'].EUR_par_lyceen_prebac_par_an_operations_directes)))
