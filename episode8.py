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
    # Creating a function in simplest form
    def simple():
        pass # returns None by default

    # Calling a function
    simple()

    # 1. Defining Function with no Arguments
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
    print(subtract(5, 3)) # 2
    print(subtract(3, 5)) # -2

    # 4. Function with 1 Positional and 1 default argument
    def divide(a, b=1):
        return a / b
    print(divide(10)) # You don't need to pass in b because it has a default value
    print(divide(10, 2)) # You can pass in b to override the default value

    # 5. Function CALL using keyword arguments (same divide)
    print(divide(b=2, a=10)) # Pass in arguments by name, using keyword=value syntax

    # 6. Function with Variable Length Arguments
    def sum_all(*args):
        return sum(args)
    print(sum_all(1, 2, 3, 4, 5)) # 15

    # 7. More complex example with Variable Length Arguments
    def calculate_it(mode, *args):
        """
        You pass in a string 'mode' to qualify the operation you want to perform
        and then you pass in a variable number of arguments to perform the operation on.
        """
        if mode == 'sum':
            return sum(args)
        elif mode == 'product':
            result = 1
            for num in args:
                result *= num
            return result
        else:
            raise ValueError("Invalid mode. Use 'sum' or 'product'.")
        
    print(calculate_it('sum', 1, 2, 3, 4, 5)) # 15
    print(calculate_it('product', 1, 2, 3, 4, 5)) # 120

    # 8. Function with Keyword Variable Length Arguments
    def print_info(**kwargs):
        for key, value in kwargs.items():
            print(f"{key}: {value}")
    print_info(name="John", age=30, city="New York")
    """
    *Note: For more complex functions in the 'real world' so to speak, you will find that
    the variable length keyword arguments are used to pass in multiple parameters to a function
    without having to define each one explicitly.  This is especially useful when you have a lot of parameters
    or when you want to pass in optional parameters.
    """

    # 9. Real Life Example with Tkinter - GUI Elements
    """
    A potential use case for **kwargs is if you want to create a function that creates a GUI element
    with a lot of optional parameters.  For example, if you want to create a button with Tkinter,
    you can pass in a lot of optional parameters to customize the appearance and behavior of the element.
    Here is an example of creating a button with Tkinter using **kwargs:
    """
    import tkinter as tk

    def create_button(master, text, command=None, **kwargs): # This is a function that uses **kwargs to accept optional keyword-value pairs.

        button = tk.Button(master, text=text, command=command, **kwargs) # When using the ** in a function call, it unpacks the dictionary into keyword arguments.
        button.pack()
        return button
    
    root = tk.Tk()
    create_button(root, "Click Me", command=lambda: print("Button Clicked!"), bg="blue", fg="white")
    root.mainloop()

    # 10. Example of utilizing function call argument unpacking
    list_of_args = [(1, 2), (3, 4), (5, 6)]
    def add(a, b):
        return a + b
    
    for args in list_of_args:
        print(add(*args)) # The asterisk here unpacks the tuple into positional arguments

    # 11. Example of utilizing function call with dictionary unpacking
    dict_of_args = {'a': 1, 'b': 2}
    def multiply(a, b):
        return a * b
    
    print(multiply(**dict_of_args)) # The double asterisk here unpacks the dictionary into keyword arguments

    # 12. Function with Type Notation
    def multiply(a: int, b: int) -> int:
        return a * b
    print(multiply(2, 3)) # 6
    """
    *Note: Type notation is not enforced by Python, but it is a good practice to use it
    to help you and others understand what types of arguments the function expects
    and what type of value it returns.
    """

if __name__ == "__main__":
    main()


