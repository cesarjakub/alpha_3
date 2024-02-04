import sys
sys.path.append("..")
from db_classes import Doctor
from database_conn import DBConnection

class DAODoctor:
    """
    DAODoctor class for interacting with the database to perform CRUD operations on Doctor entities.

    Parameters:
    - doctor (Doctor): An instance of the Doctor class.

    Methods:
    - create_doctor(spec_name: str, first_name: str, last_name: str, title: str, date_of_birth: str, tel: str) -> str:
      Creates a new Doctor in the database with the provided information.
    """
    def __init__(self, doctor: Doctor):
        self.doctor = doctor

    def create_doctor(self, spec_name, first_name, last_name, title, date_of_birth, tel):
        """
        Creates a new Doctor in the database with the provided information.

        Parameters:
        - spec_name (str): The specialization name of the doctor.
        - first_name (str): The first name of the doctor.
        - last_name (str): The last name of the doctor.
        - title (str): The title of the doctor.
        - date_of_birth (str): The date of birth of the doctor.
        - tel (str): The telephone number of the doctor.

        Returns:
        str: A message indicating the success or failure of the operation.
        """
        try:
            connection = DBConnection.connect()
            cursor = connection.cursor()
            query = "EXEC Create_doctor  @SpecializationName = ?, @FirstName = ?, @LastName = ?, @Title = ?, @DateOfBirth = ?, @Telephone = ?;"
            values = (spec_name, first_name, last_name, title, date_of_birth, tel)
            cursor.execute(query, values)
            cursor.commit()
            return "Doctor created successfully"
        except:
            return "Something went wrong"
        finally:
            DBConnection.close_connection()