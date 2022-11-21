import random
import os
import time
import sys

score1 = 0
score2 = 0
matchNul = 0
dernier_coup = (0, 0)


#  Écrire une fonction grille_vide() qui renvoie une grille vide.
# 6 lignes et 7 colonnes rempli de 0.

def grille_vide():
    """Renvoie une grille vide"""
    return [[0 for i in range(7)] for j in range(6)]

# Écrire une fonction affiche_grille(g) qui affiche la grille g
def affiche(grille, pseudo1, pseudo2, tour=0):
    """
    grille: grille, pseudo1: str, pseudo2: str, tour: int => None
    Affiche la grille de jeu
    """
    global score1, score2
    os.system("cls||clear")
    print("\x1b[30;20m================\x1b[0m \033[1mPUISSANCE 4\x1b[0m\x1b[30;20m ================\x1b[0m")
    text = "\x1b[31mJoueur 1:\x1b[0m " + pseudo1
    print(text, end="")
    print(" "*(50-len(text))+str(score1)) # Utilisé pour aligner les scores des deux joueurs, peu importe la longueur de leur pseudo
    text = "\x1b[34mJoueur 2:\x1b[0m " + pseudo2
    print(text, end="")
    print(" "*(50-len(text))+str(score2))
    print("============================================")
    if(tour != 0): # Si jamais on veut afficher la grille sans afficher le tour actuel, pour la fin du jeu par exemple
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
            elif(grille[ligne][colonne] == 3): # Pour afficher les cases gagnantes à la fin du jeu
                print("\x1b[42m + \x1b[0m|", end='')
            else:
                print(" . |", end='')
        print()
        # print("\n"+" "*7+"-----------------------------")
    print("============================================")


# Écrire une fonction coup_possible(g, c) qui renvoie un booléen indiquant s’il est possible de jouer dans la colonne c. Il est possible de jouer dans la colonne c si elle n’est pas déjà pleine, c’est-à-dire si la case la plus haute de la colonne c contient un zéro.
def coup_possible(g, c):
    """
    g: grille, c: int => bool
    Renvoie True si le coup est possible, False sinon
    """
    try:
        return g[len(g)-1][c] == 0
    except IndexError:
        return False
    

# Ecrire une fonction jouer(g, j, c) qui joue un coup du joueur j dans la colonne c en supposant que la colonne c n’est pas pleine.
# Indication : la première case vide de la colonne c, en partant du bas (c’est-à-dire de plus petit indice) prendra la valeur j (1 ou 2 donc).

def jouer(g, j, c):
    """
    g: grille, j: int, c: int => None
    Joue un coup du joueur j dans la colonne c
    """
    global dernier_coup
    for ligne in range(len(g)): # On parcourt les lignes de la grille, pour accéder à la première case vide de la colonne c
        if(g[ligne][c] == 0): # Si la case est vide
            g[ligne][c] = j
            dernier_coup = (ligne, c) # On stocke la position du dernier coup joué, au cas où il faudrait l'annuler
            break # On sort de la boucle, pour ne pas modifier les cases en dessous de la première case vide
    
    
# Écrire 4 fonctions horiz(g, j, l, c), vert(g, j, l, c), diag1(g, j, l, c) et diag2(g, j, l, c) qui déterminent respectivement s’il y a un alignement de 4 pions du joueur j commençant à la case (l,c). Les 4 fonctions renvoient un booléen (qui vaut True en cas d’alignement, False sinon).
# Précisément, les 3 pions permettant de réaliser un alignement avec le pion de la case (l,c) dans les fonctions horiz(g, j, l, c), vert(g, j, l, c) et diag1(g, j, l, c) sont situés dans les cases à droite ou au-dessus de (l,c). Dans la fonction diag2(g, j, l,c) , ils sont situés au-dessus à gauche.

