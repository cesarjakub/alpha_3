import sys
sys.path.append("..")
from db_classes import Specialization
from database_conn import DBConnection

class DAOSpecialization:
    def __init__(self, specialization: Specialization):
        self.specialization = specialization

    def get_specialization(self):
        try:
            connection = DBConnection.connect()
            cursor = connection.cursor()
            query = "SELECT specialization.Name FROM specialization;"
            cursor.execute(query)
            records = cursor.fetchall()
            return records
        except Exception:
            return "Something went wrong"
        finally:
            DBConnection.close_connection()