class Addation1:
    
    def __init__(self,x,y,z=0,d=0):
        self.x =x
        self.y =y
        self.z =z
        self.d =d
    

    def sump(self):
        """ sump 2 numbers"""
        return self.x+self.y



    
class Addation2(Addation1):
    """ class inhertance from class Addational"""

    def sump(self):
          """ this function has Polymorphism because it call sump but add 3 numbers """
          return self.x+self.y+self.z
    


class Addation3(Addation1):
    

    def sump(self):
        """ this function has Polymorphism because it call sump but add 4 numbers """
        return self.x+self.y+self.z+self.d




m = Addation1(5,9)
r = Addation2(3,5,2)
v = Addation3(3,5,2,1)

print (m.sump())
print (r.sump())
print (v.sump())











       
       
