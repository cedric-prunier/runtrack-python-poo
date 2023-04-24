class Student:
    def __init__(self, prenom, nom, numero_etudiant, credits: int = 0):
        self.__nom = nom
        self.__prenom = prenom
        self.__numero_etudiant = numero_etudiant
        self.__credits = credits

    def get_prenom(self):
        return self.__prenom

    def get_nom(self):
        return self.__nom

    def get_credits(self):
        return self.__credits

    def set_add_credits(self, nouveau_credits):
        self.__credits = self.__credits + nouveau_credits

    def get_numero_etudiant(self):
        return self.__numero_etudiant

    def studentEval(self):
        if self.__credits >= 90:
            return "Excellent"
        if self.__credits >= 90:
            return "Excellent"
        if self.__credits >= 70:
            return "Bien"
        if self.__credits >= 60:
            return "Passable"
        if self.__credits < 60:
            return "Insuffisant"


etudiant = Student("John", "DOE", "1273", 0)


etudiant.set_add_credits(10)
etudiant.set_add_credits(10)
etudiant.set_add_credits(10)

print(
    "Le nombre de crédits de",
    etudiant.get_prenom(),
    etudiant.get_nom(),
    "est de",
    etudiant.get_credits(),
)

print(etudiant.studentEval())
