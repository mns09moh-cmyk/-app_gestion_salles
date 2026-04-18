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

    def update_salle(self, salle):
        conn = self.get_connection()
        cursor = conn.cursor()
        query = "UPDATE salle SET libelle=%s, type=%s, capacite=%s WHERE code=%s"
        values = (salle.libelle, salle.type, salle.capacite, salle.code)
        cursor.execute(query, values)
        conn.commit()
        cursor.close()
        conn.close()

    def delete_salle(self, code):
        conn = self.get_connection()
        cursor = conn.cursor()
        query = "DELETE FROM salle WHERE code=%s"
        cursor.execute(query, (code,))
        conn.commit()
        cursor.close()
        conn.close()