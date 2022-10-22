
class Student:
##############################################################
#number objects of students=> start 0 this is atrbiut of class
##############################################################
    number_of_sutdents = 0
#############################################################
# initial method of class Student, it has 3 paremeters
#############################################################
    def __init__(self, name, age, courses):
        self.__name = name # after add __ atribut name  be privte atribut
        self.__age = age
        self.__courses = courses # list courses
        Student.number_of_sutdents +=1  # sum of stuents number

#############################################################
# Instance method of class whose get atributes of class 
#############################################################

    def get_atribut_init(self):
        return self.__name, self.__age, self.__courses

#############################################################
# Instance method of class whose set atributes of class 
#############################################################

    def set_atribut_init(self,newname,newage,newcourses ):
       self.__name =newname
       self.__age =newage
       self.__courses = newcourses
        

#############################################################
# Instance method of class whose disply atributes of class 
#############################################################
    def disply_atributs(self):
        print (f"my name is {self.__name} and my age is {self.__age}")

        
 #########################################################################
# Instance method of class with 1 argument whose disply atributes of class 
###########################################################################
    def is_old_age(self,numb):
        if self.__age <= numb:
            print (" student is old")
        else:
            print ("student is not old")



#############################################################
# every cahage any atribut you cant that from method set_atribut_init and you dont change that dirct, because atributes
# now are privte in inaitl metode (add __ )
#############################################################

stud1 = Student("Ahmed",32,["cs","html","python"])
stud2 = Student("Ali",35,["jscribt","os","math"])
print(stud1.get_atribut_init())
stud1.set_atribut_init("husain", 55, ["mat","eng","arabic"])
print(stud1.get_atribut_init())

        
