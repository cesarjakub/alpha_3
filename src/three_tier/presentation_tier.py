import datetime
import os

class Presentation:
    def __init__(self):
        self.application = None

    def mian_menu(self):
        options = [("1. display e-prescription by ID", self.application.get_prescription_by_id),#
                   ("2. delete e-prescription by ID", self.application.delete_prescription),#
                   ("3. modify e-prescription", self.application.update_prescription),
                   ("4. create e-prescription", self.application.create_prescription),#--
                   ("5. create medicine", self.application.create_medicine),# dodelat aby videl nazvy manufactureru
                   ("6. create patient", self.application.create_patient),#
                   ("7. create doctor", self.application.create_doctor),# dodělat ješte názvy specializací
                   ("8. import json", self.application.import_json_data),#
                   ("9. generate report", self.application.create_report),#
                   ("10. exit", self.application.exit)]#

        print("+----------------------------------+")
        for text, work in options:
            print(text)
        print("+----------------------------------+")
        selected_number = None
        while selected_number is None:
            try:
                selected_number = int(input(f"Please enter number (1-{str(len(options))}): "))

                if selected_number < 0 or selected_number > len(options):
                    raise Exception()
            except Exception:
                print("Please enter valid input")
                selected_number = None
        return options[selected_number-1][1]()

    # first option
    def print_prescription_by_id(self, prescriptions, num_of_rows):
        labels = ['ID', 'First Name', 'Last Name', 'Date of Birth', 'Health insurance number', 'Issued',
                  'Validity', 'Title', 'Doctor First Name', 'Doctor Last Name', 'Phone Number',
                  'Medication', 'Amount', 'Dosage', 'Payment']
        if num_of_rows == 0:
            print("There are no records")
        for prescription in prescriptions:
            for label, pres in zip(labels, prescription):
                print(f"{label}: {pres}")


    def new_id_input(self, text):
        id_input = None
        while id_input is None:
            try:
                id_input = int(input(text))
                return id_input
            except Exception:
                print("Please enter valid input")
                id_input = None

    # fourth prescription
    def ask_for_prescription_input(self):
        try:
            first_name = input("Enter patient's first name: ")
            last_name = input("Enter patient's last name: ")
            patientDOB = datetime.datetime.strptime(input("Enter the patient's birth date (YYYY-MM-DD): "), "%Y-%m-%d")
            medicine_name = input("Enter medicine's name: ")
            doctor_first_name = input("Enter doctor's first name: ")
            doctor_last_name = input("Enter doctor's last name: ")
            issued = datetime.datetime.strptime(input("Enter the date the prescription was issued (YYYY-MM-DD): "), "%Y-%m-%d")
            validity = datetime.datetime.strptime(input("Enter the validity period of the prescription (YYYY-MM-DD): "), "%Y-%m-%d")

            if None in [first_name, last_name, patientDOB, medicine_name, doctor_first_name, doctor_last_name, issued, validity]:
                self.ask_for_prescription_input()

            return first_name, last_name, patientDOB, medicine_name, doctor_first_name, doctor_last_name, issued, validity
        except:
            raise Exception("Error please try again")

    # fifth option
    def ask_for_medicine_input(self):
        try:
            manufacturer_name = input("Enter the manufacturer's name: ")
            medicine_name = input("Enter the medicine's name: ")
            Amount = int(input("Enter the amount: "))
            Dosage = int(input("Enter the dosage: "))
            Payment = input("Enter the payment (Insurance/Patient): ")

            if None in [manufacturer_name, medicine_name, Amount, Dosage, Payment]:
                self.ask_for_medicine_input()

            return manufacturer_name, medicine_name, Amount, Dosage, Payment
        except:
            raise Exception("Error please try again")

    # sixth option
    def ask_for_patient_input(self):
        try:
            first_name = input("Enter the patient's first name: ")
            last_name = input("Enter the patient's first name: ")
            date_of_Birth = datetime.datetime.strptime(input("Enter the patient's birth date (YYYY-MM-DD): "), "%Y-%m-%d")
            address = input("Enter the patient's address: ")
            health_insurance_number = int(input("Enter the patient's health insurance number: "))

            if None in [first_name, last_name, date_of_Birth, address, health_insurance_number]:
                self.ask_for_patient_input()

            return first_name, last_name, date_of_Birth, address, health_insurance_number
        except:
            raise Exception("Error please try again")

    # seventh option
    def ask_for_doctor_input(self):
        try:
            spec_name = input("Enter specialization name: ")
            first_name = input("Enter the doctor's first name: ")
            last_name = input("Enter the doctor's last name: ")
            title = input("Enter the doctor's title ('Dr.' OR 'PhD'): ")
            date_of_birth = datetime.datetime.strptime(input("Enter the doctor's birth date (YYYY-MM-DD): "), "%Y-%m-%d")
            tel = input("Enter the doctor's telephone: ")

            if None in [spec_name, first_name, last_name, title, date_of_birth, tel]:
                self.ask_for_doctor_input()

            return spec_name, first_name, last_name, title, date_of_birth, tel
        except:
            raise Exception("Error please try again")

    # eighth option
    def new_input(self, text):
        user_input = None
        while user_input is None:
            try:
                user_input = input(text)
                return user_input
            except Exception:
                print("Please enter valid input")
                user_input = None

    # ninth option
    def print_report(self, prescriptions, num_of_rows):
        report = ""
        if num_of_rows == 0:
            print("There are no records")
        for prescription in prescriptions:
            patient_info = f"Patient: {prescription[1]} {prescription[2]} {prescription[3]}\t  ZP: {prescription[4]}"
            issued_validity = f"Issued: {prescription[5]} \tValidity: {prescription[6]}"
            doctor_info = f"Doctor: {prescription[7]} {prescription[8]} {prescription[9]}\ttelephone: {prescription[10]}"
            medication_info = f"Lék:\n\t{prescription[11]}\n\tAmount: {prescription[12]} \tDosage: {prescription[13]}\n\tpayment: {prescription[14]}"
            report += "=" * 64 + "\n"
            report += f"{patient_info}\n{issued_validity}\n"
            report += "=" * 64 + "\n"
            report += f"{doctor_info}\n"
            report += "=" * 64 + "\n"
            report += f"{medication_info}\n"
            report += "=" * 64 + "\n"
        return report

    # print id
    def print_just_ids(self, ids):
        print("+----------------------------------+")
        id_list = []
        for id_tuple in ids:
            id_list.append(str(id_tuple[0]))
        result = ','.join(id_list)
        print(f'ids: {result}')

    # clear console
    def clear_console(self):
        print("+----------------------------------+")
        input("Press ENTER to continue")
        os.system('cls')

    # print message
    def print_message(self, message):
        print(message)