def appliquer_remise(prix, remise):
    """
    Cette fonction permet de faire la remise sur un produit.

    :param prix: Montant du produit en question
    :param remise: Remise sur le prix du produit
    :return: Montant total après la remise appliqué
    """
    prix_final = prix * (1 - remise)
    return prix_final

def compter_commandes_superieures(commandes, seuil):
    """
    Cette fonction permet de compter les afin de gérer un stock

    :param commandes: Nombre de commande effectué
    :param seuil: Seuil a ne pas dépasser
    :return: Le nombre de commandes passée 
    """
    compteur = 0
    for montant in commandes:
        if montant >= seuil:
            compteur += 1
    return compteur

def normaliser_email(email):
    """
    Cette fonction permet de mettre en minuscule les emails

    :param email: Email de l'utilisateur
    :return: Renvoie l'email du user en minuscules. Sans majuscules
    """
    return email.strip().lower()

help(appliquer_remise)