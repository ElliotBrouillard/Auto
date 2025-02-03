class Auto:
    """
    Classe auto qui permet de choisir une auto
    """
    def __init__(self, marque, modele, prix, nombre_portes, type_auto):
        self.marque = marque
        self.modele = modele
        self.prix = prix
        self.nombre_portes = nombre_portes
        self.type_auto = type_auto

    def se_deplacer(self):
        print("L'auto se déplace")



camry = Auto("Toyota", "Camry", 30000, 5, "berline")
camry.se_deplacer()