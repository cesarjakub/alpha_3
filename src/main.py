import pyodbc
from config_reader import ConfigReader
import time
from three_tier import Application
from three_tier import Presentation

def main():
    """
    app = Application()

    presentation = Presentation()
    presentation.application = app
    app.presentation = presentation

    app.run()
    """
    conf = ConfigReader("../Config/config.json")
    server_name, server_database, server_uid, server_pwd = conf.get_database_config()
    path_csv, path_json = conf.get_imports_config()
    print(path_csv, "\n", path_json)

    connection = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};SERVER="+server_name+";DATABASE="+server_database+";UID="+server_uid+";PWD="+server_pwd)

    print("Připojeno.")

    connection.close()


if __name__ == '__main__':
    main()