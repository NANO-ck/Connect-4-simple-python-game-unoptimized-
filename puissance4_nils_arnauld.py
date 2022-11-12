import random
import os
import time

score1 = 0
score2 = 0
dernier_coup = (0, 0)


#  Écrire une fonction grille_vide() qui renvoie une grille vide.
# Indications : Qu’obtient-on avec L = [0]*7 ?
# Comment obtenir une liste de 6 lignes de 7 zéros ?
# Indice : on peut utiliser une liste en compréhension pour définir un tableau de
# 6 lignes et 7 colonnes rempli de 0.
# Faire ce tableau avec une liste en compréhension

def grille_vide():
    return [[0 for i in range(7)] for j in range(6)]

# Écrire une fonction affiche() qui affiche une grille, avec le caractère . pour une case vide, le caractère X pour le joueur 1 et le caractère O pour le joueur
# On prendra soin d’afficher les lignes de haut en bas, c’est-à-dire que la ligne d’indice 5 sera la première à être affichée et celle d’indice 0 la dernière.
# Indications : la fonction affiche prend en argument une grille g. Il faut parcourir toutes les cases du tableau g : si une case contient un 1, on affichera le caractère ‘X’, si elle contient un 2, on affichera le caractère ‘O’ et si elle contient un 0, on affichera un point ‘.’ . Vous devrez utiliser deux boucles imbriquées, pour parcourir les lignes et les colonnes.

def affiche(grille, pseudo1, pseudo2, tour=0):
    global score1, score2
    # Affiche la grille inversée en mettant x pour le joueur 1, o pour le joueur 2 et . pour une case vide.
    os.system("cls||clear")
    print("\x1b[30;20m================\x1b[0m \033[1mPUISSANCE 4\x1b[0m\x1b[30;20m ================\x1b[0m")
    text = "\x1b[31mJoueur 1:\x1b[0m " + pseudo1
    print(text, end="")
    print(" "*(50-len(text))+str(score1))
    text = "\x1b[34mJoueur 2:\x1b[0m " + pseudo2
    print(text, end="")
    print(" "*(50-len(text))+str(score2))
    print("============================================")
    if(tour != 0):
        if(tour == 1):
            print("C'est au tour de \x1b[41m " + pseudo1 + " \x1b[0m\n")
        else:
            print("C'est au tour de \x1b[44m " + pseudo2 + " \x1b[0m\n")

    print("\x1b[33;20m "*7, end='')
    print(" ", end='')
    for colonne in range(len(grille[0])):
        print(" " + str(colonne+1) + "  ", end='')
    print("\x1b[0m")
    for ligne in range(len(grille)-1, -1, -1):
        print(" "*7, end='')
        print("|", end='')
        for colonne in range(len(grille[0])):
            if(grille[ligne][colonne] == 1):
                print("\x1b[41m X \x1b[0m|", end='')
            elif(grille[ligne][colonne] == 2):
                print("\x1b[44m O \x1b[0m|", end='')
            elif(grille[ligne][colonne] == 3):
                print("\x1b[42m + \x1b[0m|", end='')
            else:
                print(" . |", end='')
        print()
        # print("\n"+" "*7+"-----------------------------")
    print("============================================")


    # print(grille)
    # grille_inversee = grille[::-1]
    # print(grille_inversee)
    # for ligne in grille_inversee:
    #     list = ""
    #     for case in ligne:
    #         if case == 0:
    #             list += "."
    #         elif case == 1:
    #             list += "X"
    #         elif case == 2:
    #             list += "O"
    #     print(list)
    # print("  0 1 2 3 4 5 6")


        

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
    global dernier_coup
    # G est la grille
    # J est le joueur 1 ou 2
    # C est la colonne
    # Assigner la valeur J à la première case vide de la colonne
    for ligne in range(len(g)):
        if(g[ligne][c] == 0):
            g[ligne][c] = j
            dernier_coup = (ligne, c)
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
    # Vérifier si il y a un alignement adiagonal de 4 pions du joueur J commençant à la case (L,C)
    if(l+3 < len(g) and c-3 >= 0):
        if(g[l][c] == j and g[l+1][c-1] == j and g[l+2][c-2] == j and g[l+3][c-3] == j):
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
                return ligne, colonne
    return False



# Écrire une fonction match_nul(g) qui renvoie un booléen indiquant s’il y a match nul, c’est-à-dire si la grille est totalement remplie. Indication : on pourra se contenter d’examiner la ligne du haut.

def match_nul(g):
    # G est la grille
    # Vérifier si la grille est totalement remplie
    for colonne in range(len(g[0])):
        if(g[len(g)-1][colonne] == 0):
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

