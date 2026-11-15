# Journal de bord – HAI716I Projet 2, partie 1

Projet réalisé seule. Langage : Python.

## 1. Protocole

- **Matrice de gains** (celle du cours) :

  |             | adversaire C | adversaire D |
  |-------------|--------------|--------------|
  | **moi C**   | 3, 3         | 0, 5         |
  | **moi D**   | 5, 0         | 2, 2         |

- **Format du tournoi** : chaque paire de stratégies joue 5 parties de 200 tours (format d'Axelrod, imposé par l'énoncé). Le score d'une stratégie est la somme de tous ses points sur le tournoi.
- **Parties contre soi-même** : oui, chaque stratégie joue aussi contre une copie d'elle-même (on ne compte qu'un des deux scores). Axelrod le faisait dans son tournoi. Je relance aussi le tournoi sans ces parties pour voir si ce choix change le classement.
- **Graine aléatoire** : `random.seed(42)` au début de chaque tournoi, pour que RANDOM et JOSS fassent toujours les mêmes tirages et que les résultats soient reproductibles. 42 est un choix arbitraire, n'importe quel nombre fixe marche.
- **Représentation d'une stratégie** : une fonction `strategie(mes_coups, coups_adv)` qui reçoit les deux historiques et renvoie `'C'` ou `'D'`. Dans le moteur, les deux coups sont demandés avant d'être ajoutés aux historiques : aucune stratégie ne voit le coup de l'autre au même tour (coups simultanés).

### Vérification du moteur

Avant de lancer le tournoi, j'ai vérifié le moteur avec l'exemple du cours (diapositive 67) : sur 10 tours, TIT-FOR-TAT contre ALL-D doit donner 18 contre 23.
Commande : `py test.py`, résultat obtenu : `(18, 23)`. Le moteur calcule bien les points.

## 2. Les stratégies du cours

**ALL-D**
- *Règle* : trahit à chaque tour.
- *Origine* : c'est la stratégie « rationnelle » quand le nombre de tours est connu (raisonnement par récurrence à rebours, vu en cours).
- *Devrait bien jouer contre* : les stratégies qui ne ripostent pas, comme RANDOM, qui coopère une fois sur deux.
- *Devrait mal jouer contre* : les stratégies qui ripostent (TIT-FOR-TAT, JOSS), car après le 1er tour elles trahissent aussi et ALL-D ne gagne plus que 2 par tour.

**RANDOM**
- *Règle* : joue C ou D au hasard, avec une chance sur deux.
- *Origine* : stratégie témoin du tournoi d'Axelrod.
- *Devrait bien jouer contre* : personne en particulier.
- *Devrait mal jouer contre* : ALL-D, qui l'exploite chaque fois qu'elle coopère. Elle sert de référence : une bonne stratégie doit faire mieux qu'elle.

**TIT-FOR-TAT**
- *Règle* : coopère au 1er tour, puis copie le dernier coup de l'adversaire.
- *Origine* : Anatol Rapoport, gagnante du tournoi d'Axelrod en 1980.
- *Devrait bien jouer contre* : les stratégies qui coopèrent (coopération totale, 600 points par partie).
- *Devrait mal jouer contre* : JOSS, dont les trahisons surprises déclenchent des représailles en écho. D'après le cours, elle ne gagne jamais un duel : elle ne peut gagner qu'en accumulant des points sur tout le tournoi.

**TESTER**
- *Règle* : trahit au 1er tour. Si l'adversaire riposte, elle joue TIT-FOR-TAT ; sinon elle répète le motif C, C, D.
- *Origine* : stratégie soumise au tournoi d'Axelrod.
- *Mon interprétation* : « riposter » veut dire que l'adversaire a joué D au moins une fois. Dès que c'est le cas, TESTER joue TIT-FOR-TAT jusqu'à la fin.
- *Devrait bien jouer contre* : les stratégies qui ne ripostent jamais, qu'elle exploite avec son motif.
- *Devrait mal jouer contre* : les stratégies qui ripostent, car sa trahison du 1er tour lance des représailles.

**JOSS**
- *Règle* : comme TIT-FOR-TAT, mais remplace un C par un D une fois sur dix.
- *Origine* : stratégie soumise au tournoi d'Axelrod.
- *Devrait bien jouer contre* : les stratégies qui coopèrent sans riposter.
- *Devrait mal jouer contre* : TIT-FOR-TAT et elle-même, car chaque trahison surprise déclenche des représailles.

## 3. Étape 1 : le tournoi de base

### Prédiction (écrite avant le lancement)

Je pense que TIT-FOR-TAT va gagner, comme dans le tournoi d'Axelrod : elle coopère avec ceux qui coopèrent et punit ceux qui trahissent, donc elle ne se fait jamais exploiter longtemps. TESTER pourrait être juste derrière, car elle exploite les stratégies qui ne ripostent pas, mais contre TIT-FOR-TAT et JOSS sa trahison du premier tour déclenche des représailles. Je pense que RANDOM sera dernière : elle joue au hasard, donc ALL-D l'exploite quand elle coopère et les stratégies qui ripostent la punissent quand elle trahit.

### Résultats

(à compléter après `py etape1.py`)

## Impasses

**Impasse 1 : erreur de syntaxe dans la matrice.** Au premier lancement, Python affichait `SyntaxError: invalid syntax` à la ligne 8 de `moteur.py`. J'avais séparé les éléments du dictionnaire `GAINS` par des `;` au lieu de `,`. Corrigé en mettant des virgules.

**Impasse 2 : la partie s'arrêtait après un tour.** Le test donnait `(0, 5)` au lieu de `(18, 23)` : c'est le score d'un seul tour (TFT coopère, ALL-D trahit). Le `return score1, score2` était indenté *dans* la boucle `for`, donc la fonction s'arrêtait dès la fin du 1er tour. Corrigé en mettant le `return` au même niveau que le `for`. Sans le test avec l'exemple du cours, je ne l'aurais pas vu tout de suite.