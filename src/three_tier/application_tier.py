class Application:
    def __init__(self):
        self._running = False
        self.database = None
        self.presentation = None

    def run(self):
        self._running = True
        while self._running:
            self.presentation.mian_menu()
            self.presentation.clear_console()

    # shut down program
    def exit(self):
        self._running = False

    # first option
    def get_prescription_by_id(self):
        ids = self.database.get_just_ids()
        self.presentation.print_just_ids(ids)
        e_id = self.presentation.new_id_input("Please Enter ID of e-prescription: ")
        prescription, num_of_rows = self.database.get_prescription_by_id(e_id)
        self.presentation.print_prescription_by_id(prescription, num_of_rows)

    # third option
    def update_prescription(self):
        try:

            e_id, first_name, last_name, patientDOB, medicine_name, doctor_first_name, doctor_last_name, issued, validity = self.presentation.ask_for_update_prescription_input()
            msg = self.database.update_prescription(e_id, first_name, last_name, patientDOB, medicine_name, doctor_first_name, doctor_last_name, issued, validity)
            self.presentation.print_message(msg)
        except Exception as e:
            self.presentation.print_message(e)

    # fourth option
    def create_prescription(self):
        try:
            first_name, last_name, patientDOB, medicine_name, doctor_first_name, doctor_last_name, issued, validity = self.presentation.ask_for_prescription_input()
            msg = self.database.create_prescription(first_name, last_name, patientDOB, medicine_name, doctor_first_name, doctor_last_name, issued, validity)
            self.presentation.print_message(msg)
        except Exception as e:
            self.presentation.print_message(e)

    # fifth option
    def create_medicine(self):
        try:
            manufacturer_name, medicine_name, Amount, Dosage, Payment = self.presentation.ask_for_medicine_input()
            msg = self.database.create_medicine(manufacturer_name, medicine_name, Amount, Dosage, Payment)
            self.presentation.print_message(msg)
        except Exception as e:
            self.presentation.print_message(e)

    # sixth option
    def create_patient(self):
        try:
            first_name, last_name, date_of_Birth, address, health_insurance_number = self.presentation.ask_for_patient_input()
            msg = self.database.create_patient(first_name, last_name, date_of_Birth, address, health_insurance_number)
            self.presentation.print_message(msg)
        except Exception as e:
            self.presentation.print_message(e)

    # seventh option
    def create_doctor(self):
        try:
            spec_name, first_name, last_name, title, date_of_birth, tel = self.presentation.ask_for_doctor_input()
            msg = self.database.create_doctor(spec_name, first_name, last_name, title, date_of_birth, tel)
            self.presentation.print_message(msg)
        except Exception as e:
            self.presentation.print_message(e)

    # eighth option
    def import_json_data(self):
        which_data = self.presentation.new_input("Please Enter name of data (medicine/patient): ")
        msg = self.database.import_json_data(which_data)
        self.presentation.print_message(msg)

    # ninth option
    def create_report(self):
        e_id = self.presentation.new_id_input("Please Enter ID of e-prescription: ")
        prescription, num_of_rows = self.database.get_prescription_by_id(e_id)
        data = self.presentation.print_report(prescription, num_of_rows)
        msg = self.database.create_report(data)
        self.presentation.print_message(msg)

    # second option
    def delete_prescription(self):
        ids = self.database.get_just_ids()
        self.presentation.print_just_ids(ids)
        e_id = self.presentation.new_id_input("Please Enter ID of e-prescription: ")
        msg = self.database.delete_prescription_by_id(e_id)
        self.presentation.print_message(msg)

    def update_prescription(self):
        pass