class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def get_longueur(self):
        return self.__longueur

    def set_longueur(self, nouvelle_longueur):
        self.__longueur = nouvelle_longueur

    def get_largeur(self):
        return self.__largeur

    def set_largeur(self, nouvelle_largeur):
        self.__largeur = nouvelle_largeur


# attribution des valeurs initiales du rectangle
dimension = Rectangle(10, 5)

# Afficher la longueur
print("Longueur : ", dimension.get_longueur())

# Modifier longueur
dimension.set_longueur(12)

# Afficher nouvelle longueur
print("Nouvelle longueur : ", dimension.get_longueur())

# Afficher largeur
print("Largeur : ", dimension.get_largeur())

# Modifier largeur
dimension.set_largeur(7)

# Afficher nouvelle largeur
print("Nouvelle largeur : ", dimension.get_largeur())
