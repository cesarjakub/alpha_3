import sys
sys.path.append("..")
from DAO import DAOEPrescription
from db_classes import EPrescription
from DAO import DAOPatient
from db_classes import Patient
from DAO import DAOMedicine
from db_classes import Medicine
from db_classes import Doctor
from DAO import DAODoctor
from db_classes import Manufacturer
from DAO import DAOManufacturer
from db_classes import Specialization
from DAO import DAOSpecialization

from database_conn import DBConnection

from import_export_data import ImportData
from import_export_data import ExportData

class Database:
    """
    Database class for handling interactions with the database.

    Attributes:
    - daoeprescription (DAOEPrescription): Data Access Object for EPrescription entities.
    - daopatient (DAOPatient): Data Access Object for Patient entities.
    - daomedicine (DAOMedicine): Data Access Object for Medicine entities.
    - daodoctor (DAODoctor): Data Access Object for Doctor entities.
    - daomanufacturer (DAOManufacturer): Data Access Object for Manufacturer entities.
    - daospecialization (DAOSpecialization): Data Access Object for Specialization entities.

    Methods:
    - get_prescription_by_id(e_id: int) -> Tuple[list, int]:
      Retrieves prescription details based on the provided ID.

    - get_just_ids() -> List[Tuple]:
      Retrieves only the IDs of all EPrescriptions in the database.

    - delete_prescription_by_id(e_id: int) -> str:
      Deletes a prescription from the database based on its ID.

    - update_prescription(e_id: int, first_name: str, last_name: str, patientDOB: str, medicine_name: str, doctor_first_name: str, doctor_last_name: str, issued: str, validity: str) -> str:
      Updates the details of a prescription in the database.

    - create_prescription(first_name: str, last_name: str, patientDOB: str, medicine_name: str, doctor_first_name: str, doctor_last_name: str, issued: str, validity: str) -> str:
      Creates a new prescription in the database.

    - create_medicine(manufacturer_name: str, medicine_name: str, Amount: float, Dosage: str, Payment: float) -> str:
      Creates a new Medicine in the database.

    - get_manufacturer() -> List[Tuple]:
      Retrieves the names of all manufacturers from the database.

    - create_patient(first_name: str, last_name: str, date_of_Birth: str, address: str, health_insurance_number: str) -> str:
      Creates a new Patient in the database.

    - create_doctor(spec_name: str, first_name: str, last_name: str, title: str, date_of_birth: str, tel: str) -> str:
      Creates a new Doctor in the database.

    - get_specialization() -> List[Tuple]:
      Retrieves the names of all specializations from the database.

    - import_json_data(which_data: str) -> str:
      Imports data from a JSON file into the specified table in the database.

    - create_report(data: str) -> str:
      Creates a report by exporting the provided data to a file.
    """
    def __init__(self):
        self.daoeprescription = DAOEPrescription(EPrescription())
        self.daopatient = DAOPatient(Patient())
        self.daomedicine = DAOMedicine(Medicine())
        self.daodoctor = DAODoctor(Doctor())
        self.daomanufacturer = DAOManufacturer(Manufacturer())
        self.daospecialization = DAOSpecialization(Specialization())

    # first option
    def get_prescription_by_id(self, e_id):
        """
        Retrieves prescription details based on the provided ID.

        Parameters:
        - e_id (int): The ID of the EPrescription.

        Returns:
        Tuple[list, int]: A tuple containing a list of prescription details and the row count.
        """
        prescription_list = list()
        prescription, rowcount = self.daoeprescription.get_prescription_by_id(e_id)
        prescription_list = prescription
        return prescription_list, rowcount

    def get_just_ids(self):
        """
        Retrieves only the IDs of all EPrescriptions in the database.

        Returns:
        List[Tuple]: A list of EPrescription IDs.
        """
        ids = self.daoeprescription.get_just_ids()
        return ids

    # second option
    def delete_prescription_by_id(self, e_id):
        """
        Deletes a prescription from the database based on its ID.

        Parameters:
        - e_id (int): The ID of the EPrescription to be deleted.

        Returns:
        str: A message indicating the success or failure of the operation.
        """
        msg = self.daoeprescription.delete_prescription_by_id(e_id)
        return msg

    # third option
    def update_prescription(self, e_id, first_name, last_name, patientDOB, medicine_name, doctor_first_name, doctor_last_name, issued, validity):
        """
        Updates the details of a prescription in the database.

        Parameters:
        - e_id (int): The ID of the EPrescription.
        - first_name (str): The first name of the patient.
        - last_name (str): The last name of the patient.
        - patientDOB (str): The date of birth of the patient.
        - medicine_name (str): The name of the prescribed medicine.
        - doctor_first_name (str): The first name of the prescribing doctor.
        - doctor_last_name (str): The last name of the prescribing doctor.
        - issued (str): The date the prescription was issued.
        - validity (str): The validity period of the prescription.

        Returns:
        str: A message indicating the success or failure of the operation.
        """
        msg = self.daoeprescription.update_prescription(e_id, first_name, last_name, patientDOB, medicine_name, doctor_first_name, doctor_last_name, issued, validity)
        return msg

    # fourth option
    def create_prescription(self, first_name, last_name, patientDOB, medicine_name, doctor_first_name, doctor_last_name, issued, validity):
        """
        Creates a new prescription in the database.

        Parameters:
        - first_name (str): The first name of the patient.
        - last_name (str): The last name of the patient.
        - patientDOB (str): The date of birth of the patient.
        - medicine_name (str): The name of the prescribed medicine.
        - doctor_first_name (str): The first name of the prescribing doctor.
        - doctor_last_name (str): The last name of the prescribing doctor.
        - issued (str): The date the prescription was issued.
        - validity (str): The validity period of the prescription.

        Returns:
        str: A message indicating the success or failure of the operation.
        """
        msg = self.daoeprescription.create_prescription(first_name, last_name, patientDOB, medicine_name, doctor_first_name, doctor_last_name, issued, validity)
        return msg

    # fifth option
    def create_medicine(self, manufacturer_name, medicine_name, Amount, Dosage, Payment):
        """
        Creates a new Medicine in the database.

        Parameters:
        - manufacturer_name (str): The name of the medicine manufacturer.
        - medicine_name (str): The name of the medicine.
        - Amount (float): The amount of the medicine.
        - Dosage (str): The dosage information of the medicine.
        - Payment (float): The payment associated with the medicine.

        Returns:
        str: A message indicating the success or failure of the operation.
        """
        msg = self.daomedicine.create_medicine(manufacturer_name, medicine_name, Amount, Dosage, Payment)
        return msg

    def get_manufacturer(self):
        """
        Retrieves the names of all manufacturers from the database.

        Returns:
        List[Tuple]: A list of manufacturer names.
        """
        manufacturer_list = list()
        manufacturer = self.daomanufacturer.get_manufacturer()
        manufacturer_list = manufacturer
        return manufacturer_list

    # sixth option
    def create_patient(self, first_name, last_name, date_of_Birth, address, health_insurance_number):
        """
        Creates a new Patient in the database.

        Parameters:
        - first_name (str): The first name of the patient.
        - last_name (str): The last name of the patient.
        - date_of_Birth (str): The date of birth of the patient.
        - address (str): The address of the patient.
        - health_insurance_number (str): The health insurance number of the patient.

        Returns:
        str: A message indicating the success or failure of the operation.
        """
        msg = self.daopatient.create_patient(first_name, last_name, date_of_Birth, address, health_insurance_number)
        return msg

    # seventh option
    def create_doctor(self, spec_name, first_name, last_name, title, date_of_birth, tel):
        """
        Creates a new Doctor in the database.

        Parameters:
        - spec_name (str): The name of the specialization of the doctor.
        - first_name (str): The first name of the doctor.
        - last_name (str): The last name of the doctor.
        - title (str): The title of the doctor.
        - date_of_birth (str): The date of birth of the doctor.
        - tel (str): The telephone number of the doctor.

        Returns:
        str: A message indicating the success or failure of the operation.
        """
        msg = self.daodoctor.create_doctor(spec_name, first_name, last_name, title, date_of_birth, tel)
        return msg

    def get_specialization(self):
        """
        Retrieves the names of all specializations from the database.

        Returns:
        List[Tuple]: A list of specialization names.
        """
        specialization_list = list()
        manufacturer = self.daospecialization.get_specialization()
        specialization_list = manufacturer
        return specialization_list

    # eighth option
    def import_json_data(self, which_data: str):
        """
        Imports data from a JSON file into the specified table in the database.

        Parameters:
        - which_data (str): The type of data to import.

        Returns:
        str: A message indicating the success or failure of the operation.
        """
        try:
            import_data = ImportData()
            connection = DBConnection.connect()
            cursor = connection.cursor()
            if which_data.lower() == "medicine":
                for medicine in import_data.import_into()["medicine"]:
                    query = """INSERT INTO medicine (manufacturer_ID, Name, Amount, Dosage, Payment) 
                               VALUES (?, ?, ?, ?, ?)"""
                    values = (medicine["manufacturer_ID"], medicine["Name"], medicine["Amount"], medicine["Dosage"], medicine["Payment"])
                    cursor.execute(query, values)
                cursor.commit()
                return "Data was successfully added"
            elif which_data.lower() == "patient":
                for medicine in import_data.import_into()["patient"]:
                    query = """INSERT INTO patient (First_name, Last_name, Date_of_birth, Address, Health_insurance_number) 
                               VALUES (?, ?, ?, ?, ?)"""
                    values = (medicine["First_name"], medicine["Last_name"], medicine["Date_of_birth"], medicine["Address"], medicine["health_insurance_number"])
                    cursor.execute(query, values)
                cursor.commit()
                return "Data was successfully added"
            else:
                return "Invalid input try again"

        except Exception as e:
            return f"ERROR PLEASE TRY AGAIN {e}"
        finally:
            DBConnection.close_connection()

    # ninth option
    def create_report(self, data):
        """
        Creates a report by exporting the provided data to a file.

        Parameters:
        - data (str): The data to be included in the report.

        Returns:
        str: A message indicating the success or failure of the operation.
        """
        try:
            export_data = ExportData()
            export_data.export_into_file(data)
            return "Report is created please check \"Data/Report/\" file"
        except:
            return "Something went wrong"
