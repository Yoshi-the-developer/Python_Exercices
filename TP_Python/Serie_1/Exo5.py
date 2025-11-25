
# Exercice 5
prix = [9.99, 14.5, 3.2, 29.0]

for i in range(len(prix)):
    print(prix[i])

print('----------------------------')

print(f'Prix total : {sum(prix)} €')
print(f'Prix moyen : {sum(prix) / len(prix)} €')

# Afficher uniquement les prix en dessous de 10 €
print('----------------------------')
print("Prix en dessous de 10 € :")
for p in prix:
    if p < 10:
        print(p)