def horiz(g, j, l, c):
    """
    g: grille, j: int, l: int, c: int => boolean
    Renvoie True si il y a un alignement horizontal de 4 pions du joueur j
    """
    if(c+3 < len(g[0])):
        if(g[l][c] == j and g[l][c+1] == j and g[l][c+2] == j and g[l][c+3] == j):
            return True
    return False

def vert(g, j, l, c):
    """
    g: grille, j: int, l: int, c: int => boolean
    Renvoie True si il y a un alignement vertical de 4 pions du joueur j
    """
    if(l+3 < len(g)):
        if(g[l][c] == j and g[l+1][c] == j and g[l+2][c] == j and g[l+3][c] == j):
            return True
    return False


def diag1(g, j, l, c):
    """
    g: grille, j: int, l: int, c: int => boolean
    Renvoie True si il y a un alignement diagonal de 4 pions du joueur j
    """
    if(l+3 < len(g) and c+3 < len(g[0])):
        if(g[l][c] == j and g[l+1][c+1] == j and g[l+2][c+2] == j and g[l+3][c+3] == j):
            return True
    return False


def diag2(g, j, l, c):
    """
    g: grille, j: int, l: int, c: int => boolean
    Renvoie True si il y a un alignement adiagonal de 4 pions du joueur j
    """
    if(l+3 < len(g) and c-3 >= 0):
        if(g[l][c] == j and g[l+1][c-1] == j and g[l+2][c-2] == j and g[l+3][c-3] == j):
            return True
    return False
    


# Écrire une fonction victoire(g,j) qui renvoie un booléen indiquant si le joueur j a gagné.

def victoire(g, j):
    """
    g: grille, j: int => boolean
    Renvoie True si le joueur j a gagné
    """
    for ligne in range(len(g)):
        for colonne in range(len(g[0])):
            if(horiz(g, j, ligne, colonne) or vert(g, j, ligne, colonne) or diag1(g, j, ligne, colonne) or diag2(g, j, ligne, colonne)):
                return ligne, colonne
    return False



# Écrire une fonction match_nul(g) qui renvoie un booléen indiquant s’il y a match nul, c’est-à-dire si la grille est totalement remplie. Indication : on pourra se contenter d’examiner la ligne du haut.

def match_nul(g):
    """
    G: grille => Boolean
    Vérifier si la grille est totalement remplie
    """
    for colonne in range(len(g[0])):
        if(g[len(g)-1][colonne] == 0): # Si jamais on trouve une case de la dernière ligne qui fait exception
            return False
    return True # Si on a parcouru toute la dernière ligne sans exception, alors la grille est totalement remplie



# Écrire une fonction coup_aleatoire(g,j) qui joue un coup aléatoire pour le joueur j, en supposant que la grille n’est pas pleine.

def coup_aleatoire(g, j):
    """
    G: grille, J: joueur (1 ou 2) => None
    Jouer un coup aléatoire pour le joueur J
    """
    colonne = random.randint(0, len(g[0])-1)
    while(not coup_possible(g, colonne)):
        colonne = random.randint(0, len(g[0])-1)
    jouer(g, j, colonne)


# Écrire une fonction puissance4_2joueurs() qui utilise toutes les fonctions ci-dessus pour faire jouer deux adversaires aléatoirement et à tour de rôle, en affichant la grille après chaque coup, et qui s’arrête dès qu’un joueur gagne ou que la partie est nulle.

