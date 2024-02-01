import json


class ConfigReader:
    def __init__(self, path):
        self.path = path

    def get_database_config(self):
        with open(self.path, 'r') as reader:
            db_conn_data = json.load(reader)

        server_name = db_conn_data["database"]["server"]
        server_database = db_conn_data["database"]["DATABASE"]
        server_uid = db_conn_data["database"]["UID"]
        server_pwd = db_conn_data["database"]["PWD"]

        return server_name, server_database, server_uid, server_pwd

    def get_imports_config(self):
        with open(self.path, "r") as reader:
            file_imports_data = json.load(reader)

        path_json = file_imports_data["imports_path"]["path_json"]

        return path_json

    def get_export_config(self):
        with open(self.path, "r") as reader:
            file_imports_data = json.load(reader)

        path_json = file_imports_data["export_path"]["path"]

        return path_json
