print("Je demande prénom, nom,année de naissance et ville")
prenom = (input("Entrez prénom: "))
nom = (input("Entrez nom: "))
annee_de_naissance = (input("Entrez année de naissance: "))
ville = (input("Entrez ville: "))
import string
import random

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
numbers = string.digits
symbols = string.punctuation

password_length = int(input("Saisissez la longueur souhaitée pour votre mot de:"))

characters = []
characters.extend(list(lowercase))
characters.extend(list(uppercase))
characters.extend(list(numbers))
characters.extend(list(symbols))

words = ["apple", "banana", "cherry", "date", "elderberry", "fig"]
random_words = random.sample(words, k=3)

generated_password = "".join(random.sample(characters, password_length))
random_chars = random.sample(characters, password_length)

all_elements = random_words + random_chars
generated_password = "".join(all_elements)

print("Votre mot de passe : ", generated_password)


