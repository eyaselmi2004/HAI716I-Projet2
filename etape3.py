# 2 modifications du tournoi avec les 7 stratégies de l'étape 2
#   1/ bruit : chaque coup est inversé avec une probabilité de 5 %
#   2/ autres gains : chasse au cerf (matrice du cours, section 07)
# Lancer : py etape3.py

from moteur import tournoi, afficher_classement, afficher_duels, CHASSE_AU_CERF
from strategies import STRATEGIES_ETAPE2

# --- modification 1 : bruit de 5 % ---
print("=== Étape 3 : bruit de 5 % ===")
totaux, duels = tournoi(STRATEGIES_ETAPE2, bruit=0.05)
afficher_classement(totaux)
print()
print("Score moyen par partie (ligne contre colonne) :")
afficher_duels(duels)

# --- modification 2 : chasse au cerf ---
print()
print("=== Étape 3 : chasse au cerf ===")
totaux2, duels2 = tournoi(STRATEGIES_ETAPE2, gains=CHASSE_AU_CERF)
afficher_classement(totaux2)
print()
print("Score moyen par partie (ligne contre colonne) :")
afficher_duels(duels2)