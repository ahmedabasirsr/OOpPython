
class Student:
##############################################################
#number objects of students=> start 0 this is atrbiut of class
##############################################################
    number_of_sutdents = 0
#############################################################
# initial method of class Student, it has 3 paremeters
#############################################################
    def __init__(self, name, age, courses):
        self.name = name
        self.age = age
        self.courses = courses # list courses
        Student.number_of_sutdents +=1  # sum of stuents number

#############################################################
# Instance method of class whose disply atributes of class 
#############################################################
    def disply_atributs(self):
        print (f"my name is {self.name} and my age is {self.age}")

        
 #############################################################
# Instance method of class whose disply atributes of class 
#############################################################
    def is_old_age(self,numb):
        if self.age <= numb:
            print (" student is old")
        else:
            print ("student is not old")





stud1 = Student("Ahmed",32,["cs","html","python"])
stud2 = Student("Ali",35,["jscribt","os","math"])
stud1.disply_atributs()
stud2.disply_atributs()
stud1.is_old_age(25)
stud2.is_old_age(40)

        
