# Episode 17: Practice:

# 1. What is the basic syntax for a try...except block?
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
# 2. When does the else block execute in a try...except statement?
"""
When no exceptions were raised in the try block, the else block will execute.
"""
# 3. When does the finally block execute in a try...except statement?
"""
The finally block will execute regardless of whether an exception occurred or not, but
the exception will need to be handled in the except block.  If the exception is not handled,
the finally block may not be reached.
"""
# 4. What is the purpose of the raise statement in Python?
"""
You can raise your own exceptions based on your own conditions.  This is useful for
debugging.
"""
# 5. Create a mini example of some code that raises an exception and handles it using a try..except block.
# try:
#     t = tuple([1, 2, 3])
#     t[0] = 4
# except TypeError as e:
#     print(f"TypeError: {e}")
# This will raise a TypeError because tuples are immutable and cannot be modified.

# 6. When does a finally block execute in a try...except statement?
"""
This always executes solong as there aren't any fatal exceptions before it is reached.
"""
# 8. What would happen in the following code:
"""
try:
    a = 0
    b = 't'
    res = a / b
except ZeroDivisionError as e:
    print("Division by zero error")
finally:
    print("print something to log file")
"""
try: 
    a = 0
    b = 't'
    res = a / b
except ZeroDivisionError as e:
    print("Division by zero error")
# This code will raise a TypeError because you cannot divide by a string.
# The ZeroDivisionError exception will not be raised, so the except block will not execute.
# The finally block will execute and print "print something to log file".