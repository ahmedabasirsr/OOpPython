'''
variable a and b they are variables of class Digit(global)
   Global variable: vlues is constan in all cod
   local variable:  values is constant in only method
'''

class Digit():
    a = 20
    b =10

    def __init__(self,a,b):
        self.a =a
        self.b =b

    def add1(self):
        #self.a =a
        #self.b =b
        return (self.a + self.b)

    def mul(self):
        #self.a =a
        #self.b =b
        return  self.a * self.b 

    def div(self):
        
        return self.a/self.b
        

    def subt(self):
        return self.a - self.b


x = Digit(5,2)
print (x.add1(), x.subt(), x.div(),x.mul())
print ("print variable of class Digit",x.a, x.b)


