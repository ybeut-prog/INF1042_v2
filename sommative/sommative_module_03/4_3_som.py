import random
ops_1 = 0
ops_2 = 0
ops_3 = 0
ops_4 = 0
n = int(input("met un nombre pour nombre de tire"))

print(f"Théorique est 1/4")
ops =["1","2","3","4"]
for i in range(1,n+1):
    mon= random.choice(ops)
    if mon == "1":
        ops_1 += 1
    if mon == "2":
        ops_2 += 1
    if mon == "3":
        ops_3 += 1
    if mon == "4":
        ops_4 += 1
print(f"choix 1,2,3 et 4 était choisi {ops_1/n*100, ops_2/n*100, ops_3/n*100, ops_4/n*100}")
