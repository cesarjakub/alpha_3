import sys
sys.path.append("..")
from db_classes import Specialization
from database_conn import DBConnection

class DAOSpecialization:
    """
    DAOSpecialization class for interacting with the database to retrieve Specialization information.

    Parameters:
    - specialization (Specialization): An instance of the Specialization class.

    Methods:
    - get_specialization() -> Union[str, List[Tuple]]:
      Retrieves the names of all specializations from the database.
    """
    def __init__(self, specialization: Specialization):
        self.specialization = specialization

    def get_specialization(self):
        """
        Retrieves the names of all specializations from the database.

        Returns:
        Either an error message or a list of specialization names.
        """
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