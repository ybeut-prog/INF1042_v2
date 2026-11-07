import random
options = ["pierre", "papier", "ciseaux"]
Invalide = True
reponse = ""
fois_de_jeu = 0
perdu = 0
egale = 0
while 1:

    choix = random.choice(options)

    while Invalide :
        reponse = input("\nChoisissez un choix de Pierre, Papier, Ciseaux, ou quitter")
        reponse = reponse.lower().strip()
        if reponse == "pierre" or reponse == "pierre" or reponse == "papier" or reponse == "quitter":
            Invalide = False
        else:
            print("Pas un réponse")


    Invalide = True
    if reponse == "quitter":
        break
    if reponse == choix:
        print("Pas de gagnant")
        egale += 1
    elif reponse == "pierre" and choix == "ciseaux":
        print("Tu as gagné!")
    elif reponse == "ciseaux" and choix == "papier":
        print("Tu as gagné!")
    elif reponse == "papier" and choix == "pierre":
        print("Tu as gagné")
    else:
        print("Tu as perdu")
        perdu += 1
    fois_de_jeu += 1

    print(f"L'ordinateur a joué {choix}")

print(f"Victoires : {fois_de_jeu-perdu-egale}\nDéfaites : {perdu}\nÉgalités : {egale}\nTotal de parties : {fois_de_jeu}")
