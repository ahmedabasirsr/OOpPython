

class Pizza:
    def __init__(self,ingredients):
        self.ingredients = ingredients


    @classmethod
    def veg(cls):
        return cls(["mushrooms", "olives","onions"])

    @classmethod
    def margherita(cls):
        return cls(["mozarellra", "sauce"])

# we can to change method stre as we want#################
##########################################################
    def __str__(self):
        return f" Pizza ingredients are {self.ingredients}"

pizza1 = Pizza(["tomato","olives"])
pizza2 = Pizza.veg()
# __main__.Pizza object at 0x03E73A70> <__main__.Pizza object at 0x03E73C30
print(pizza1, pizza2) # disply only adress in memmory not text if you do not
######################## have method __str .

# Display every Dunder method whose class use, like __str__,__class__ ...
#print (dir(Pizza))
print(pizza1, pizza2)
