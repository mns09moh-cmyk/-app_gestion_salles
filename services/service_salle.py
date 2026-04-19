from Data.dao_salle import DataSalle
class ServiceSalle:
    def __init__(self):
        self.dao_salle = DataSalle()

    def ajouter_salle(self, salle):
        if not salle.code or not salle.libelle or not salle.type or salle.capacite == "":
            return False, "Tous les champs sont obligatoires."

        try:
            capacite = int(salle.capacite)
        except ValueError:
            return False, "La capacité doit être un nombre."

        if capacite < 1:
            return False, "La capacité doit être supérieure ou égale à 1."

        salle.capacite = capacite

        if self.dao_salle.get_salle(salle.code):
            return False, "Une salle avec ce code existe déjà."

        self.dao_salle.insert_salle(salle)
        return True, "Salle ajoutée avec succès."