class Livre:
    def __init__(
        self, titre: str = "", auteur: str = "", nbr_pages: int = 0, disponible=True
    ):
        self.__titre = titre
        self.__auteur = auteur
        self.__nbr_pages = nbr_pages
        self.__disponible = disponible

    def get_titre(self):
        return self.__titre

    def get_auteur(self):
        return self.__auteur

    def get_nbr_pages(self):
        return self.__nbr_pages

    def get_verification(self):
        if self.__disponible == True:
            return "Ce livre est disponible"
        else:
            return "Ce livre n'est pas disponible"

    def get_emprunter(self):
        if self.__disponible:
            self.__disponible = False
            return "Ce livre a été emprunté."
        else:
            return "Ce livre n'est pas disponible pour l'emprunt."

    def set_rendre(self):
        if not self._disponible:
            self._disponible = True
            return "Ce livre a été rendu"
        else:
            return "Ce livre n'a pas été emprunté ou a déjà été rendu"

    def set_titre(self, nouveau_titre):
        self.__titre = nouveau_titre

    def set_auteur(self, nouvel_auteur):
        self.__auteur = nouvel_auteur

    def set_nbr_pages(self, nouveau_nbr_pages):
        if nouveau_nbr_pages < 0:
            print("Veuillez choisir un nombre de pages supérieur à 0")
        else:
            self.__nbr_pages = nouveau_nbr_pages


Livre1 = Livre("Le rochet", "Marlène", 357, True)
Livre2 = Livre("Le rochet", "Marlène", 357, False)

# Afficher les données originales
print("Titre : ", Livre1.get_titre())
print("Auteur : ", Livre1.get_auteur())
print("Nombre de Pages : ", Livre1.get_nbr_pages())
print(Livre1.get_verification())
print(Livre1.get_emprunter())

print(Livre2.get_verification())
print(Livre2.get_emprunter())
