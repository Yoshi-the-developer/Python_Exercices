class Rectangle: 
    """
    Represente un rectangle définit par la largeur et hauteur.
    Fournit son air et son périmetre
    """

    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
    
    def surface(self):
        """ Retourne l'air du rectangle """ 
        return self.largeur * self.hauteur
    
    def perimetre(self):
        """ Retourne le périmetre du rectangle """
        return 2 * (self.largeur * self.hauteur)
    
    def afficher(self):
        """ Afficher les resultats des dimensino et de la surface """
        air = self.surface()
        perimetre = self.perimetre()

        print('-' * 10)
        print('Inforamtion du rectangle')
        print('-' * 10)

        print(f"largeur du rect : {self.largeur} / Hauteur du rect : {self.hauteur}")

        print('\n')

        print('-' * 10)
        print('Surface du rectangle')
        print('-' * 10)

        print(f'Surface : {air}')

        print('\n')

        print('-' * 10)
        print('Périmetre du rectangle')
        print('-' * 10)

        print(f'Périmetre : {perimetre}')


if __name__ == '__main__':
    rect1 = Rectangle(largeur=4, hauteur=10)
    rect2 = Rectangle(largeur=10, hauteur=15)

    print('Rectange 1 : ')
    rect1.afficher()

    # print('Rectangle 2 : ')
    # rect2.afficher()