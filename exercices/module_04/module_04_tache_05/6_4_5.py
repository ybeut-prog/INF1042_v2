
matchs = (
    ("Tigres", "Lynx", 25, 18),
    ("Aigles", "Panthères", 22, 25),
    ("Tigres", "Panthères", 25, 23),
    ("Lynx", "Aigles", 19, 25),
    ("Tigres", "Aigles", 21, 25),
    ("Lynx", "Panthères", 25, 20)
)

victoires = {}
defaites = {}
points = {}

for match in matchs:
    equipe1, equipe2, score1, score2 = match

    for equipe in (equipe1, equipe2):
        if equipe not in victoires:
            victoires[equipe] = 0
            defaites[equipe] = 0
            points[equipe] = 0

print("GAGNANTS DE CHAQUE MATCH")
print("------------------------")

for equipe1, equipe2, score1, score2 in matchs:

    points[equipe1] += score1
    points[equipe2] += score2

    if score1 > score2:
        print(f"Les {equipe1} ont battu les {equipe2} par {score1} à {score2}.")
        victoires[equipe1] += 1
        defaites[equipe2] += 1

    else:
        print(f"Les {equipe2} ont battu les {equipe1} par {score2} à {score1}.")
        victoires[equipe2] += 1
        defaites[equipe1] += 1

print("\nNOMBRE DE VICTOIRES")
print("-------------------")

for equipe in victoires:
    print(f"{equipe} : {victoires[equipe]} victoire(s)")

meilleure_equipe = max(victoires, key=victoires.get)

print("\nÉQUIPE AVEC LE PLUS DE VICTOIRES")
print("--------------------------------")
print(f"{meilleure_equipe} avec {victoires[meilleure_equipe]} victoire(s).")

# Afficher le total des points
print("\nTOTAL DES POINTS")
print("----------------")

for equipe in points:
    print(f"{equipe} : {points[equipe]} points")

meilleure_equipe_points = max(points, key=points.get)

print("\nÉQUIPE AVEC LE PLUS DE POINTS")
print("-----------------------------")
print(f"{meilleure_equipe_points} avec {points[meilleure_equipe_points]} points.")

print("\nBILAN DES ÉQUIPES")
print("-----------------")

for equipe in victoires:
    v = victoires[equipe]
    d = defaites[equipe]

    if v > d:
        bilan = "plus de victoires que de défaites"
    elif v == d:
        bilan = "autant de victoires que de défaites"
    else:
        bilan = "plus de défaites que de victoires"

    print(f"{equipe} : {v} victoire(s), {d} défaite(s) - {bilan}.")
