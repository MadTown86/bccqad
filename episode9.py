# Episode 9: Conditionals

"""
This episode will cover the basics of conditional statements in Python.

Conditionals are used to make decisions in your code based on certain conditions.

if condition:
#     # code block to execute if condition is true
elif another_condition:
#     # code block to execute if another_condition is true
else:
#     # code block to execute if none of the above conditions are true

"""

# 1. Different ways to compare values and objects in Python
#    1. Comparison Operators: ==, !=, <, >, <=, >=
#    2. Logical Operators: and, or, not
#    3. Membership Operators: in, not in
#    4. Empty Container or existence check: empty or not empty
#    5. Identity Operators: is, is not
#    6. isInstance() function

a = 1
b = 2
c = 3
d = 1
l = [1, 2]

# 2. Basic if statement with equals comparison operator
if a == 1:
    print("a is 1")

# 3. if-else statement with equals comparison operator
if a == c:
    print("a is equal to c")
else:
    print("a is not equal to c")

# 4. if-elif-else statement with greater than and less than comparison operators
if a < b:
    print("a is less than b")
elif a > b:
    print("a is greater than b")
else:
    print("a is equal to b")

# 5. if statement with logical operators
if a == 1 and b == 2:
    print("a is 1 and b is 2")
else:
    print("a is not 1 or b is not 2")

# 6. Multi-conditional if statement during variable assignment
"""
This can make code not readable, so use with caution.
"""
x = 25 if a > b else 10 if a < b and d < c > b else 5
print(x)

# Example of a value 'between' two values syntax
if 1 < a < 3:
    print("a is between 1 and 3")
else:
    print("a is not between 1 and 3")

# This is equivalent to:
if a > b:
    x = 25
elif a < b and d < c > b:
    x = 10
else:
    x = 5
print(x)
"""
Note that single line multi conditional statements would not be great for readability if you use arbitrary
variable naming. It is better to use descriptive variable names and keep the code readable.
"""

# 7. if statement with membership operators
if a in l:
    print("a is in the list")
else:
    print("a is not in the list")

# 8. if statement with not membership operator
if d not in l:
    print("d is not in the list")
else:
    print("d is in the list")

# 9. Note - Membership operators work differently for different data types
#    - For strings, it checks if the substring is present in the string
#    - For lists, it checks if the element is present in the list
#    - For dictionaries, it checks if the key is present in the dictionary

"""
Remember the above concept.  It is an important source of bugs in code, and also an important concept to understand when
you start to code your own classes.  YOU can control and modify the behavior of these operators when you
start to create classes, which we will cover later.
"""

# 10. Existence/Not Empty Check
#     - You can use if statements to check if a variable is not empty or not None
l = [1, 2, 3]
l2 = []
if l:
    print("l is not empty")
else:
    print("l is empty")
if l2:
    print("l2 is not empty")
else:
    print("l2 is empty")

# 11. Identity Operators
#     - is checks if two objects are the same object
#     - is not checks if two objects are not the same object

astring = 'String'
bstring = 'String'
cstring = bstring

if astring is bstring:
    print("astring is bstring - the same object in memory")
else:
    print("astring is not bstring - different objects in memory")

if bstring is cstring:
    print("bstring is cstring - the same object in memory")
else:
    print("bstring is not cstring - different objects in memory")

# 12. isinstance() function
#     - This function checks if an object is an instance of a class or a subclass thereof

if isinstance(a, int): # note that this is a class so no parenthesis
    print("a is an integer")
else:
    print("a is not an integer")

"""
Using isInstance() is often frowned upon in Python, as it is better to use duck typing and try to avoid type checking.

Duck typing in my own terms is programming in a way that you aren't trying to force types in your code, you are
trying to force behavior.  

It changes where the error is caught and how it is caught.  Instead of saying 'hey' thats not a string,
you can't do that, you say 'hey' that doesn't have a 'length' attribute, you can't do that.

Although, I am not yet an expert.  I believe it makes the source of errors easier to understand than type checking.

*However, it is useful when you are starting out and don't have a good grasp on which type of functions return what type of objects.
"""


