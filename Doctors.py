
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




