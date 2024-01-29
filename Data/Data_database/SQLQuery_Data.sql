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
    ('Medical Innovations', '789 Health Ave, Cureburg', 'med@example.com');
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
    ('Dermatology', 'Focus on skin conditions and diseases');
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