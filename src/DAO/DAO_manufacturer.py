import sys
sys.path.append("..")
from db_classes import Manufacturer
from database_conn import DBConnection


class DAOManufacturer:
    def __init__(self, manufacturer: Manufacturer):
        self.manufacturer = manufacturer

    def get_manufacturer(self):
        try:
            connection = DBConnection.connect()
            cursor = connection.cursor()
            query = "SELECT manufacturer.Name FROM manufacturer;"
            cursor.execute(query)
            records = cursor.fetchall()
            return records
        except Exception:
            return "Something went wrong"
        finally:
            DBConnection.close_connection()