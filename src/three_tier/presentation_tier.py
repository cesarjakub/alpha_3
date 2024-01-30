class Presentation:
    def __init__(self):
        self.application = None

    def mian_menu(self):
        options = [("1. vypis e-receptu podle ID", self.application.get_prescription_by_id),
                   ("2. vytvoření e-receptu", self.application.create_prescription),
                   ("3. vytvoření léku", self.application.create_medicine),
                   ("4. vytvoření pacienta", self.application.create_patient),
                   ("5. vztvoření doktora", self.application.create_doctor),
                   ("6. ukončit", self.application.exit)]

