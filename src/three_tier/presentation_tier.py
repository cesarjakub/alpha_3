import os

class Presentation:
    def __init__(self):
        self.application = None

    def mian_menu(self):
        options = [("1. display e-prescription by ID", self.application.get_prescription_by_id),#
                   ("2. delete e-prescription by ID", self.application.delete_prescription),
                   ("3. modify e-prescription", self.application.update_prescription),
                   ("4. create e-prescription", self.application.create_prescription),
                   ("5. create medicine", self.application.create_medicine),
                   ("6. create patient", self.application.create_patient),
                   ("7. create doctor", self.application.create_doctor),
                   ("8. import json", self.application.import_json_data),#
                   ("9. generate report", self.application.create_report),
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

    # second option

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