##############Dunder Function#################
#Duplicate Under-class order has list cart and neme customer ##
##############################################

class Order:
    def __init__(self,cart,customer):
        self.cart = cart
        self.customer = customer

    def __len__(self):       ########## Do not forget this method return integer##########
        #object directlu use lenlen ==> (nameobject)
        return len(self.cart)

    def __call__(self):
        # object directlu use call ==> nameobject()
        return self.customer    ########## call method calls object, so to do smothing#######

    def __str__(self):
        # object directlu use str ==> new format string(name customer bouth list articles)
        return f"{self.customer} bouth {self.cart}" #allways return string

    def __bool__(self):
        # object directlu use bool
        return len(self.cart)>0   ########## if list cart has atleast one parmeter==> true

order1=Order(["laptop","monitor","mouse"],"Svetozar")
print (bool(order1)," ===> result allways true or false")

if order1:                      #if order1 is true 
    print (f"{order1.customer} order is processing")
else:
    print ("Shopping cart is empty")


