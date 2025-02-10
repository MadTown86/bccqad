# EPISODE 2: BUILT-IN BASICS AND DATA TYPES

# First order of business is to point you to the definitive source of all Python answers: https://docs.python.org/3/library/index.html
# However, it is DENSE and can be overwhelming for beginners.  If you are a beginner, you will find that
# almost every other word refers to something you don't understand yet.  So, I will try to break it down for you in a way that you can understand.

"""
****GOTCHA****
The first 'gotcha' I want to emphasize is the importance you do not name things (your classes, functions, methods, variables, etc.) with the same name
as the built-in functions, classes, etc. in Python. This is because you will overwrite the built-in version and won't be able to use them.

Of course there is a way to fix this when it does happen, but why go through the hassle right when you are still learning the basics.

The few I will mention are: 
1. str - don't name a string str
2. int - don't name an integer int
3. list - don't name a list list

Example: int() is a built-in function that creates an integer.  If you do this:
int = 10
Oops, I just overwrote the built-in integer constructor with the integer 10.  Now I can't use int() to create an integer anymore.

If I try int('10') I will get an error: 'TypeError: 'int' object is not callable.'

Now I have to import the builtins module and reassign the int function to the built-in int function.
'import builtins'
'int = builtins.int'

There are many more, but these are the few I will mention.
Try not to overwrite these - https://docs.python.org/3/library/functions.html
****GOTCHA****
"""

# 1. Variables and Basic Data Types : https://docs.python.org/3/library/stdtypes.html

# Variables are used to store data values. A variable is created the moment you first assign a value to it.  Assignment is done with the '=' sign.

# Numeric Types
a = 10 
# The variable here is the 'a' and the value of 'a' becomes the integer 10

# List
l = [1, 2, 3, 4, 5] 
# The variable here is the 'l' and the value of 'l' becomes the list [1, 2, 3, 4, 5] because of the use of brackets []

# Range
r = range(5)
# The variable here is the 'r' and the value of 'r' becomes the range(0, 5) because of the use of the range() function

# String
s = "Hello, World!"
# The variable here is the 's' and the value of 's' becomes the string 'Hello, World!' because of the use of quotes ""

s2 = 'Hello, World!' 
# You can use single quotes or double quotes to create a string

# Boolean
f = False
# The variable here is the 'f' and the value of 'f' becomes the boolean False

# Tuple
t = (1, 2, 3, 4, 5)
# The variable here is the 't' and the value of 't' becomes the tuple (1, 2, 3, 4, 5) because of the use of parentheses ()

# Set
ss = {1, 2, 3, 4, 5}
# The variable here is the 'ss' and the value of 'ss' becomes the set {1, 2, 3, 4, 5} because of the use of curly braces {}
# Note here that the set is differentiated from the dictionary, which also uses the curly braces, by the absence of a key-value pair

# Dictionary
d = {"name": "John", "age": 36}
# The variable here is the 'd' and the value of 'd' becomes the dictionary {"name": "John", "age": 36} because of the use of curly braces {} and key-value pairs

# 2. Numeric Types: https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex

"""
First aside: the built-in function 'type()' returns the type of an object.  In larger programs you may have conflicting types and this function can help you debug.
i = 10
print(type(i)) # <class 'int'>
"""

# 2.1. Integers : https://docs.python.org/3/library/functions.html#int
i = 10
# There is no decimal, aka no fractional part to the number, it is whole

# 2.2. Floats : https://docs.python.org/3/library/functions.html#float
f = 10.1 # or f = float(10.1)
# There is a decimal, aka a fractional part to the number

# 2.3. Complex Numbers : https://docs.python.org/3/library/functions.html#complex
c = 1 + 2j # or c = complex(1, 2)
# A complex number is a number that can be expressed in the form a + bi, where a and b are real numbers, and i is a solution of the equation x^2 = -1

# 3. Sequence Types: https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range
# 3.1. Lists : https://docs.python.org/3/library/stdtypes.html#lists

# Sequence types are a bit more versatile and have a lot more to go over, so they will be stand-alone in episode 3.


def main():
    """
    ****GOTCHA****
    You will notice that I reuse a lot of the same variable names, this isn't an issue because I am just overwriting the ones previously defined.
    It is however, something you will want to keep in mind.  Code is read from top left to bottom right, so if you are reusing variable names, make sure
    you are doing it intentionally.
    """
    # Section 2 Examples
    print("\nSection 2 Examples\n")
    basic_operators = ['+', '-', '*', '/', '//', '%', '**', '==', '!=', '>', '<', '>=', '<=', 'and', 'or', 'not']
    print("Basic Operators: ", basic_operators)

    # The only ones I will mention here are the //, % and ** operators
    a = 5
    b = 2
    print("a // b = ", a // b, type(a // b)) # integer division, returns the floor of the quotient, returns an integer
    print("a / b = ", a / b, type(a / b)) # normal division, returns a float

    print("a % b = ", a % b) # modulo, returns the remainder of the division of a by b

    print("a ** b = ", a ** b) # exponentiation, returns a raised to the power of b

    # You can assign the result of an equation to a variable
    a = 10**2
    b = 10 / 3
    c = 10 * 5
    d = a + b
    e = d / c
    f = d // c
    g = d % c
    
    # You can group these using a list
    x = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    l = [a, b, c, d, e, f, g]

    # You can loop through the list and print the result of the equation without having to re-type 'print' each time
    for i in range(len(l)):
        print(f'This is the result of equation {x[i]} :: {l[i]}', type(l[i]))

    # Other modules to use with numbers
    import math
    print("math.sqrt(16) = ", math.sqrt(16)) # square root
    print("math.ceil(4.1) = ", math.ceil(4.1)) # ceiling, returns the smallest integer greater than or equal to the number
    print("math.floor(4.9) = ", math.floor(4.9)) # floor, returns the largest integer less than or equal to the number
    print("math.trunc(4.9) = ", math.trunc(4.9)) # trunc, returns the integer part of the number
    print("math.pi = ", math.pi) # pi

    import random
    print("random.random() = ", random.random()) # random number between 0 and 1
    print("random.randint(1, 10) = ", random.randint(1, 10)) # random integer between 1 and 10
    print("random.choice([1, 2, 3, 4, 5]) = ", random.choice([1, 2, 3, 4, 5])) # random choice from a list

    # Episode 2 Practice:
    # 1. Create a function that will add two numbers together from user input.
    """
    Become comfortable using numbers, assigning variables, using those variables in equations and printing the results.  Also make note of the 
    order of operations if you start doing complex equations.  Remember, PEMDAS - Parentheses, Exponents, Multiplication and Division (left-to-right),
    """


if __name__ == "__main__":
    main()






