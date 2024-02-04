import json


class ConfigReader:
    """
        ConfigReader class for reading configuration from a JSON file.

        Parameters:
        - path (str): The path to the JSON configuration file.

        Methods:
        - get_database_config() -> Tuple[str, str, str, str]:
          Extracts database connection information from the JSON file.

        - get_imports_config() -> str:
          Retrieves the path to the JSON file with import configurations.

        - get_export_config() -> str:
          Retrieves the path to the JSON file with export configurations.
        """

    def __init__(self, path):
        self.path = path

    def get_database_config(self):
        """
        Reads the JSON configuration file and returns database connection information.

        Returns:
        Tuple[str, str, str, str]: A tuple containing server_name, server_database, server_uid, and server_pwd.
        """
        with open(self.path, 'r') as reader:
            db_conn_data = json.load(reader)

        server_name = db_conn_data["database"]["server"]
        server_database = db_conn_data["database"]["DATABASE"]
        server_uid = db_conn_data["database"]["UID"]
        server_pwd = db_conn_data["database"]["PWD"]

        return server_name, server_database, server_uid, server_pwd

    def get_imports_config(self):
        """
        Reads the JSON configuration file and returns the path to the JSON file with import configurations.

        Returns:
        str: The path to the JSON file containing import configurations.
        """
        with open(self.path, "r") as reader:
            file_imports_data = json.load(reader)

        path_json = file_imports_data["imports_path"]["path_json"]

        return path_json

    def get_export_config(self):
        """
        Reads the JSON configuration file and returns the path to the JSON file with export configurations.

        Returns:
        str: The path to the JSON file for export configurations.
        """
        with open(self.path, "r") as reader:
            file_imports_data = json.load(reader)

        path_json = file_imports_data["export_path"]["path"]

        return path_json
