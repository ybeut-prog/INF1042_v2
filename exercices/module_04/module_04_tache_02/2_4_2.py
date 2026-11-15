with open("valeurs.txt", "r") as file:
    valeurs = []

    for ligne in file:
        valeur = int(ligne)
        valeurs.append(valeur)

maximum = max(valeurs)
minimum = min(valeurs)
moyenne = sum(valeurs) / len(valeurs)

print("Valeur maximale :", maximum)
print("Valeur minimale :", minimum)
print("Moyenne :", moyenne)