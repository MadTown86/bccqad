def main():
    # 1. How do you define variables in Python?
    """
    You write a name for the variable and then use the assignment operator '=' to assign a value to the variable.
    """
    # 2. What is the difference between division and floor division?
    """
    Division is the normal division operation that you are used to.  It will return a float value.
    Floor division is the division operation that will return the integer value of the division operation.
    """
    # 3. How do you create an exponent in Python?
    """
    You use the double asterisk '**' to create an exponent in Python.
    """
    # 4. What is the modulo operator and what does it do?
    """
    The modulo operator is the percent sign '%' and it returns the remainder of a division operation.
    """
    # 5. Name one useful method from the math module
    """
    The math module has a lot of useful methods.  One of the most useful is the math.sqrt() method.
    """
    # 6. What does the random module do?
    """
    The random module is used to generate random numbers in Python.
    """
    # 7. Stretch Problem:
    x = input("Enter a number: ")
    y = input("Enter another number: ")
    return int(x) + int(y)

def alternate_main():
    return int(input("Enter a number: ")) + int(input("Enter another number: "))

if __name__ == "__main__":
    print(main())

    # One thing you may have struggled with here is that you didn't print your 'main()' function so no result was output.
    # The other issue would be that you didn't convert the inputs into integers but kept them as strings.
    # The third issue could be that you looked a bit deeper into things yourself and put both inputs into the function definition.
    # --> This calls them twice, once upon function creation and once upon function call.  This is why I used the input() function inside the function.

