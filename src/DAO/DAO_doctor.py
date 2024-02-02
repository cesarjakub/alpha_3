import sys
sys.path.append("..")
from db_classes import Doctor
from database_conn import DBConnection

class DAODoctor:
    def __init__(self, doctor: Doctor):
        self.doctor = doctor

    def create_doctor(self, spec_name, first_name, last_name, title, date_of_birth, tel):
        try:
            connection = DBConnection.connect()
            cursor = connection.cursor()
            query = "EXEC Create_doctor  @SpecializationName = ?, @FirstName = ?, @LastName = ?, @Title = ?, @DateOfBirth = ?, @Telephone = ?;"
            values = (spec_name, first_name, last_name, title, date_of_birth, tel)
            cursor.execute(query, values)
            cursor.commit()
            return "Doctor created successfully"
        except:
            return "Something went wrong"
        finally:
            DBConnection.close_connection()