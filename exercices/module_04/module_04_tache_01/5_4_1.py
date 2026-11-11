phrase = input("Entrez une phrase : ")

voyelles = "aeiouy"
compteur = 0

for caractere in phrase.lower():
    if caractere in voyelles:
        compteur += 1

print("Nombre total de voyelles :", compteur)