import sys
sys.path.append("..")
from db_classes import Manufacturer

class DAOManufacturer:
    def __init__(self, manufacturer: Manufacturer):
        self.manufacturer = manufacturer