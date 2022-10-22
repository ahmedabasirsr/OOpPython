##############Dunder Function#################
#Duplicate Under-class order has list cart and neme customer ##
##############################################

class Order:
    def __init__(self,cart,customer):
        self.cart = cart
        self.customer = customer

    def __len__(self):
        ########## modifcation dunduner function len ########
        # Now I can use this function direct with any object of class Order##########
        return len(self.cart)

    def __call__(self):
        ########## modifcation dunduner function call ########
        ########## call method, now  calls(name custmor) with any object of class Order####
        return self.customer

    def __str__(self):
        #allways return string
        return f"{self.customer} bouth {self.cart}"




order1=Order(["laptop","monitor","mouse"],"Svetozar")
print (" with modifcation len method, now i can to get len for object: ",len(order1))
print ("call method calls object order1,to print name customer: ", order1())
#print (order1,"print object, allways will ==>","<__main__.Order object at 0x03D13950>")
print(order1)
order2=Order(["book","pencil"],"Markovic")
print("I use call withe object directly",order2())

