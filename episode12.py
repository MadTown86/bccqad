# Episode 12: Classes 1 of 2

"""
Simple Terms:
A class is a way for the developer to package code into a reusable structure.

The class itself is a blueprint from which instance objects are created.

It's utility becomes more apparent when you dive deeper into object-oriented
programming.  To give a simplified explanation of OOP, it is a way to break
a large program down into smaller chunks that are easier to manage, as well as
easier to delegate to different developers.

Lastly, classes are great for making programs that can be easily extended and
maintained through inheritance and polymorphism.
"""

"""
For this episode, please focus on the following:
1. Class definition
2. Class instantiation
2. Attribute creation, calling
3. Method creation, calling

Basic Class Creation Syntax:

class ClassName(ParentClass1, ParentClass2, ...):
    def __init__(self, attribute1, attribute2, ...):
        self.attribute1 = attribute1
        self.attribute2 = attribute2
        ...
    
    def method1(self):
        return something

    def method2(self):
        return something

Basic Class Instantiation Syntax:

instance1 = ClassName(attribute1, attribute2, ...)
instance2 = ClassName(attribute1, attribute2, ...)

Class Attribute Call Syntax:

instance1.attribute1
instance1.attribute2

Class Method Call Syntax: ### Methods are just the name of functions belonging to a class

instance1.method1()
instance1.method2()

One strange thing that is important is the use of 'self'.
'self' is a reference to the instance of the class.  It is used to access
variables that belong to the class.  It is also used to call other methods
within the class.

To simplify the explanation, 'self' is just the way Python refers to the instance
of the class.  It is similar to 'this' in other programming languages and simply
is a syntactical requirement.

Lastly and most importantly, classes are the way you can fully customize the behavior of
Python objects.  You will learn more about how to do this in the next episode classes 2 of 2.

The way classes behave is a large part of object-oriented programming (OOP).  This is a complex topic
that can be difficult to grasp.
"""

# Simple Class Creation:
class Employee:
    pass

# Instantiation:
emp_1 = Employee()
emp_2 = Employee()

# Class With Attributes:
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

# Instantiation:
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 600)

print(emp_1)
print(dir(emp_1))
"""
Here you are creating two objects in memory that are instances of the Employee class.
Each object has its own state, which is stored in attributes.
"""

# Accessing Attributes:
print(emp_1.first)
print(emp_1.last)

# Class With Attributes and Methods:
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.placeholder = None

    def full_name(self):
        return f'{self.first} {self.last}'
    
    def apply_raise(self):
        self.pay = int(self.pay * 1.04)
    
    def alter_placeholder(self, value):
        self.placeholder = value

# Instantiation:
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 600)

# Updating Attributes:
print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

# Accessing Methods:
print(emp_1.full_name())
print(emp_2.full_name())

