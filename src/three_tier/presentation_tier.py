import os

class Presentation:
    def __init__(self):
        self.application = None

    def mian_menu(self):
        options = [("1. display e-prescription by ID", self.application.get_prescription_by_id),
                   ("2. delete e-prescription", self.application.delete__prescription),
                   ("3. modify e-prescription", self.application.update_prescription),
                   ("4. create e-prescription", self.application.create_prescription),
                   ("5. create medicine", self.application.create_medicine),
                   ("6. create patient", self.application.create_patient),
                   ("7. create doctor", self.application.create_doctor),
                   ("8. import csv/json", self.application.import_scv_json),
                   ("9. exit", self.application.exit)]

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

    def clear_console(self):
        print("+----------------------------------+")
        input("Press ENTER to continue")
        os.system('cls')