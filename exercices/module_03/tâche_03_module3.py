
#1
age = int(input("Quel âge as-tu ? "))

if age >= 18:
    print("Accès autorisé")
else:
    print("Accès restreint")

#2
mot_de_passe = input("Entrez le mot de passe : ")

if mot_de_passe == "Boréal":
    print("Accès accordé")
else:
    print("Accès refusé")

#3
note = float(input("Entrez la note de l'élève : "))

if note >= 60:
    print("Réussite")
elif note >= 50:
    print("Rattrapage")
else:
    print("Échec")

#4
nombre = int(input("Entrez un nombre entier : "))

if nombre > 0 and nombre < 100:
    print("Nombre valide")
else:
    print("Nombre hors limite")

#5
import random

choix_ordinateur = random.choice(["Pierre", "Papier", "Ciseaux"])
choix_utilisateur = input("Choisis Pierre, Papier ou Ciseaux : ")

print("Choix de l'ordinateur :", choix_ordinateur)

if choix_utilisateur == choix_ordinateur:
    print("Égalité !")
else:
    print("Choix différents !")
