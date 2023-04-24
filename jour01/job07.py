class Livre:
    def __init__(self, titre: str = "", auteur: str = "", nbr_pages: int = 0):
        self.__titre = titre
        self.__auteur = auteur
        self.__nbr_pages = nbr_pages

    def get_titre(self):
        return self.__titre

    def get_auteur(self):
        return self.__auteur

    def get_nbr_pages(self):
        return self.__nbr_pages

    def set_titre(self, nouveau_titre):
        self.__titre = nouveau_titre

    def set_auteur(self, nouvel_auteur):
        self.__auteur = nouvel_auteur

    def set_nbr_pages(self, nouveau_nbr_pages):
        if not isinstance(nouveau_nbr_pages, int):
            print("Le nombre de pages doit être un entier positif.")
        else:
            self.__nbr_pages = nouveau_nbr_pages


Livre1 = Livre("Le rochet", "Marlène", 357)
# Afficher les données originales
print("Titre : ", Livre1.get_titre())
print("AUteur : ", Livre1.get_auteur())
print("Nombre de Pages : ", Livre1.get_nbr_pages())

# Modifier les données
Livre1.set_titre("L'arche")
Livre1.set_auteur("Daniel")
Livre1.set_nbr_pages(477)

# Afficher les nouvelles données
print("Le nouveau titre est :", Livre1.get_titre())
print("Le nouvel auteur est :", Livre1.get_auteur())
print("Le nouveau nombre de page est :", Livre1.get_nbr_pages())
