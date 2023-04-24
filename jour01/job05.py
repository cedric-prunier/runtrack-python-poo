class Animal:
    def __init__(self, age: int = 0, prenom: str = ""):
        self.age = age
        self.prenom = prenom

    def age_animal(self):
        print("L'âge de l'animal", self.age, "ans")

    def vieillir(self):
        print("L'âge de l'animal", self.age + 1, "ans")

    def nommer(self):
        print("L'animal se nomme", self.prenom)


animal1 = Animal(0, "Jean")

animal1.age_animal()
animal1.vieillir()
animal1.nommer()
