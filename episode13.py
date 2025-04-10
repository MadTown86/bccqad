# Episode 13: Classes 2: Inheritance 
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

# Think of trying to categorize the types of food at a burger joint.

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
    def set_ingredients(self, ingredients: List[str]):
        self._ingredients = ingredients


B = Burger(1.00, 2.00) # Creating a new instance of Burger class using the constructor of the Entree class.  INHERITED

print(B._price)
print(B._cost)

B.set_name("Big Mac") # Setting the name of the burger method, found in the Burger class.

print(B.get_name())

B.set_ingredients(["Lettuce", "Tomato", "Pickles", "Onions", "4oz Beef Patty"]) # Burger class

B.update_price(2.50) # Entree Class method

B.update_cost(1.50) # Entree Class method

print(B.get_price())
print(B.get_cost())



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




# Inheritence Search Example - Method Resolution:

"""
Note in the below example that the order of inheritence matters.  

Again the method resolution order is searching the tree for the first matching method.

1. If method is in the child class, it will be used.
2. If method is not in the child class, it will search the first parent class for the method.
3. If method is not in the first parent class, it will search the second parent class for the method.
4. and so on.
"""

class GrandParent:
    def __init__(self, name):
        print("GrandParent constructor")
        self.name = name
    def method1(self):
        return "GrandParent method1"
    def method2(self):
        return "GrandParent method2"
    def method3(self):
        return "GrandParent method3"
    def method5(self):
        return "GrandParent method5"
    
class Parent1(GrandParent):
    def __init__(self, name):
        GrandParent.__init__(self, name)  # Call the constructor of GrandParent
    def method1(self):
        return "Parent1 method1"
    def parent1_special_method(self):
        return "Parent1 special method"
    
class Parent2(GrandParent):
    def __init__(self, name): # Overriding the constructor of GrandParent
        self.name = name
    def method1(self):
        return "Parent2 method1"
    def method2(self):
        return "Parent2 method2"
    def method3(self):
        return "Parent2 method3"
    def parent2_special_method(self):
        return "Parent2 special method"
    
class Parent3(GrandParent):
    def __init__(self, name):
        print("Parent3 constructor")
        self.name = name
    def method1(self):
        return "Parent3 method1"
    def method2(self):
        return "Parent3 method2"
    def method3(self):
        return GrandParent.method3(self)  # Call GrandParent's method3
    def method4(self):
        return "Parent3 method4"
    def parent3_special_method(self):
        return "Parent3 special method"
    
class OtherGrandParent:
    def method1(self):
        return "OtherGrandParent method1"
    
class Child10(Parent1, Parent2, Parent3):
    def __init__(self, name):
        Parent1.__init__(self, name)  # Call Parent1's constructor

    def method1(self):
        Parent3.method1(self)
    
class Parent4(OtherGrandParent, Parent3):
    pass

# 
# Child classes inheriting from multiple parents
# Order of inheritance changes which same-name method is called
class Child(Parent1, Parent2, Parent3):
    pass

class Child2(Parent1, Parent3, Parent2):
    pass

class Child3(Parent2, Parent1, Parent3):
    pass

class Child4(Parent3, Parent2, Parent1):
    pass

class Child5(Parent4):
    pass


if __name__ == "__main__":
    # Creating instances of the different child classes and calling their methods
    C1 = Child("Child1")
    print(f'{C1.name} : {C1.method1()}')  # Calls method1 from Parent1
    print(C1.method2())  # Calls method2 from Parent2
    print(C1.method3())  # Calls method3 from GrandParent
    print(C1.method4())  # Calls method4 from Parent3
    print(C1.method5())  # Calls method5 from GrandParent

    print("\n")  

    C2 = Child2("Child2")
    print(f'{C2.name} : {C2.method1()}')  # Calls method1 from GrandParent
    print(C2.method2())  # Calls method2 from Parent1
    print(C2.method3())  # Calls method3 from Parent2
    print(C2.method4())  # Calls method4 from Parent3

    print("\n")

    C3 = Child3("Child3")
    print(f'{C3.name} : {C3.method1()}')  # Calls method1 from Parent2
    print(C3.method2())  # Calls method2 from Parent1
    print(C3.method3())  # Calls method3 from Parent3
    print(C3.method4())  # Calls method4 from Parent3

    print("\n")
    
    C4 = Child4("Child4")
    print(f'{C4.name} : {C4.method1()}')  # Calls method1 from Parent3
    print(C4.method2())  # Calls method2 from Parent2
    print(C4.method3())  # Calls method3 from Parent1
    print(C4.method4())  # Calls method4 from Parent3
    print(C4.method5())  # Calls method5 from Parent3

    print("\n")

    C5 = Child5("Child5")
    print(f'{C5.name} : {C5.method1()}')  # Calls method1 from OtherGrandParent
    print(C5.method2())  # Calls method2 from Parent3
    print(C5.method3())  # Calls method3 from Parent3
    print(C5.method4())  # Calls method4 from Parent3
    print(C5.method5())  # Calls method5 from Parent3

"""
The important thing to note here is just where the method call resolves for each child and
which constructor is used.
"""
