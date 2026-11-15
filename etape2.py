# Étape 2 : tournoi avec les 5 stratégies du cours + 2 nouvelles (GRIM, TFT-GENEREUX)
# Lancer : py etape2.py

from moteur import tournoi, afficher_classement, afficher_duels
from strategies import STRATEGIES_ETAPE2

print("=== Étape 2 : 7 stratégies (avec parties contre soi-même) ===")
totaux, duels = tournoi(STRATEGIES_ETAPE2)
afficher_classement(totaux)

print()
print("Score moyen par partie (ligne contre colonne) :")
afficher_duels(duels)

# comme à l'étape 1, on regarde aussi sans les parties contre soi-même
print()
print("=== Étape 2 : sans parties contre soi-même ===")
totaux2, duels2 = tournoi(STRATEGIES_ETAPE2, contre_soi=False)
afficher_classement(totaux2)