class Patient:
    """
    Patient class representing an individual seeking medical care.

    Attributes:
    - ID: The unique identifier of the patient.
    - First_name: The first name of the patient.
    - Last_name: The last name of the patient.
    - Date_of_birth: The date of birth of the patient.
    - Address: The address of the patient.
    - Health_insurance_number: The health insurance number of the patient.
    """
    def __init__(self, ID=None, First_name=None, Last_name=None, Date_of_birth=None, Address=None, Health_insurance_number=None):
        self.ID = ID
        self.First_name = First_name
        self.Last_name = Last_name
        self.Date_of_birth = Date_of_birth
        self.Address = Address
        self.Health_insurance_number = Health_insurance_number