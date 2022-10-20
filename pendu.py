#importation des modules
from random import randrange

#définition de la fonction
def pendu(lettre, nb):
    #boucle de vérification de la lettre dans le mot
    if lettre in soluce:
        print("La lettre", lettre, "est dans le mot.")
        #boucle de remplacement des "-" par la lettre
        for i in range(len(soluce)):
            if soluce[i] == lettre:
                mot = mot[:i] + lettre + mot[i+1:]
    else:
        print("La lettre", lettre, "n'est pas dans le mot.")
        nb -= 1
    return mot, nb
#Pas réussi

###     message de début   ###
print("Bienvenue dans le jeu du pendu !")
choix = input("Voulez-vous jouer ? (o/n) : ")
while choix != "o" and choix != "n":
    print("Veuillez répondre 'o' pour oui ou 'n' pour non.")
    choix = input("Voulez-vous jouer ? (o/n) : ")

while choix == "o":

    #ouverture du dico utilisé pour le pendu
    dico = open("dico_france.txt", "r", encoding="iso-8859-1")
    liste= dico.read().splitlines()

    ###     choix d'un mot au hasard dans le dico   ###
    soluce = liste[randrange(len(liste))]
    #boucle de transformation du mot en "_"
    mot = "-" * (len(soluce))
    print(mot)

    dico.close()

    ###         choix difficulté   ###

    diff = int(input("Choisissez une difficulté (facile = 1, intermédiaire = 2, expert = 3) : "))
    #boucle de vérification d'erreur de saisie
    while diff != 1 and diff != 2 and diff != 3:
        print("Veuillez choisir une difficulté valide.")
        diff = int(input("Choisissez une difficulté (facile = 1, intermédiaire = 2, expert = 3) : "))


    ###     boucle des différentes difficultés  ###
    #Difficulté facile
    if diff == 1 :
        nb_essais = 10
        lettreutilisee = []
        print("Vous avez choisi la difficulté facile. Vous avez", nb_essais, "essais.")
        #boucle du jeu
        while nb_essais != 0 and mot != soluce:
            print ("le mot contient ", len(soluce), "lettres")
            print (mot)
            lettre = input("Choisissez une lettre : ")

            #boucle de vérification d'erreur de saisie
            while len(lettre) != 1 or lettre.isalpha() == False:
                print("Veuillez saisir une lettre et seulement une (pas un chiffre).")
                lettre = input("Choisissez une lettre : ")
            lettreutilisee.append(lettre)

            ###### fonction pendu ######
            #mot, nb_essais = pendu(lettre, nb_essais)
            #boucle de vérification de la lettre dans le mot
            if lettre in soluce:
                print("La lettre", lettre, "est dans le mot.")
                #boucle de remplacement des "-" par la lettre
                for i in range(len(soluce)):
                    if soluce[i] == lettre:
                        mot = mot[:i] + lettre + mot[i+1:]
            else:
                print("La lettre", lettre, "n'est pas dans le mot.")
                nb_essais -= 1
            print ("Il vous reste", nb_essais, "essais.")
            print ("lettres déjà utilisées :", lettreutilisee)

        #boucle de vérification de victoire
        if mot == soluce:
            print("Bravo ! Vous avez gagné !")
            print("Vous avez utilisé les lettres suivantes :", lettreutilisee)
            print("Le mot était", soluce)
            print ("Vous avez trouvé en", len(lettreutilisee), "coups.")
            print ("Il vous restait", nb_essais, "vies.")
        elif nb_essais == 0:
            print("Vous avez perdu !")
            print("Vous avez utilisé les lettres suivantes :", lettreutilisee)
            print("Le mot était", soluce)

    #Difficulté moyenne
    elif diff == 2:
        nb_essais = 7
        lettreutilisee = []
        print("Vous avez choisi la difficulté intermédiaire. Vous avez", nb_essais, "essais.")
        #boucle du jeu
        while nb_essais != 0 and mot != soluce:
            print ("le mot contient ", len(soluce), "lettres")
            print (mot)
            lettre = input("Choisissez une lettre : ")
            lettreutilisee.append(lettre)
            #boucle de vérification d'erreur de saisie
            while len(lettre) != 1 or lettre.isalpha() == False:
                print("Veuillez saisir une lettre et seulement une (pas un chiffre).")
                lettre = input("Choisissez une lettre : ")
            #boucle de vérification de la lettre dans le mot
            if lettre in soluce:
                print("La lettre", lettre, "est dans le mot.")
                #boucle de remplacement des "-" par la lettre
                for i in range(len(soluce)):
                    if soluce[i] == lettre:
                        mot = mot[:i] + lettre + mot[i+1:]
            else:
                print("La lettre", lettre, "n'est pas dans le mot.")
                nb_essais -= 1
            print ("Il vous reste", nb_essais, "essais.")
            print ("lettres déjà utilisées :", lettreutilisee)

        #boucle de vérification de victoire
        if mot == soluce:
            print("Bravo ! Vous avez gagné !")
            print("Vous avez utilisé les lettres suivantes :", lettreutilisee)
            print("Le mot était", soluce)
            print ("Vous avez trouvé en", len(lettreutilisee), "coups.")
            print ("Il vous restait", nb_essais, "vies.")
        elif nb_essais == 0:
            print("Vous avez perdu !")
            print("Vous avez utilisé les lettres suivantes :", lettreutilisee)
            print("Le mot était", soluce)

    #Difficulté expert
    elif diff == 3:
        nb_essais = 5
        lettreutilisee = []
        print("Vous avez choisi la difficulté expert. Vous avez", nb_essais, "essais.")
        print("dans cette difficulté, les lettres déjà utilisées ne sont pas affichées.")
        #boucle du jeu
        while nb_essais != 0 and mot != soluce:
            print ("le mot contient ", len(soluce), "lettres")
            print (mot)
            lettre = input("Choisissez une lettre : ")
            lettreutilisee.append(lettre)
            #boucle de vérification d'erreur de saisie
            while len(lettre) != 1 or lettre.isalpha() == False:
                print("Veuillez saisir une lettre et seulement une (pas un chiffre).")
                lettre = input("Choisissez une lettre : ")
            #boucle de vérification de la lettre dans le mot
            if lettre in soluce:
                print("La lettre", lettre, "est dans le mot.")
                #boucle de remplacement des "-" par la lettre
                for i in range(len(soluce)):
                    if soluce[i] == lettre:
                        mot = mot[:i] + lettre + mot[i+1:]
            else:
                print("La lettre", lettre, "n'est pas dans le mot.")
                nb_essais -= 1
            print ("Il vous reste", nb_essais, "essais.")

        #boucle de vérification de victoire
        if mot == soluce:
            print("Bravo ! Vous avez gagné !")
            print("Vous avez utilisé les lettres suivantes :", lettreutilisee)
            print("Le mot était", soluce)
            print ("Vous avez trouvé en", len(lettreutilisee), "coups.")
            print ("Il vous restait", nb_essais, "vies.")
        elif nb_essais == 0:
            print("Vous avez perdu !")
            print("Vous avez utilisé les lettres suivantes :", lettreutilisee)
            print("Le mot était", soluce)

    ###        Vouloir rejouer ?        ###
    choix = input("Voulez-vous rejouer ? (o/n) : ")
    while choix != "o" and choix != "n":
        print("Veuillez saisir 'o' pour oui ou 'n' pour non.")
        choix = input("Voulez-vous rejouer ? (o/n) : ")

print("Merci d'avoir joué !")
print("A bientôt !")