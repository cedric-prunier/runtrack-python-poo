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


class Eleve(Personne):
    def aller_en_cours(self):
        print("Je vais en cours")

    def affichage_age(self):
        print("J'ai", self.age, "ans")


class Professeur(Personne):
    def __init__(self, age, matiere_enseignee):
        super().__init__(age)
        self.__matiere_enseignee = matiere_enseignee

    def enseigner(self):
        print("Le cours de", self.__matiere_enseignee, "va commencer")


eleve1 = Eleve()

eleve1.bonjour()
eleve1.aller_en_cours()
eleve1.affichage_age()
eleve1.modifier_age(15)
eleve1.affichage_age()


prof1 = Professeur(40, "mathématiques")
prof1.bonjour()
prof1.enseigner()