def puissance4_2joueurs(pseudo1, pseudo2):
    """
    Pseudo1: str, Pseudo2: str => None
    Faire jouer deux adversaires aléatoirement et à tour de rôle, en affichant la grille après chaque coup, et qui s’arrête dès qu’un joueur gagne ou que la partie est nulle.
    """
    g = grille_vide()
    joueur = 1
    affiche(g, pseudo1, pseudo2, tour=joueur)
    while(not victoire(g, 1 if joueur == 2 else 2) and not match_nul(g)):
        colonne = demander_colonne(g, texte=("\x1b[31mJoueur 1\x1b[0m ( \x1b[31m" + pseudo1 + "\x1b[0m )" if joueur == 1 else "\x1b[34mJoueur 2\x1b[0m ( \x1b[34m"+pseudo2+"\x1b[0m )") + ", entrez le numéro de la colonne : ")
        while(not coup_possible(g, colonne)):
            colonne = demander_colonne(g, texte=("\x1b[31mJoueur 1\x1b[0m ( \x1b[31m" + pseudo1 + "\x1b[0m )" if joueur == 1 else "\x1b[34mJoueur 2\x1b[0m ( \x1b[34m"+pseudo2+"\x1b[0m )") + ", entrez le numéro de la colonne : ")
        jouer(g, joueur, colonne)
        joueur = 2 if joueur == 1 else 1
        affiche(g, pseudo1, pseudo2, tour=joueur)
    affiche(g, pseudo1, pseudo2)
    if(victoire(g, 1)):
        won(g, 1, pseudo1, pseudo2)
    elif(victoire(g, 2)):
        won(g, 2, pseudo1, pseudo2)
    else:
        end_match_nul(g, pseudo1, pseudo2)


# Écrire enfin une fonction puissance4_1joueur() qui permet à l’utilisateur de jouer contre l’ordinateur qui joue aléatoirement, en affichant la grille après chaque coup et le résultat en fin de partie.

def puissance4_1joueur(pseudo1, pseudo2):
    """
    Pseudo1: str, Pseudo2: str => None
    Permet à l’utilisateur de jouer contre l’ordinateur qui joue aléatoirement, en affichant la grille après chaque coup et le résultat en fin de partie.
    """
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
            typing_effect("L'ordinateur est en train de penser...")
            time.sleep(1)
            if(mode == 1): # Mode simple
                coup_aleatoire(g, 2)
            elif(mode == 2): # Mode compliqué
                coup_ordinateur(g)
            affiche(g, pseudo1, pseudo2, tour=1)

    # Dès que la partie est terminée, afficher le résultat
    if(victoire(g, 1)):
        won(g, 1, pseudo1, pseudo2)
    elif(victoire(g, 2)):
        won(g, 2, pseudo1, pseudo2)
    else:
        end_match_nul(g, pseudo1, pseudo2)


# Fonction pour demander une colonne sans avoir d'erreur possible. Si la colonne n'est pas valide, on redemande une colonne. Le texte est modifiable selon le type de jeu.
def demander_colonne(g, texte="Entrez le \x1b[33;20mnuméro de la colonne\x1b[0m où vous voulez jouer : "):
    """
    G: grille, Texte: str => int
    Demande une colonne sans avoir d'erreur possible. Si la colonne n'est pas valide, on redemande une colonne. Le texte est modifiable selon le type de jeu.
    """
    colonne = ask_integer(texte)
    if(not coup_possible(g, colonne-1)):
        print("Veuillez entrer le numéro d'une colonne affichée et non pleine")
        return demander_colonne(g)
    else:
        return colonne-1


def won(grille, joueur, pseudo1, pseudo2):
    """
    Grille: grille, Joueur: int, Pseudo1: str, Pseudo2: str => None
    Affiche le gagnant de la partie
    """
    global score1, score2
    os.system("cls||clear")
    # On récupère les données de victoire pour créer une petite animation
    (ligne, colonne) = victoire(grille, joueur)
    # On modifie les cases qui concernent cette victoire
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
    print("\r\x1b[41m\x1b[37m"+text+"\x1b[0m", end="")
    time.sleep(0.5)
    print("\r\x1b[47m\x1b[31m"+text+"\x1b[0m", end="")
    time.sleep(0.5)
    print("\r\x1b[41m\x1b[37m"+text+"\x1b[0m", end='')
    time.sleep(0.5)
    print("\r\x1b[47m\x1b[31m"+text+"\x1b[0m", end="")
    time.sleep(0.5)
    print("\r\x1b[41m\x1b[37m"+text+"\x1b[0m")
    

