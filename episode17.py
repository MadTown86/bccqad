# Episode 17: Exceptions - try, except, raise, finally

"""
I am only going to describe this in laymens terms as this is a beginning
Python tutorial.

Exception handling ensures that your program can run as intended when
errors occur.  

This has an open-ended meaning in that, if you want your application to
crash if X conditions are met, then you can make that happen.

If you want your program to continue running and simply notify the user of
an issue, you can do that as well.

What we are going to cover:
1. Brief overview of the exception class tree.
2. How to use try and except blocks to handle exceptions.
3. How to use the raise statement to raise exceptions.
4. How to use the finally block to execute code regardless of whether an 
exception occurred or not.



Exception Class Tree:
1. BaseException (the base class for all exceptions)
2. Exception (the base class for all non-exiting exceptions)
3. StandardError (the base class for all standard exceptions)
4. ArithmeticError (the base class for all arithmetic exceptions)
5. LookupError (the base class for all lookup exceptions)
6. ValueError (the base class for all value exceptions)
7. etc...

So this list goes on and on.  

***You need to remember that these exist and that you can use them to 
handle specific exception types.***
"""

# Basic Syntax for try and except blocks:

"""
try:
    # Code that may raise an exception
except ExceptionType as e:
    # Code to handle the exception
else:
    # Code to execute if no exceptions were raised
finally:
    # Code that will always execute, regardless of whether an exception occurred or not
"""

# Example of no internal try/except blocks:
def my_divide(a, b):
    return a / b

# Example of an internal try/except block that handles all exceptions:
def my_divide_with_try(a, b):
    try:
        return a / b
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# This is a custom error check that raises a specific exception if the condition is met.
def my_divide_with_raise(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

# Example of an internal try/except block that handles a specific exception with a finally block:
def my_divide_with_finally(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        print(f"Cannot divide by zero: {e}")
        return None
    finally:
        print("Execution completed.")

# External try block and specific exception handled
try:
    a, b = 10, 'ten'
    result = my_divide(a, b)
    print(f"Result: {result}")
except ZeroDivisionError as e: # Specific exception handled
    print(f"Cannot divide by zero: {e}")
finally:
    print("Execution completed.")

# NOTE: No others will be handled and a generic exception will be raised



