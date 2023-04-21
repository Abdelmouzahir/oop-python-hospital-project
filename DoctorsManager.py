from Doctors import Doctor
class DoctorsManager :
    def __init__(self):
        self.Doctors = []
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
                DoctorsManager.displayDoctorInfo(list[i])
                is_there = 1
        if is_there == 0:
            print("Can't find the doctor with the same ID on the system\n")
                

    def searchDoctorByName(list):
        selected_name = input("Please enter the name of the doctor: ")
        is_there = 0
        for i in range(0, len(list)):
            if str(list[i].name) == selected_name:
                DoctorsManager.displayDoctorInfo(list[i])
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
        doctorList = DoctorsManager.readDoctorsFile()
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
    

def doctorMenu():
    listOfDoctors = DoctorsManager.readDoctorsFile()
    doctorMenuSelection = True
    while doctorMenuSelection:
        choice = int(input("Doctors Menu:\n1 - Display Doctors list\n2 - Search for doctor by ID\n3 - Search for doctor by name\n4 - Add doctor\n5 - Edit doctor into\n6 - Back to the Main Menu\n>>> "))
        if choice == 1: 
            DoctorsManager.displayDoctorsList()
        if choice == 2:
            DoctorsManager.searchDoctorById(listOfDoctors)
        if choice == 3:
            DoctorsManager.searchDoctorByName(listOfDoctors)
        if choice == 4:
            inputDoctor = DoctorsManager.enterDrInfo()
            DoctorsManager.addDrToFile(inputDoctor)
        if choice == 5:
            DoctorsManager.editDoctorInfo(listOfDoctors)
            DoctorsManager.writeListOfDoctorsToFile(listOfDoctors)
        if choice == 6:
            doctorMenuSelection = False

if __name__ == "__main__":
   doctorMenu()                       