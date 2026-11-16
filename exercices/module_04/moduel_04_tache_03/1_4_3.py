notes = [12, 15, 9, 18, 15, 12]
totale = 0
moyenne =0
for index in range(0,len(notes)):
    totale = totale + (notes[index])

moyenne = totale / len(notes)
print(moyenne)
