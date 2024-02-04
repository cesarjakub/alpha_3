import sys
sys.path.append("..")
from db_classes import EPrescription
from database_conn import DBConnection

class DAOEPrescription:
    """
    DAOEPrescription class for interacting with the database to perform CRUD operations on EPrescription entities.

    Parameters:
    - eprescription (EPrescription): An instance of the EPrescription class.

    Methods:
    - update_prescription(e_id: int, first_name: str, last_name: str, patientDOB: str, medicine_name: str, doctor_first_name: str, doctor_last_name: str, issued: str, validity: str) -> str:
      Updates an existing prescription in the database with the provided information.

    - create_prescription(first_name: str, last_name: str, patientDOB: str, medicine_name: str, doctor_first_name: str, doctor_last_name: str, issued: str, validity: str) -> str:
      Creates a new prescription in the database with the provided information.

    - get_prescription_by_id(e_id: int) -> Tuple[Union[str, List[Tuple]], int]:
      Retrieves the details of a prescription based on its ID.

    - delete_prescription_by_id(e_id: int) -> str:
      Deletes a prescription from the database based on its ID.

    - get_just_ids() -> Union[str, List[Tuple]]:
      Retrieves only the IDs of all EPrescriptions in the database.
    """
    def __init__(self, eprescription: EPrescription):
        self.eprescription = eprescription

    def update_prescription(self, e_id, first_name, last_name, patientDOB, medicine_name, doctor_first_name, doctor_last_name, issued, validity):
        """
        Updates an existing prescription in the database with the provided information.

        Parameters:
        - e_id (int): The ID of the EPrescription to be updated.
        - first_name (str): The first name of the patient.
        - last_name (str): The last name of the patient.
        - patientDOB (str): The date of birth of the patient.
        - medicine_name (str): The name of the prescribed medicine.
        - doctor_first_name (str): The first name of the prescribing doctor.
        - doctor_last_name (str): The last name of the prescribing doctor.
        - issued (str): The date the prescription was issued.
        - validity (str): The validity period of the prescription.

        Returns:
        str: A message indicating the success or failure of the operation.
        """
        try:
            connection = DBConnection.connect()
            cursor = connection.cursor()
            query = "EXEC Update_prescription ?, ?, ?, ?, ?, ?, ?, ?, ?;"
            values = (e_id, first_name, last_name, patientDOB, medicine_name, doctor_first_name, doctor_last_name, issued, validity)
            cursor.execute(query, values)
            cursor.commit()
            return "Prescription updated successfully"
        except:
            return "Something went wrong"
        finally:
            DBConnection.close_connection()

    def create_prescription(self, first_name, last_name, patientDOB, medicine_name, doctor_first_name, doctor_last_name, issued, validity):
        """
        Creates a new prescription in the database with the provided information.

        Parameters:
        - first_name (str): The first name of the patient.
        - last_name (str): The last name of the patient.
        - patientDOB (str): The date of birth of the patient.
        - medicine_name (str): The name of the prescribed medicine.
        - doctor_first_name (str): The first name of the prescribing doctor.
        - doctor_last_name (str): The last name of the prescribing doctor.
        - issued (str): The date the prescription was issued.
        - validity (str): The validity period of the prescription.

        Returns:
        str: A message indicating the success or failure of the operation.
        """
        try:
            connection = DBConnection.connect()
            cursor = connection.cursor()
            query = "EXEC Create_prescription ?, ?, ?, ?, ?, ?, ?, ?;"
            values = (first_name, last_name, patientDOB, medicine_name, doctor_first_name, doctor_last_name, issued, validity)
            cursor.execute(query, values)
            cursor.commit()
            return "Prescription created successfully"
        except:
            return "Something went wrong"
        finally:
            DBConnection.close_connection()

    def get_prescription_by_id(self, e_id):
        """
        Retrieves the details of a prescription based on its ID.

        Parameters:
        - e_id (int): The ID of the EPrescription to be retrieved.

        Returns:
        A tuple containing either an error message or a list of prescription records and the number of records.
        """
        try:
            connection = DBConnection.connect()
            cursor = connection.cursor()
            query = "SELECT * FROM EPrescriptionView WHERE e_ID = ?;"
            cursor.execute(query, (e_id,))
            records = cursor.fetchall()
            return records, cursor.rowcount
        except Exception:
            return "Something went wrong"
        finally:
            DBConnection.close_connection()

    def delete_prescription_by_id(self, e_id):
        """
        Deletes a prescription from the database based on its ID.

        Parameters:
        - e_id (int): The ID of the EPrescription to be deleted.

        Returns:
        str: A message indicating the success or failure of the operation.
        """
        try:
            connection = DBConnection.connect()
            cursor = connection.cursor()
            query = "DELETE FROM eprescription WHERE ID = ?;"
            cursor.execute(query, (e_id,))
            cursor.commit()
            return "The e-prescription has been successfully deleted"
        except:
            return "Something went wrong"
        finally:
            DBConnection.close_connection()

    def get_just_ids(self):
        """
        Retrieves only the IDs of all EPrescriptions in the database.

        Returns:
        Either an error message or a list of EPrescription IDs.
        """
        try:
            connection = DBConnection.connect()
            cursor = connection.cursor()
            query = "SELECT e_ID FROM EPrescriptionView;"
            cursor.execute(query)
            records = cursor.fetchall()
            return records
        except Exception:
            return "Something went wrong"
        finally:
            DBConnection.close_connection()