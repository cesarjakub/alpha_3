import datetime
import os

class Presentation:
    """
    Presentation class for handling user interface interactions.

    Attributes:
    - application: The instance of the application_tier class.

    Methods:
    - main_menu() -> Any:
      Displays the main menu and executes the selected option.

    - print_prescription_by_id(prescriptions: List[Tuple], num_of_rows: int) -> None:
      Prints the details of EPrescriptions based on the provided list and row count.

    - new_id_input(text: str) -> int:
      Prompts the user to input an ID and returns the entered ID.

    - ask_for_update_prescription_input() -> Tuple[int, str, str, datetime.datetime, str, str, str, datetime.datetime, datetime.datetime]:
      Prompts the user for input to update a prescription and returns the entered values.

    - ask_for_prescription_input() -> Tuple[str, str, datetime.datetime, str, str, str, datetime.datetime, datetime.datetime]:
      Prompts the user for input to create a new prescription and returns the entered values.

    - ask_for_medicine_input() -> Tuple[str, str, int, int, str]:
      Prompts the user for input to create a new medicine and returns the entered values.

    - ask_for_patient_input() -> Tuple[str, str, datetime.datetime, str, int]:
      Prompts the user for input to create a new patient and returns the entered values.

    - ask_for_doctor_input() -> Tuple[str, str, str, str, datetime.datetime, str]:
      Prompts the user for input to create a new doctor and returns the entered values.

    - new_input(text: str) -> str:
      Prompts the user for general input and returns the entered value.

    - print_report(prescriptions: List[Tuple], num_of_rows: int) -> str:
      Prints a report based on the provided list of prescriptions and row count.

    - help_print(tmp: List[Tuple], text: str) -> None:
      Prints information based on the provided list and text.

    - clear_console() -> None:
      Clears the console and waits for user input.

    - print_message(message: str) -> None:
      Prints a general message to the console.
    """
    def __init__(self):
        self.application = None

    def mian_menu(self):
        """
        Displays the main menu and executes the selected option.

        Returns:
        Any: The result of the selected option.
        """
        options = [("1. display e-prescription by ID", self.application.get_prescription_by_id),
                   ("2. delete e-prescription by ID", self.application.delete_prescription),
                   ("3. modify e-prescription", self.application.update_prescription),
                   ("4. create e-prescription", self.application.create_prescription),
                   ("5. create medicine", self.application.create_medicine),
                   ("6. create patient", self.application.create_patient),
                   ("7. create doctor", self.application.create_doctor),# dodělat ješte názvy specializací
                   ("8. import json", self.application.import_json_data),
                   ("9. generate report", self.application.create_report),
                   ("10. exit", self.application.exit)]

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
                self.print_message("Please enter valid input")
                selected_number = None
        return options[selected_number-1][1]()

    # first option
    def print_prescription_by_id(self, prescriptions, num_of_rows):
        """
        Prints the details of EPrescriptions based on the provided list or print error message if the number of rows is equal to 0.

        Parameters:
        - prescriptions (List[Tuple]): A list of EPrescription details.
        - num_of_rows (int): The number of rows that returns database
        """
        labels = ['ID', 'First Name', 'Last Name', 'Date of Birth', 'Health insurance number', 'Issued',
                  'Validity', 'Title', 'Doctor First Name', 'Doctor Last Name', 'Phone Number',
                  'Medication', 'Amount', 'Dosage', 'Payment']
        if num_of_rows == 0:
            self.print_message("There are no records")
        for prescription in prescriptions:
            for label, pres in zip(labels, prescription):
                print(f"{label}: {pres}")


    def new_id_input(self, text):
        """
        Prompts the user to input an ID and returns the entered ID.

        Parameters:
        - text (str): The prompt message.

        Returns:
        int: The entered ID.
        """
        id_input = None
        while id_input is None:
            try:
                id_input = int(input(text))
                return id_input
            except Exception:
                self.print_message("Please enter valid input")
                id_input = None

    # third option
    def ask_for_update_prescription_input(self):
        """
        Prompts the user for input to update a prescription and returns the entered values.

        Returns:
        Tuple[int, str, str, datetime.datetime, str, str, str, datetime.datetime, datetime.datetime]:
          The entered values for updating a prescription.
        An error message if an exception occurs
        """
        try:
            e_id = int(input("Enter prescriptions id: "))
            first_name = input("Enter patient's first name: ")
            last_name = input("Enter patient's last name: ")
            patientDOB = datetime.datetime.strptime(input("Enter the patient's birth date (YYYY-MM-DD): "), "%Y-%m-%d")
            medicine_name = input("Enter medicine's name: ")
            doctor_first_name = input("Enter doctor's first name: ")
            doctor_last_name = input("Enter doctor's last name: ")
            issued = datetime.datetime.strptime(input("Enter the date the prescription was issued (YYYY-MM-DD): "),"%Y-%m-%d")
            validity = datetime.datetime.strptime(input("Enter the validity period of the prescription (YYYY-MM-DD): "),"%Y-%m-%d")

            if None in [e_id, first_name, last_name, patientDOB, medicine_name, doctor_first_name, doctor_last_name, issued,
                        validity]:
                self.ask_for_prescription_input()

            return e_id, first_name, last_name, patientDOB, medicine_name, doctor_first_name, doctor_last_name, issued, validity
        except:
            raise Exception("Error wrong input try again")

    # fourth prescription
    def ask_for_prescription_input(self):
        """
        Prompts the user for input to create a new prescription and returns the entered values.

        Returns:
        Tuple[str, str, datetime.datetime, str, str, str, datetime.datetime, datetime.datetime]:
          The entered values for creating a new prescription.
        An error message if an exception occurs
        """
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
            raise Exception("Error wrong input try again")

    # fifth option
    def ask_for_medicine_input(self):
        """
        Prompts the user for input to create a new medicine and returns the entered values.

        Returns:
        Tuple[str, str, int, int, str]: The entered values for creating a new medicine.
        An error message if an exception occurs
        """
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
            raise Exception("Error wrong input try again")

    # sixth option
    def ask_for_patient_input(self):
        """
        Prompts the user for input to create a new patient and returns the entered values.

        Returns:
        Tuple[str, str, datetime.datetime, str, int]: The entered values for creating a new patient.
        An error message if an exception occurs
        """
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
            raise Exception("Error wrong input try again")

    # seventh option
    def ask_for_doctor_input(self):
        """
        Prompts the user for input to create a new doctor and returns the entered values.

        Returns:
        Tuple[str, str, str, str, datetime.datetime, str]: The entered values for creating a new doctor.
        An error message if an exception occurs
        """
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
            raise Exception("Error wrong input try again")

    # eighth option
    def new_input(self, text):
        """
        Prompts the user for general input and returns the entered value.

        Parameters:
        - text (str): The prompt message.

        Returns:
        str: The entered value.
        An error message if an exception occurs
        """
        user_input = None
        while user_input is None:
            try:
                user_input = input(text)
                return user_input
            except Exception:
                self.print_message("Please enter valid input")
                user_input = None

    # ninth option
    def print_report(self, prescriptions, num_of_rows):
        """
        Prints a report based on the provided list of prescriptions or print error message if the number of rows is equal to 0..

        Parameters:
        - prescriptions (List[Tuple]): A list of EPrescription details.
        - num_of_rows (int): The row count of the prescriptions.

        Returns:
        str: The generated report.
        """
        report = ""
        if num_of_rows == 0:
            self.print_message("There are no records")
        for prescription in prescriptions:
            patient_info = f"Patient: {prescription[1]} {prescription[2]} {prescription[3]}\t  HIN: {prescription[4]}"
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
    def help_print(self, tmp, text):
        """
        Prints information based on the provided list and text.

        Parameters:
        - tmp (List[Tuple]): The list of tuples.
        - text (str): The message text.
        """
        self.print_message("+----------------------------------+")
        temp_list = []
        for tmp_tuple in tmp:
            temp_list.append(str(tmp_tuple[0]))
        result = ', '.join(temp_list)
        self.print_message(f'{text}: {result}')

    # clear console
    def clear_console(self):
        """
        Clears the console and waits for user input.
        """
        self.print_message("+----------------------------------+")
        input("Press ENTER to continue")
        os.system('cls')

    # print message
    def print_message(self, message):
        """
        Prints a general message to the console.
        """
        print(message)