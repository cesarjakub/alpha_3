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

    def exit(self):
        self._running = False

    def get_prescription_by_id(self):
        pass

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