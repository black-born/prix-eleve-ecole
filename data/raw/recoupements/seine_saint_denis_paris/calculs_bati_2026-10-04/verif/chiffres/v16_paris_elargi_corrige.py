# Paris "au plus" (investissement ecoles + postes scolaires hors fonctions "ecoles"), avec l'ecole de la ZAC
# Saint-Vincent-de-Paul payee en 2024 en "participations aux operations d'urbanisme" (CA 2024, rapport financier, p. 29 :
# "une ecole (6,0 MEUR)"), de meme nature que l'acompte de 4,2 MEUR de 2025 retenu par la recherche A (CA 2025, p. 33).
import sys
sys.stdout.reconfigure(encoding='utf-8')
fonctions = {2023: 72.91654368, 2024: 62.41590083, 2025: 63.17236121}      # DGFiP, A15
hors_A = {2023: 15.4, 2024: 29.0, 2025: 36.5}                              # A14
ajout = {2023: 0.0, 2024: 6.0, 2025: 0.0}                                  # CA 2024 p. 29
eleves = {2023: 108538, 2024: 105848, 2025: 103593}                        # rentree N-1
ssd = 1223.3008686614546
totA = sum(fonctions[y] + hors_A[y] for y in eleves); totC = sum(fonctions[y] + hors_A[y] + ajout[y] for y in eleves); E = sum(eleves.values())
for y in eleves:
    print(y, 'hors fonctions A', hors_A[y], '-> corrige', hors_A[y] + ajout[y], '; elargi EUR/eleve A', round((fonctions[y]+hors_A[y])*1e6/eleves[y]), '-> corrige', round((fonctions[y]+hors_A[y]+ajout[y])*1e6/eleves[y]))
print('Moyenne 2023-2025 : A', round(totA*1e6/E, 1), '-> corrige', round(totC*1e6/E, 1))
print('93 / Paris elargi : A', round(ssd/(totA*1e6/E), 3), '-> corrige', round(ssd/(totC*1e6/E), 3))
