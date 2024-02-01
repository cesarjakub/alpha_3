import uuid
import sys
sys.path.append("..")
from config_reader import ConfigReader

class ExportData:
    def __init__(self):
        pass

    def export_data_from_json(self):
        conf = ConfigReader("../Config/config.json")
        path = conf.get_export_config()
        return path

    def export_into_file(self, data):
        uuid_timestamp = uuid.uuid1()
        with open(f"{self.export_data_from_json()}_{uuid_timestamp}.txt", "w", encoding="utf-8") as writer:
            writer.write(data)

