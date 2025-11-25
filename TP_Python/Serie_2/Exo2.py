notes = [12, 9, 15.5, 7, 18]

print("Min :", min(notes))
print("Max :", max(notes))
print("Nombre de notes :", len(notes))

print('----------------------------')

compteur_reussite = 0

for note in notes:
    if note >= 10:
        compteur_reussite = compteur_reussite + 1

print("Nombre de réussites :", compteur_reussite)

print('----------------------------')


# Calucul du pourcentage de réussite
pourcentage_reussite = (compteur_reussite / len(notes)) * 100
print("Pourcentage de réussites :", pourcentage_reussite, "%")