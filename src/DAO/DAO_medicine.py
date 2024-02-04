import sys
sys.path.append("..")
from db_classes import Medicine
from database_conn import DBConnection

class DAOMedicine:
    """
    DAOMedicine class for interacting with the database to perform CRUD operations on Medicine entities.

    Parameters:
    - medicine (Medicine): An instance of the Medicine class.

    Methods:
    - create_medicine(manufacturer_name: str, medicine_name: str, Amount: float, Dosage: str, Payment: float) -> str:
      Creates a new Medicine in the database with the provided information.
    """
    def __init__(self, medicine: Medicine):
        self.medicine = medicine

    def create_medicine(self, manufacturer_name, medicine_name, Amount, Dosage, Payment):
        """
        Creates a new Medicine in the database with the provided information.

        Parameters:
        - manufacturer_name (str): The name of the manufacturer of the medicine.
        - medicine_name (str): The name of the medicine.
        - Amount (float): The amount of the medicine.
        - Dosage (str): The dosage information of the medicine.
        - Payment (float): The payment associated with the medicine.

        Returns:
        str: A message indicating the success or failure of the operation.
        """
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