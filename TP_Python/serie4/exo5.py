class CommandeInvalidError(Exception):
    pass

def valider_commande(montant):
    if montant <= 0:
        raise CommandeInvalidError('Le montant doit être positif')
    elif montant > 10000:
        raise CommandeInvalidError("Le montant ne doit pas dépasser 10 000")
    else: 
        return True
    
if __name__ == '__main__':
    try: 
        montant = int(input('Entrez votre montant :'))
        valider_commande(montant)
    except ValueError:  
        print('Entrez un nombre entier')
    except CommandeInvalidError:
        print('Votre commande est invalide')
    else: 
        print('Commande valide')

