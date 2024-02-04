class Medicine:
    """
    Medicine class representing a prescribed medication.

    Attributes:
    - ID: The unique identifier of the medicine.
    - manufacturer_ID: The ID of the manufacturer of the medicine.
    - Name : The name of the medicine.
    - Amount: The amount of the medicine.
    - Dosage: The dosage information of the medicine.
    - Payment: The payment associated with the medicine.
    """
    def __init__(self, ID=None, manufacturer_ID=None, Name=None, Amount=None, Dosage=None, Payment=None):
        self.ID = ID
        self.manufacturer_ID = manufacturer_ID
        self.Name = Name
        self.Amount = Amount
        self.Dosage = Dosage
        self.Payment = Payment