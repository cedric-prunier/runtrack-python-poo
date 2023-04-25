class Personne:
    def __init__(self, age=14):
        if not isinstance(age, int):
            print("L'âge doit être un entier.")
        else:
            self.age = age

    def afficher_age(self):
        print("L'age de la personne est de", self.age, "ans")

    def bonjour(self):
        print("Hello")

    def modifier_age(self, nouvel_age):
        if not isinstance(nouvel_age, int):
            print("L'âge doit être un entier.")
        else:
            self.age = nouvel_age


personne1 = Personne()
personne1.afficher_age()
personne1.modifier_age(17.8)
personne1.afficher_age()

personne1.afficher_age()
personne1.modifier_age(37)
personne1.afficher_age()

personne1.bonjour()


class Eleve(Personne):
    def aller_en_cours(self):
        print("Je vais en cours")

    def affichage_age(self):
        print("J'ai", self.age, "ans")


eleve1 = Eleve


class Professeur:
    def __init__(self, matiere_enseignee):
        self.__matiere_enseignee = matiere_enseignee

    def enseigner(self):
        print("Le cours de", self.__matiere_enseignee, "va commencer")


prof1 = Professeur("mathématiques")
prof1.enseigner()

personne1 = Personne()
eleve1 = Eleve()

print("L'âge de l'élève est", eleve1.age)
eleve1.bonjour()
eleve1.aller_en_cours()

eleve1.modifier_age(15)
eleve1.affichage_age()
