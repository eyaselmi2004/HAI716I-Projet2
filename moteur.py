import random

#matrice: GAINS [(mon coup, coup de l'adversaire)]=(mes points, ses points)
GAINS={
    ('C', 'C'): (3, 3), #les 2 cooperent
    ('C', 'D'): (0, 5), #je coopere il trahit
    ('D', 'C'): (5, 0), #je trahis, il coopere
    ('D', 'D'): (2, 2), #les 2 trahissent
}

#une strategie(strat) =une fonction qui prend (mes_coups, coups_adv) et qui renvoie 'C' ou 'D'
def partie(strat1, strat2, n_tours=200):
    coups1 = [] #liste des coups joues par le joueur 1 (son historique)
    coups2 = [] #celle de joueur 2
    score1 = 0
    score2 = 0
    for t in range(n_tours):
        c1 = strat1(coups1, coups2)
        c2 = strat2(coups2, coups1)
        # on regarde dans la matrice combien chacun gagne
        g1, g2= GAINS[(c1,c2)]
        score1 += g1
        score2 += g2

        #on ajoute les coups à l'historique pour les strategies ls voient au tour suivant
        coups1.append(c1)
        coups2.append(c2)

    return score1, score2


#le tournoi 
# graine :pour que le hasard soit toujours le meme (resultats reproductibles)
# contre_soi :true si chaque strategie joue aussi contre une copie d'elle-meme
def tournoi(strategies, n_parties=5, n_tours=200, graine=42, contre_soi=True ):
    random.seed(graine)
    noms = list(strategies.keys())

    #score total de chaque strategie (commence à 0)
    totaux= {}
    for nom in noms:
        totaux[nom] = 0

    duels = {} #duels[a][b] = score moyen de a contre b sur une partie de 200 tours (c'est ce qui permet de voir qui gagne contre qui)
    for nom in noms:
        duels[nom] = {}
    #double boucle pour faire toutes les paires(j commence à i :comme ça A contre B n'est joué qu'une fois)
    for i in range(len(noms)):
        for j in range(i, len(noms)):
            a = noms[i]
            b = noms[j]

            # si on veut pas les parties contre soi meme on saute
            if a == b and not contre_soi:
                continue


            somme_a = 0  #total de a sur les 5 parties contre b
            somme_b = 0  #total de b sur les 5 parties contre a
            
                        # 5 parties de 200 tours pour chaque paire
            for p in range(n_parties):
                s1, s2 = partie(strategies[a], strategies[b], n_tours)
                somme_a += s1   # on cumule les points de a contre b sur les 5 parties
                somme_b += s2   # pareil pour b contre a
                if a == b:
                    # contre soi-meme :c'est la meme stratégie des 2 côtés
                    # donc on ne compte qu'un seul des deux scores
                    totaux[a] += s1
                else:
                    totaux[a] += s1
                    totaux[b] += s2
            
            #on divise par le nombre de parties -> score moyen d'une partie
            duels[a][b] = somme_a / n_parties
            duels[b][a] = somme_b / n_parties

    return totaux, duels

#afficher le classement
# on trie les strategies du plus grand score au plus petit
# totaux.items() donne des couples (nom, score),
# key=lambda x: x[1] -> on trie selon le score (2e element du couple)
def afficher_classement(totaux):
    classement = sorted(totaux.items(), key=lambda x: x[1], reverse=True)
    rang = 1
    for nom, score in classement:
        print(rang, nom, score)
        rang += 1

#affiche le tableau des duels 
# ligne = la stratégie qui joue, colonne = son adversaire
def afficher_duels(duels):
    noms = list(duels.keys())
    # ligne d'en-tête avec le nom des adversaires (coupé à 8 lettres pour l'alignement)
    print(" " * 12, end="")
    for b in noms:
        print(f"{b[:8]:>9}", end="")
    print()
    # une ligne par stratégie
    for a in noms:
        print(f"{a:<12}", end="")
        for b in noms:
            if b in duels[a]:
                print(f"{duels[a][b]:>9.0f}", end="")   # .0f = sans virgule
            else:
                print(f"{'-':>9}", end="")   # pas de duel (ex : contre soi-même désactivé)
        print()
