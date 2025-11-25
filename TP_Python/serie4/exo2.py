def division_securise():
    try:
        x = int(input("Entrez le numérateur :"))
        y = int(input('Entrez le dénominateur :'))
        resultat = x / y 
    except ValueError:
        print('Entrez un nombre entier')
        return None
    except ZeroDivisionError:
        print('Le dénominateur ne peut pas être 0')
        return None
    else:
        print(f'Le resultat est {resultat}')

if __name__ == '__main__':
    division_securise()