# Exercie 2
tva = float(input("Taux de TVA (%) : "))
prix_ht = float(input("Prix HT : "))

taux_tva = 20


tva = prix_ht * taux_tva / 100
prix_ttc = prix_ht + tva

print(f"Pour un prix de {prix_ht} € HT, la TVA est de {tva} € et le prix TTC est de {prix_ttc} €.")
