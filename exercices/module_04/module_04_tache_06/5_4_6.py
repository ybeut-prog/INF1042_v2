eleves_A = {"Mia", "Noah", "Liam", "Zoe"}
eleves_B = {"Zoe", "Emma", "Liam", "Olivier"}


groupe_A_seulement = eleves_A - eleves_B


eleves_communs = eleves_A & eleves_B


difference_symetrique = eleves_A ^ eleves_B

print("Groupe A seulement :", groupe_A_seulement)
print("Élèves communs :", eleves_communs)
print("Différence symétrique :", difference_symetrique)
