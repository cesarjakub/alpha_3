import sys
sys.path.append("..")
from config_reader import ConfigReader
import json

class ImportData:
    def __init__(self):
        pass

    def import_data_from_json(self):
        conf = ConfigReader("../Config/config.json")
        path = conf.get_imports_config()
        return path

    def import_into_medicine(self):
        with open(self.import_data_from_json(), "r") as reader:
            data = json.load(reader)

        return data