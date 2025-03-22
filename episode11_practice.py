# Episode 11: Practice

def main():
    # 1. In what order does Python search for variables?
    # 2. We haven't formally covered this, but try to define what a 'namespace' is in Python.
    # 3. What will the 'global' level x equal after the following code is run?  How about the local level x?
    x = 5
    def f():
        x = 10
        return x
    print(f())
    
    # 4. What will the following code print? Why?
    x = 5
    def f():
        y = 10
        z = y + x
        return z
    print(f())

    # 5. What will the following code print? Why?
    x = 5
    def f():
        global x
        x = 10
        return x

    print(f())
    
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

    # 7. How do you change the following code so that the enclosing function's x is modified?
    x = 5
    def f():
        y = 10
        x = 25
        def f2():
            x += y
            print(x + y)
        f2()
    print(f())


if __name__ == "__main__":
    main()