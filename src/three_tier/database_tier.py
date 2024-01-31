import sys
sys.path.append("..")
from DAO import DAOEPrescription
from db_classes import EPrescription

class Database:
    def __init__(self):
        self.daoeprescription = DAOEPrescription(EPrescription())

    # first option
    def get_prescription_by_id(self, e_id):
        prescription_list = list()
        prescription, rowcount = self.daoeprescription.get_prescription_by_id(e_id)
        prescription_list = prescription

        return prescription_list, rowcount

    def get_just_ids(self):
        ids = self.daoeprescription.get_just_ids()

        return ids