import sys
sys.path.append("..")
from db_classes import Medicine
from database_conn import DBConnection

class DAOMedicine:
    def __init__(self, medicine: Medicine):
        self.medicine = medicine

    def create_medicine(self, manufacturer_name, medicine_name, Amount, Dosage, Payment):
        try:
            connection = DBConnection.connect()
            cursor = connection.cursor()
            query = "EXEC Create_medicine ?, ?, ?, ?, ?;"
            values = (manufacturer_name, medicine_name, Amount, Dosage, Payment)
            cursor.execute(query, values)
            cursor.commit()
            return "Medicine created successfully"
        except Exception:
            return f"Something went wrong"
        finally:
            DBConnection.close_connection()