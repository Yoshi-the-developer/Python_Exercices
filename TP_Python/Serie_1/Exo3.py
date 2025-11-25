# Exercice 3
age = int(input("Votre âge : "))

if age < 12:
    print("Tarif enfant : 5€")
elif age < 17:
    print("Tarif jeune : 7€")
elif age < 25:
    print("Tarif plein : 8.5€")
else: 
    print("Tarif adulte : 10€")
