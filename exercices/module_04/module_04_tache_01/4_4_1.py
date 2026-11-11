phrase = input("Entrez une phrase : ")

mots = phrase.split()

print("Liste des mots :", mots)

nombre_mots = len(mots)
print("Nombre total de mots :", nombre_mots)

phrase_assemblee = "-".join(mots)

print("Phrase avec des tirets :", phrase_assemblee)