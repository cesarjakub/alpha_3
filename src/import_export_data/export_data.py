import os
import sys
sys.path.append("..")
from config_reader import ConfigReader
import json

class ExportData:
    def __init__(self):
        pass

    def export_data_from_json(self):
        conf = ConfigReader("../Config/config.json")
        path = conf.get_export_config()
        return path

    def export_into_file(self, data):
        with open(self.export_data_from_json(), "a") as writer:
            writer.write(data)

