
from datetime import date
class Student:

#############################################################
# initial method of class Student, it has 2 paremeters
#############################################################

    def __init__(self, name, age):
        self.name = name 
        self.age = age

#############################################################
# Instance method of class whose disply atributes of class 
#############################################################
    def disply_atributs(self):
        print (f"my name is {self.name} and my age is {self.age}")

#############################################################
# @classmethods: it not can to access atributes , but it can to change 
# her behavior work==> replace age to brith year
#############################################################

    @classmethod
    def from_birth_year(cls,name,birthyear):
        return cls(name, date.today().year-birthyear)

stud1 = Student("Ahmed",59)
stud1.disply_atributs()
stud2 = Student.from_birth_year("Ali",1993)
stud2.disply_atributs()





        
