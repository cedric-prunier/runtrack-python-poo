class Vehicule:
    def __init__(self, marque, annee, prix):
        self.marque = marque
        self.annee = annee
        self.prix = prix

    def informationsVehicule(self, modele):
        print("Marque :", self.marque)
        print("Modèle :", modele)
        print("Année :", self.annee)
        print("Prix :", self.prix)

    def demarrer():
        print("Attention, je roule.")


voiture = Vehicule("Audi", "2020", "13990")
voiture.informationsVehicule("A1")


class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix, portes=4):
        super().__init__(marque, annee, prix)
        self.modele = modele
        self.portes = portes

    def informationsVehicule(self):
        super().informationsVehicule(self.modele)
        print("Nombre de portes :", self.portes)

    def demarrer(self):
        print("Attention, la voiture roule.")


voiture2 = Voiture(
    "Audi",
    "A1",
    "2020",
    "13990",
)
voiture2.informationsVehicule()
voiture2.demarrer()


class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix, roue=2):
        super().__init__(marque, annee, prix)
        self.modele = modele
        self.roue = roue

    def informationsVehicule(self):
        super().informationsVehicule(self.modele)
        print("Nombre de roue :", self.roue)

    def demarrer(self):
        print("Attention, la moto roule.")


moto = Moto("Yamaha", "1200 Vmax", "1987", "4500")
moto.informationsVehicule()
moto.demarrer()
