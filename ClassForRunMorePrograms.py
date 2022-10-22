class Mixprogramms:
    def __init__(self):
        print (" Mixprograms have many programs".center(80,"*"))
        print (" Press [1] to start Odd-even programm")
        print (" Press [2] to start Summ-Averrage programm")
        print (" Press [3] to start Multiplcation tabel programm")


######################################################################
        # Method can to choose user any programs(methods of class)
######################################################################
    def press_123(self):
        while True :
            try:
                     
                press = int(input(" Enter 1,2 or 3 to choose programm: ")) 
                if press == 1 :
                    self.Odd_even()
                elif press == 2:
                    self.summ_averrage()
                elif press == 3:
                    self.multiplcation()
            except ValueError:
                    print ("Error please press 1,2 or 3")
##########################################################################
        # Method disply number odd or even
##########################################################################
    def Odd_even(self):
        
        print (" programm knows number odd or even".center(80,"*"))
        print(" please enter only integer number if you will exist enter x")

        while True:
            
            number = input("Enter integer number ")
            
            if number == "x" :
                print (" you enter x to exist, thank you")
                break
            try:
                number = int(number)
                if number%2==0:
                    print ("Number is Even ")
                else:
                    print (" Number is odd ")
         
            except ValueError:
                print ("Please enter an valiad number")
###############################################################################
        # Method can to sum any may numbers and count averrage them
###############################################################################
    def summ_averrage(self):
        
        print ("This programm will take serveral numbers and print the sum and avaraage of them")
        print (" how many number would you like to sum : ".center(80,"*"))

        sum_number = 0
        count_number =0

        try:    
            number = int(input("enter numbers of sum numbers "))


            while count_number < number :
                numbers = float(input("enter values numbers of sum numbers: "))
                sum_number +=numbers
                count_number +=1

            print ("Sum of numbers is =", sum_number,"Avarrage of numbers is =", sum_number/number)
                
        except ValueError :
            print("Ivaild error number")

################################################################################
        #Metod displt Multiplcation table
################################################################################
    def multiplcation(self):
        print (" Program for choose multiplcation table".center(80,"*"))
        print ("**************************************".center(80,"*"))

        while True:
   
            start_nuber = int(input("start number of talble multiplcation: "))
            end_number = int(input("End number of talble multiplcation: "))
            
            for i in range (start_nuber,end_number+1):
                for j in range(1,end_number+1):
                    print(i,"x",j,"=",i*j)
                print("*********")
            k = input(" enter any key will you continue or x will you exist ")
            if k== "x" :
                break
###################################################################################

x = Mixprogramms()
x.press_123()
