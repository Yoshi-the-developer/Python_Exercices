def lire_fichier_securiser(nom_fichier):
    try:
        with open(nom_fichier, 'r') as f:
            contenu = f.read()
        print('Voter fichier est lu sans problème')
    except FileNotFoundError:
        print('Votre fichier n\'existe pas')
    return None

if __name__ == '__main__':
    lire_fichier_securiser('exo4.txt')