commandes = [
    {"id": 1, "client": "alice@example.com",  "montant": 49.90, "statut": "payee"},
    {"id": 2, "client": "bob@example.com",    "montant": 15.00, "statut": "annulee"},
    {"id": 3, "client": "alice@example.com",  "montant": 19.90, "statut": "payee"},
    {"id": 4, "client": "charlie@example.com","montant": 120.0, "statut": "en_attente"},
    {"id": 5, "client": "bob@example.com",    "montant": 35.0,  "statut": "payee"},
]

def total_payee(commandes):
    total = 0
    for commande in commandes:
        if commande["statut"] == "payee":
            total += commande["montant"]
    return total

print("Total des commandes payées :", total_payee(commandes))
print('-----------------------------')


def commande_by_status(commandes, statut):
    payee = 0
    annulee = 0
    en_attente = 0

    for i in range(len(commandes)):
        if commandes[i]["statut"] == "payee":
            payee += 1
        elif commandes[i]["statut"] == "annulee":
            annulee += 1
        elif commandes[i]["statut"] == "en_attente":
            en_attente += 1
    return f"Payée: {payee}, Annulée: {annulee}, En attente: {en_attente}"

print(commande_by_status(commandes, "statut"))

print('-----------------------------')

def total_by_client(commandes):
    total = {}

    for commande in commandes:
        client = commande["client"]
        montant = commande["montant"]

        if client not in total:
            total[client] = 0
        
        total[client] += montant

    return total

# Test de al fonction total par client 
print(total_by_client(commandes))