class Client: 
    def __init__(self, nom: str, email: str):
        self.nom = nom
        self.email = email
    
    def __str__(self):
        return f"Client: {self.nom} <{self.email}>"

class LigneCommande:
    def __init__(self, description: str, quantite: int, prix_unitaire: float):
        self.description = description
        self.quantite = quantite
        self.prix_unitaire = prix_unitaire

    def total_ligne(self):
        self.quantite * self.prix_unitaire

    def __str__(self):
        return f" - {self.description} | {self.quantite} x {self.prix_unitaire:.2f}€ = {self.total_ligne():.2f}€"
        
class Commande:
    def __init__(self, client: Client):
        # Attribut client (instance de Client)
        self.client = client
        # Attribut lignes (liste de LigneCommande, initialement vide)
        self.lignes = []

    def ajouter_ligne(self, ligne: LigneCommande):
        """Ajoute une LigneCommande à la liste des lignes de la commande."""
        self.lignes.append(ligne)

    def total(self) -> float:
        """Calcule le montant total de la commande en sommant toutes les lignes."""
        montant_total = 0.0
        for ligne in self.lignes:
            montant_total += ligne.total_ligne()
        return montant_total
        
    # Méthode pour afficher le récapitulatif (Étape 4)
    def afficher_recap(self):
        """Affiche le récapitulatif complet de la commande."""
        print("\n" + "="*40)
        print(f"COMMANDE POUR : {self.client.nom}")
        print(f"Email : {self.client.email}")
        print("-" * 40)
        
        if not self.lignes:
            print("Aucune ligne de commande.")
            return

        for ligne in self.lignes:
            print(ligne) # Utilise la méthode __str__ de LigneCommande
            
        print("-" * 40)
        print(f"MONTANT TOTAL : {self.total():.2f}€")
        print("="*40)


if __name__ == '__main__':
    
    # 1. Créer un client
    client_principal = Client(nom="Marie Dubois", email="marie.dubois@mail.com")
    
    # 2. Créer plusieurs lignes de commande
    ligne1 = LigneCommande(description="Pack 10h de support", quantite=1, prix_unitaire=500.00)
    ligne2 = LigneCommande(description="Licence Logiciel Annuelle", quantite=2, prix_unitaire=120.00)
    ligne3 = LigneCommande(description="Documentation Papier", quantite=5, prix_unitaire=8.50)
    
    # 3. Créer une commande associée au client
    commande_client = Commande(client=client_principal)
    
    # 4. Ajouter les lignes à la commande
    commande_client.ajouter_ligne(ligne1)
    commande_client.ajouter_ligne(ligne2)
    commande_client.ajouter_ligne(ligne3)
    
    # 5. Afficher un petit récapitulatif (client, lignes, total)
    commande_client.afficher_recap()
    
    # Vérification du total (doit être 500 + 240 + 42.50 = 782.50)
    print(f"\n[Vérification du total calculé] : {commande_client.total():.2f}€")