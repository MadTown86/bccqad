# Episode 13: Classes 2 of 2 : Inheritence
from typing import List

"""
The class is one of the most complex and powerful concepts in many programming languages.

It allows for so much customization that it will require a while for you to even brush the surface of
it's full capabilities.  I intend to cover nearly everything there is to know about classes, but first
we will start with the concept of inheritence.  

What this means is that you can create a class that is a direct descendent of a 'parent' class.  The
child class inherits all of the features of the parent class.

However, unlike humans (heh), classes can have an infinite number of parents. This creates a family
tree for each class. 

The order of the parents does matter because of the following two things:

1. Attribute inheritence search
2. Method resolution order

I will discuss why these two things are important a bit later on after a few examples.
"""

# Think of trying to categorize the types of food at McDonalds

"""
(I am using McDonalds because I believe everyone the world over can relate to some menu items at McDonalds.
Whether you think that is fortunate or unfortunate is for you to decide, I am staying out of it.)
"""

class Entree:
    """
    A base class that represents an entree on the menu.
    """
    def __init__(self, cost: int, price: int): # This is called a constructor. This line makes the class require arguments when instantiated.
        self._cost = cost # You can use underscores to indicate that these are private variables that shouldn't be accessed directly.
        self._price = price

    def update_price(self, value): # This is a setter method that allows you to change the price of the entree.
        self._price = value

    def update_cost(self, value): # This is a setter method that allows you to change the cost of the entree.
        self._cost = value

class Burger(Entree):
    """
    A class that represents a burger on the menu.

    Note: this class is a child of the Entree class.  This means that it inherits all of the features of the Entree class.

    You do NOT have to redefine the __init__ method or the update_price or update_cost methods in this class.

    If you do, you will be overriding the methods in the parent class DUE to the aforementioned "method resolution order".
    """
    def get_name(self):
        return self._name
    def get_cost(self):
        return self._cost
    def get_price(self):
        return self._price
    def get_ingredients(self):
        return self._ingredients
    
    def set_name(self, name: str):
        self._name = name
    def set_ingredients(self, ingredients: List[str, str]):
        self._ingredients = ingredients


B = Burger(1.00, 2.00) # Creating a new instance of Burger class using the constructor of the Entree class.  INHERITED
B.set_name("Big Mac") # Setting the name of the burger method, found in the Burger class.
B.set_ingredients(["Lettuce", "Tomato", "Pickles", "Onions", "4oz Beef Patty"]) # Burger class
B.update_price(2.50) # Entree Class method
B.update_cost(1.50) # Entree Class method

"""
Even with this small example, you can start to see the power of classes and how they can be used to create a hierarchy of objects.

If you wanted to implement working versions of a program to solve simple problems first and then build on it to create a more complex program,
you can do this with classes in a way that 'adding' new features to a program doesn't break the existing code.

You should also start to see how it will be important to understand how the class hierarchy works.  Especially if you start to work with
other people's code and have to try to make sense of an extraoardinarly large and complex class hierarchy that is not well documented.  You may
find that some larger OOP programs still require the use of parents, grandparents, great grandparents, children, grandchildren, etc., to function 
properly.
"""

class AdvancedBurger(Burger, Entree):
    """
    An updated version of the Burger class that is rearranging the inheritence order by updating the constructor.
    """
    def __init__(self, cost: int, price: int, name: str, ingredients: dict):
        Entree.__init__(cost, price) # Calling the constructor of the Entree class.
        self._name = name
        self._ingredients = ingredients

    def set_ingredients(self):
        raise NotImplementedError("This method is not available in the AdvancedBurger class.")


    


