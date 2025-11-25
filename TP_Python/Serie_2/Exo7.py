import json 


#--------------------------------------------
# JSON
#--------------------------------------------

commandes = [
    {"id": 1, "client": "alice@example.com",  "montant": 49.90, "statut": "payee"},
    {"id": 2, "client": "bob@example.com",    "montant": 15.00, "statut": "annulee"},
    {"id": 3, "client": "alice@example.com",  "montant": 19.90, "statut": "payee"},
    {"id": 4, "client": "charlie@example.com","montant": 120.0, "statut": "en_attente"},
    {"id": 5, "client": "bob@example.com",    "montant": 35.0,  "statut": "payee"},
]

with open("commandes.json", 'w', encoding='utf-8') as f:
    json_str = json.dumps(commandes, indent=2, ensure_ascii=False)
    f.write(json_str)
print("Données JSON écrites dans Exo7.json")

print('----------------------------')

with open("commandes.json", 'r', encoding='utf-8') as f:
    commandes_lues = json.load(f)

print(type(commandes_lues), len(commandes_lues))



#--------------------------------------------
# Fonction 
#--------------------------------------------

def calculer_ca(commandse):
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

print('-----------------------------')
print("Chiffre d'affaires total des commandes", calculer_ca(commandes))
print('-----------------------------')
print("Nombre de commandes par statut :", compter_commandes_par_statut(commandes))
print('-----------------------------')
print("Total des commandes par client :", total_par_client(commandes))
print('-----------------------------')
