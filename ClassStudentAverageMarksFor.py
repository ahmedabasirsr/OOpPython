class Student_date:
    # this class date, it takes name and last nam and crate empty list marks
    
    def __init__(self,name,lastname):
        self.name = name
        self.lastname = lastname
        self.marks = []
        print (f"Wlcom {self.name} {self.lastname} to the collage")

    def fill_list_marks(self,mark):
        # function fill marks of student in list marks. it takes mark and add in list marks
        self.marks.append(mark)


    def avarrage_marks(self):
        # function return average of list marks
        return(sum(self.marks)/len(self.marks))

# for loop of numbers students
for i in range (1,3):
    n=input("enter name of student: ")
    ln=input("enter last name of student: ")
    s1 = Student_date(n,ln)
    # create object s1 from student
    for j in range (1,6):
        # for loop of numbers marks
        d = int(input("enter mark of student: "))       
        s1.fill_list_marks(d)
    print(" print fill list marks:",s1.marks)
    av =s1.avarrage_marks()
    print (i,")",f"avarrage marks of {n} {ln}  : ".center(80,"-"),av)
#.center(100,"-") this sintax center
#for comments and add characher"-"

