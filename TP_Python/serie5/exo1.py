utilisateur = {
    "nom": "Alice",
    "email": "alice@example.com",
    "age": 30
}

# =============================
# Méthode LBLY 
# =============================

def get_age_lbly(utilisateur):
    if "age" in utilisateur:
        return utilisateur["age"]
    else:
        print('La clé n\'existe pas')
    return None

# =============================
# Méthode EAFP
# =============================

def get_age_eafp(utilisateur):
    try:
        return utilisateur["age"]
    except KeyError:
        print("La clé existe pas")
        return None

# =============================
# Bloc de Test
# =============================
if __name__ == '__main__':
    print('=' * 15)
    print('Méthode LBLY')
    print('=' * 15)
    age_alice_lbly = get_age_lbly(utilisateur)
    print(f"Age de Alice : {age_alice_lbly}")

    # Méthode EAFP
    age_alice_eafp = get_age_eafp(utilisateur)
    print('=' * 15)
    print('Méthode EAFP')
    print('=' * 15)
    print(f"Age de Alice {age_alice_eafp}")