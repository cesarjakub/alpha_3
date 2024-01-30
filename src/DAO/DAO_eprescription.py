from ..db_classes import EPrescription

class DAOEPrescription:
    def __init__(self, eprescription: EPrescription):
        self.eprescription = eprescription