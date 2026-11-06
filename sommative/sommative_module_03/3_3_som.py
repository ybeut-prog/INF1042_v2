M_O = int(input("L'argent?"))
if M_O > 100:
    rabais = 0.5
elif 50 <= M_O <= 100:
    rabais = 0.4
else:
    rabais = 0.25
montant = (1-rabais)*M_O
print(f"Le facture est {montant} avec {rabais} de rabais et le montant original était {M_O}")