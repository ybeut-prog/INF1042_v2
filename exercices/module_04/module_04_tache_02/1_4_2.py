import random

with open("valeurs.txt", "w") as file:
    for i in range(1000):
        valeur = random.randint(0, 100000)
        file.write(str(valeur) + "\n")

print("Les 1000 valeurs ont été enregistrées dans valeurs.txt.")