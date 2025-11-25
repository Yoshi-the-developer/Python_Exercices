produits = ["PC Portable", "Écran", "Clavier", "Souris", "Casque"]


try:
    index_user = int(input('Entrez l\'indice du produit :'))
    print(f'Le produit de l\'indice choisi est {produits[index_user]}')
except ValueError:
    print('Veuillez choisir un nombre entier')
except IndexError:
    print('Votre indice est trop élevé')
    print(f'Veuillez choisir un indice compris entre 0 et {len(produits)}')