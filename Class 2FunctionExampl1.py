##############Dunder Function#################
#Duplicate Under-class order has list cart and neme customer ##
##############################################

class Order:
    def __init__(self,cart,customer):
        self.cart = cart
        self.customer = customer

    def get_cart_len(self):
        return len(self.cart)


order1=Order(["laptop","monitor"],"Svetozar")
#print("TypeError: object of type 'Order' has no len()",len(order1))
print (" call method get_cart_len==>2: ",order1.get_cart_len())

# I want to to slove this error(TypeError: object of type 'Order' has no len())
# slove in DunderFunction Example2
