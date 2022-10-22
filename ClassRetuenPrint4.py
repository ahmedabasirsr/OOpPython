class Student_date:
    
  def __init__(self,name,age):
      """ this function does not returne any value because this is
      a special metod
      """
        self.name = name
        self.age = age
        print (f"Wlcom {self.name} to the collage,he has {self.age}")



 def ppp(self, name, age):
     """ this function does print and returne any value"""
     self.name = name
     self.age = age
     print(f"Wlcom {self.name} to the collage,he has {self.age}")
     return (self.name, self.age)


s1 = Student_date()
m=s1.ppp("Ahmed",55)
print(m)

"""
s1,s5 = Student_date("Ali",20)
print(type(s1))
s2 = Student_date("Ahmed",22)
s3 = Student_date("Husian",21)
s4 = Student_date("Abas",19)
"""