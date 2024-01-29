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

GO
CREATE VIEW EPrescriptionView AS
SELECT 
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

SELECT * FROM patient;
SELECT * FROM manufacturer;
SELECT * FROM medicine;
SELECT * FROM specialization;
SELECT * FROM doctor;
SELECT * FROM eprescription;

USE master;

IF NOT EXISTS 
    (SELECT name
     FROM master.sys.server_principals
     WHERE name = 'test')
BEGIN
    CREATE LOGIN test WITH PASSWORD = '1234';
END

begin transaction;
go
CREATE USER [test] FOR LOGIN [test] WITH DEFAULT_SCHEMA=[dbo];
GO
ALTER ROLE [db_owner] ADD MEMBER [test];
commit;