def puissance4_2joueurs(pseudo1, pseudo2):
    # Jouer une partie de puissance 4 à 2 joueurs
    g = grille_vide()
    joueur = 1
    affiche(g, pseudo1, pseudo2, tour=joueur)
    while(not victoire(g, 1 if joueur == 2 else 2) and not match_nul(g)):
        colonne = demander_colonne(g, texte=("\x1b[31mJoueur 1\x1b[0m ( \x1b[31m" + pseudo1 + "\x1b[0m )" if joueur == 1 else "\x1b[34mJoueur 2\x1b[0m ( \x1b[34m"+pseudo2+"\x1b[0m )") + ", entrez le numéro de la colonne : ")
        while(not coup_possible(g, colonne)):
            colonne = demander_colonne(g, texte=("\x1b[31mJoueur 1\x1b[0m ( \x1b[31m" + pseudo1 + "\x1b[0m )" if joueur == 1 else "\x1b[34mJoueur 2\x1b[0m ( \x1b[34m"+pseudo2+"\x1b[0m )") + ", entrez le numéro de la colonne : ")
        jouer(g, joueur, colonne)
        affiche(g, pseudo1, pseudo2, tour=joueur)
        joueur = 2 if joueur == 1 else 1
    affiche(g, pseudo1, pseudo2)
    if(victoire(g, 1)):
        won(g, 1, pseudo1, pseudo2)
    elif(victoire(g, 2)):
        won(g, 2, pseudo1, pseudo2)
    else:
        end_match_nul(g)





# Écrire enfin une fonction puissance4_1joueur() qui permet à l’utilisateur de jouer contre l’ordinateur qui joue aléatoirement, en affichant la grille après chaque coup et le résultat en fin de partie.

def puissance4_1joueur(pseudo1, pseudo2):
    # Jouer une partie de puissance 4 à 1 joueur
    os.system("cls||clear")
    g = grille_vide()
    mode = ask_integer("Choisissez le mode de jeu :\n1. Simple\n2. Compliqué\n")
    while(mode != 1 and mode != 2):
        mode = ask_integer("Choisissez le mode de jeu :\n1. Simple\n2. Compliqué\n")

    affiche(g, pseudo1, pseudo2, tour=1)


    while(not victoire(g, 1) and not victoire(g, 2) and not match_nul(g)):
        colonne = demander_colonne(g)
        jouer(g, 1, colonne)
        if(not victoire(g, 1) and not victoire(g, 2) and not match_nul(g)): # Si ce coup n'a pas permi au joueur de gagner, faire jouer l'ordinateur
            affiche(g, pseudo1, pseudo2, tour=2)
            print("L'ordinateur est en train de penser...")
            time.sleep(1.5)
            # coup_aleatoire(g, 2)
            if(mode == 1):
                coup_aleatoire(g, 2)
            elif(mode == 2):
                coup_ordinateur(g)
            affiche(g, pseudo1, pseudo2, tour=1)

    # Récupérer les données de la fonction victoire
    if(victoire(g, 1)):
        won(g, 1, pseudo1, pseudo2)
    elif(victoire(g, 2)):
        won(g, 2, pseudo1, pseudo2)
    else:
        end_match_nul(g)


def demander_colonne(g, texte="Entrez le \x1b[33;20mnuméro de la colonne\x1b[0m où vous voulez jouer : "):
    colonne = ask_integer(texte)
    if(not coup_possible(g, colonne-1)):
        print("Veuillez entrer le numéro d'une colonne affichée et non pleine")
        return demander_colonne(g)
    else:
        return colonne-1
    

# Pour aller plus loin, écrire une stratégie de jeu pour l’ordinateur et l’implémenter.


