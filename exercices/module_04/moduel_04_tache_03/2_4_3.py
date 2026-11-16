L = [3, -1, 4, -2, 0, 5, -9]

for x in L[:]:
    if x < 0:
        print(x)
        L.remove(x)

print(L)