def end_match_nul(grille, pseudo1, pseudo2):
    """
    Grille: grille, Pseudo1: str, Pseudo2: str => None
    Affiche le match nul
    """
    global matchNul
    matchNul = matchNul+1
    affiche(grille, pseudo1, pseudo2)
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
    """
    Grille: grille => None
    Joue un coup pour l'ordinateur de  façon intelligente. L'ordinateur doit gagner si possible, sinon il doit bloquer le joueur s'il peut, sinon il joue aléatoirement. L'ordinateur est le joueur 2
    Si le joueur 1 peut gagner, jouer le coup qui permet de gagner
    """
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
    """
    Grille: grille => None
    Annule le dernier coup joué
    """
    global dernier_coup # On récupère la variable globale, déclarée en haut du programme
    ligne, colonne = dernier_coup
    g[ligne][colonne] = 0
    

# Faire une fonction jouer qui demande à l'utilisateur combien ils sont, et leurs pseudonymes, puis lance la partie correspondante.
def play():
    """
    None => None
    Lance une partie
    """
    global score1, score2, matchNul # On récupère les variables globales, déclarées en haut du programme
    nb_manche = ask_integer("Combien de manches voulez-vous jouer ? ")
    if(nb_manche <= 0):
        typing_effect("Vous devez jouer au moins une manche !")
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
        typing_effect("Vous devez jouer à 1 ou 2 joueurs !")
        return play()
    while(score1+score2+matchNul < nb_manche):
        if(nb_joueurs == 1):
            puissance4_1joueur(pseudo1, pseudo2)
        elif(nb_joueurs == 2):
            puissance4_2joueurs(pseudo1, pseudo2)
        time.sleep(2)
    if(score1 > score2):
        typing_effect(pseudo1 + " a gagné la partie avec " + str(score1) + " manches gagnées face à " + str(score2) + " pour " + pseudo2)
    elif(score2 > score1):
        typing_effect(pseudo2 + " a gagné la partie avec " + str(score2) + " manches gagnées face à " + str(score1) + " pour " + pseudo1)
    else:
        typing_effect("Match nul avec " + str(score1) + " manches gagnées pour chaque joueur")
    input("Appuyez sur une touche pour quitter...")


def ask_integer(text): # Nous utilisons cette fonction pour être certain que l'utilisateur entre bien un nombre entier, et qu'on ait pas d'erreur
    """
    text: str -> int
    Renvoie un entier saisi par l'utilisateur à la demande de votre texte
    """
    try:
        return int(input(text))
    except ValueError: # Si l'utilisateur n'a pas entré un nombre entier
        typing_effect("Veuillez entrer un nombre.")
        return ask_integer(text)

def typing_effect(text, speed=0.02): # Nous utilisons cette fonction pour faire un effet de type
    """
    text: str -> None
    Affiche le texte en entrée caractère par caractère
    """
    for letter in text:
        print(letter, end="") # On affiche le caractère
        sys.stdout.flush() # On force l'affichage
        time.sleep(speed)
    print()

def launch():
    """
    None -> None
    Lance le jeu
    """
    os.system("cls||clear") # On efface l'écran
    # Faire une animation de bienvenue avec un typing effect
    textes = ["Bienvenue dans le jeu du Puissance 4 !", "Vous allez pouvoir jouer à 1 ou 2 joueurs.", "Vous pouvez choisir le nombre de manches à jouer.", "Bonne chance !"]
    for texte in textes:
        # On change aléatoirement la couleur de la console
        print("\x1b[3" + str(random.randint(1, 7)) + "m", end="")
        typing_effect(texte)
        # On remet la couleur de la console à la normale
        print("\x1b[0m", end="")
        time.sleep(1)
    play()

launch()
