class Livre:
    def __init__(self, titre, auteur, nbr_pages: int):
        self.__titre = titre
        self.__auteur = auteur
        self.__nbr_pages = nbr_pages
        if nbr_pages < 0:
            print("Veuillez choisir un nombre de pages supérieur à 0")

    def get_titre(self):
        return self.__titre

    def get_auteur(self):
        return self.__auteur

    def get_nbr_pages(self):
        return self.__nbr_pages

    def set_titre(self, nouveau_titre):
        self.__largeur = nouveau_titre

    def set_auteur(self, nouvel_auteur):
        self.__largeur = nouvel_auteur

    def set_titre(self, nouveau_titre):
        self.__largeur = nouveau_titre
