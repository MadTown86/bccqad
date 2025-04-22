# Episode 18: Debugging Features on IDE's VSCode
"""
VSCode:
1. Debugging in VSCode is done using the built-in debugger.
2. You can set breakpoints by clicking on the left margin of the code editor.
3. You can also use the "Run and Debug" button in the sidebar to start debugging your code.
4. VSCode provides a "Debug Console" that allows you to inspect variables and evaluate expressions while debugging.
5. You can step through your code line by line, inspect variables, and evaluate expressions in the debug console.

"""

"""
PyCharm:
1. PyCharm has a powerful built-in debugger.
2. You can set breakpoints by clicking on the left margin of the code editor.
3. You can also use the "Debug" button to start debugging your code.
4. PyCharm provides a "Debug" tool window that shows the call stack, variables, and other useful information.
5. You can step through your code line by line, inspect variables, and evaluate expressions in the debugger console.
6. PyCharm also provides a "Run" tool window that shows the output of your code and any errors that occur.
"""

"""
Terms:
1. Breakpoint: A point where the debugger will pause execution.
2. Call Stack: A list of function calls that led to the current point in the code.
3. Variable Watch: You can choose specific variables to watch their value change as you step
4. Step Over Button: Executes the current line of code and moves to the next line.
5. Step Into Button: If the current line of code is a function call, this will take you into that function.
6. Step Out Button: If you are inside a function, this will take you back to the line of code that called that function.
7. Continue Button: This will continue execution until the next breakpoint is hit.
"""

# Universal Example of Broken Code For Debugging Purposes
    
def add_to_dict(my_dict, lst: list):
    """
    Add a list of values to a dictionaries values.
    """
    if len(my_dict) < len(lst):
        raise IndexError("The list is longer than the dictionary.")
    for key, value in my_dict.items():
        val = lst.pop(0)
        my_dict[key] = value + val
    
def func_i_dont_want_to_see():
    """
    This function is not relevant to the debugging process.
    """
    a = 0
    for i in range(10):
        a = i + 1

if __name__ == "__main__":
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    lst = [4, 5, 6]
    
    # Call the function to add values to the dictionary
    add_to_dict(my_dict, lst)
    func_i_dont_want_to_see()
    
    # Print the updated dictionary
    print(my_dict)  # Output: {'a': 5, 'b': 7, 'c': 9}

    lst2 = [4, 5, 6]  # Extra value in the list
    add_to_dict(my_dict, lst2)  # This will cause an IndexError
    func_i_dont_want_to_see()

    lst3 = [4, 5, 't']
    add_to_dict(my_dict, lst3)  # This will cause a TypeError
    # The above code will raise an IndexError because the list is empty when trying to pop an element.