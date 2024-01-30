class EPrescription:
    def __init__(self, ID=None, patient_ID=None, medicine_ID=None, doctor_ID=None, Issued=None, Validity=None):
        self.ID = ID
        self.patient_ID = patient_ID
        self.medicine_ID = medicine_ID
        self.doctor_ID = doctor_ID
        self.Issued = Issued
        self.Validity = Validity