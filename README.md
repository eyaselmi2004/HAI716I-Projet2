# HAI716I-Projet2
# Projet 2, partie 1 : tournoi du dilemme du prisonnier itéré

Projet réalisé en Python (testé avec Python 3.11). Aucune bibliothèque externe n'est nécessaire.

## Fichiers

| Fichier | Rôle |
|---|---|
| `moteur.py` | matrices de gains, une partie, le tournoi tous contre tous, l'affichage |
| `strategies.py` | les 5 stratégies du cours + GRIM et TFT-GÉNÉREUX |
| `test.py` | vérifie le moteur avec l'exemple du cours (TFT contre ALL-D sur 10 tours = 18 contre 23) |
| `etape1.py` | tournoi de l'étape 1 (5 stratégies du cours) |
| `etape2.py` | tournoi de l'étape 2 (+ GRIM et TFT-GÉNÉREUX) |
| `etape3.py` | étape 3 : bruit de 5 % et chasse au cerf |
| `journal.md` | journal de bord (avec les captures) |
| `captures/` | captures d'écran des résultats |

## Relancer chaque tournoi

Depuis le dossier du projet :

    python test.py      # vérification du moteur : doit afficher (18, 23)
    python etape1.py    # étape 1
    python etape2.py    # étape 2
    python etape3.py    # étape 3 (bruit puis chasse au cerf)

Sous Windows, on peut remplacer `python` par `py`.

La graine aléatoire est fixée à 42 : chaque commande redonne exactement les résultats du journal.