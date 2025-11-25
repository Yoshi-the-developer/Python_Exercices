class Employe:
    """ Representation d'un employé """
    def __init__(self, nom: str, salaire_base: float):
        self.nom = nom
        self.salaireBase = salaire_base # <-- Notez le 'B' majuscule

    def calculer_salaire(self):
        """ Retourner le calcule du salaire. Formule : salaire de base """
        return self.salaireBase
    
class Developpeur(Employe):
    """
    Representation d'un developpeur 
    Salaire = salaire de base + prime technique
    """
    def __init__(self, nom: str, salaire_base: float, prime_technique: float):
        super().__init__(nom, salaire_base)
        self.prime_technique = prime_technique
    
    def calculer_salaire(self):
        # CORRECTION : Utiliser self.salaireBase
        return self.salaireBase + self.prime_technique 

class Manager(Employe):
    def __init__(self, nom: str, salaire_base: float, prime_management: float):
        super().__init__(nom, salaire_base)
        self.prime_management = prime_management

    def calculer_salaire(self):
        # CORRECTION : Utiliser self.salaireBase
        return self.salaireBase + self.prime_management
    


# Bloc principal

if __name__ == '__main__':
    # Simple employé
    e1 = Employe(nom="Jean", salaire_base=3000.00)

    # Employé Developpeur 
    dev1 = Developpeur(nom="Alice", salaire_base=3500.00, prime_technique=500.00)
    dev2 = Developpeur(nom="Patrick", salaire_base=4500.90, prime_technique=650.00)

    # Employé Manager
    man1 = Manager(nom="Christophe", salaire_base=2300.00, prime_management=1000.00)
    man2 = Manager(nom="Florence", salaire_base=2200.00, prime_management=800.00)

    # Liste de tout les Employés
    listeEmploye = [e1, dev1, dev2, man1, man2]

    print('--- Calcul des Salaires ---')
    for employe in listeEmploye:
        type_employe = employe.__class__.__name__

        salaire_calcul = employe.calculer_salaire()

        print(f"[{type_employe:<12}] Nom : {employe.nom} | Salaire calculé : {salaire_calcul:.2f} €")
    print("---------------------------")