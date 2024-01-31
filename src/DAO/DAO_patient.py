import sys
sys.path.append("..")
from db_classes import Patient

class DAOPatient:
    def __init__(self, patient: Patient):
        self.patient = patient