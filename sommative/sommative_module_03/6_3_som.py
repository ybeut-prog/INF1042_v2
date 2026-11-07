import math
montant = 0
elec = ""
Temps_c =0
Temps_ac = 0
Invalide = True
rabais = 0
while Invalide:
    elec = input("\nUne voiture électrique? oui ou non")
    elec = elec.lower().strip()
    if elec == "non" or elec == "oui" :
        Invalide = False
Invalide = True

while Invalide:
    Temps_c = input("Donne-nous votre heures pour stationner")
    Temps_c = Temps_c.strip()
    try:
        Temps_c = float(Temps_c)
        Invalide = False
    except ValueError:
        Invalide = True

Temps_ac = math.ceil(float(Temps_c))

if (Temps_ac / 24) < 1 :
   Temps_R = Temps_ac-1
   montant += 4
   montant += Temps_R*2.5
else:
    montant = math.ceil(Temps_ac/24)*20
if elec == "oui":
    rabais = 0.2

print(f"Durée : {Temps_c} heures\nHeures facturées : {Temps_ac}\nPrix avant rabais : {montant:.2f} $")
print(f"Rabais véhicule électrique : {rabais*montant:.2f} $\nTotal : {montant*(1-rabais):.2f} $")







