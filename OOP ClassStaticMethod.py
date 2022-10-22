#Static method call from class. it gives arguments or not, Depends on the job
# Static method not takes any atributes from initail class
# Static method is utilty method for class  or nay method in class

class Math:

    @staticmethod
    def add (x,y):
        return x+y

    @staticmethod
    def add5 (num):
        return num+5
    
    @staticmethod
    def add10 (num):
        return num+10
    
    @staticmethod
    def PI():
        return 3.14

m = Math
print(m.add(5,10))
print(m.add5(5))
print(m.add10(5))
# can call dirct from class
x = Math.add(5,10)
y = Math.add5(x)
z = Math.add10(y)
print (x,y,z)
    
    
