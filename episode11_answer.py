# Episode 11: Practice

def main():
    # 1. In what order does Python search for variables?
    """
    LEGB
    1. Local (Examples are directly inside a function code block, if - code block, etc.)
    2. Enclosing (Examples are functions inside other functions, or nested functions)
    3. Global (Examples are variables defined at the top level of a module or script)
    4. Built-in (Examples are built-in functions and types, like print(), len(), etc.)
    """
    # 2. We haven't formally covered this, but try to define what a 'namespace' is in Python.
    """
    Using my own words and not looking up Meriam-Webster like definitions, a namespace is a 
    table that stores references to objects in memory.  These tables exist at all of the
    different scopes that are created when a script runs.  Each overall file or module has its
    namespace.  Then each function itself, whether defined at the top level or nested inside
    another function, has its own namespace.  

    The way Python functions is that when it is performing what is called 'name resolution',
    it searches for the variable being referenced in the aforementioned order.  It uses the
    location of the variable that needs to be resolved to determine which namespace to search first.

    """
    
    # 3. What will the 'global' level x equal after the following code is run?  How about the local level x?
    x = 5
    def f():
        x = 10
        return x
    print(f())
    """
    It does not change it equals 5.  The x inside the f() function is a local variable 
    function f()
    """
    
    # 4. What will the following code print? Why?
    x = 5
    def f():
        y = 10
        z = y + x
        return z
    print(f())
    """
    Z will equal 15 and be the output here.  You can ACCESS the global variables 1-level enclosed 
    if you haven't defined a local variable with the same name.
    """

    # 5. What will the following code print? Why?
    x = 5
    def f():
        global x
        x = 10
        return x

    print(f())

    """
    The global variable x will be modified to equal 10 and that will be the output here because
    the global keyword changed any references in the local f() namespace to now point to the
    global x variable.
    """
    
    # 6. What does the global variable x equal after the following code is run?
    x = 10
    def f():
        y = 10
        x = 25
        def f2():
            global x
            x += y
    f()
    print(x)  # What does this print?
    """
    This will print 20.  The global x was modified to equal 20 because the f2() function
    was called inside the f() function.  The local x variable inside f() was not modified
    """

    # 7. How do you change the following code so that the enclosing function's x is modified?
    x = 5
    def f():
        y = 10
        x = 25
        def f2():
            nonlocal x # Change this to nonlocal to modify the enclosing function's x
            x += y
            print(x + y)
        f2()
    print(f())

    """
    Remember that nonlocal and global give you 'write' capabilities on a variable that is
    external to the location where it is being referenced.  The nonlocal keyword allows you to modify
    the variable in the nearest enclosing scope, while global allows you to modify the variable
    in the global scope.  So in this case, we want to modify the x variable in the enclosing.
    """


if __name__ == "__main__":
    main()