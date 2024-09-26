class Std_Info():
    def __init__(self, s_ID, s_Name, s_DoB):
        self.s_ID = s_ID
        self.s_Name = s_Name
        self.s_DoB = s_DoB

    #set
    def set_s_Name(self,s_Name):
        self.s_Name = s_Name
    def set_s_ID(self,s_ID):
        self.s_ID = s_ID
    def set_s_DoB(self,S_Dob):
        self.s_DoB = S_Dob

    #get
    def get_s_Name(self):
        return self.s_Name
    def get_s_ID(self):
        return self.s_ID
    def get_s_DoB(self):
        return self.S_DoB

class Course_Info():
    def __init__(self, c_ID, c_Name):
        self.c_ID = c_ID
        self.c_Name = c_Name

    #set
    def set_c_Name(self,c_Name):
        self.c_Name = c_Name
    def set_c_ID(self,c_ID):
        self.c_ID = c_ID

    #get
    def get_c_Name(self):
        return self.c_Name
    def get_c_ID(self):
        return self.c_ID

class mark_Course():

    def __init__(self, s_ID, c_ID,mark):
        self.s_ID = s_ID
        self.c_ID = c_ID
        self.mark = mark

    #set
    def set_s_ID(self,s_ID):
        self.s_ID = s_ID
    def set_c_ID(self,c_ID):
        self.c_ID = c_ID
    def set_mark(self,mark):
        self.mark = mark

    #get
    def get_s_ID(self):
        return self.s_ID
    def get_c_ID(self):
        return self.c_ID
    def get_mark(self):
        return self.mark

class averageGPA():
def __init__(self,id,name,gpa):
    self.id = id
    self.name = name
    self.gpa = gpa
    
    def display(self):
        print(self.id, end = "\t\t")
        print(self.name, end = "\t\t")
        print(self.gpa)