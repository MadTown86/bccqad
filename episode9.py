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

# 1. Operators
#    1. Comparison Operators: ==, !=, <, >, <=, >=
#    2. Logical Operators: and, or, not
#    3. Membership Operators: in, not in

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