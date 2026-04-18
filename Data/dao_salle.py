import json
import mysql.connector
from models.salle import Salle


class DataSalle:
    def get_connection(self):
        with open("Data/config.json", "r", encoding="utf-8") as file:
            config = json.load(file)
        return mysql.connector.connect(**config)

    def insert_salle(self, salle):
        conn = self.get_connection()
        cursor = conn.cursor()
        query = "INSERT INTO salle (code, libelle, type, capacite) VALUES (%s, %s, %s, %s)"
        values = (salle.code, salle.libelle, salle.type, salle.capacite)
        cursor.execute(query, values)
        conn.commit()
        cursor.close()
        conn.close()
