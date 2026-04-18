class Salle:
    def __init__(self, code, libelle, type_salle, capacite):
        self.code = code
        self.libelle = libelle
        self.type = type_salle
        self.capacite = capacite

    def afficher_infos(self):
        return f"Code: {self.code}, Libellé: {self.libelle}, Type: {self.type}, Capacité: {self.capacite}"