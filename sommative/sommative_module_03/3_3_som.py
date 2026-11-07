M_O = int(input("L'argent?"))
if M_O > 100:
    rabais = 0.1
elif 50 <= M_O <= 100:
    rabais = 0.05
else:
    rabais = 0.0
montant = (1-rabais)*M_O*1.13
montant = round(montant, 2)
print(f"Le facture avec taxe est {montant}$ avec {rabais*100}% de rabais, c'est {round((1-rabais)*M_O,2):.2f}$ et le montant original était {M_O}$")