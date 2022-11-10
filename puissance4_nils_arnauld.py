import random
import os


#  Écrire une fonction grille_vide() qui renvoie une grille vide.
# Indications : Qu’obtient-on avec L = [0]*7 ?
# Comment obtenir une liste de 6 lignes de 7 zéros ?
# Indice : on peut utiliser une liste en compréhension pour définir un tableau de
# 6 lignes et 7 colonnes rempli de 0.

def grille_vide():
    L = [0]*7
    grille = [L]*6
    return grille

# Écrire une fonction affiche() qui affiche une grille, avec le caractère . pour une case vide, le caractère X pour le joueur 1 et le caractère O pour le joueur
# On prendra soin d’afficher les lignes de haut en bas, c’est-à-dire que la ligne d’indice 5 sera la première à être affichée et celle d’indice 0 la dernière.
# Indications : la fonction affiche prend en argument une grille g. Il faut parcourir toutes les cases du tableau g : si une case contient un 1, on affichera le caractère ‘X’, si elle contient un 2, on affichera le caractère ‘O’ et si elle contient un 0, on affichera un point ‘.’ . Vous devrez utiliser deux boucles imbriquées, pour parcourir les lignes et les colonnes.

def affiche(grille, pseudo1, pseudo2): # Axe d'amélioration: Liste en compréhension pour chaque ligne avec join
    os.system("cls||clear")
    print("================ PUISSANCE 4 ================")
    print("Joueur 1: " + pseudo1 + " | Joueur 2: " + pseudo2)

    grille_inversee = grille[::-1]
    for ligne in grille_inversee:
        list = ""
        for case in ligne:
            if case == 0:
                list += "."
            elif case == 1:
                list += "X"
            elif case == 2:
                list += "O"
        print(list)


        

# Écrire une fonction coup_possible(g, c) qui renvoie un booléen indiquant s’il est possible de jouer dans la colonne c. Il est possible de jouer dans la colonne c si elle n’est pas déjà pleine, c’est-à-dire si la case la plus haute de la colonne c contient un zéro.

def coup_possible(g, c):
    # G est la grille
    # C est la colonne
    try:
        return g[len(g)-1][c] == 0
    except IndexError:
        return False
    

# Ecrire une fonction jouer(g, j, c) qui joue un coup du joueur j dans la colonne c en supposant que la colonne c n’est pas pleine.
# Indication : la première case vide de la colonne c, en partant du bas (c’est-à-dire de plus petit indice) prendra la valeur j (1 ou 2 donc).

def jouer(g, j, c):
    # G est la grille
    # J est le joueur 1 ou 2
    # C est la colonne
    # Assigner la valeur J à la première case vide de la colonne 
    for ligne in g:
        if ligne[c] == 0:
            ligne[c] = j
            print("ça joue")
            break


    
    
# Écrire 4 fonctions horiz(g, j, l, c), vert(g, j, l, c), diag1(g, j, l, c) et diag2(g, j, l, c) qui déterminent respectivement s’il y a un alignement de 4 pions du joueur j commençant à la case (l,c). Les 4 fonctions renvoient un booléen (qui vaut True en cas d’alignement, False sinon).
# Précisément, les 3 pions permettant de réaliser un alignement avec le pion de la case (l,c) dans les fonctions horiz(g, j, l, c), vert(g, j, l, c) et diag1(g, j, l, c) sont situés dans les cases à droite ou au-dessus de (l,c). Dans la fonction diag2(g, j, l,c) , ils sont situés au-dessus à gauche.

def horiz(g, j, l, c):
    # G est la grille
    # J est le joueur 1 ou 2
    # L est la ligne
    # C est la colonne
    # Vérifier si il y a un alignement horizontal de 4 pions du joueur J commençant à la case (L,C)
    if(c+3 < len(g[0])):
        if(g[l][c] == j and g[l][c+1] == j and g[l][c+2] == j and g[l][c+3] == j):
            return True
    return False

def vert(g, j, l, c):
    # G est la grille
    # J est le joueur 1 ou 2
    # L est la ligne
    # C est la colonne
    # Vérifier si il y a un alignement vertical de 4 pions du joueur J commençant à la case (L,C)
    if(l+3 < len(g)):
        if(g[l][c] == j and g[l+1][c] == j and g[l+2][c] == j and g[l+3][c] == j):
            return True
    return False


def diag1(g, j, l, c):
    # G est la grille
    # J est le joueur 1 ou 2
    # L est la ligne
    # C est la colonne
    # Vérifier si il y a un alignement diagonal de 4 pions du joueur J commençant à la case (L,C)
    if(l+3 < len(g) and c+3 < len(g[0])):
        if(g[l][c] == j and g[l+1][c+1] == j and g[l+2][c+2] == j and g[l+3][c+3] == j):
            return True
    return False


def diag2(g, j, l, c):
    # G est la grille
    # J est le joueur 1 ou 2
    # L est la ligne
    # C est la colonne
    # Vérifier si il y a un alignement diagonal de 4 pions du joueur J commençant à la case (L,C)
    if(l-3 >= 0 and c+3 < len(g[0])):
        if(g[l][c] == j and g[l-1][c+1] == j and g[l-2][c+2] == j and g[l-3][c+3] == j):
            return True
    return False


# Écrire une fonction victoire(g,j) qui renvoie un booléen indiquant si le joueur j a gagné.

