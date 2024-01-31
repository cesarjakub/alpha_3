import pyodbc
import sys
sys.path.append("..")
from config_reader import ConfigReader

class DBConnection:
    connection = None

    @staticmethod
    def connect():
        conf = ConfigReader("../Config/config.json")
        server_name, server_database, server_uid, server_pwd = conf.get_database_config()

        DBConnection.connection = pyodbc.connect(
            "DRIVER={ODBC Driver 17 for SQL Server};SERVER=" + server_name + ";DATABASE=" + server_database + ";UID=" + server_uid + ";PWD=" + server_pwd)

        return DBConnection.connection

    @staticmethod
    def close_connection():
        DBConnection.connection.close()