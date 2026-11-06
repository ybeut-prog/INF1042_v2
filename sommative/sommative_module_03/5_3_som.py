import random
options = ["pierre", "papier", "ciseaux"]
choix = random.choice(options)
reponse = input("Choisissez un choix de Pierre, Papier, Ciseaux")
reponse = reponse.lower()
reponse = reponse.strip()
if reponse == choix:
    print("Pas de gagnant")
elif reponse == "pierre" and options == "ciseaux":
    print("Tu as gagné!")
elif reponse == "ciseaux" and options == "papier":
    print("Tu as gagné!")
elif reponse == "papier" and options == "pierre":
    print("tu as gagné")
else:
    print("Tu as perdu")

print(f"L'ordinateur a joué {choix}")