def victoire(g, j):
    # G est la grille
    # J est le joueur 1 ou 2
    # Vérifier si le joueur J a gagné
    for ligne in range(len(g)):
        for colonne in range(len(g[0])):
            if(horiz(g, j, ligne, colonne) or vert(g, j, ligne, colonne) or diag1(g, j, ligne, colonne) or diag2(g, j, ligne, colonne)):
                return True
    return False



# Écrire une fonction match_nul(g) qui renvoie un booléen indiquant s’il y a match nul, c’est-à-dire si la grille est totalement remplie. Indication : on pourra se contenter d’examiner la ligne du haut.

def match_nul(g):
    # G est la grille
    # Vérifier si la grille est totalement remplie
    for colonne in range(len(g[0])):
        if(g[0][colonne] == 0):
            return False
    return True



# Écrire une fonction coup_aleatoire(g,j) qui joue un coup aléatoire pour le joueur j, en supposant que la grille n’est pas pleine.

def coup_aleatoire(g, j):
    # G est la grille
    # J est le joueur 1 ou 2
    # Jouer un coup aléatoire pour le joueur J
    colonne = random.randint(0, len(g[0])-1)
    while(not coup_possible(g, colonne)):
        colonne = random.randint(0, len(g[0])-1)
    jouer(g, j, colonne)




# Écrire une fonction puissance4_2joueurs() qui utilise toutes les fonctions ci-dessus pour faire jouer deux adversaires aléatoirement et à tour de rôle, en affichant la grille après chaque coup, et qui s’arrête dès qu’un joueur gagne ou que la partie est nulle.

def puissance4_2joueurs():
    # Jouer une partie de puissance 4 à 2 joueurs
    pseudo1 = input("Entrez le pseudo du joueur 1 : ")
    os.system("cls||clear")
    pseudo2 = input("Entrez le pseudo du joueur 2 : ")

    g = grille_vide()
    affiche(g, pseudo1, pseudo2)

    while(not victoire(g, 1) and not victoire(g, 2) and not match_nul(g)): # Tant que personne n'a gagné et que la grille n'est pas pleine
        coup_aleatoire(g, 1)
        affiche(g, pseudo1, pseudo2)
        if(not victoire(g, 1) and not victoire(g, 2) and not match_nul(g)):
            coup_aleatoire(g, 2)
            affiche(g, pseudo1, pseudo2)
    if(victoire(g, 1)):
        print("Le joueur 1 a gagné !")
    elif(victoire(g, 2)):
        print("Le joueur 2 a gagné !")
    else:
        print("Match nul !")




# Écrire enfin une fonction puissance4_1joueur() qui permet à l’utilisateur de jouer contre l’ordinateur qui joue aléatoirement, en affichant la grille après chaque coup et le résultat en fin de partie.

def puissance4_1joueur():
    # Jouer une partie de puissance 4 à 1 joueur
    pseudo1 = input("Entrez votre pseudonyme: ")
    pseudo2 = "Ordinateur"

    g = grille_vide()
    affiche(g, pseudo1, pseudo2)


    while(not victoire(g, 1) and not victoire(g, 2) and not match_nul(g)):
        colonne = demander_colonne(g)
        while(not coup_possible(g, colonne)):
            colonne = demander_colonne(g)
        jouer(g, 1, colonne)
        affiche(g, pseudo1, pseudo2)

        if(not victoire(g, 1) and not victoire(g, 2) and not match_nul(g)): # Si ce coup n'a pas permi au joueur de gagner, faire jouer l'ordinateur
            # coup_aleatoire(g, 2)
            coup_ordinateur(g, 2)
            affiche(g, pseudo1, pseudo2)

    if(victoire(g, 1)):
        won(g, 1, pseudo1, pseudo2)
    elif(victoire(g, 2)):
        print("L'ordinateur a gagné !")
    else:
        print("Match nul !")


def demander_colonne(g):
    try: 
        colonne = int(input("Entrez le numéro de la colonne où vous voulez jouer : "))
        while(not coup_possible(g, colonne)):
            print("Veuillez entrer le numéro d'une colonne affichée et non pleine")
            colonne = demander_colonne(g)
        return colonne-1
    except ValueError:
        print("Vous devez entrer un nombre !")
        return demander_colonne(g)
    

# Pour aller plus loin, écrire une stratégie de jeu pour l’ordinateur et l’implémenter.


def won(grille, joueur, pseudo1, pseudo2):
    os.system("cls||clear")
    if(joueur == 1):
        print("Vous avez gagné !")
    else:
        print("L'ordinateur a gagné !")

def coup_ordinateur(g, j):
    # G est la grille
    # J est le joueur 1 ou 2
    # Jouer un coup pour l'ordinateur
    colonne = random.randint(0, len(g[0])-1)
    while(not coup_possible(g, colonne)):
        colonne = random.randint(0, len(g[0])-1)
    jouer(g, j, colonne)

# Faire une fonction jouer qui demande à l'utilisateur combien ils sont, et leurs pseudonymes, puis lance la partie correspondante.

def play():
    try:
        nb_joueurs = int(input("Combien de joueurs ? "))
        if(nb_joueurs == 1):
            puissance4_1joueur()
        elif(nb_joueurs == 2):
            puissance4_2joueurs()
        else:
            os.system("cls||clear")
            print("Je n'ai pas de version disponible pour ce nombre de joueurs, veuillez entrer 1 ou 2.")
            return play()
    except ValueError:
        os.system("cls||clear")
        print("Veuillez entrer un nombre.")
        return play()

def launch():
    os.system("cls||clear")
    play()

launch()