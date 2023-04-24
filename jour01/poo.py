def afficher_info_perso(nom, age):
    print("La personne s'appelle {nom},son age est {age} ans".format(nom=nom, age=age))


def demander_nom():
    nom = input("Quel est votre nom ?")
    return nom


# Personne (entité --> class)
#     Données: un nom, age
#     Actions: (méthodes) --> = fonctions
#        - Se présenter()
#        - Demander nom()/input

"""nom1 = "Jean"
age1 = 30

nom2 = "Paul"
age2 = 25

nom3 = demander_nom()
age3 = 18

afficher_info_perso(nom1, age1)
afficher_info_perso(nom2, age2)
afficher_info_perso(nom3, age3)"""


# ---Définition----
class Personne:
    def __init__(self, nom: str = "", age: int = 0):
        self.nom = nom  # crée une variable d'instance: nom
        self.age = age
        if nom == "":
            self.DemanderNom()

        print("Constructeur personne " + nom)

    def se_presenter(self):
        info_personne = "je m'appelle " + self.nom
        if self.age != 0:
            info_personne += "j'ai " + str(self.age) + " ans"

        print(info_personne)

        if self.age != 0:
            if self.EstMajeur():
                print("Je suis majeur ")
            else:
                print("Je suis mineur")

    def EstMajeur(self):
        return self.age >= 18

    def DemanderNom(self):
        self.nom = input("Nom de la personne: ")


# ---Utilisation---
personne1 = Personne(
    "Jean", 30
)  # Je crée une personne --> personne1 est une instance de la classe personne
personne2 = Personne(
    "Paul", 15
)  # Je crée une personne --> personne1 est une instance de la classe personne

personne3 = Personne()
personne4 = Personne()


personne1.se_presenter()  # Je crée une personne
personne2.se_presenter()  # Je crée une personne
personne3.se_presenter()  # Je crée une personne
personne4.se_presenter()  # Je crée une personne
