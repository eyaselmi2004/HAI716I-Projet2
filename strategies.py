# strategies.py
# chaque strategie est une fonction qui reçoit :
#   mes_coups : la liste de mes coups passés
#   coups_adv : la liste des coups passés de l'ADVERSAIRE
# et qui renvoie 'C' ou 'D'

import random   # pour RANDOM et JOSS (la graine est fixée dans tournoi())


# ALL-D : trahit toujours, quoi qu'il arrive
def all_d(mes_coups, coups_adv):
    return 'D'


# TIT-FOR-TAT : coopère au 1er tour, puis copie le dernier coup de l'adversaire
def tit_for_tat(mes_coups, coups_adv):
    if len(coups_adv) == 0:     # 1er tour : l'adversaire n'a encore rien joué
        return 'C'
    return coups_adv[-1]        # [-1] = le dernier élément de la liste


# (je l'appelle random_strat et pas random, sinon ça écrase le module random)
def random_strat(mes_coups, coups_adv):
    # random.random() donne un nombre entre 0 et 1
    # -> il est < 0.5 dans 50 % des cas
    if random.random() < 0.5:
        return 'C'
    return 'D'


# TESTER : trahit au 1er tour pour "tester" l'adversaire
#   - si l'adversaire riposte (il a joué D au moins une fois) -> joue TIT-FOR-TAT
#   - sinon il répète le motif C, C, D
# mon interprétation : "riposter" = l'adversaire a joué D au moins une fois
def tester(mes_coups, coups_adv):
    t = len(mes_coups)              # numéro du tour (0 = 1er tour)
    if t == 0:
        return 'D'                  # 1er tour : on teste en trahissant
    if 'D' in coups_adv:            # l'adversaire a riposté au moins une fois
        return coups_adv[-1]        # -> on fait comme TIT-FOR-TAT
    # sinon motif C, C, D :
    # tours 1, 2 -> C ; tour 3 -> D ; tours 4, 5 -> C ; tour 6 -> D ...
    if t % 3 == 0:                  # % = reste de la division, vrai pour t = 3, 6, 9...
        return 'D'
    return 'C'


# JOSS : comme TIT-FOR-TAT, mais remplace C par D une fois sur dix
def joss(mes_coups, coups_adv):
    if len(coups_adv) == 0:
        coup = 'C'                  # 1er tour : coopère (comme TFT)
    else:
        coup = coups_adv[-1]        # sinon copie le dernier coup adverse (comme TFT)
    # si on allait coopérer, on trahit quand même 1 fois sur 10
    if coup == 'C' and random.random() < 0.1:
        return 'D'
    return coup


# dictionnaire des 5 stratégies du cours : nom -> fonction
# (c'est ce qu'on donne à tournoi() dans etape1.py)
STRATEGIES_COURS = {
    'ALL-D': all_d,
    'RANDOM': random_strat,
    'TIT-FOR-TAT': tit_for_tat,
    'TESTER': tester,
    'JOSS': joss,
}