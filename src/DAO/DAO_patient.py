import sys
sys.path.append("..")
from db_classes import Patient
from database_conn import DBConnection

class DAOPatient:
    """
    DAOPatient class for interacting with the database to perform CRUD operations on Patient entities.

    Parameters:
    - patient (Patient): An instance of the Patient class.

    Methods:
    - create_patient(first_name: str, last_name: str, date_of_Birth: str, address: str, health_insurance_number: str) -> str:
      Creates a new Patient in the database with the provided information.
    """
    def __init__(self, patient: Patient):
        self.patient = patient

    def create_patient(self, first_name, last_name, date_of_Birth, address, health_insurance_number):
        """
        Creates a new Patient in the database with the provided information.

        Parameters:
        - first_name (str): The first name of the patient.
        - last_name (str): The last name of the patient.
        - date_of_Birth (str): The date of birth of the patient.
        - address (str): The address of the patient.
        - health_insurance_number (str): The health insurance number of the patient.

        Returns:
        str: A message indicating the success or failure of the operation.
        """
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