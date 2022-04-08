import random

################################################################################
#                        Fonctions                                             #
################################################################################

def initialiser():
    """
    retourne un tableau (liste de liste) python de
    6 lignes et 7 colonnes de 0.
    """
    return [[0 for col in range(7)] for line in range(6)]

def alignements():
    """
    Construit le dictionnaire dont les clés sont les cases
    (line, col) et les valeurs, une liste d'alignements auxquels
    participite la case
    """
    alignements = {}
    for line in range(6):
        for col in range(7):
            hor = [[(line, col-i+j) for j in range(4)] for i in range(4)]
            ver = [[(line-i+j, col) for j in range(4)] for i in range(4)]
            dd  = [[(line-i+j, col-i+j) for j in range(4)] for i in range(4)]
            dm  = [[(line+i-j, col-i+j) for j in range(4)] for i in range(4)]
            A = hor + ver + dd + dm
            align_faux = []
            for align in A:
                for l, c in align:
                    if not(0 <= l <= 5 and 0 <= c <= 6):
                        align_faux.append(align)
                        break
            for elem in align_faux:
                A.remove(elem)
            alignements[(line, col)] = A
    return alignements

def grille_pleine(tab):
    for line in range(6):
        for col in range(7):
            if tab[line][col] == 0:
                return False
    return True

def ordinateur_a_gagne(tab):
    """
    Retourne True ou False selon que l'ordinateur
    a gagné ou non
    """
    dic = alignements()
    # On parcourt toutes les cases du tableau
    for line in range(6):
        for col in range(7):
            aligns = dic[(line, col)] # on récupère les alignements
            for align in aligns:               # auxquels participe la case
                # pour chaque alignement on additionne toutes les cases
                som = 0
                for l,c in align:
                    som = som + tab[l][c]
                if som == -4:   # la seule valeur qui permet de dire que
                    return True # l'ordinateur a gagné
    return False

def joueur_a_gagne(tab):
    dic = alignements()
    # On parcourt toutes les cases du tableau
    for line in range(6):
        for col in range(7):
            aligns = dic[(line, col)] # on récupère les alignements
            for align in aligns:               # auxquels participe la case
                # pour chaque alignement on additionne toutes les cases
                som = 0
                for l,c in align:
                    som = som + tab[l][c]
                if som == 4:    # la seule valeur qui permet de dire que
                    return True # le joueur a gagné
    return False

def affiche(tab):
    def affiche_ligne(ligne):
        ch = ""
        for elem in ligne:
            if elem == 0:
                ch = ch + "| "
            elif elem == -1:
                ch = ch + "|X"
            else:
                ch = ch + "|O"
        ch = ch + "|"
        return ch
    print(" 1 2 3 4 5 6 7 ")
    for ligne in tab:
        print(affiche_ligne(ligne))


def ligne_jouee(tab, col):
    """
    Retourne la position de la ligne la plus basse que l'on
    peut jouer. On supposera que col est bien un entier compris
    entre 1 et 7.
    """
    line = 0
    while line <= 5 and tab[line][col-1] == 0: #décalage de la colonne
        line = line + 1
    return line - 1 # si la colonne est pleine on retourne -1

def joueur_joue(tab):
    """
    On suppose que c'est un joueur qui ne commet pas d'erreur
    dans le sens : choisir une colonne non pleine
    """
    col = eval(input("Choisissez une colonne"))
    if 1<= col <=7:
        line = ligne_jouee(tab, col)
        tab[line][col-1] = 1
    else:
        print("Veuillez choisir une colonne valide !")
        joueur_joue(tab)

def evaluer_jeu(tab):
    pass
    #donne un score d'évaluation de la grille sous la forme d'une matrice d'adjacence, fonction permettant à l'ordinateur de calculer les coups
    #en avance.

def ordinateur_joue(tab):
    ##jeu aléatoire
    line_sup = tab[0]
    # une colonne sera pleine si la valeur correspondante
    # à la colonne dans cette liste est différente de 0
    L = []
    for i in range(7):
        if line_sup[i] == 0: # On ajoute dans L l'indice des
                             # colonnes jouables (non pleines)
            L.append(i)

    ind = random.randint(0,len(L)-1)
    col = L[ind]
    line = ligne_jouee(tab, col+1)
    tab[line][col] = -1
    ##jeu réflechi:
    #   l'ordinateur devra utiliser la fonction evaluer_jeu(tab) pour pouvoir effectuer ses coups et agir de manière intelligente.


################################################################################
#                    Programme principal                                       #
################################################################################

TAB = initialiser()
while not(grille_pleine(TAB)) and not(joueur_a_gagne(TAB)):
    ordinateur_joue(TAB)
    affiche(TAB)
    if not(grille_pleine(TAB)) and not(ordinateur_a_gagne(TAB)):
        joueur_joue(TAB)
        affiche(TAB)
if joueur_a_gagne(TAB):
    print("Vous avez gagné")
elif ordinateur_a_gagne(TAB):
    print("Vous avez perdu")
else:
    print("Match nul")


