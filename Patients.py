class Patient:
    def __init__(self, pid=-1, name='', disease='', gender='', age=-1):
        if pid != -1:
            self.pid = pid
        if name != '':
            self.name = name
        if disease != '':
            self.disease = disease
        if gender != '':
            self.gender = gender
        if age != -1:
            self.age = age
    def get_Patient_id(self):
        return self.pid
    def get_Pname(self):
        return self.name
    def get_disease(self):
        return self.disease 
    def get_gender(self):
        return self.gender
    def get_age(self):
        return self.age
    def set_pid(self,new_Pid):
        self.pid = new_Pid
    def set_Pname(self,new_Pname):
        self.name = new_Pname
    def set_disease(self,new_disease):
        self.disease = new_disease
    def set_gender(self,new_gender):
        self.gender = new_gender
    def set_age(self,age_qualification):
        self.age = age_qualification