with open("valeurs.txt", "r") as fichier:
    with open("bas.txt", "w") as bas:
        with open("haut.txt", "w") as haut:

            for ligne in fichier:
                valeur = int(ligne)

                if valeur < 50000:
                    bas.write(str(valeur) + "\n")
                else:
                    haut.write(str(valeur) + "\n")

print("Les fichiers bas.txt et haut.txt ont été créés.")