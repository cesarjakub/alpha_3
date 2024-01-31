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
        e_id = self.presentation.new_id_input()
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

    def import_scv_json(self):
        pass

    def delete__prescription(self):
        pass

    def update_prescription(self):
        pass