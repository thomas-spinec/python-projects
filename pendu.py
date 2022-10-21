#importation des modules
from random import randrange

################# Définition des fonctions #################
#fonction pour mettre en minuscule et enlever les accents
def case(phrase):
    alphabet = 'abcdefghijklmnopqrstuvwxyzaaeeeeiioucABCDEFGHIJKLMNOPQRSTUVWXYZàâéèêëîïôùç'
    result = ""
    for x in phrase:
        if x not in alphabet or alphabet.index(x)<=35:  #cherche dans l'alphabet si la lettre est en minuscule
            result += x
        elif x in alphabet and alphabet.index(x)>35:   #cherche dans l'alphabet si la lettre est en majuscule
            result += alphabet[alphabet.index(x)-35]
    return result

#####  fonction du jeu #####
#boucle du jeu
def pendu(level, nb_essais, mot, lettreutilisee):
    global soluce
    print("\n--------------------")
    print("Vous avez choisi la difficulté", level, ". Vous avez", nb_essais, "essais.")
    if level == "expert":
        print("dans cette difficulté, les lettres déjà utilisées ne sont pas affichées.")
    elif level == "extrême":
        print("Cependant, les lettres déjà utilisées ne sont pas affichées.")
        print("De plus, le mot est caché, sauf les lettres trouvées.")
    while nb_essais != 0 and mot != soluce:
        if diff < 4:
            print ("le mot contient ", len(soluce), "lettres")
        print (mot)
        lettre = input("Choisissez une lettre : ")

        #boucle de vérification d'erreur de saisie
        while len(lettre) != 1 or lettre.isalpha() == False:
            print("Veuillez saisir une lettre et seulement une (pas un chiffre).")
            lettre = input("Choisissez une lettre : ")
        lettreutilisee = lettreutilisee + lettre + ", "

        #boucle de vérification de la lettre dans le mot
        if lettre in soluce:
            print("-------------------------")
            print("\nLa lettre -", lettre, "- est dans le mot.")
            #boucle de remplacement des "-" par la lettre
            for i in range(len(soluce)):
                if soluce[i] == lettre:
                    mot = mot[:i] + lettre + mot[i+1:]
        else:
            print("-------------------------")
            print("\nLa lettre", lettre, "n'est pas dans le mot.")
            nb_essais -= 1

        print ("Il vous reste", nb_essais, "essais.")
        if diff < 3:
            print ("lettres déjà utilisées :", lettreutilisee)
    #boucle de vérification de victoire
    if mot == soluce:
        victoire(lettreutilisee, soluce, nb_essais)
    
    elif nb_essais == 0:
        defaite(lettreutilisee,soluce)
    # return mot, nb_essais, lettreutilisee

#####      fonction de victoire
def victoire(lettreutilisee, soluce, nb_essais):
    print("\n--------------------")
    print("Bravo ! Vous avez gagné !")
    print("Vous avez utilisé les lettres suivantes :", lettreutilisee)
    print("Le mot était", soluce)
    print ("Vous avez trouvé en", len(lettreutilisee), "coups.")
    print ("Il vous restait", nb_essais, "vies.")

######     fonction de défaite
def defaite(lettreutilisee,soluce):
    print("\n--------------------")
    print("Vous avez perdu !")
    print("Vous avez utilisé les lettres suivantes :", lettreutilisee)
    print("Le mot était", soluce)
##################################################################

###     message de début   ###
print("Bonjour!\nBienvenue dans le jeu du pendu !")
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
    soluce = case(soluce)

    #boucle de transformation du mot en "_"
    mot = "-" * (len(soluce))
    print(mot)

    dico.close()

    ###         choix difficulté ou informations   ###
    inf = input("choisissez si vous voulez afficher les informations du jeu ou directement choisir la difficulté \n'i' pour les informations\n'd' pour les difficultées :")
    while inf != "i" and inf != "d":
        print("Veuillez répondre 'i' pour les informations ou 'd' pour les difficultées.")
        inf = input("choisissez si vous voulez afficher les informations du jeu ou directement choisir la difficulté \n'i' pour les informations\n'd' pour les difficultées : ")
    
    while inf == "i":
        print("\nLe but du jeu est de deviner le mot mystère en trouvant toutes les lettres qui le compose (accents non compris).")
        print("En mode facile, vous avez le droit à 10 erreurs pour trouver le mot mystère.")
        print("En mode intérmédiaire, vous avez le droit à 7 erreurs.")
        print("En mode expert, vous avez le droit à 5 erreurs\nDe plus les lettres déjà utilisées ne sont pas affichées dans ce mode.")
        print("En mode extrême, vous avez le droit à 10 erreurs mais les lettres déjà utilisées ne sont pas affichées")
        print("De plus le mot est caché et seules les lettres correctes sont affichées")
        inf = input("\nTapez 'd' pour aller au choix des difficultées :")
        while inf != "d":
            inf = input("\nVeuillez taper 'd' pour aller au choix des difficultées : ")

    ###     choix de la difficulté   ###
    diff = input("\nChoisissez une difficulté\nfacile = 1 \nintermédiaire = 2\nexpert = 3 \nextrême = 4 : ")
    #boucle de vérification d'erreur de saisie
    while diff != "1" and diff != "2" and diff != "3" and diff != "4":
        print("Veuillez choisir une difficulté valide.")
        diff = input("\nChoisissez une difficulté\nfacile = 1 \nintermédiaire = 2\nexpert = 3 \nextrême = 4 : ")
    diff = int(diff)


    ###     boucle des différentes difficultés  ###
    #Difficulté facile
    if diff == 1 :
        nb_essais = 10
        lettreutilisee = ""
        level = "facile"
        #boucle du jeu
        pendu(level, nb_essais, mot, lettreutilisee)

    #Difficulté moyenne
    elif diff == 2:
        nb_essais = 7
        lettreutilisee = ""
        level = "intermédiaire"
        #boucle du jeu
        pendu(level, nb_essais, mot, lettreutilisee)

    #Difficulté expert
    elif diff == 3:
        nb_essais = 5
        lettreutilisee = ""
        level = "expert"
        #boucle du jeu
        pendu(level, nb_essais, mot, lettreutilisee)

    #Difficulté extrême
    elif diff == 4:
        mot = " " * (len(soluce))
        nb_essais = 10
        lettreutilisee = ""
        level = "extrême"
        #boucle du jeu
        pendu(level, nb_essais, mot, lettreutilisee)

    ###        Vouloir rejouer ?        ###
    print("\n--------------------")
    choix = input("Voulez-vous rejouer ? (o/n) : ")
    while choix != "o" and choix != "n":
        print("Veuillez saisir 'o' pour oui ou 'n' pour non.")
        choix = input("Voulez-vous rejouer ? (o/n) : ")

print("Merci d'avoir joué !")
print("A bientôt !")