class Produit:
    """
    Représente un produit avec son nom, son prix Hors Taxe (HT) et son stock.
    """
    
    # 1. Constructeur __init__
    def __init__(self, nom: str, prix_ht: float, stock: int):
        """Initialise un nouveau produit."""
        self.nom = nom        # Nom du produit (chaîne)
        self.prix_ht = prix_ht  # Prix unitaire Hors Taxe (nombre décimal)
        self.stock = stock    # Quantité en stock (nombre entier)

    # 2. Méthode prix_ttc
    def prix_ttc(self, taux_tva: float) -> float:
        """
        Calcule et retourne le prix TTC (Toutes Taxes Comprises).
        Formule: Prix HT * (1 + Taux TVA)
        """
        return self.prix_ht * (1 + taux_tva)

    # 2. Méthode valeur_stock_ttc
    def valeur_stock_ttc(self, taux_tva: float) -> float:
        """
        Calcule et retourne la valeur totale du stock (TTC) pour ce produit.
        Formule: Stock * Prix TTC
        """
        prix_unitaire_ttc = self.prix_ttc(taux_tva)
        return self.stock * prix_unitaire_ttc

    # Méthode d'affichage simplifiée pour le bloc principal
    def __str__(self):
        return f"{self.nom} | HT: {self.prix_ht:.2f} | Stock: {self.stock}"

if __name__ == '__main__':
    
    # Taux de TVA commun à utiliser (exemple 20%)
    TAUX_TVA = 0.20
    
    # 3. Créer au moins 3 produits différents
    produit_a = Produit(nom="Clavier Mécanique", prix_ht=80.00, stock=10)
    produit_b = Produit(nom="Souris Gaming", prix_ht=35.50, stock=25)
    produit_c = Produit(nom="Tapis XXL", prix_ht=15.00, stock=5)
    
    # Stocker les produits dans une liste catalogue
    catalogue = [produit_a, produit_b, produit_c]
    
    somme_stock_ttc_total = 0.0
    
    print(f"--- CATALOGUE DES PRODUITS (TVA: {TAUX_TVA * 100}%) ---")
    
    # Affichage pour chaque produit et cumul du total
    for produit in catalogue:
        
        # Calculer le prix TTC pour l'affichage
        ttc = produit.prix_ttc(TAUX_TVA)
        
        # Calculer la valeur totale du stock TTC pour le produit
        valeur_stock = produit.valeur_stock_ttc(TAUX_TVA)
        
        # Accumuler la valeur pour le total final
        somme_stock_ttc_total += valeur_stock
        
        # Afficher les informations demandées
        print("\n" + "="*40)
        print(f"Nom : {produit.nom}")
        print(f"Prix HT : {produit.prix_ht:.2f} €")
        print(f"Prix TTC : {ttc:.2f} €")
        print(f"Stock Disponible : {produit.stock} unités")
        print(f"Valeur Stock TTC : {valeur_stock:.2f} €")
        print("="*40)

    # Calculer et afficher la somme de toutes les valeurs de stock TTC
    print("\n--- RÉSUMÉ DU CATALOGUE ---")
    print(f"Valeur Totale du Stock TTC du Catalogue : {somme_stock_ttc_total:.2f} €")