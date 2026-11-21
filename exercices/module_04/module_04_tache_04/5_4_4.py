grille = [[1,2,3],[4,5,6],[7,8,9]]
add =[]
som = 0
for i in grille:
    for j in i:
        som += j
    add.append(som)
    som = 0
print(add)