from Patients import Patient
file_for_patients = 'patients.txt'
list_of_patients = []

class PatientManager:
    def __init__(self):
        self.patients = []

    def formatPatientInfo(self, txt_to_format):
        formatted = '_'.join(txt_to_format)
        return formatted

    
    def enterPatientInfo(self):
        self.pid = int(input("Enter patients's ID: "))
        self.name = input("Enter patient's name: ")
        self.disease = input("Enter patient's disease: ")
        self.gender = input("Enter patient's gender: ")
        self.age = int(input("Enter patient's age: "))
        print(f'\nPatient whose ID is {self.pid} has been added\n')
        return [str(self.pid), self.name, self.disease, self.gender, str(self.age)]

    
    def readPatientsFile(self):
        file = open(file_for_patients, 'r')
        list_of_patients = []
        for each_line in file:
            list_of_patients.append(each_line.rstrip().split('_'))
        file.close()
        return list_of_patients

    
    def searchPatientByID(self):
        id_number = int(input("Enter the Patient's ID: "))
        list_of_patients = self.readPatientsFile()
        total_rows = len(list_of_patients)
        current_row = 1
        last_row = total_rows - 1
        patient_found = ''
        while current_row < total_rows:
            if str(id_number) == list_of_patients[current_row][0]:
                print(f'{"ID":<10}' + f'{"Name":<15}' + f'{"Disease":<15}' + f'{"Gender":<15}' + "Age",end='\n\n')
                print(
                    f'{list_of_patients[current_row][0]:<10}' + f'{list_of_patients[current_row][1]:<15}' + f'{list_of_patients[current_row][2]:<15}' + f'{list_of_patients[current_row][3]:<15}' +
                    list_of_patients[current_row][4]
                    )
                print()
                patient_found = 'yes'
                break
            if patient_found != 'yes' and current_row == last_row:
                print("Can't find the patient with the same ID on the system.\n")
            current_row += 1

    
    def editPatientInfo(self, list_of_patients):
        id_number = int(input("Please enter the id of the patient that you want to edit their information: "))
        self.pid = id_number
        total_rows = len(list_of_patients)
        current_row = 1
        last_row = total_rows - 1
        patient_found = False
        while current_row < total_rows:
            if str(id_number) == list_of_patients[current_row][0]:
                input_name = input("Enter new Name: ")
                input_disease = input("Enter new disease: ")
                input_gender = input("Enter new gender: ")
                input_age = input("Enter new age: ")
                list_of_patients[current_row][1] = input_name
                list_of_patients[current_row][2] = input_disease
                list_of_patients[current_row][3] = input_gender
                list_of_patients[current_row][4] = input_age
                patient_found = True
                break
            current_row += 1
        if not patient_found or current_row == last_row:
            print("Can't find the patient with the same ID on the system\n")
        else:
            self.writeListOfPatientsToFile(list_of_patients)
            print(f'\nPatient whose ID is {id_number} has been edited\n')

    
    def displayPatientInfo(self):
        list_of_patients = self.readPatientsFile()
        total_rows = len(list_of_patients)
        current_row = 1
        print(f'{"ID":<10}' + f'{"Name":<15}' + f'{"Disease":<15}' + f'{"Gender":<15}' + "Age",end='\n\n')
        while current_row < total_rows:
            print(
                f'{list_of_patients[current_row][0]:<10}' + f'{list_of_patients[current_row][1]:<15}' + f'{list_of_patients[current_row][2]:<15}' + f'{list_of_patients[current_row][3]:<15}' +
                list_of_patients[current_row][4])
            print()
            current_row += 1

   
    def writeListOfPatientsToFile(self, list_of_patients):
        patients_file = open(file_for_patients, 'w')
        for each_line in list_of_patients:
            add_line = self.formatPatientInfo(each_line)
            patients_file.write(add_line)
            patients_file.write('\n')
        patients_file.close()

    
    def addPatientToFile(self):
        list_of_patients = self.readPatientsFile()
        self.writeListOfPatientsToFile(list_of_patients)
        patient_to_add = self.enterPatientInfo()
        patients_file = open(file_for_patients, 'a')
        patients_file.write(self.formatPatientInfo(patient_to_add))
        patients_file.write('\n')
        patients_file.close()


def patientMenu():

    my_patient = PatientManager()
    isRunning = True

    while isRunning:

        #list of patients
        patient_list = my_patient.readPatientsFile()

        patients_menu = int(input("Patients Menu:\n1 - Display patients list\n2 - Search for patient by ID\n3 - Add patient\n4 - Edit patient info\n5 - Back to the Main Menu\n>>> "))

        if patients_menu == 1:
            my_patient.displayPatientInfo() 
        if patients_menu == 2:
            my_patient.searchPatientByID()
        if patients_menu == 3:
            my_patient.addPatientToFile()
        if patients_menu == 4:
            my_patient.editPatientInfo(patient_list)
        if patients_menu == 5:
            isRunning = False

if __name__ == "__main__":
    patientMenu()                      