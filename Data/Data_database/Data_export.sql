USE [EPrescription]
GO
SET IDENTITY_INSERT [dbo].[patient] ON 

INSERT [dbo].[patient] ([ID], [First_name], [Last_name], [Date_of_birth], [Address], [Health_insurance_number]) VALUES (1, N'John', N'Doe', CAST(N'1990-05-15' AS Date), N'123 Main St, City', 201)
INSERT [dbo].[patient] ([ID], [First_name], [Last_name], [Date_of_birth], [Address], [Health_insurance_number]) VALUES (2, N'Alice', N'Smith', CAST(N'1985-12-10' AS Date), N'456 Oak Ave, Town', 205)
INSERT [dbo].[patient] ([ID], [First_name], [Last_name], [Date_of_birth], [Address], [Health_insurance_number]) VALUES (3, N'Bob', N'Johnson', CAST(N'1978-08-22' AS Date), N'789 Pine Rd, Village', 207)
INSERT [dbo].[patient] ([ID], [First_name], [Last_name], [Date_of_birth], [Address], [Health_insurance_number]) VALUES (4, N'Jack', N'White', CAST(N'1980-10-08' AS Date), N'652 Down River', 207)
SET IDENTITY_INSERT [dbo].[patient] OFF
GO
SET IDENTITY_INSERT [dbo].[manufacturer] ON 

INSERT [dbo].[manufacturer] ([ID], [Name], [Address], [Email]) VALUES (1, N'ABC Pharmaceuticals', N'123 Pharma St, Medtown', N'abc@example.com')
INSERT [dbo].[manufacturer] ([ID], [Name], [Address], [Email]) VALUES (2, N'XYZ Labs', N'456 Science Blvd, Labville', N'xyz@example.com')
INSERT [dbo].[manufacturer] ([ID], [Name], [Address], [Email]) VALUES (3, N'Medical Innovations', N'789 Health Ave, Cureburg', N'med@example.com')
INSERT [dbo].[manufacturer] ([ID], [Name], [Address], [Email]) VALUES (4, N'PharmaCare', N'101 Medicine Road, Remedy City', N'pharmacare@example.com')
INSERT [dbo].[manufacturer] ([ID], [Name], [Address], [Email]) VALUES (5, N'Global Health Solutions', N'555 Wellness Lane, Healington', N'globalhealth@example.com')
INSERT [dbo].[manufacturer] ([ID], [Name], [Address], [Email]) VALUES (6, N'CureTech Industries', N'888 Remedy Street, Medville', N'curetech@example.com')
INSERT [dbo].[manufacturer] ([ID], [Name], [Address], [Email]) VALUES (7, N'BioMed Pharma', N'202 Health Plaza, Biocity', N'biomed@example.com')
INSERT [dbo].[manufacturer] ([ID], [Name], [Address], [Email]) VALUES (8, N'LifeScience Innovators', N'303 Cure Avenue, Lifetown', N'lifescience@example.com')
INSERT [dbo].[manufacturer] ([ID], [Name], [Address], [Email]) VALUES (9, N'Nature Cure Pharmaceuticals', N'404 Herbal Lane, Naturville', N'naturecure@example.com')
INSERT [dbo].[manufacturer] ([ID], [Name], [Address], [Email]) VALUES (10, N'GenoMed Labs', N'505 Genetic Blvd, Genetica', N'genomed@example.com')
SET IDENTITY_INSERT [dbo].[manufacturer] OFF
GO
SET IDENTITY_INSERT [dbo].[medicine] ON 

INSERT [dbo].[medicine] ([ID], [manufacturer_ID], [Name], [Amount], [Dosage], [Payment]) VALUES (1, 1, N'PainRelief', 50, 10, N'Insurance')
INSERT [dbo].[medicine] ([ID], [manufacturer_ID], [Name], [Amount], [Dosage], [Payment]) VALUES (2, 2, N'ColdCure', 30, 5, N'Patient')
INSERT [dbo].[medicine] ([ID], [manufacturer_ID], [Name], [Amount], [Dosage], [Payment]) VALUES (3, 3, N'HeartMed', 20, 15, N'Insurance')
INSERT [dbo].[medicine] ([ID], [manufacturer_ID], [Name], [Amount], [Dosage], [Payment]) VALUES (4, 1, N'PainRelief', 30, 3, N'Insurance')
SET IDENTITY_INSERT [dbo].[medicine] OFF
GO
SET IDENTITY_INSERT [dbo].[specialization] ON 

