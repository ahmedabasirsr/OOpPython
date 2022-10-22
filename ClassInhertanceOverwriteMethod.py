class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        return f"nam is {self.name} and age is {self.age}"

class Man(Person):
# propeties of the class men are gender and number of men
    gender ="Male" 
    no_of_men = 0
# inhertance from class Person(from __init ==> name and age)
# man class will hans onther atribut voice
    def __init__(self,name,age,voice):
        super().__init__(name,age)
        #in this way add onther atribut voice
        self.voice = voice
        Man.no_of_men +=1


#inhertance from class Person(display =>nam is {self.name} and age is {self.age}")
# This metod is overwrite from person
    def display(self):
        """overwrite function, its has string(from person class,function display
        and new display (voice and gender)"""
        string = super().display()# take complet is person in variabl string
        return string +f" and voice is {self.voice} and gender is {self.gender}"


man1 = Man("Ahmed",60,"hard")
""" print display from class Person
and  print display from class Man
"""
print (man1.display())
print (Man.no_of_men)
man2 = Person("Ali",45)       # print only display from class Person 
print (man2.display())
