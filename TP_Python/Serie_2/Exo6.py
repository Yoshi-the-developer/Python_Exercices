commandes = []
cles = ["id", "client", "montant", "statut"]

try:
    with open('Exo6.txt', 'r', encoding='utf-8') as fichier:
        for ligne in fichier:
            ligne_nettoyee = ligne.strip()
            
            if ligne_nettoyee:
                elements = ligne_nettoyee.split(';')
                
                if len(elements) == 4:
                    
                    commande_dict = {}
                    
                    for cle, valeur in zip(cles, elements):
                        
                        if cle == "montant":
                            commande_dict[cle] = float(valeur)
                        elif cle == "id":
                            commande_dict[cle] = int(valeur)
                        else:
                            commande_dict[cle] = valeur
                            
                    commandes.append(commande_dict)
                else:
                    print(f"Ligne ignorée (mauvais format) : {ligne_nettoyee}")

except FileNotFoundError:
    print("Erreur: Le fichier 'commandes.txt' n'a pas été trouvé. Veuillez le créer.")
    exit()

print("\n Liste finale des commandes (dictionnaires) :")
for cmd in commandes:
    print(cmd)