class Application:
    """
    The Application class manages the main functionality of the pharmacy or healthcare-related database system.

    Attributes:
    - _running (bool): Indicates whether the application is running.
    - database: An instance of the database handling class.
    - presentation: An instance of the presentation (UI) handling class.

    Methods:
    - run(): Initiates the main loop of the application.
    - exit(): Shuts down the program.
    - get_prescription_by_id(): Displays e-prescription details based on the entered ID.
    - update_prescription(): Modifies an existing e-prescription.
    - create_prescription(): Creates a new e-prescription.
    - create_medicine(): Adds a new medicine entry to the database.
    - create_patient(): Creates a new patient record.
    - create_doctor(): Creates a new doctor record.
    - import_json_data(): Imports data (medicine or patient) from a JSON file.
    - create_report(): Generates a report based on a selected e-prescription.
    - delete_prescription(): Deletes an e-prescription based on the entered ID.
    """
    def __init__(self):
        """
        Initializes the Application class.
        """
        self._running = False
        self.database = None
        self.presentation = None

    def run(self):
        """
        Initiates the main loop of the application.
        """
        self._running = True
        while self._running:
            self.presentation.mian_menu()
            self.presentation.clear_console()

    # shut down program
    def exit(self):
        """
        Shuts down the program.
        """
        self._running = False

    # first option
    def get_prescription_by_id(self):
        """
        Displays e-prescription details based on the entered ID.
        """
        try:
            ids = self.database.get_just_ids()
            self.presentation.help_print(ids, "ids")
            e_id = self.presentation.new_id_input("Please Enter ID of e-prescription: ")
            prescription, num_of_rows = self.database.get_prescription_by_id(e_id)
            self.presentation.print_prescription_by_id(prescription, num_of_rows)
        except KeyboardInterrupt:
            self.presentation.print_message("Please enter valid input")
    # third option
    def update_prescription(self):
        """
        Modifies an existing e-prescription based on the entered ID.
        """
        try:
            ids = self.database.get_just_ids()
            self.presentation.help_print(ids, "ids")
            e_id, first_name, last_name, patientDOB, medicine_name, doctor_first_name, doctor_last_name, issued, validity = self.presentation.ask_for_update_prescription_input()
            msg = self.database.update_prescription(e_id, first_name, last_name, patientDOB, medicine_name, doctor_first_name, doctor_last_name, issued, validity)
            self.presentation.print_message(msg)
        except Exception as e:
            self.presentation.print_message(e)

    # fourth option
    def create_prescription(self):
        """
        Creates a new e-prescription.
        """
        try:
            first_name, last_name, patientDOB, medicine_name, doctor_first_name, doctor_last_name, issued, validity = self.presentation.ask_for_prescription_input()
            msg = self.database.create_prescription(first_name, last_name, patientDOB, medicine_name, doctor_first_name, doctor_last_name, issued, validity)
            self.presentation.print_message(msg)
        except Exception as e:
            self.presentation.print_message(e)

    # fifth option
    def create_medicine(self):
        """
        Creates a new medicine.
        """
        try:
            manufacturer = self.database.get_manufacturer()
            self.presentation.help_print(manufacturer, "Manufacturer")
            manufacturer_name, medicine_name, Amount, Dosage, Payment = self.presentation.ask_for_medicine_input()
            msg = self.database.create_medicine(manufacturer_name, medicine_name, Amount, Dosage, Payment)
            self.presentation.print_message(msg)
        except Exception as e:
            self.presentation.print_message(e)

    # sixth option
    def create_patient(self):
        """
        Creates a new patient record.
        """
        try:
            first_name, last_name, date_of_Birth, address, health_insurance_number = self.presentation.ask_for_patient_input()
            msg = self.database.create_patient(first_name, last_name, date_of_Birth, address, health_insurance_number)
            self.presentation.print_message(msg)
        except Exception as e:
            self.presentation.print_message(e)

    # seventh option
    def create_doctor(self):
        """
        Creates a new doctor record.
        """
        try:
            specialization = self.database.get_specialization()
            self.presentation.help_print(specialization, "Specialization")
            spec_name, first_name, last_name, title, date_of_birth, tel = self.presentation.ask_for_doctor_input()
            msg = self.database.create_doctor(spec_name, first_name, last_name, title, date_of_birth, tel)
            self.presentation.print_message(msg)
        except Exception as e:
            self.presentation.print_message(e)

    # eighth option
    def import_json_data(self):
        """
        Imports data (medicine or patient) from a JSON file.
        """
        which_data = self.presentation.new_input("Please Enter name of data (medicine/patient): ")
        msg = self.database.import_json_data(which_data)
        self.presentation.print_message(msg)

    # ninth option
    def create_report(self):
        """
        Generates a report based on a selected e-prescription.
        """
        try:
            ids = self.database.get_just_ids()
            self.presentation.help_print(ids, "ids")
            e_id = self.presentation.new_id_input("Please Enter ID of e-prescription: ")
            prescription, num_of_rows = self.database.get_prescription_by_id(e_id)
            data = self.presentation.print_report(prescription, num_of_rows)
            msg = self.database.create_report(data)
            self.presentation.print_message(msg)
        except Exception as e:
            self.presentation.print_message(e)

    # second option
    def delete_prescription(self):
        """
        Deletes an e-prescription based on the entered ID.
        """
        try:
            ids = self.database.get_just_ids()
            self.presentation.help_print(ids, "ids")
            e_id = self.presentation.new_id_input("Please Enter ID of e-prescription: ")
            msg = self.database.delete_prescription_by_id(e_id)
            self.presentation.print_message(msg)
        except KeyboardInterrupt:
            self.presentation.print_message("Please enter valid input")
