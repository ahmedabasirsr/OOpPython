class Man():
    def __init__(self,name,age):
        self.name = name
        self.age = age
####################################
#Dunder method add  with change her work
#####################################
    def __add__(self,other):
        #function adds names for 2 object(man1 and man2) and adde ages for man1 and man2
        names = self.name + " and " +other.name # other object(man2)
        ages = self.age + other.age
        return f" names combined are {names} and sum of ages is {ages}"

####################################
#Dunder method lt with change her work
#####################################
    def __lt__(self,other):
        # function compars 2 objects(age of man1 and man2
        return self.age < other.age
    



man1 = Man("Ahmed", 40)
man2 = Man ("ali", 30)
print (man1 + man2)  # this line works only through method add
print (man1<man2)    # this line works only through metod lt
