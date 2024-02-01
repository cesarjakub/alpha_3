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

    def create_prescription(self):
        pass

    def create_medicine(self):
        pass

    def create_patient(self):
        pass

    def create_doctor(self):
        pass

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

    def delete_prescription(self):
        pass

    def update_prescription(self):
        pass