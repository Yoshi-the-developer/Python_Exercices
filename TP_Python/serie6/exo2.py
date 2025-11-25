class CompteBancaire:
    """ 
    Representation d'un compte bancaire 
    :param titulaire: nom du titulaire du compte
    :param solde: montant restant sur le compte
    """
    def __init__(self, titulaire: str, solde: float, total: float):
        self.titulaire = titulaire
        self.solde = solde
        self.total = total 

        # Initialisation du solde a 0
        solde = 0
    
    def deposer(self):
        if self.solde >= 0:
            ajouter = float(input('Entrer le montant à ajouter au compte :'))
            self.total = ajouter + self.solde
            print(self.total)
        return self.total
    
    def retirer(self):
        montant = float(input('Entrez le montant à retirer :'))
        if self.solde <= montant:
            self.solde = self.total - montant
            print(f"total apres retrait {self.solde}")
        else: 
            print(f'Votre solde est insuffisant : {self.solde}')
        return self.solde
    
    def afficher(self):
        titulaire = self.titulaire
        solde = self.solde

        print('-' * 10)
        print('Information du compte')
        print('-' * 10)

        print(f'Titulaire du compte : {titulaire}')
        print(f'Solde du compte : {solde}')

if __name__ == '__main__':
    Compte1 = CompteBancaire(titulaire="Alice", solde=0, total=0)

    Compte1.deposer()
    print('Compte apres dépot')
    Compte1.afficher()

    Compte1.retirer()
    print('Compte apres retrait')
    Compte1.afficher()

