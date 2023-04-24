class Personne:
    def __init__(self, prenom: str = "", nom: str = ""):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        info_personne = "Je suis " + self.prenom + " " + self.nom
        print(info_personne)


personne1 = Personne("John", "Doe")
personne2 = Personne("Jean", "Dupond")

personne1.SePresenter()
personne2.SePresenter()
