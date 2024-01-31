import sys
sys.path.append("..")
from db_classes import Doctor

class DAODoctor:
    def __init__(self, doctor: Doctor):
        self.doctor = doctor