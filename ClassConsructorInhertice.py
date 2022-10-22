class animal:
    # Constructor Inheritance (Super)
    def __init__(self,name):
        #Method constructor has only 1 atribute name
        self.name = name
        


class Dog(animal):
    """this class child and inhertance from animal only name but we want
        to add onther atribute food """
    def __init__(self,name,food):
        super(Dog, self).__init__(name)
        """ write super(child class,self) and . init(name)"""
        self.food = food

class Inher_of(animal):
    # class has will only atribute name
    pass



x= Dog("Miko","fish")
print (x.name, x.food)
y =Inher_of("Samer")
print(y.name)
#print((y.food)) this line does not work because it not has atribut food

