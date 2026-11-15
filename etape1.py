# Étape 1 : tournoi avec les 5 stratégies du cours (format Axelrod)
# (5 parties de 200 tours par paire, graine 42).
# Lancer : py etape1.py

from moteur import tournoi, afficher_classement
from strategies import STRATEGIES_COURS

# tournoi principal : chaque stratégie joue aussi contre elle-même (comme Axelrod)
print("=== Étape 1 : avec parties contre soi-même ===")
totaux = tournoi(STRATEGIES_COURS)
afficher_classement(totaux)

# on relance sans les parties contre soi-même
# pour voir si ce choix change le classement
print()
print("=== Étape 1 : sans parties contre soi-même ===")
totaux2 = tournoi(STRATEGIES_COURS, contre_soi=False)
afficher_classement(totaux2)