import re
num_format = re.compile('[1-3]')
##################################
###  Definition des fonctions  ###
# fonction du plateau de jeu

def draw(m):
    print("\n")
    for i in range(0,3):
        print(m[i][0],m[i][1],m[i][2])
    return 1

# fonction de vérification de victoire
def check(m):
    #verification des lignes
    if (m[0][0] == m[0][1] == m[0][2] != "-"):  #verif 1ère ligne
        return 1
    elif (m[1][0] == m[1][1] == m[1][2] != "-"): #verif 2eme ligne
        return 1
    elif (m[2][0] == m[2][1] == m[2][2] != "-"): # verif 3eme ligne
        return 1
    #verification des colonnes
    elif (m[0][0] == m[1][0] == m[2][0] != "-"):
        return 1
    elif (m[0][1] == m[1][1] == m[2][1] != "-"):
        return 1
    elif (m[0][2] == m[1][2] == m[2][2] != "-"):
        return 1
    #verification des diagonales
    elif (m[0][0] == m[1][1] == m[2][2] != "-"):
        return 1
    elif (m[0][2] == m[1][1] == m[2][0] != "-"):
        return 1
    #verification du match nul
    elif m[0][0] != "-" and m[0][1] != "-" and m[0][2] != "-" and m[1][0] != "-" and m[1][1] != "-" and m[1][2] != "-" and m[2][0] != "-" and m[2][1] != "-" and m[2][2] != "-":
        return 2
    else:
        return 0

# fonction du score
def score(player):
    print("Le tableau des score est mis à jour.")
    scr = []
    txt = open("score.txt", "r")
    texte = txt.readlines()
    #boucle de vérification de l'existence du joueur dans le fichier
    for i in texte:
        if i.find(player) != -1:
            file = open("score.txt", "r")
            #boucle pour "ranger" les players et les scores dans un tableau
            for line in file:
                tableau = line.split(" :")
                scr.append({"nom" : tableau[0], "score" : int(tableau[1])})
            file.close()

            #boucle pour trouver le gagnant et ajouter 1 au score
            for tableau in scr:
                if tableau["nom"] == player:
                    tableau["score"] += 1

            #enregistrement du score dans le fichier
            score = open("score.txt", "w")
            for tableau in scr:
                score.write(tableau["nom"] + " : " + str(tableau["score"]) + "\n")
            score.close()
            break
        #boucle pour ajouter le joueur dans le fichier
        elif i.find(player) == -1:
            score = open("score.txt", "a")
            score.write(player + " : 1\n")
            score.close()
            break
    txt.close()

#fonction de vérification de saisie
def verif_jouer(jouer):
    while jouer != "j" and jouer != "s":
            print("Veuillez saisir j pour jouer ou s pour voir les scores.")
            jouer = input("Souhaites tu jouer ou voir les scores ? (j/s) : ")
    return jouer

#fonction du jeu
def play():
    x = input("Saisir la ligne : ")
    while num_format.match(x) == None:
        print("Veuillez saisir un chiffre, entre 1 et 3.")
        x = input("Saisir la ligne : ")

    y = input("Saisir la colonne : ")
    while num_format.match(y) == None:
        print("Veuillez saisir un chiffre, entre 1 et 3.")
        y = input("Saisir la colonne : ")

    x = (int(x) -1)
    y = (int(y) -1)
    while m[x][y] != "-":
        print("Cette case est déjà prise !")
        x = input("Saisir la ligne : ")
        while num_format.match(x) == None:
            print("Veuillez saisir un chiffre, entre 1 et 3.")
            x = input("Saisir la ligne : ")

        y = input("Saisir la colonne : ")
        while num_format.match(y) == None:
            print("Veuillez saisir un chiffre, entre 1 et 3.")
            y = input("Saisir la colonne : ")

        x = (int(x) -1)
        y = (int(y) -1)
    return x, y

######   Initialisation ##########
file = open("score.txt", "a")  #permet de créer le fichier score.txt s'il n'existe pas
file.close()
rejouer = "o"  # variable de boucle de rejouer (ne peux être modifiée qu'après une partie)

###### Message de début  #############
print("Bonjour !\nBienvenue dans le jeu du morpion !")

while rejouer == "o":
    jouer = input("Souhaites tu jouer ou voir les scores ? (j/s) : ")
    #verification de la saisie
    verif_jouer(jouer)
    
    #boucle des scores
    while jouer == "s":
        file = open("score.txt", "r")
        print("\nVoici les scores :")
        print(file.read())
        file.close()
        jouer = input("\nSouhaites tu jouer ou voir les scores ? (j/s) : ")
        verif_jouer(jouer)

    while jouer == "j":
        player1 = input("Joueur 1 (croix), quel est ton prénom ? : ")
        player2 = input("Joueur 2 (rond), quel est ton prénom ? : ")
        vide = "-"
        m= [[vide, vide, vide], [vide, vide, vide], [vide, vide, vide]]
        draw(m)
        #########     boucle de jeu   #########
        while check(m) == 0:
            #tour du joueur 1
            print("Au tour de", player1, "de jouer !")
            x, y =play()

            m[x][y] = "X"
            draw(m)

            #verification de la victoire
            if check(m) == 1:
                print("Bravo", player1, "tu as gagné !")
                score(player1)
                break

            elif check(m) == 2:
                print("Match nul !")
                break

            #tour du joueur 2
            print("Au tour de", player2, "de jouer !")
            x, y = play()

            m[x][y] = "O"
            draw(m)

            #verification de la victoire
            if check(m) == 1:
                print("Bravo", player2, "tu as gagné !")
                score(player2)
                break

            elif check(m) == 2:
                print("Match nul !")
                break

        #rejouer ?
        rejouer = input("Souhaites tu rejouer ? (o/n) : ")
        while rejouer != "o" and rejouer != "n":
            print("Veuillez saisir o pour rejouer ou n pour quitter.")
            rejouer = input("Souhaites tu rejouer ? (o/n) : ")
        if rejouer == "o":
            jouer = ""
        elif rejouer == "n":
            print ("Merci d'avoir joué !")
            print ("A bientôt !")
            exit()

