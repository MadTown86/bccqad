# Aside: Bare Bottomed Basics - How to Write Python Code

"""
Syntax:
    Programming languages use text that is formatted in a certain way
    to accomplish specific tasks.  This is often called syntax.

    The main thing to understand about syntax is that it ultimately means the placement
    of text, characters, spacing and indentation need to be done in a specific way.

    Too many spaces, too few spaces, or the wrong characters can cause your code to not work
    as expected.

    Python uses indentation to denote blocks of code, and new lines to separate statements.

Scope:
    Scope is the context in which a variable is defined and can be accessed.  To 
    water it down to the level I understand it, scope is like 'ownership' of a
    variable and is where the variable is callable (or usable) in your code.

    This is determined by indentation and the placement of the variable. 

    
Keywords:
    Keywords are reserved words in Python that have a specific meaning and cannot be used as variable names.
    Examples include: if, else, elif, for, while, def, class, try, except, import, etc.

    They perform an action and require a specific syntax to use them, but they are the basic building blocks of Python.

Built-In Functions:
    Python has a number of built-in functions that are always available for use. 
    Examples include: print(), len(), type(), str(), int(), float(), list(), dict(), etc.

    These functions perform specific tasks and can be used without needing to define them.

List of keyword usage that requires indentation after the keyword:
    
        - def (function definition)
        - if (conditional statement)
        - elif (conditional statement)
        - else (conditional statement)
        - for (loop)
        - while (loop)
        - try (exception handling)
        - except (exception handling)
"""


# Write single line comments with a #

"""
Triple-quoted strings or multi-line comments
"""



"""
"""

def main(): # Notice how all the code is indented under the main function.
    
    # 1. Basic syntax of Python - Variable Assignment with Equals Sign
    a = 1
    b = 2
    c = 3
    # No indentation required during basic variable assignment

    # 2. Function Definition Syntax - Requires Indentation
    def my_function(): 
        d = 4
        # Indented, inside the function, can only be used inside the function (scope)
        print(a, b, c, d)
        # This will print 1 2 3 4

    my_function()

    # 3. Try, Except Syntax - Requires Indentation 
    try:
        print(d)
        # This will raise a NameError because d is not defined in this scope
    except NameError as e:
        print(f"Error: {e}")

    # 4. Conditional Statement Syntax - Requires Indentation
    if a < b:
        print("a is less than b")
    elif a > b:
        print("a is greater than b")
    else:
        print("a is equal to b")



    # 5. Loop syntax - Requires Indentation
    i = 36
    for i in range(5):
        print(i) # This will print 0 to 4, not 36
    # Note here that the 'i' in the for loop is scoped to the loop itself
    # There isn't any risk of it conflicting with an 'i' defined outside the loop.

    while c < 10:
        # This 'c' is scoped to the main function, not the while loop
        # Need to watch for name-clashes here
        print(c)
        c += 1

def print_it(a):
    print(a)
    return None

if __name__ == "__main__":
    main()
    print_it(1)







