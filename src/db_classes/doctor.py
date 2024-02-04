class Doctor:
    """
    Doctor class representing a medical professional.

    Attributes:
    - ID: The unique identifier of the doctor.
    - specialization_ID: The ID of the specialization the doctor belongs to.
    - First_name: The first name of the doctor.
    - Last_name: The last name of the doctor.
    - Title: The title of the doctor.
    - Date_of_birth: The date of birth of the doctor.
    - Telephone: The telephone number of the doctor.
    """
    def __init__(self, ID=None, specialization_ID=None, First_name=None, Last_name=None, Title=None, Date_of_birth=None, Telephone=None):
        self.ID = ID
        self.specialization_ID = specialization_ID
        self.First_name = First_name
        self.Last_name = Last_name
        self.Title = Title
        self.Date_of_birth = Date_of_birth
        self.Telephone = Telephone
