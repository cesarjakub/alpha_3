import sys
sys.path.append("..")
from db_classes import Patient
from database_conn import DBConnection

class DAOPatient:
    def __init__(self, patient: Patient):
        self.patient = patient

    def create_patient(self, first_name, last_name, date_of_Birth, address, health_insurance_number):
        try:
            connection = DBConnection.connect()
            cursor = connection.cursor()
            query = "EXEC Create_patient ?, ?, ?, ?, ?;"
            values = (first_name, last_name, date_of_Birth, address, health_insurance_number)
            cursor.execute(query, values)
            cursor.commit()
            return "Patient created successfully"
        except:
            return "Something went wrong"
        finally:
            DBConnection.close_connection()