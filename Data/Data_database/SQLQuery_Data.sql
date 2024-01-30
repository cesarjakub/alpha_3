BEGIN TRANSACTION;
INSERT INTO patient (First_name, Last_name, Date_of_birth, Address, Health_insurance_number)
VALUES 
    ('John', 'Doe', '1990-05-15', '123 Main St, City', 201),
    ('Alice', 'Smith', '1985-12-10', '456 Oak Ave, Town', 205),
    ('Bob', 'Johnson', '1978-08-22', '789 Pine Rd, Village', 207);
COMMIT;

BEGIN TRANSACTION;
INSERT INTO manufacturer (Name, Address, Email)
VALUES
    ('ABC Pharmaceuticals', '123 Pharma St, Medtown', 'abc@example.com'),
    ('XYZ Labs', '456 Science Blvd, Labville', 'xyz@example.com'),
    ('Medical Innovations', '789 Health Ave, Cureburg', 'med@example.com'),
    ('PharmaCare', '101 Medicine Road, Remedy City', 'pharmacare@example.com'),
    ('Global Health Solutions', '555 Wellness Lane, Healington', 'globalhealth@example.com'),
    ('CureTech Industries', '888 Remedy Street, Medville', 'curetech@example.com'),
    ('BioMed Pharma', '202 Health Plaza, Biocity', 'biomed@example.com'),
    ('LifeScience Innovators', '303 Cure Avenue, Lifetown', 'lifescience@example.com'),
    ('Nature Cure Pharmaceuticals', '404 Herbal Lane, Naturville', 'naturecure@example.com'),
    ('GenoMed Labs', '505 Genetic Blvd, Genetica', 'genomed@example.com');
COMMIT;

BEGIN TRANSACTION;
INSERT INTO medicine (manufacturer_ID, Name, Amount, Dosage, Payment)
VALUES
    (1, 'PainRelief', 50, 10, 'Insurance'),
    (2, 'ColdCure', 30, 5, 'Patient'),
    (3, 'HeartMed', 20, 15, 'Insurance');
COMMIT;

BEGIN TRANSACTION;
INSERT INTO specialization (Name, Description)
VALUES
    ('Cardiology', 'Specializing in heart-related issues'),
    ('Orthopedics', 'Dealing with musculoskeletal disorders'),
    ('Dermatology', 'Focus on skin conditions and diseases'),
    ('Gastroenterology', 'Specializing in digestive system disorders'),
    ('Neurology', 'Dealing with disorders of the nervous system'),
    ('Ophthalmology', 'Focus on eye and vision care'),
    ('Otolaryngology', 'Specializing in ear, nose, and throat disorders'),
    ('Urology', 'Dealing with urinary system disorders'),
    ('Endocrinology', 'Specializing in endocrine system disorders'),
    ('Rheumatology', 'Focus on autoimmune and inflammatory disorders'),
    ('Pediatrics', 'Specializing in the care of children'),
    ('Geriatrics', 'Dealing with health issues of the elderly'),
    ('Pulmonology', 'Specializing in respiratory system disorders'),
    ('Hematology', 'Dealing with blood disorders');
COMMIT;

BEGIN TRANSACTION;
INSERT INTO doctor (specialization_ID, First_name, Last_name, Title, Date_of_birth, Telephone)
VALUES
    (1, 'Sarah', 'Jones', 'Dr.', '1980-03-12', '+12345678901'),
    (2, 'Mark', 'Miller', 'Dr.', '1975-09-20', '+19876543210'),
    (3, 'Emily', 'White', 'PhD', '1988-06-05', '+11223344556');
COMMIT;

BEGIN TRANSACTION;
INSERT INTO eprescription (patient_ID, medicine_ID, doctor_ID, Issued, Validity)
VALUES
    (1, 1, 1, '2022-01-05', '2022-02-05'),
    (2, 2, 2, '2022-02-10', '2022-03-10'),
    (3, 3, 3, '2022-03-15', '2022-04-15');
COMMIT;