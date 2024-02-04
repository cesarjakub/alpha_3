class EPrescription:
    """
    EPrescription class representing an electronic prescription.

    Attributes:
    - ID: The unique identifier of the prescription.
    - patient_ID: The ID of the patient receiving the prescription.
    - medicine_ID: The ID of the prescribed medicine.
    - doctor_ID: The ID of the prescribing doctor.
    - Issued: The date the prescription was issued.
    - Validity: The validity period of the prescription.
    """
    def __init__(self, ID=None, patient_ID=None, medicine_ID=None, doctor_ID=None, Issued=None, Validity=None):
        self.ID = ID
        self.patient_ID = patient_ID
        self.medicine_ID = medicine_ID
        self.doctor_ID = doctor_ID
        self.Issued = Issued
        self.Validity = Validity