# Exercice 4
nombre = int(input("Entrez un nombre entier : "))

compteur = 0 
for compteur in range(1, 11):
    print(f'{nombre} x {compteur} = ', nombre * compteur)
    compteur += 1

