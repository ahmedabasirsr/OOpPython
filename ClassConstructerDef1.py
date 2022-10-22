class Digit:
    """ Class works as calcualter and takes 2 argument throught __init__"""
    def __init__(self,a,b):
        """constructor function has 2 numbers """
        self.a = a
        self.b = b

    def add1(self):
        """add1 function  adds 2 number"""
        return self.a + self.b

    def mul(self):
        """mul function  multiplication 2 number"""
        return  self.a * self.b

    def div(self):
        """mul function  division 2 number"""
        return self.a/self.b

    def subt(self):
        """mul function  subtracts 2 number"""
        return self.a - self.b

x = Digit(10,5)
print(10,5,"==>",x.add1(), x.mul(), x.div(),x.subt())

y = Digit(8,4)
r = y.add1()
r1 = y.mul()
r2 = y.div()
r3 = y.subt()
print(8,4,"==>",r,r1,r2,r3)
