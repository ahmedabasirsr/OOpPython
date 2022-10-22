class Digit:
    def __init__(self,a,b):
        self.a =a
        self.b =b
    
    def operators(self):
        """return will return 4 values in type tuple"""
        return (self.a + self.b,self.a - self.b,self.a * self.b,self.a/self.b)


x = Digit(5,10)
r = x.operators()
print(r)    # results are in tuple
print (list(r)) # results change in list

