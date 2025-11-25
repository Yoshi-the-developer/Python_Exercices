import os

# --- Définition des fichiers pour le test ---
NOM_FICHIER_EXISTANT = "exo2.txt"
NOM_FICHIER_INEXISTANT = "test_inexistant.txt"

# ==================================
# 1. Méthode LBYL 
# ==================================

def lire_fichier_lbyl(nom_fichier):
    """Vérifie l'existence du fichier avant de tenter de le lire."""
    
    # Vérification de l'existence du fichier.
    if os.path.exists(nom_fichier):
        try:
            # Si le fichier existe, on l'ouvre et on lit son contenu
            with open(nom_fichier, 'r', encoding='utf-8') as f:
                contenu = f.read()
                return contenu
        except FileNotFoundError:
            # La clé manque : afficher le message et retourner None
            print(f"LBYL: Fichier manquant trouvé pour : {nom_fichier}")
            return None

# ==================================
# 2. Méthode EAFP (Easier to Ask for Forgiveness than Permission)
# ==================================

def lire_fichier_eafp(nom_fichier):
    """Tente d'ouvrir le fichier et gère l'exception en cas d'échec."""
    
    # EAFP : On essaie directement l'opération critique.
    try:
        with open(nom_fichier, 'r', encoding='utf-8') as f:
            contenu = f.read()
            return contenu
            
    # On intercepte spécifiquement l'erreur de fichier introuvable.
    except FileNotFoundError:
        print(f"EAFP: Fichier introuvable géré pour : {nom_fichier}")
        return None

# ==================================
# 3. Test des fonctions
# ==================================

if __name__ == '__main__':
    
    # --- Test 1 : Fichier Existant (devrait retourner le contenu) ---
    print("\n--- TEST AVEC FICHIER EXISTANT ---")
    
    contenu_lbyl_exist = lire_fichier_lbyl(NOM_FICHIER_EXISTANT)
    print(f"[LBYL] Contenu lu (début): {contenu_lbyl_exist}...")
    
    contenu_eafp_exist = lire_fichier_eafp(NOM_FICHIER_EXISTANT)
    print(f"[EAFP] Contenu lu (début): {contenu_eafp_exist}...")
    
    # --- Test 2 : Fichier Inexistant (devrait retourner None) ---
    print("\n--- TEST AVEC FICHIER INEXISTANT ---")
    
    contenu_lbyl_inexist = lire_fichier_lbyl(NOM_FICHIER_INEXISTANT)
    print(f"[LBYL] Résultat : {contenu_lbyl_inexist}")
    
    contenu_eafp_inexist = lire_fichier_eafp(NOM_FICHIER_INEXISTANT)
    print(f"[EAFP] Résultat : {contenu_eafp_inexist}")