def won(grille, joueur, pseudo1, pseudo2):
    global score1, score2
    os.system("cls||clear")
    # Make an animation of the winning line by getting the data from the victoire function
    (ligne, colonne) = victoire(grille, joueur)

    # if(horiz(g, j, ligne, colonne) or vert(g, j, ligne, colonne) or diag1(g, j, ligne, colonne) or diag2(g, j, ligne, colonne)):
    if(horiz(grille, joueur, ligne, colonne)):
        for i in range(4):
            grille[ligne][colonne+i] = 3
    elif(vert(grille, joueur, ligne, colonne)):
        for i in range(4):
            grille[ligne+i][colonne] = 3
    elif(diag1(grille, joueur, ligne, colonne)):
        for i in range(4):
            grille[ligne+i][colonne+i] = 3
    elif(diag2(grille, joueur, ligne, colonne)):
        for i in range(4):
            grille[ligne+i][colonne-i] = 3
    affiche(grille, pseudo1, pseudo2)
    if(joueur == 1):
        score1 = score1+1
        text = pseudo1 + " a gagné !"
    else:
        score2 = score2+1
        text = pseudo2 + " a gagné !"
    print("Match nul !", end="")
    time.sleep(0.5)
    print("\r\x1b[47m\x1b[31m"+text+"\x1b[0m", end="")
    time.sleep(0.5)
    print("\r\x1b[41m\x1b[37m"+text+"\x1b[0m", end='')
    time.sleep(0.5)
    print("\r\x1b[47m\x1b[31m"+text+"\x1b[0m", end="")
    time.sleep(0.5)
    print("\r\x1b[41m\x1b[37m"+text+"\x1b[0m")
    

def end_match_nul(grille):
    # Faire clignoter le tableau en rouge
    for i in range(5):
        affiche(grille, "Joueur 1", "Joueur 2")
        print("Match nul !", end="")
        time.sleep(0.5)
        print("\r\x1b[47m\x1b[31mMatch nul !\x1b[0m", end="")
        time.sleep(0.5)
        print("\r\x1b[41m\x1b[37mMatch nul !\x1b[0m", end='')
        time.sleep(0.5)
        print("\r\x1b[47m\x1b[31mMatch nul !\x1b[0m", end="")
        time.sleep(0.5)
        print("\r\x1b[41m\x1b[37mMatch nul !\x1b[0m", end='')

def coup_ordinateur(g):
    # G est la grille
    # J est le joueur 1 ou 2
    # Jouer un coup pour l'ordinateur de façon intelligente. L'ordinateur doit gagner si possible, sinon il doit bloquer le joueur s'il peut, sinon il joue aléatoirement. L'ordinateur est le joueur 2
    # Si le joueur 1 peut gagner, jouer le coup qui permet de gagner
    for i in range(7):
        if(coup_possible(g, i)):
            jouer(g, 2, i)
            if(victoire(g, 2)):
                return
            else:
                annuler_dernier_coup(g)
    # Si le joueur 1 peut bloquer le joueur 2, jouer le coup qui permet de bloquer
    for i in range(7):
        if(coup_possible(g, i)):
            jouer(g, 1, i)
            if(victoire(g, 1)):
                annuler_dernier_coup(g)
                jouer(g, 2, i)
                return
            else:
                annuler_dernier_coup(g)
    # Sinon jouer aléatoirement
    coup_aleatoire(g, 2)

def annuler_dernier_coup(g):
    # Annuler le dernier coup joué
    global dernier_coup
    ligne, colonne = dernier_coup
    g[ligne][colonne] = 0
    

# Faire une fonction jouer qui demande à l'utilisateur combien ils sont, et leurs pseudonymes, puis lance la partie correspondante.

def play():
    global score1, score2
    nb_manche = ask_integer("Combien de manches voulez-vous jouer ? ")
    if(nb_manche <= 0):
        print("Vous devez jouer au moins une manche !")
        return play()
    nb_joueurs = ask_integer("Combien de joueurs ? ")
    if(nb_joueurs == 1):
        pseudo1 = input("Entrez votre pseudonyme: ")
        pseudo2 = "L'ordinateur"
    elif(nb_joueurs == 2):
        pseudo1 = input("Entrez le pseudonyme du joueur 1: ")
        pseudo2 = input("Entrez le pseudonyme du joueur 2: ")
    else:
        os.system("cls||clear")
        print("Vous devez jouer à 1 ou 2 joueurs !")
        return play()
    while(score1+score2 != nb_manche):
        if(nb_joueurs == 1):
            puissance4_1joueur(pseudo1, pseudo2)
        elif(nb_joueurs == 2):
            puissance4_2joueurs(pseudo1, pseudo2)
        time.sleep(2)
    if(score1 > score2):
        print(pseudo1 + " a gagné la partie avec " + str(score1) + " manches gagnées face à " + str(score2) + " pour " + pseudo2)
    elif(score2 > score1):
        print(pseudo2 + " a gagné la partie avec " + str(score2) + " manches gagnées face à " + str(score1) + " pour " + pseudo1)
    else:
        print("Match nul, vous avez tous les deux gagné!")


def ask_integer(text):
    try:
        return int(input(text))
    except ValueError:
        print("Veuillez entrer un nombre.")
        return ask_integer(text)

def launch():
    os.system("cls||clear")
    print("Bienvenue dans le jeu du Puissance 4 !")
    play()

launch()