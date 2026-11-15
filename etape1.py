# etape1.py
# Étape 1 : tournoi avec les 5 stratégies du cours, format Axelrod
# Lancer : py etape1.py

from moteur import tournoi, afficher_classement, afficher_duels
from strategies import STRATEGIES_COURS

# tournoi principal : chaque stratégie joue aussi contre elle-même (comme Axelrod)
print("=== Étape 1 : avec parties contre soi-même ===")
totaux, duels = tournoi(STRATEGIES_COURS)   # tournoi renvoie les totaux ET les duels
afficher_classement(totaux)

# tableau des duels : pour comprendre POURQUOI le classement est comme ça
print()
print("Score moyen par partie (ligne contre colonne) :")
afficher_duels(duels)

# on relance sans les parties contre soi-même
print()
print("=== Étape 1 : sans parties contre soi-même ===")
totaux2, duels2 = tournoi(STRATEGIES_COURS, contre_soi=False)
afficher_classement(totaux2)