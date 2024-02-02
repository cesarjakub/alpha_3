import sys
sys.path.append("..")
from db_classes import EPrescription
from database_conn import DBConnection

class DAOEPrescription:
    def __init__(self, eprescription: EPrescription):
        self.eprescription = eprescription


    def create_prescription(self, first_name, last_name, patientDOB, medicine_name, doctor_first_name, doctor_last_name, issued, validity):
        try:
            connection = DBConnection.connect()
            cursor = connection.cursor()
            query = "EXEC Create_prescription ?, ?, ?, ?, ?, ?, ?, ?;"
            values = (first_name, last_name, patientDOB, medicine_name, doctor_first_name, doctor_last_name, issued, validity)
            cursor.execute(query, values)
            cursor.commit()
            return "Prescription created successfully"
        except:
            return "Something went wrong"
        finally:
            DBConnection.close_connection()

    def get_prescription_by_id(self, e_id):
        try:
            connection = DBConnection.connect()
            cursor = connection.cursor()
            query = "SELECT * FROM EPrescriptionView WHERE e_ID = ?;"
            cursor.execute(query, (e_id,))
            records = cursor.fetchall()
            return records, cursor.rowcount
        except Exception:
            return "Something went wrong"
        finally:
            DBConnection.close_connection()

    def delete_prescription_by_id(self, e_id):
        try:
            connection = DBConnection.connect()
            cursor = connection.cursor()
            query = "DELETE FROM eprescription WHERE ID = ?;"
            cursor.execute(query, (e_id,))
            cursor.commit()
            return "The e-prescription has been successfully deleted"
        except:
            return "Something went wrong"
        finally:
            DBConnection.close_connection()

    def get_just_ids(self):
        try:
            connection = DBConnection.connect()
            cursor = connection.cursor()
            query = "SELECT e_ID FROM EPrescriptionView;"
            cursor.execute(query)
            records = cursor.fetchall()
            return records
        except Exception:
            return "Something went wrong"
        finally:
            DBConnection.close_connection()