INSERT [dbo].[specialization] ([ID], [Name], [Description]) VALUES (1, N'Cardiology', N'Specializing in heart-related issues')
INSERT [dbo].[specialization] ([ID], [Name], [Description]) VALUES (2, N'Orthopedics', N'Dealing with musculoskeletal disorders')
INSERT [dbo].[specialization] ([ID], [Name], [Description]) VALUES (3, N'Dermatology', N'Focus on skin conditions and diseases')
INSERT [dbo].[specialization] ([ID], [Name], [Description]) VALUES (4, N'Gastroenterology', N'Specializing in digestive system disorders')
INSERT [dbo].[specialization] ([ID], [Name], [Description]) VALUES (5, N'Neurology', N'Dealing with disorders of the nervous system')
INSERT [dbo].[specialization] ([ID], [Name], [Description]) VALUES (6, N'Ophthalmology', N'Focus on eye and vision care')
INSERT [dbo].[specialization] ([ID], [Name], [Description]) VALUES (7, N'Otolaryngology', N'Specializing in ear, nose, and throat disorders')
INSERT [dbo].[specialization] ([ID], [Name], [Description]) VALUES (8, N'Urology', N'Dealing with urinary system disorders')
INSERT [dbo].[specialization] ([ID], [Name], [Description]) VALUES (9, N'Endocrinology', N'Specializing in endocrine system disorders')
INSERT [dbo].[specialization] ([ID], [Name], [Description]) VALUES (10, N'Rheumatology', N'Focus on autoimmune and inflammatory disorders')
INSERT [dbo].[specialization] ([ID], [Name], [Description]) VALUES (11, N'Pediatrics', N'Specializing in the care of children')
INSERT [dbo].[specialization] ([ID], [Name], [Description]) VALUES (12, N'Geriatrics', N'Dealing with health issues of the elderly')
INSERT [dbo].[specialization] ([ID], [Name], [Description]) VALUES (13, N'Pulmonology', N'Specializing in respiratory system disorders')
INSERT [dbo].[specialization] ([ID], [Name], [Description]) VALUES (14, N'Hematology', N'Dealing with blood disorders')
SET IDENTITY_INSERT [dbo].[specialization] OFF
GO
SET IDENTITY_INSERT [dbo].[doctor] ON 

INSERT [dbo].[doctor] ([ID], [specialization_ID], [First_name], [Last_name], [Title], [Date_of_birth], [Telephone]) VALUES (1, 1, N'Sarah', N'Jones', N'Dr.', CAST(N'1980-03-12' AS Date), N'+12345678901')
INSERT [dbo].[doctor] ([ID], [specialization_ID], [First_name], [Last_name], [Title], [Date_of_birth], [Telephone]) VALUES (2, 2, N'Mark', N'Miller', N'Dr.', CAST(N'1975-09-20' AS Date), N'+19876543210')
INSERT [dbo].[doctor] ([ID], [specialization_ID], [First_name], [Last_name], [Title], [Date_of_birth], [Telephone]) VALUES (3, 3, N'Emily', N'White', N'PhD', CAST(N'1988-06-05' AS Date), N'+11223344556')
INSERT [dbo].[doctor] ([ID], [specialization_ID], [First_name], [Last_name], [Title], [Date_of_birth], [Telephone]) VALUES (4, 1, N'Jacob', N'Smith', N'Dr.', CAST(N'1990-02-22' AS Date), N'+420584754896')
SET IDENTITY_INSERT [dbo].[doctor] OFF
GO
SET IDENTITY_INSERT [dbo].[eprescription] ON 

INSERT [dbo].[eprescription] ([ID], [patient_ID], [medicine_ID], [doctor_ID], [Issued], [Validity]) VALUES (1, 1, 1, 1, CAST(N'2022-01-05' AS Date), CAST(N'2022-02-05' AS Date))
INSERT [dbo].[eprescription] ([ID], [patient_ID], [medicine_ID], [doctor_ID], [Issued], [Validity]) VALUES (2, 2, 2, 2, CAST(N'2022-02-10' AS Date), CAST(N'2022-03-10' AS Date))
INSERT [dbo].[eprescription] ([ID], [patient_ID], [medicine_ID], [doctor_ID], [Issued], [Validity]) VALUES (3, 3, 3, 3, CAST(N'2022-03-15' AS Date), CAST(N'2022-04-15' AS Date))
SET IDENTITY_INSERT [dbo].[eprescription] OFF
GO
