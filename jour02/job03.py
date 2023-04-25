class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def perimetre(self):
        print("Périmètre:", (self.__longueur + self.__largeur) * 2)

    def surface(self):
        print("Surface:", self.__longueur * self.__largeur)

    def get_longueur(self):
        return self.__longueur

    def set_longueur(self, nouvelle_longueur):
        self.__longueur = nouvelle_longueur

    def get_largeur(self):
        return self.__largeur

    def set_largeur(self, nouvelle_largeur):
        self.__largeur = nouvelle_largeur


class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.__hauteur = hauteur

    def volume(self):
        print("Volume:", self.get_longueur() * self.get_largeur() * self.__hauteur)


rectangle = Rectangle(10, 14)
rectangle.perimetre()
rectangle.surface()
print(rectangle.get_longueur())
rectangle.set_longueur(12)
print(rectangle.get_longueur())

parallelepipede = Parallelepipede(10, 14, 7)
parallelepipede.volume()
