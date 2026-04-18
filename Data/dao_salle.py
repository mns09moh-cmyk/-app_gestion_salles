import json
import mysql.connector
from models.salle import Salle


class DataSalle:
    def get_connection(self):
        with open("Data/config.json", "r", encoding="utf-8") as file:
            config = json.load(file)
        return mysql.connector.connect(**config)