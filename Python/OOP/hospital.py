# hospital.py
# Patient:
# Attributes:
# • Id: an id number
# • Name
# • Allergies
# • Bed number: should be none by default
# Hospital
# Attributes:
# • Patients: an empty array
# • Name: hospital name
# • Capacity: an integer indicating the maximum number of patients the hospital can hold.
# Methods:
# • Admit: add a patient to the list of patients. Assign the patient a bed number. If the length of the list is >= the capacity do not admit the patient. Return a message either confirming that admission is complete or saying the hospital is full.
# # • Discharge: look up and remove a patient from the list of patients. Change bed number for that patient back to none.
# id:idnumber
# name
# Allergies
# bednumber
# hospital
# patients
# hospitalname
# capacity
class Patients(object):
	bednumber =1
	patient_num = 1
	def __init__(self, patient, reason, *allergies ):
		for allergy in allergies:
			print(allergy)
		self.patient = patient
		self.patient_num = Patients.patient_num
		Patients.patient_num +=1
		self.reason = reason
		self.allergies = allergies
	def display(self):
		print("Patient Name: " + self.patient)

class Hospital(object):
	def __init__(self):
		self.patients = []
		self.patient_list = len(self.patients)
	def add(self, patients):
		self.patients.append(new_patient)
		self.patient_list = len(self.patients)
		return self
	def discharge(self, num):
		self.patients.pop(0)
		self.patient_list = len(self.patients)
		return self

# 	def admit(self):

# class Hospital(object):
# 	def __init__(self):
# 		self.name = name
# 		self.patients = patients
# 		self.capacity = capacity



# choc = Hospital("",200, "CHOC")
# choc.display()

patient_1 = Patients("Clayton Kershaw","Choking", "Postseason Wins","World Series","Postseason MVPs")
choc = Hospital
patient_1.discharge()
