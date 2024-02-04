import uuid
import sys
sys.path.append("..")
from config_reader import ConfigReader

class ExportData:
    """
    ExportData class for exporting data to a file.

    Methods:
    - export_data_from_json() -> str:
      Retrieves the export path from the configuration file.

    - export_into_file(data: str):
      Exports the provided data into a file with a unique filename based on a UUID and the export path.
    """
    def __init__(self):
        pass

    def export_data_from_json(self):
        """
        Retrieves the export path from the configuration file.

        Returns:
        str: The export path.
        """
        conf = ConfigReader("../Config/config.json")
        path = conf.get_export_config()
        return path

    def export_into_file(self, data):
        """
        Exports the provided data into a file with a unique filename based on a UUID and the export path.

        Parameters:
        - data (str): The data to be exported.
        """
        uuid_timestamp = uuid.uuid1()
        with open(f"{self.export_data_from_json()}_{uuid_timestamp}.txt", "w", encoding="utf-8") as writer:
            writer.write(data)

