import pyodbc
from config_reader import ConfigReader

def main():

    conn = ConfigReader("../Config/config.json")
    server_name, server_database, server_uid, server_pwd = conn.get_database_config()

    connection = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};SERVER="+server_name+";DATABASE="+server_database+";UID="+server_uid+";PWD="+server_pwd)

    print("Připojeno.")

    connection.close()


if __name__ == '__main__':
    main()