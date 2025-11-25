# Exercice 6
def est_pair(n):
    return n % 2 == 0

def calc_tva(prix_ht, taux_tva):
    tva = prix_ht * taux_tva / 100
    prix_ttc = prix_ht + tva
    return tva, prix_ttc

def moyenne(liste):
    if len(liste) == 0:
        return 0
    return sum(liste) / len(liste)