# Episode 8: Functions
import math
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
2. Keyword Arguments - argument values that are assigned by variable_name = value syntax when calling the function
3. Default Arguments
4. Variable Length Arguments (*args, **kwargs)

They are defined in the following order:
def function_name(positional_args, keyword_args, default_args, *args, **kwargs):
    # code block
    return value

*Note: For those that haven't caught on yet.  After you create a function using def function_name():,
You can CALL the function by using function_name().  The fact that it is called CALLING a function is
what I wanted to point out.

Function Header = your def statement that defines the function
Function Call = when you actually use the function by name
"""

def main():
    """
    1. Start by defining functions with various argument types
    2. Then go into adding type notation to functions to help you in the future
    """
    # 1. Defining Simple Function
    def greet():
        print("Hello, World!")
    greet()

    # 2. Defining Function with 2 Positional Arguments
    def pythag(a, b):
        return math.sqrt(a**2 + b**2)
    print(pythag(3, 4))

    # 3. Function 2 Positional Arguments That Position Matters
    def subtract(a, b):
        return a - b
    print(subtract(5, 3))
    print(subtract(3, 5))

    """
    Keyword functions and default values get confusing.
    """

    # 4. Function with 1 Positional and 1 Keyword Argument
    def divide(a, b=1):
        return a / b
    print(divide(10)) # You don't need to pass in b because it has a default value
    print(divide(10, 2)) # You can pass in b to override the default value



if __name__ == "__main__":
    main()


