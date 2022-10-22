##############Dunder Function#################
#Duplicate Under-class order has list cart and neme customer ##
##############################################

class Order:
    def __init__(self,cart,customer):
        self.cart = cart
        self.customer = customer

    def __len__(self):          ########## Do not forget this method return integer##########
        return len(self.cart)

    def __call__(self):
        return self.customer    ########## call method calls object, so to do smothing#######

    def __str__(self):
        return f"{self.customer} bouth {self.cart}" #allways return string

    def __bool__(self):
        return len(self.cart)>0   ########## if list cart has atleast one parmeter==> true


    def add_item(self,other):
        # object directlu use add_item to add in list cart
        return self.cart.append(other)

    def __add__(self,other):
        self.cart.append(other)
        return self.cart


    def __add__(self,other):
        new_cart =self.cart.copy()
        new_cart.append(other)
        return Order(new_cart, self.customer)

    def __iadd__(self,other):
        self.cart.append(other)
        return self

    def __radd__(self,other):
        new_cart =self.cart.copy()
        new_cart.insert(0,other)
        return Order(new_cart, self.customer)

    def __getitem__(self,key):
        return self.cart[key]

    def __setitem__(self,key,value):
        self.cart[key] = value
        return self



order1=Order(["laptop","monitor","mouse"],"Svetozar")
order1.add_item("keyboard") # this one way
print ("\n Object use dirktly add_item",order1.cart)
order1+"usb stick"
print("\n Object use dirktly + for add item",order1.cart)          # this second way
order1 = order1 + "usb mem" # only this format write
print(order1.cart)          # this third way
order1 +="cellphon"
print(order1.cart)
order1 ="tv" + order1
print(order1.cart)
print (order1[2])
order1[2] = "Ekran"
print(order1)







