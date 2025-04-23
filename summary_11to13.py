# BCC Summary 11-13 Episode Review

"""
What's Covered:
1. LEGB Rule and Scope
2. Class Creation
3. Class Inheritance Overview
"""

# 1. LEGB Rule and Scope:
# LEGB stands for Local, Enclosing, Global, Built-in.
# Global Scope
a = 10
b = 20
print("Global a and b initially: ", (a, b))

# Local Scope
def using_local_a():
    a = 5
    print("\n function:using_local_a()")
    print(a)


def using_global_a():
    # Pulled a from global variables
    print("\n function:using_global_a()")
    print(a)

def altering_global_a():
    global a
    a = 15
    print("\n function:altering_global_a()")
    print(a)

def wrapper():
    # Local scope in reference to wrapper()
    # Enclosing Scope in reference to inner_function()
    a = 30
    def inner_function():
        # Local scope to inner_function()
        nonlocal a 
        a = 25
        print("\n function:inner_function()")
        print(a)
    inner_function()
    print("\n function:wrapper()")
    print(a)

# 2. Class Creation:
class MyClass:
    a = 20 # Class Variable
    def __init__(self, value): # Called a Constructor
        self.value = value # Called an Instance Variable/Attribute

    def display(self): # Instance Method
        print(f"MyClass value: {self.value}")

C = MyClass(10) # Class Instantiation Using Constructor
C.display() # Class method call to .display()

# 3. Class Inheritance Overview:
class BaseClass:
    a = 20
    def __init__(self, base_value):
        self.base_value = base_value
    
    def display_base(self):
        print(f"BaseClass value: {self.base_value}")

    def display(self):
        print(f"BaseClass value: {self.base_value}")

class SubClass1(BaseClass):
    a = 30
    def __init__(self, base_value, sub_value1):
        BaseClass.__init__(self, base_value)  # Call the constructor of BaseClass
        self.sub_value1 = sub_value1

    def display(self):
        print(f"SubClass1 value: {self.sub_value1}")

class SubClass2(BaseClass):
    b = 40
    def __init__(self, base_value, sub_value2):
        BaseClass.__init__(self, base_value)  # Call the constructor of BaseClass
        self.sub_value2 = sub_value2

    def display(self):
        print(f"SubClass2 value: {self.sub_value2}")

class Child1(SubClass1, SubClass2):
    def __init__(self, base_value, sub_value1):
        super().__init__(base_value, sub_value1)  # Call the constructor of SubClass1

class Child2(SubClass2, SubClass1):
    def __init__(self, base_value, sub_value2):
        super().__init__(base_value, sub_value2)  # Call the constructor of SubClass2
        
if __name__ == "__main__":
    using_local_a()  # Output: 5 (local variable)
    using_global_a()  # Output: 10 (global variable)
    altering_global_a()  # Output: 15 (global variable altered)
    print("Global a after update: ", a)
    wrapper()  # Output: 25 (non-local variable) and then 30 (local variable)

    C1 = Child1(10, 20)  # Class Instantiation Using Constructor
    C1.display_base()  # Output: BaseClass value: 10
    C1.display()  # Output: SubClass1 value: 20
    print("\nC1.a")
    print(C1.a) # Output: 30 (SubClass1 variable)

    C2 = Child2(10, 20)  # Class Instantiation Using Constructor
    C2.display_base()  # Output: BaseClass value: 10
    C2.display()  # Output: SubClass2 value: 30
    print("\nC2.a")
    print(C2.a) # Output: 20 (SubClass2 variable)