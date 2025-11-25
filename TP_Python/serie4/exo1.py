age_valide = False

while not age_valide:
    try:
        age = int(input('Entrez votre age :'))
        age_valide = True
        print(f'Vous avez {age} ans')
    except ValueError:
        print('Entrez un nombre entier')