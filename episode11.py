# EPISODE 11: Scope (LEGB)

"""
This episode is going to cover the following:
1. Scope (LEGB)
    -Local
    -Enclosing
    -Global
    -Built-in
2. Global Keyword
3. Nonlocal Keyword

Basic Explanation of Scope:
So when you define variables they are added to a collection of variables called a namespace.  The namespace is a mapping of names 
to objects.  Each scope has its own namespace.  When you reference a variable, Python will search for the variable in the current
scope and then move outwards to the enclosing scope, global scope, and finally the built-in scope.  This is called the LEGB rule.
"""


# 'Global' Scope
x = 10
"""
This 'x' variable is defined on what is called the top-level or 'global' scope.  Global in terms of Python means that it is
defined at the top-level of a program and accessible from anywhere in the file.  This is the highest level of scope in Python.
"""

# 1. Local Scope (L)
def foo():
    y = 20
    print(y)

foo()

"""
The 'y' variable is defined within the function 'foo'.  This is an example of a 'local' scope.  Local in terms of Python means
that it is defined within a function and only accessible within that function.  This is the lowest level of scope in Python.
"""

# Try Block Showing 'y' Variable as Inaccessible
try: 
    print(y)
except NameError as e:
    print("ERROR: 'y' variable is only accessible from within the 'foo' function definition.  You can't change it from outside the function.")



# 2. Enclosing Scope (E)
def outer_enclosing():
    z = 30
    def inner():
        print(z)
    inner()

outer_enclosing()

""""
"z" is defined within the 'outer' function.  The 'inner' function is nested within the 'outer' function.  The 'z' variable is
accessible from the 'inner' function because it is in the 'enclosing' scope.  Enclosing in terms of Python means that it is
defined within a function that contains another function.  It is accessible from the inner function.
"""

# 3. Global Scope (G)
def outer():
    y = 10
    d = y + x # This works because it is just accessing the value, not changing it
    print(d)
    print(x)

outer()

""""
"x" is defined at the top-level of the program.  The 'outer' function is able to access the 'x' variable because it is in the
'global' scope.  Global in terms of Python means that it is defined at the top-level of a program and accessible from anywhere
in the file."
"""

# 3-2. Global Scope (G)
# Showing that you can't change the value of a global variable, once you try to assign a value to the variable, it will create a new local variable.
def outer2():
    x += 10 # This will throw an error because you are trying to change the value of a global variable from within a function.
    print(x)

try:
    outer2()
except UnboundLocalError as e:
    print("ERROR: You can't change the value of a global variable from within a function.  You can only access it.  \nIf you want to change it"
    " you need to use the 'global' keyword.")

# 3-3. Global Keyword + Global Scope (G)
def outer3():
    global x
    x += 10
    print(x)

outer3()
print(x) # This print is taking place at the global scope, so it will show the updated value of 'x'.
"""
Use the global keyword to change the value of a global variable from within a function.

Careful with trying to use global variables.  A lot of issues can take place with larger programs when you incorrectly use and alter
global level variables.
"""

# 4. Built-in Scope (B)

def outer4():
    print(len("Hello World!"))

outer4()

""""
"len" is a built-in function in Python.  Built-in in terms of Python means that it is a function that is available to you without
having to import anything.  It is part of the Python language itself."
"""

# 5. Nonlocal Keyword
def outer5():
    x = 10
    def inner():
        nonlocal x
        x += 10
        print(x)
    inner()

outer5()

""""
"nonlocal" is used to change the value of a variable in the enclosing scope.  In this case, the 'x' variable is in the 'outer' function
and the 'inner' function is nested within the 'outer' function.  The 'nonlocal' keyword allows you to change the value of the 'x' variable
from within the 'inner' function.
"""