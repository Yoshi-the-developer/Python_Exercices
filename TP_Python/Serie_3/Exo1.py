donnees_produits = [
    {"id": 1, "nom": "Clavier",  "categorie": "Informatique", "prix": 39.99, "stock": 10},
    {"id": 2, "nom": "Souris",   "categorie": "Informatique", "prix": 19.99, "stock": 0},
    {"id": 3, "nom": "Écran",    "categorie": "Informatique", "prix": 129.90, "stock": 5},
    {"id": 4, "nom": "Chaise",   "categorie": "Bureau",       "prix": 89.90, "stock": 2}
]

class Produit:
    def __init__(self, id, nom, categorie, prix, stock):
        self.id = id
        self.nom = nom
        self.categorie = categorie
        self.prix = prix
        self.stock = stock
    
    def est_en_rupture(self):
        if self.stock == 0:
            return True
    
    def afficher_resume(self):
        return f"Nom du produit : {self.nom} - Catégorie : {self.categorie} - Prix : {self.prix}€ (Stock : {self.stock})"

class Catalogue:
    def __init__(self):
        self.produits = []

    def ajouter_produit(self, produit):
        self.produits.append(produit)

    def produit_par_categorie(self, categorie_cible):
        produits_trouver = []
        for produit in self.produits:
            if produit.categorie == categorie_cible:
                produits_trouver.append(produit)
        return produits_trouver
    
    def prix_moyen(self):
        if not self.produits:
            return 0.0
        
        somme_prix = sum(p.prix for p in self.produits)
        return somme_prix / len(self.produits)
    
    def produit_en_rupture(self):
        produits_rupture = []
        for produit in self.produits:
            if produit.est_en_rupture():
                produits_rupture.append(produit)
        return produits_rupture
    

# --------------------------------------------------
# Bloc Principal 
# --------------------------------------------------

def main():
    # 1. Création de l'instance du Catalogue
    catalogue = Catalogue()
    
    # 2. Conversion et Ajout des objets Produit au Catalogue
    for dictionnaire_produit in donnees_produits:
        nouveau_produit = Produit(
            id=dictionnaire_produit['id'],
            nom=dictionnaire_produit['nom'],
            categorie=dictionnaire_produit['categorie'],
            prix=dictionnaire_produit['prix'],
            stock=dictionnaire_produit['stock']
        )
        # Ajouter l'objet au catalogue
        catalogue.ajouter_produit(nouveau_produit)



    # Afficher le prix moyen
    prix_moyen = catalogue.prix_moyen()
    print(f"1. Prix moyen des produits : {prix_moyen:.2f}€")

    # Afficher la liste des ruptures
    ruptures = catalogue.produit_en_rupture()
    print("\n 2. Produits en rupture de stock :")
    if ruptures:
        for produit in ruptures:
            print(f"  - {produit.afficher_resume()}")
    else:
        print("Aucun produit en rupture.")
        
    # Afficher les produits de catégorie "Informatique"
    categorie_cible = "Informatique"
    produits_info = catalogue.produit_par_categorie(categorie_cible)
    print(f"\n 3. Produits de la catégorie '{categorie_cible}' :")
    for produit in produits_info:
        print(f"  - {produit.afficher_resume()}")

if __name__ == "__main__":
    main()