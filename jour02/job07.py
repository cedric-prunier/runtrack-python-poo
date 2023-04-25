import random


class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

    def __str__(self):
        return f"{self.valeur} de {self.couleur}"


class Jeu:
    def __init__(self):
        valeurs = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        couleurs = ["Coeur", "Carreau", "Trefle", "Pique"]
        self.paquet = [
            Carte(valeur, couleur) for valeur in valeurs for couleur in couleurs
        ]
        random.shuffle(self.paquet)

    def tirer_carte(self):
        return self.paquet.pop()


def valeur_main(main):
    valeur = 0
    as_present = False
    for carte in main:
        if carte.valeur in ["J", "Q", "K"]:
            valeur += 10
        elif carte.valeur == "A":
            as_present = True
            valeur += 11
        else:
            valeur += int(carte.valeur)

    if as_present and valeur > 21:
        valeur -= 10

    return valeur


def afficher_main(main, joueur=True):
    print("Main du", "joueur" if joueur else "croupier")
    for carte in main:
        print(carte)
    print("Total:", valeur_main(main), "\n")


def jouer():
    jeu = Jeu()

    main_joueur = [jeu.tirer_carte(), jeu.tirer_carte()]
    main_croupier = [jeu.tirer_carte(), jeu.tirer_carte()]

    afficher_main(main_joueur)
    afficher_main(main_croupier, joueur=False)

    while True:
        choix = input("Voulez-vous prendre (P) ou passer (S)? ").upper()

        if choix == "P":
            main_joueur.append(jeu.tirer_carte())
            afficher_main(main_joueur)

            if valeur_main(main_joueur) > 21:
                print("Vous avez dépassé 21. Vous avez perdu.")
                return
        elif choix == "S":
            break
        else:
            print("Choix invalide. Veuillez entrer P ou S.")

    while valeur_main(main_croupier) < 17:
        main_croupier.append(jeu.tirer_carte())

    afficher_main(main_croupier, joueur=False)

    if valeur_main(main_croupier) > 21:
        print("Le croupier a dépassé 21. Vous avez gagné!")
    elif valeur_main(main_joueur) > valeur_main(main_croupier):
        print("Vous avez gagné!")
    else:
        print("Le croupier a gagné.")


if __name__ == "__main__":
    jouer()
