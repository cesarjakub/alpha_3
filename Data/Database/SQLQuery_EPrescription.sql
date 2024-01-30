CREATE DATABASE EPrescription;
USE EPrescription;

CREATE TABLE patient(
ID INT PRIMARY KEY IDENTITY(1,1),
First_name VARCHAR(20) NOT NULL,
Last_name VARCHAR(20) NOT NULL,
Date_of_birth DATE NOT NULL,
Address VARCHAR(50) NOT NULL,
Health_insurance_number INT NOT NULL
);

CREATE TABLE manufacturer(
ID INT PRIMARY KEY IDENTITY(1,1),
Name VARCHAR(50) NOT NULL,
Address VARCHAR(50) NOT NULL,
Email VARCHAR(50) NOT NULL CHECK(Email LIKE '%@%')
);

CREATE TABLE medicine(
ID INT PRIMARY KEY IDENTITY(1,1),
manufacturer_ID INT  NOT NULL FOREIGN KEY REFERENCES manufacturer(ID),
Name VARCHAR(50) NOT NULL,
Amount INT NOT NULL,
Dosage INT NOT NULL,
Payment VARCHAR(50) NOT NULL CHECK(Payment IN ('Insurance','Patient'))
);

CREATE TABLE specialization(
ID INT PRIMARY KEY IDENTITY(1,1),
Name VARCHAR(50) NOT NULL,
Description VARCHAR(255) NOT NULL
);

CREATE TABLE doctor(
ID INT PRIMARY KEY IDENTITY(1,1),
specialization_ID INT  NOT NULL FOREIGN KEY REFERENCES specialization(ID),
First_name VARCHAR(20) NOT NULL,
Last_name VARCHAR(20) NOT NULL,
Title VARCHAR(20) NOT NULL CHECK(Title IN ('Dr.', 'PhD')),
Date_of_birth DATE NOT NULL,
Telephone VARCHAR(13) NOT NULL
);

CREATE TABLE eprescription(
ID INT PRIMARY KEY IDENTITY(1,1),
patient_ID INT  NOT NULL FOREIGN KEY REFERENCES patient(ID),
medicine_ID INT  NOT NULL FOREIGN KEY REFERENCES medicine(ID),
doctor_ID INT  NOT NULL FOREIGN KEY REFERENCES doctor(ID),
Issued DATE NOT NULL,
Validity DATE NOT NULL
);


--views
GO
CREATE VIEW EPrescriptionView AS
SELECT 
eprescription.ID,
patient.First_name AS Patient_FirstName, patient.Last_name AS Patient_LastName, patient.Date_of_birth, patient.Health_insurance_number, 
eprescription.Issued, eprescription.Validity, 
doctor.Title, doctor.First_name AS Doctor_FirstName, doctor.Last_name AS Doctor_LastName, doctor.Telephone,
medicine.Name, medicine.Amount, medicine.Dosage, medicine.Payment
FROM eprescription INNER JOIN patient ON eprescription.patient_ID = patient.ID INNER JOIN doctor ON eprescription.doctor_ID = doctor.ID INNER JOIN medicine ON eprescription.medicine_ID = medicine.ID;
GO


SELECT * FROM EPrescriptionView;


GO
CREATE VIEW  AS
SELECT 
GO


--procedury
GO
CREATE PROC Create_doctor @SpecializationName VARCHAR(50), @FirstName VARCHAR(20), @LastName VARCHAR(20), @Title VARCHAR(20), @DateOfBirth DATE, @Telephone VARCHAR(13)
AS
BEGIN
    BEGIN TRANSACTION;

    DECLARE @SpecializationID INT;

    SELECT @SpecializationID = ID
    FROM specialization
    WHERE Name = @SpecializationName;

    INSERT INTO doctor (specialization_ID, First_name, Last_name, Title, Date_of_birth, Telephone)
    VALUES (@SpecializationID, @FirstName, @LastName, @Title, @DateOfBirth, @Telephone);

    COMMIT;
END;
GO

EXEC Create_doctor  @SpecializationName = 'Cardiology', @FirstName = 'Jacob', @LastName = 'Smith', @Title = 'Dr.', @DateOfBirth = '1990-02-22', @Telephone = '+420584754896';

GO
CREATE PROCEDURE Create_patient @FirstName VARCHAR(20), @LastName VARCHAR(20), @DateOfBirth DATE, @Address VARCHAR(50), @HealthInsuranceNumber INT
AS
BEGIN
    BEGIN TRANSACTION;

    INSERT INTO patient (First_name, Last_name, Date_of_birth, Address, Health_insurance_number)
    VALUES (@FirstName, @LastName, @DateOfBirth, @Address, @HealthInsuranceNumber);

    COMMIT;
END;
GO

EXEC Create_patient 'Jack', 'White', '1980-10-08', '652 Down River', 207;


GO
CREATE PROCEDURE Create_medicine @ManufacturerName VARCHAR(50), @MedicineName VARCHAR(50), @Amount INT, @Dosage INT, @Payment VARCHAR(50)
AS
BEGIN
    BEGIN TRANSACTION;

    DECLARE @ManufacturerID INT;

    SELECT @ManufacturerID = ID
    FROM manufacturer
    WHERE Name = @ManufacturerName;

    INSERT INTO medicine (manufacturer_ID, Name, Amount, Dosage, Payment)
    VALUES (@ManufacturerID, @MedicineName, @Amount, @Dosage, @Payment);

    COMMIT;
END;
GO

EXEC Create_medicine 'ABC Pharmaceuticals', 'PainRelief', 30, 3, 'Insurance';


SELECT * FROM patient;
SELECT * FROM manufacturer;
SELECT * FROM medicine;
SELECT * FROM specialization;
SELECT * FROM doctor;
SELECT * FROM eprescription;
