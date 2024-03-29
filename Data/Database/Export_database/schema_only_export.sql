USE [master]
GO
/****** Object:  Database [EPrescription]    Script Date: 04.02.2024 11:03:29 ******/
CREATE DATABASE [EPrescription]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'EPrescription', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL16.SQLEXPRESS\MSSQL\DATA\EPrescription.mdf' , SIZE = 8192KB , MAXSIZE = UNLIMITED, FILEGROWTH = 65536KB )
 LOG ON 
( NAME = N'EPrescription_log', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL16.SQLEXPRESS\MSSQL\DATA\EPrescription_log.ldf' , SIZE = 8192KB , MAXSIZE = 2048GB , FILEGROWTH = 65536KB )
 WITH CATALOG_COLLATION = DATABASE_DEFAULT, LEDGER = OFF
GO
ALTER DATABASE [EPrescription] SET COMPATIBILITY_LEVEL = 160
GO
IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [EPrescription].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO
ALTER DATABASE [EPrescription] SET ANSI_NULL_DEFAULT OFF 
GO
ALTER DATABASE [EPrescription] SET ANSI_NULLS OFF 
GO
ALTER DATABASE [EPrescription] SET ANSI_PADDING OFF 
GO
ALTER DATABASE [EPrescription] SET ANSI_WARNINGS OFF 
GO
ALTER DATABASE [EPrescription] SET ARITHABORT OFF 
GO
ALTER DATABASE [EPrescription] SET AUTO_CLOSE ON 
GO
ALTER DATABASE [EPrescription] SET AUTO_SHRINK OFF 
GO
ALTER DATABASE [EPrescription] SET AUTO_UPDATE_STATISTICS ON 
GO
ALTER DATABASE [EPrescription] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO
ALTER DATABASE [EPrescription] SET CURSOR_DEFAULT  GLOBAL 
GO
ALTER DATABASE [EPrescription] SET CONCAT_NULL_YIELDS_NULL OFF 
GO
ALTER DATABASE [EPrescription] SET NUMERIC_ROUNDABORT OFF 
GO
ALTER DATABASE [EPrescription] SET QUOTED_IDENTIFIER OFF 
GO
ALTER DATABASE [EPrescription] SET RECURSIVE_TRIGGERS OFF 
GO
ALTER DATABASE [EPrescription] SET  ENABLE_BROKER 
GO
ALTER DATABASE [EPrescription] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO
ALTER DATABASE [EPrescription] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO
ALTER DATABASE [EPrescription] SET TRUSTWORTHY OFF 
GO
ALTER DATABASE [EPrescription] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO
ALTER DATABASE [EPrescription] SET PARAMETERIZATION SIMPLE 
GO
ALTER DATABASE [EPrescription] SET READ_COMMITTED_SNAPSHOT OFF 
GO
ALTER DATABASE [EPrescription] SET HONOR_BROKER_PRIORITY OFF 
GO
ALTER DATABASE [EPrescription] SET RECOVERY SIMPLE 
GO
ALTER DATABASE [EPrescription] SET  MULTI_USER 
GO
ALTER DATABASE [EPrescription] SET PAGE_VERIFY CHECKSUM  
GO
ALTER DATABASE [EPrescription] SET DB_CHAINING OFF 
GO
ALTER DATABASE [EPrescription] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO
ALTER DATABASE [EPrescription] SET TARGET_RECOVERY_TIME = 60 SECONDS 
GO
ALTER DATABASE [EPrescription] SET DELAYED_DURABILITY = DISABLED 
GO
ALTER DATABASE [EPrescription] SET ACCELERATED_DATABASE_RECOVERY = OFF  
GO
ALTER DATABASE [EPrescription] SET QUERY_STORE = ON
GO
ALTER DATABASE [EPrescription] SET QUERY_STORE (OPERATION_MODE = READ_WRITE, CLEANUP_POLICY = (STALE_QUERY_THRESHOLD_DAYS = 30), DATA_FLUSH_INTERVAL_SECONDS = 900, INTERVAL_LENGTH_MINUTES = 60, MAX_STORAGE_SIZE_MB = 1000, QUERY_CAPTURE_MODE = AUTO, SIZE_BASED_CLEANUP_MODE = AUTO, MAX_PLANS_PER_QUERY = 200, WAIT_STATS_CAPTURE_MODE = ON)
GO
USE [EPrescription]
GO
/****** Object:  User [test]    Script Date: 04.02.2024 11:03:29 ******/
CREATE USER [test] FOR LOGIN [test] WITH DEFAULT_SCHEMA=[dbo]
GO
ALTER ROLE [db_owner] ADD MEMBER [test]
GO
/****** Object:  Table [dbo].[patient]    Script Date: 04.02.2024 11:03:29 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[patient](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[First_name] [varchar](20) NOT NULL,
	[Last_name] [varchar](20) NOT NULL,
	[Date_of_birth] [date] NOT NULL,
	[Address] [varchar](50) NOT NULL,
	[Health_insurance_number] [int] NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[medicine]    Script Date: 04.02.2024 11:03:29 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[medicine](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[manufacturer_ID] [int] NOT NULL,
	[Name] [varchar](50) NOT NULL,
	[Amount] [int] NOT NULL,
	[Dosage] [int] NOT NULL,
	[Payment] [varchar](50) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[doctor]    Script Date: 04.02.2024 11:03:29 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[doctor](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[specialization_ID] [int] NOT NULL,
	[First_name] [varchar](20) NOT NULL,
	[Last_name] [varchar](20) NOT NULL,
	[Title] [varchar](20) NOT NULL,
	[Date_of_birth] [date] NOT NULL,
	[Telephone] [varchar](13) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[eprescription]    Script Date: 04.02.2024 11:03:29 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[eprescription](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[patient_ID] [int] NOT NULL,
	[medicine_ID] [int] NOT NULL,
	[doctor_ID] [int] NOT NULL,
	[Issued] [date] NOT NULL,
	[Validity] [date] NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  View [dbo].[EPrescriptionView]    Script Date: 04.02.2024 11:03:29 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE VIEW [dbo].[EPrescriptionView] AS
SELECT 
eprescription.ID as e_ID,
patient.First_name AS Patient_FirstName, patient.Last_name AS Patient_LastName, patient.Date_of_birth, patient.Health_insurance_number, 
eprescription.Issued, eprescription.Validity, 
doctor.Title, doctor.First_name AS Doctor_FirstName, doctor.Last_name AS Doctor_LastName, doctor.Telephone,
medicine.Name, medicine.Amount, medicine.Dosage, medicine.Payment
FROM eprescription INNER JOIN patient ON eprescription.patient_ID = patient.ID INNER JOIN doctor ON eprescription.doctor_ID = doctor.ID INNER JOIN medicine ON eprescription.medicine_ID = medicine.ID;
GO
/****** Object:  Table [dbo].[manufacturer]    Script Date: 04.02.2024 11:03:29 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[manufacturer](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[Name] [varchar](50) NOT NULL,
	[Address] [varchar](50) NOT NULL,
	[Email] [varchar](50) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[specialization]    Script Date: 04.02.2024 11:03:29 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[specialization](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[Name] [varchar](50) NOT NULL,
	[Description] [varchar](255) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[doctor]  WITH CHECK ADD FOREIGN KEY([specialization_ID])
REFERENCES [dbo].[specialization] ([ID])
GO
ALTER TABLE [dbo].[eprescription]  WITH CHECK ADD FOREIGN KEY([doctor_ID])
REFERENCES [dbo].[doctor] ([ID])
GO
ALTER TABLE [dbo].[eprescription]  WITH CHECK ADD FOREIGN KEY([medicine_ID])
REFERENCES [dbo].[medicine] ([ID])
GO
ALTER TABLE [dbo].[eprescription]  WITH CHECK ADD FOREIGN KEY([patient_ID])
REFERENCES [dbo].[patient] ([ID])
GO
ALTER TABLE [dbo].[medicine]  WITH CHECK ADD FOREIGN KEY([manufacturer_ID])
REFERENCES [dbo].[manufacturer] ([ID])
GO
ALTER TABLE [dbo].[doctor]  WITH CHECK ADD CHECK  (([Title]='PhD' OR [Title]='Dr.'))
GO
ALTER TABLE [dbo].[manufacturer]  WITH CHECK ADD CHECK  (([Email] like '%@%'))
GO
ALTER TABLE [dbo].[medicine]  WITH CHECK ADD CHECK  (([Payment]='Patient' OR [Payment]='Insurance'))
GO
/****** Object:  StoredProcedure [dbo].[Create_doctor]    Script Date: 04.02.2024 11:03:29 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROC [dbo].[Create_doctor] @SpecializationName VARCHAR(50), @FirstName VARCHAR(20), @LastName VARCHAR(20), @Title VARCHAR(20), @DateOfBirth DATE, @Telephone VARCHAR(13)
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
/****** Object:  StoredProcedure [dbo].[Create_medicine]    Script Date: 04.02.2024 11:03:29 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[Create_medicine] @ManufacturerName VARCHAR(50), @MedicineName VARCHAR(50), @Amount INT, @Dosage INT, @Payment VARCHAR(50)
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
/****** Object:  StoredProcedure [dbo].[Create_patient]    Script Date: 04.02.2024 11:03:29 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[Create_patient] @FirstName VARCHAR(20), @LastName VARCHAR(20), @DateOfBirth DATE, @Address VARCHAR(50), @HealthInsuranceNumber INT
AS
BEGIN
    BEGIN TRANSACTION;

    INSERT INTO patient (First_name, Last_name, Date_of_birth, Address, Health_insurance_number)
    VALUES (@FirstName, @LastName, @DateOfBirth, @Address, @HealthInsuranceNumber);

    COMMIT;
END;
GO
/****** Object:  StoredProcedure [dbo].[Create_prescription]    Script Date: 04.02.2024 11:03:29 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[Create_prescription] @PatientFirstName VARCHAR(20), @PatientLastName VARCHAR(20), @PatientDOB DATE, @MedicineName VARCHAR(50), @DoctorFirstName VARCHAR(20), @DoctorLastName VARCHAR(20), @Issued DATE, @Validity DATE
AS
BEGIN
    BEGIN TRANSACTION;

    DECLARE @PatientID INT;
    DECLARE @MedicineID INT;
    DECLARE @DoctorID INT;

    SELECT @PatientID = ID
    FROM patient
    WHERE First_name = @PatientFirstName AND Last_name = @PatientLastName AND Date_of_birth = @PatientDOB;

    SELECT @MedicineID = ID
    FROM medicine
    WHERE Name = @MedicineName;

    SELECT @DoctorID = ID
    FROM doctor
    WHERE First_name = @DoctorFirstName AND Last_name = @DoctorLastName;

    INSERT INTO eprescription (patient_ID, medicine_ID, doctor_ID, Issued, Validity)
    VALUES (@PatientID, @MedicineID, @DoctorID, @Issued, @Validity);

    COMMIT;
END;
GO
/****** Object:  StoredProcedure [dbo].[Update_prescription]    Script Date: 04.02.2024 11:03:29 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[Update_prescription] @ID INT, @PatientFirstName VARCHAR(20), @PatientLastName VARCHAR(20), @PatientDOB DATE, @MedicineName VARCHAR(50), @DoctorFirstName VARCHAR(20), @DoctorLastName VARCHAR(20), @Issued DATE, @Validity DATE
AS
BEGIN
    BEGIN TRANSACTION;

    DECLARE @PatientID INT;
    DECLARE @MedicineID INT;
    DECLARE @DoctorID INT;

    SELECT @PatientID = ID
    FROM patient
    WHERE First_name = @PatientFirstName AND Last_name = @PatientLastName AND Date_of_birth = @PatientDOB;

    SELECT @MedicineID = ID
    FROM medicine
    WHERE Name = @MedicineName;

    SELECT @DoctorID = ID
    FROM doctor
    WHERE First_name = @DoctorFirstName AND Last_name = @DoctorLastName;

    UPDATE eprescription 
    SET 
        eprescription.patient_ID = @PatientID,
        eprescription.medicine_ID = @MedicineID,
        eprescription.doctor_ID = @DoctorID,
        eprescription.Issued = @Issued,
        eprescription.Validity = @Validity
    WHERE
        eprescription.ID = @ID;

    COMMIT;
END;
GO
USE [master]
GO
ALTER DATABASE [EPrescription] SET  READ_WRITE 
GO
