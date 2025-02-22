# Episode 8: Functions
from typing import List, Dict

"""
Main Points Covered:
1. Defining Functions
2. Function Arguments
3. Function Return Values

The main purpose of functions is to decrease overall work by reusing code.

If you find yourself copying and pasting code to perform a certain operation multiple times, 
then you should consider creating a function to handle that operation.

Syntax:
def function_name(arg1, arg2, arg3, ...):
    # code block
    return value

*Note: 'return' is optional.  If you do not include a 'return' statement, then the function will return 'None'.

Argument Types:
1. Positional Arguments
2. Keyword Arguments
3. Default Arguments
4. Variable Length Arguments (*args, **kwargs)

They are defined in the following order:
def function_name(positional_args, keyword_args, default_args, *args, **kwargs):
    # code block
    return value
"""

# 1. Defining a Function
def say_hello():
    print("Hello, World!")
    # 'return' is optional

# Example of more complex functions:
def subtract(x, y):
    # 'x' and 'y' are positional arguments, meaning the order matters
    return x + y

def re_arrange(l: List[str], d: Dict) -> Dict:
    """
    This function takes a list and a dictionary and returns a dicitonary with the list values as keys
    and the dictionary values as values.

    I have added what are called 'type hints' to the function definition.  This is a way to allow
    the user to know what type of data the function expects and what type of data it will return.

    This is not required, but it is good practice and it can help with debugging because when incorrect
    types are passed to the function, the IDE will highlight it and throw an error.
    """
    res = {}
    if len(l) == len(d): # check if the list and dictionary are the same length
        for k, v in d.items():
            res[l.pop(0)] = (k, v)
    return res

# 2. Function Arguments
def say_hello_to(name):
    print(f"Hello, {name}!")

def say_hello_to_default(name="World"):
    print(f"Hello, {name}!")

# 3. Function Return Values
def add(x, y):
    return x + y

def add_subtract(x, y):
    return x + y, x - y
