import math
def aire_cercle(diametre):
    rayon = diametre / 2
    return math.pi * (rayon ** 2)

print("Aire pour un diamètre de 10 :", aire_cercle(10))