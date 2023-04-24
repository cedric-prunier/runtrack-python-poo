class Voiture:
    def __init__(
        self, marque, modele, annee, kilometrage, reservoir=0, en_marche=False
    ):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = en_marche
        self.__reservoir = reservoir

    def get_marque(self):
        return self.__marque

    def set_marque(self, nouvelle_marque):
        self.__marque = nouvelle_marque

    def get_modele(self):
        return self.__modele

    def set_modele(self, nouveau_modele):
        self.__modele = nouveau_modele

    def get_annee(self):
        return self.__annee

    def set_annee(self, nouvelle_annee):
        self.__annee = nouvelle_annee

    def get_kilometrage(self):
        return self.__kilometrage

    def set_kilometrage(self, nouveau_kilometrage):
        self.__kilometrage = nouveau_kilometrage

    def get_en_marche(self):
        return self.__en_marche

    def set_en_marche(self, nouveau):
        self.__en_marche = self.__en_marche + nouveau

    def set_demarrer(self):
        self.__en_marche = False

    def set_arreter(self):
        self.__en_marche = True
