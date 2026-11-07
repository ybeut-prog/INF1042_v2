import math
invalide = True
while invalide:
        cel = int(input("Donne moi un valeur de Celsius"))
        if cel > -273.15:
            invalide = False
fa = (cel*9/5+32)
kev =(cel+273.15)
print(f"{cel}°C = {fa}°F = {kev} K")

