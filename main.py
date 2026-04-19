from Data.dao_salle import DataSalle
from models.salle import Salle

dao = DataSalle()

# Test connexion
conn = dao.get_connection()
print("Connexion réussie")
conn.close()

# Test ajout
s1 = Salle("A101", "Salle Alpha", "Cours", 30)
dao.insert_salle(s1)

# Test recherche
salle = dao.get_salle("A101")
if salle:
    print(salle.afficher_infos())

# Test modification
s1.libelle = "Salle Alpha Modifiée"
s1.type = "Laboratoire"
s1.capacite = 35
dao.update_salle(s1)

# Test affichage de toutes les salles
for s in dao.get_salles():
    print(s.afficher_infos())

# Test suppression
dao.delete_salle("A101")
print("Suppression effectuée")

from services.service_salle import ServiceSalle
from models.salle import Salle

service = ServiceSalle()

# Ajouter
ok, msg = service.ajouter_salle(Salle("B201", "Salle Beta", "Cours", 40))
print(msg)

# Modifier
ok, msg = service.modifier_salle(Salle("B201", "Salle Beta Modifiée", "Bureau", 25))
print(msg)

# Rechercher
salle = service.rechercher_salle("B201")
if salle:
    print(salle.afficher_infos())

# Afficher toutes les salles
for s in service.recuperer_salles():
    print(s.afficher_infos())

# Supprimer
ok, msg = service.supprimer_salle("B201")
print(msg)

