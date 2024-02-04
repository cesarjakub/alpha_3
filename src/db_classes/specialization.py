class Specialization:
    """
    Specialization class representing a medical field or expertise.

    Attributes:
    - ID: The unique identifier of the specialization.
    - Name: The name of the specialization.
    - Description: The description of the specialization.
    """
    def __init__(self, ID=None, Name=None, Description=None):
        self.ID = ID
        self.Name = Name
        self.Description = Description