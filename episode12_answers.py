# Episode 12 Practice: Class Basics

# 1. What are functions defined in a class called?
#     - Methods
# 2. What is the term used to describe the creation of an object from a class?
#     - Instantiation

# 1. Create a class called 'Person' with the following attributes:
#     - name
#     - age
#     - occupation
#     - salary
class Person:
    def __init__(self, name, age, occupation, salary):
        self.name = name
        self.age = age
        self.occupation = occupation
        self.salary = salary
    


# 1-A. Create methods that allow you to change all of the attributes of the class.
class Person:
    def __init__(self, name, age, occupation, salary):
        self.name = name
        self.age = age
        self.occupation = occupation
        self.salary = salary
    
    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def set_occupation(self, occupation):
        self.occupation = occupation

    def set_salary(self, salary):
        self.salary = salary
    
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def get_occupation(self):
        return self.occupation
    
    def get_salary(self):
        return self.salary
    
    def give_raise(self, percentage):
        self.salary += self.salary * (percentage / 100)
    

# 1-B. Create a method that prints out all of the attributes of the class.

# 1-C. Create a method that increases the salary of the person by 10%.

# 1-D. Create two instances of this class and test all of the methods.

#2. Stretch Problem:
"""
Create a dog class with the following attributes:
    - name
    - age
    - breed
    - color
    - owner - class instance of 'Owner'

Create a class called 'Owner' with the following attributes:
    - person - class instance of 'Person'
    - pets - a list of class instances of 'Dog'

Create a cat class with the following attributes:
    - name
    - age
    - breed
    - color
    - owner - class instance of 'Owner'

Create a class called 'Customer' with the following attributes:
    - owner - class instance of 'Owner'
    - purchase_history - a list of strings

Create methods that allow you to change all of the attributes of the classes above.

Imagine that you have a petstore and are going to keep track of customers, pets, and owners.
Create instances of the classes above and test all of the methods.    
"""