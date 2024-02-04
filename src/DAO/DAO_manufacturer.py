import sys
sys.path.append("..")
from db_classes import Manufacturer
from database_conn import DBConnection


class DAOManufacturer:
    """
    DAOManufacturer class for interacting with the database to retrieve Manufacturer information.

    Parameters:
    - manufacturer (Manufacturer): An instance of the Manufacturer class.

    Methods:
    - get_manufacturer() -> Union[str, List[Tuple]]:
      Retrieves the names of all manufacturers from the database.
    """
    def __init__(self, manufacturer: Manufacturer):
        self.manufacturer = manufacturer

    def get_manufacturer(self):
        """
        Retrieves the names of all manufacturers from the database.

        Returns:
        Either an error message or a list of manufacturer names.
        """
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