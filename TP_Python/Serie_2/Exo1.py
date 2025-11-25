password = str(input('Entrez le mot de passe : '))


if len(password) < 8:
    print("Le mot de passe doit contenir au moins 8 caractères.")
elif not any(char.isdigit() for char in password):
    print("Le mot de passe doit contenir au moins un chiffre.")
elif not any(char.isupper() for char in password):
    print("Le mot de passe doit contenir au moins une lettre majuscule.")
else:
    print("Mot de passe valide.")