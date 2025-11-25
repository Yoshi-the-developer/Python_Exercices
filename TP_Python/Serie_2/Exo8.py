import json
with open("commandes.json", "r", encoding="utf-8") as file:
    commandes = json.load(file)




#--------------------------------------------
# Fonction 
#--------------------------------------------

def calculer_ca(commandes):
    ca = 0
    for commande in commandes:
        if commande["statut"] == "payee":
            ca += commande["montant"]
    return ca


def compter_commandes_par_statut(commandes):
    statut_count = {}
    for commande in commandes:
        statut = commande["statut"]
        if statut not in statut_count:
            statut_count[statut] = 0
        statut_count[statut] += 1
    return statut_count


def total_par_client(commandes):
    total_client = {}
    for commande in commandes:
        client = commande["client"]
        montant = commande["montant"]
        if client not in total_client:
            total_client[client] = 0
        total_client[client] += montant
    return total_client




# --------------------------------------------
# Affichage clair du tableau de bord des commandes
# ---------------------------------------------
print("=== Tableau de bord des commandes ===")
print(f"Chiffre d'affaire (commandes payées) : {calculer_ca(commandes):.2f} €")
print(f'Nombre de commandes par statut :')
print(f' - payee ', compter_commandes_par_statut(commandes).get("payee", 0))
print(f' - annulee ', compter_commandes_par_statut(commandes).get("annulee", 0))
print(f' - en_attente ', compter_commandes_par_statut(commandes).get("en_attente", 0))
print('Top Clients :')
# Trier les clients par montant croissant 
totaux_client = total_par_client(commandes)
clients_tries = sorted(totaux_client.items(), key=lambda x: x[1])
top_clients = clients_tries[:3]
for client, total in top_clients:
    print(f' - {client} : {total:.2f} €')
