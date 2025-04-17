# Episode 13: Answer

#1. Create a class class tree for a pizza parlour. The class tree should include the
# following classes:
#     - Entree (base class)
#     - Pizza (child class of Entree)
#     - Topping (child class of Pizza)
#     - Crust (child class of Pizza)
#     - Sauce (child class of Pizza)
#     - Cheese (child class of Pizza)

class Entree:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price
        self.ingredients = []

    def setName(self, name: str) -> None:
        self.name = name

    def getName(self) -> str:
        return self.name
    
    def setPrice(self, price: float) -> None:
        self.price = price
    
    def getPrice(self) -> float:
        return self.price
    
    def addIngredient(self, ingredient: str) -> None:
        self.ingredients.append(ingredient)
    
    def getIngredients(self) -> list:
        return self.ingredients
    
    def removeIngredient(self, ingredient: str) -> None:
        if ingredient in self.ingredients:
            self.ingredients.remove(ingredient)
        else:
            print(f"{ingredient} not found in ingredients list.")

class Pizza(Entree):
    def __init__(self, name: str, price: float, crust: str, sauce: str, cheese: str):
        super().__init__(name, price)
        self.crust = crust
        self.sauce = sauce
        self.cheese = cheese

    def setCrust(self, crust: str) -> None:
        self.crust = crust

    def getCrust(self) -> str:
        return self.crust
    
    def setSauce(self, sauce: str) -> None:
        self.sauce = sauce

    def getSauce(self) -> str:
        return self.sauce
    
    def setCheese(self, cheese: str) -> None:
        self.cheese = cheese

    def getCheese(self) -> str:
        return self.cheese
    
    def addTopping(self, topping: str) -> None:
        self.addIngredient(topping)

    def removeTopping(self, topping: str) -> None:
        self.removeIngredient(topping)

"""
I am going to stop here because this was more of a trick question than anything.

The reason being, the way I stated to have the class tree organized doesn't make
much sense because the Topping, Crust, Sauce, and Cheese classes
don't make sense as a subclass of Pizza.
"""

#1A. Do you believe this is the best way to create a class tree for a pizza parlour?
#     - Why or why not?

"""
When organizing classes, it is important to think about the desired end result.
You want to utilize inheritance to decrease the amount of code being written and
to standardize the organization of information.  For this reason, the base class
should be the most general class that has functionality that is common and useful
to ALL subclasses.  

Topping, Crust, Sauce, and Cheese should not be subclasses of
Pizza.
"""
#2. Re-Create the class tree for a pizza parlour, but think of the best way to minimize overall code.
"""
I am going to make two base classes and try to organize the data in a way that 
makes more sense.
"""

# Ingredient -> Topping, Crust, Sauce, Cheese
class Ingredient:
    """
    Base class for all ingredients in any entree.

    In this way, I can alter only the subclasses of ingredient for unique 
    functionality.
    """
    def __init__(self, name: str, cost: float = 0.00, unit: str = "grams"):
        self.name = name
        self.cost = cost
        self.unit = unit

    def setName(self, name: str) -> None:
        self.name = name

    def getName(self) -> str:
        return self.name
    
    def setPrice(self, price: float) -> None:
        self.price = price
    
    def getPrice(self) -> float:
        return self.price
    
class Topping(Ingredient):
    def __init__(self, name: str, cost: float = 0.00, unit: str = "grams", choices = ["pepperoni", "sausage", "plain"]):
        super().__init__(name, cost, unit)
        self.choices = choices
        self.toppings = []

    def addTopping(self, topping: str) -> None:
        if topping in self.choices:
            self.toppings.append(topping)
        else:
            print(f"{topping} is not a valid topping choice.")

    def removeTopping(self, topping: str) -> None:
        if topping in self.toppings:
            self.toppings.remove(topping)
        else:
            print(f"{topping} not found in toppings list.")

class Crust(Ingredient):
    def __init__(self, name: str, cost: float = 0.00, unit: str = "grams", choices = ["thin", "thick"]):
        super().__init__(name, cost, unit)
        self.choices = choices

    def setCrust(self, crust: str) -> None:
        if crust in self.choices:
            self.name = crust
        else:
            print(f"{crust} is not a valid crust choice.")

class Sauce(Ingredient):
    def __init__(self, name: str, cost: float = 0.00, unit: str = "grams", choices = ["tomato", "bbq"]):
        super().__init__(name, cost, unit)
        self.choices = choices

    def setSauce(self, sauce: str) -> None:
        if sauce in self.choices:
            self.name = sauce
        else:
            print(f"{sauce} is not a valid sauce choice.")

class Cheese(Ingredient):
    def __init__(self, name: str, cost: float = 0.00, unit: str = "grams", choices = ["mozzarella", "cheddar"]):
        super().__init__(name, cost, unit)
        self.choices = choices

    def setCheese(self, cheese: str) -> None:
        if cheese in self.choices:
            self.name = cheese
        else:
            print(f"{cheese} is not a valid cheese choice.")

class Entree:
    def __init__(self, name: str, sale_price: float):
        self.name = name
        self.sale_price = price

    def setName(self, name: str) -> None:
        self.name = name

    def getName(self) -> str:
        return self.name
    
    def setPrice(self, price: float) -> None:
        self.price = price
    
    def getPrice(self) -> float:
        return self.price
    
# Here I am going to use composition and inheritance to create the pizza class
class Pizza(Entree):
    def __init__(self, name: str, sale_price: float, crust: Crust, sauce: Sauce, cheese: Cheese):
        super().__init__(name, sale_price)
        self.crust = crust
        self.sauce = sauce
        self.cheese = cheese
        self.toppings = []

    def addTopping(self, topping: Topping) -> None:
        self.toppings.append(topping)

    def removeTopping(self, topping: Topping) -> None:
        if topping in self.toppings:
            self.toppings.remove(topping)
        else:
            print(f"{topping} not found in toppings list.")

#     - What did you change?
"""
I changed the inheritance structure so that the lower level ingredients weren't subclasses of pizza.
This way, I can use the ingredient class as a base class for all ingredients and then
use composition to create the pizza class.
"""
#     - Why did you change it?
"""
This way allows you to better manage the information that comprises the attributes of the pizza class.
You can now add any kind of ingredients for any kind of dish and then subclass Entree to create a specialized
version of Entree to handle unique choices for that subclass.  This makes it easier to manage the code and
update it in the future.
"""

#3. Explain what method resolution order is and why it is important.

"""
Method resolution order is how Python determines which method to call when there are multiple methods with the
same name in the class hierarchy.  It is important because you need to understand how to control which method
is being called when you have multiple classes inheriting from each other.  
"""
#4. Explain what attribute inheritence search is and why it is important.

"""
Attribute inheritence search is how Python determines which attribute to use when there are multiple attributes with the
same name in the class hierarchy.
"""
    