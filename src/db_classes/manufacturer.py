class Manufacturer:
    """
    Manufacturer class representing a medicine manufacturer.

    Attributes:
    - ID: The unique identifier of the manufacturer.
    - Name: The name of the manufacturer.
    - Address: The address of the manufacturer.
    - Email: The email address of the manufacturer.
    """
    def __init__(self, ID=None, Name=None, Address=None, Email=None):
        self.ID = ID
        self.Name = Name
        self.Address = Address
        self.Email = Email