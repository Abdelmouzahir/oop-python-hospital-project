
class Doctor:
    def __init__(self,doctor_id,name,specialization,working_time,qualification,room_number):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization
        self.working_time = working_time
        self.qualification = qualification
        self.room_number = room_number

    def get_doctor_id(self):
        return self.doctor_id
    def get_name(self):
        return self.name
    def get_specialization(self):
        return self.specialization 
    def get_working_time(self):
        return self.working_time
    def get_qualification(self):
        return self.qualification
    def get_room_number(self):
        return self.room_number
    
    def set_doctor_id(self,new_id):
        self.doctor_id = new_id
    def set_name(self,new_name):
        self.name = new_name
    def set_specialization(self,new_specialization):
        self.specialization = new_specialization
    def set_working_time(self,new_working_time):
        self.working_time = new_working_time
    def set_qualification(self,new_qualification):
        self.qualification = new_qualification
    def set_room_number(self,new_room_number):
        self.room_number = new_room_number
    
    def __repr__(self):
        return "{0:4} {1:22} {2:15} {3:15} {4:15} {5}".format(self.doctor_id, self.name, self.specialization, self.working_time, self.qualification, self.room_number)


    def formatDrInfo(self):
        
        formattedDoctor = "{0}_{1}_{2}_{3}_{4}_{5}".format(self.doctor_id, self.name, self.specialization, self.working_time, self.qualification, self.room_number)
        return formattedDoctor


def writeListOfDoctorsToFile(input_list):
    open('doctors.txt', 'w').close()
    f = open("doctors.txt", "a")

    f.write("id_name_specilist_timing_qualification_roomNb")
    f.write("\n")

    for i in range(1, len(input_list)):
        string = input_list[i].formatDrInfo()
        f.write(string)
        f.write("\n")
        
    f.close()



def addDrToFile(doctor):
    f = open("doctors.txt", "a")
    string = doctor.formatDrInfo()
    f.write("\n" + string)
    f.close()



def enterDrInfo():
    doctor_id = input("Enter the doctor's ID: ")
    name = input("Enter the doctor's name: ")
    spec = input("Enter the doctor's speciality: ")
    time = input("Enter the doctor's timing (e.g., 7am-10pm): ")
    qual = input("Enter the doctor's qualification: ")
    room = input("Enter the doctor's room number: ")
    print(f'\nDoctor whose ID is {doctor_id} has been added\n')
    
    return Doctor(doctor_id,name,spec,time,qual,room)
   

def displayDoctorInfo(doctor):
    print("Id   Name                   Speciality      Timing          Qualification   Room Number\n")
    print(doctor)


def searchDoctorById(list):
    selected_id = input("Please enter the doctor id: ")  
    is_there = 0
    for i in range(0, len(list)):
        if str(list[i].doctor_id) == selected_id:
            displayDoctorInfo(list[i])
            is_there = 1
    if is_there == 0:
        print("Can't find the doctor with the same ID on the system\n")
            

def searchDoctorByName(list):
    selected_name = input("Please enter the name of the doctor: ")
    is_there = 0
    for i in range(0, len(list)):
        if str(list[i].name) == selected_name:
            displayDoctorInfo(list[i])
            is_there = 1
    if is_there == 0:
        print("Can't find the doctor with the same name on the system\n")

def editDoctorInfo(list):
    selected_id = input("Please enter the id of the doctor that you want to edit their information: ")
    is_there = 0
    for i in range(0, len(list)):
        if str(list[i].doctor_id) == selected_id:
            is_there = 1
            id = selected_id
            name = input("Enter the doctor's name: ")
            spec = input("Enter the doctor's speciality: ")
            time = input("Enter the doctor's timing (e.g., 7am-10pm): ")
            qual = input("Enter the doctor's qualification: ")
            room = input("Enter the doctor's room number: ")
            inputDoctor = Doctor(id,name,spec,time,qual,room)
            list[i] = inputDoctor
            print(f'\nDoctor whose ID is {id} has been edited\n')
    if is_there == 0:
        print("Can't find the doctor with the same name on the system")
    

def displayDoctorsList():
    doctorList = readDoctorsFile()
    print("Id   Name                   Speciality      Timing          Qualification   Room Number\n")
    for i in range(1, len(doctorList)):
        print(doctorList[i])
        print("")

def readDoctorsFile():
    doctorList = []
    with open('doctors.txt') as f:
        lines = f.readlines()
        for line in lines:
            row = line.split('_')
            doctor_id, name, specilist, timing, qualification, roomNumber = [i.strip() for i in row]
            doctor = Doctor(doctor_id, name, specilist, timing, qualification, roomNumber)
            doctorList.append(doctor)
    f.close()
    return doctorList     

#Testing the doctors case
def doctorMenu():
    listOfDoctors = readDoctorsFile()
    doctorMenuSelection = True
    while doctorMenuSelection:
        choice = int(input("Doctors Menu:\n1 - Display Doctors list\n2 - Search for doctor by ID\n3 - Search for doctor by name\n4 - Add doctor\n5 - Edit doctor into\n6 - Back to the Main Menu\n>>> "))
        if choice == 1: 
            displayDoctorsList()
        if choice == 2:
            searchDoctorById(listOfDoctors)
        if choice == 3:
            searchDoctorByName(listOfDoctors)
        if choice == 4:
            inputDoctor = enterDrInfo()
            addDrToFile(inputDoctor)
        if choice == 5:
            editDoctorInfo(listOfDoctors)
            writeListOfDoctorsToFile(listOfDoctors)
        if choice == 6:
            doctorMenuSelection = False

if __name__ == "__main__":
    doctorMenu()                   