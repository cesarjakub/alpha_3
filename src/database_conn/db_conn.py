import pyodbc
import sys
sys.path.append("..")
from config_reader import ConfigReader

class DBConnection:
    """
    DBConnection class for handling database connections.

    Methods:
    - connect() -> pyodbc.Connection:
      Establishes a connection to the database using information from the configuration file.

    - close_connection():
      Closes the existing database connection.
    """
    connection = None

    @staticmethod
    def connect():
        """
        Establishes a connection to the database using information from the configuration file.

        Returns:
        pyodbc.Connection: A connection object to the database.
        """
        conf = ConfigReader("../Config/config.json")
        server_name, server_database, server_uid, server_pwd = conf.get_database_config()

        DBConnection.connection = pyodbc.connect(
            "DRIVER={ODBC Driver 17 for SQL Server};SERVER=" + server_name + ";DATABASE=" + server_database + ";UID=" + server_uid + ";PWD=" + server_pwd)

        return DBConnection.connection

    @staticmethod
    def close_connection():
        """
        Closes the existing database connection.
        """
        DBConnection.connection.close()