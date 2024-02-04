import sys
sys.path.append("..")
from config_reader import ConfigReader
import json

class ImportData:
    """
    ImportData class for importing data from a JSON file.

    Methods:
    - import_data_from_json() -> str:
      Retrieves the import path from the configuration file.

    - import_into() -> dict:
      Imports data from the specified JSON file and returns the loaded data as a dictionary.
    """
    def __init__(self):
        pass

    def import_data_from_json(self):
        """
        Retrieves the import path from the configuration file.

        Returns:
        str: The import path.
        """
        conf = ConfigReader("../Config/config.json")
        path = conf.get_imports_config()
        return path

    def import_into(self):
        """
        Imports data from the specified JSON file and returns the loaded data as a dictionary.

        Returns:
        dict: The imported data as a dictionary.
        """
        with open(self.import_data_from_json(), "r") as reader:
            data = json.load(reader)

        return data