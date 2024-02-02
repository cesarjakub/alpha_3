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

from database_conn import DBConnection

from import_export_data import ImportData
from import_export_data import ExportData

class Database:
    def __init__(self):
        self.daoeprescription = DAOEPrescription(EPrescription())
        self.daopatient = DAOPatient(Patient())
        self.daomedicine = DAOMedicine(Medicine())
        self.daodoctor = DAODoctor(Doctor())

    # first option
    def get_prescription_by_id(self, e_id):
        prescription_list = list()
        prescription, rowcount = self.daoeprescription.get_prescription_by_id(e_id)
        prescription_list = prescription
        return prescription_list, rowcount

    def get_just_ids(self):
        ids = self.daoeprescription.get_just_ids()
        return ids

    # second option
    def delete_prescription_by_id(self, e_id):
        msg = self.daoeprescription.delete_prescription_by_id(e_id)
        return msg

    # fourth option
    def create_prescription(self, first_name, last_name, patientDOB, medicine_name, doctor_first_name, doctor_last_name, issued, validity):
        msg = self.daoeprescription.create_prescription(first_name, last_name, patientDOB, medicine_name, doctor_first_name, doctor_last_name, issued, validity)
        return msg

    # fifth option
    def create_medicine(self, manufacturer_name, medicine_name, Amount, Dosage, Payment):
        msg = self.daomedicine.create_medicine(manufacturer_name, medicine_name, Amount, Dosage, Payment)
        return msg

    # sixth option
    def create_patient(self, first_name, last_name, date_of_Birth, address, health_insurance_number):
        msg = self.daopatient.create_patient(first_name, last_name, date_of_Birth, address, health_insurance_number)
        return msg

    # seventh option
    def create_doctor(self, spec_name, first_name, last_name, title, date_of_birth, tel):
        msg = self.daodoctor.create_doctor(spec_name, first_name, last_name, title, date_of_birth, tel)
        return msg

    # eighth option
    def import_json_data(self, which_data: str):
        try:
            import_data = ImportData()
            connection = DBConnection.connect()
            cursor = connection.cursor()
            if which_data.lower() == "medicine":
                for medicine in import_data.import_into_medicine()["medicine"]:
                    query = """INSERT INTO medicine (manufacturer_ID, Name, Amount, Dosage, Payment) 
                               VALUES (?, ?, ?, ?, ?)"""
                    values = (medicine["manufacturer_ID"], medicine["Name"], medicine["Amount"], medicine["Dosage"], medicine["Payment"])
                    cursor.execute(query, values)
                cursor.commit()
                return "Data was successfully added"
            elif which_data.lower() == "patient":
                for medicine in import_data.import_into_medicine()["patient"]:
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
        try:
            export_data = ExportData()
            export_data.export_into_file(data)
            return "Report is created please check \"Data/Export/export.txt\" file"
        except:
            return "Something went wrong"
