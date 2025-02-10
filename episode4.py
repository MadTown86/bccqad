# Episode 4: Strings

def main():
    """
    To start, why does text matter to begin with?  Text IS programming, everything we write, type and see from a computer can
    be boiled down to binary data.  Ones and zeroes. Text is a way to represent that data in a human readable form.

    The basic string is relatively straight forward to create and to print.

    The complexity comes in when you start to think of the different types of encodings, which account for
    different language character sets.  This is a deep rabbit hole that we won't go down in this beginner series.

    Just to mention a few here for reference, some major encodings are ASCII and UTF-8.
    
    For now, I would just understand that if you ever work with strings, large volumes of text, website text for
    various languages, etc., you will need to understand the different types of encodings.
    """
    #region String Creation
    print("\n**String Creation**")
    print("Use single quotes or double quotes for strings.  Single quotes are easier to type.\n")
    s = 'Hello, world!' # Single quotes
    x = "Hello, world!" # Double quotes
    y = str(123) # Convert a number to a string
    z = str(123.45) # Convert a float
    print("s = 'Hello, world!'")
    print('s output = ', s)
    print("\nx = \"Hello, world!\"") # The backslash is an escape character
    print('x  output = ',x)
    print("\ny = str(123)")
    print('y output = ', y)
    print("\nz = str(123.45)\n")
    print('z output = ', z)

    # Triple quotes for multi-line strings
    print("\nUse triple quotes for multi-line strings.")
    s = """Hello,
    world!"""
    print("s = '''Hello,\nworld!'''")
    print("s output = ", s)
    #endregion String Creation

    #region Types of Strings
    print("\n**Types of Strings**")
    
    # Regular Strings
    print("Regular Strings: The default string type.\n")
    s = "Hello, world!"
    print("s = 'Hello, world!'")
    print("s output = ", s)

    # Raw Strings
    print("\nRaw Strings: Use r in front of the string to ignore escape characters.  This can be useful for writing directory paths.\n")
    s = r'C:\Users\name\Documents'
    print(r"s = r'C:\Users\name\Documents'")
    print("s output = ", s)
    
    # Byte Strings
    print("\nByte Strings: Use b in front of the string to convert it to a byte string.\n")
    s = b'Hello, world!'
    print(r"s = b'Hello, world!'")
    print("s output = ", s)
    print("Byte strings are used to process binary data.\nIt becomes necessary when working with image files, audio files, etc.")
    print("Right know just understand that it exists")
    #endregion Types of Strings

    #region Escape Characters
    print("\n**Escape Characters**")
    print("Use escape characters to insert special characters into strings, they can also be used for tabs and new paragraph lines.\n")
    s = "Hello, \"world!\"" # Double quote, you can't use double quotes within each other normally
    print(r"s = 'Hello, \"world!\"'")
    print("s output = ", s)
    s = "Hello, \\world!" # Backslash
    print(r"s = 'Hello, \\world!'")
    print("s output = ", s)
    s = "Hello, \nworld!" # New line
    print(r"s = 'Hello, \nworld!'")
    print("s output = ", s)
    s = "Hello, \tworld!" # Tab
    print(r"s = 'Hello, \tworld!'")
    print("s output = ", s)
    s = "Hello, \bworld!" # Backspace
    print(r"s = 'Hello, \bworld!'")
    print("s output = ", s)
    #endregion Escape Characters
    
    # Octal and Hexadecimal Characters
    print("\nYou can use escape characters to insert octal and hexadecimal values.\n")
    s = "Hello, \110\145\154\154\157!" # Octal
    print(r"s = 'Hello, \110\145\154\154\157!'")
    print("s output = ", s)
    s = "Hello, \x48\x65\x6c\x6c\x6f!" # Hexadecimal
    print(r"s = 'Hello, \x48\x65\x6c\x6c\x6f!'")
    print("s output = ", s)
    print("**NOTE** Look up the hexadecimal and/or octal values for the characters you want to use.")
    #endregion Escape Characters

    # Unicode Characters
    print("\nUse the backslash U to insert an 8 digit Unicode character.")
    s = "I am on \U0001F525" # Unicode
    # Note that the Unicode for this character was represented as U+1F525
    print(r"s = 'I am on \U0001F525'")
    print("s output = ", s)
    #endregion Unicode Characters

    #region Indexing and Slicing Strings
    print("\n**Indexing and Slicing Strings**")

    # Indexing
    print("Use indexing to get a single character from a string.\n")
    s = "Hello, world!"
    print("s = 'Hello, world!'")
    print("s[0] output = ", s[0]) # H
    print("s[7] output = ", s[7]) # w

    # Slicing
    print("\nUse slicing to get a substring from a string.\n")
    s = "Hello, world!"
    print("s = 'Hello, world!'")
    print("s[0:5] output = ", s[0:5]) # Hello
    print("s[7:] output = ", s[7:]) # world!
    #endregion Indexing and Slicing Strings

    #region String Immutability - Can't be changed once created
    print("\n**String Immutability**")
    print("Strings are immutable, meaning they can't be changed once created.\n")
    s = "Hello, world!"
    print("s = 'Hello, world!'")
    # s[0] = 'h' # This will cause an error
    print(r"s[0] = 'h' - This causes an error")
    #endregion String Immutability

    #region String Methods
    print("\n**String Methods**")

    # len() function
    print("Use the len() function to get the length of a string.\n") # Also works on lists, tuples, sets, and dictionaries
    s = "Hello, world!"
    print("s = 'Hello, world!'")
    print("len(s) output = ", len(s))

    # lower() method
    print("\nUse the lower() method to convert a string to lowercase.\n")
    s = "Hello, world!"
    print("s = 'Hello, world!'")
    print("s.lower() output = ", s.lower())

    # upper() method
    print("\nUse the upper() method to convert a string to uppercase.\n")
    s = "Hello, world!"
    print("s = 'Hello, world!'")
    print("s.upper() output = ", s.upper())

    # strip() method
    print("\nUse the strip() method to remove leading and trailing whitespace.\n")
    s = " Hello, world! "
    print("s = ' Hello, world! '")
    print("s.strip() output = ", s.strip())

    # replace() method
    print("\nUse the replace() method to replace a substring with another substring.\n")
    s = "Hello, world!"
    print("s = 'Hello, world!'")
    print("s.replace('world', 'Python') output = ", s.replace('world', 'Python'))

    # split() method
    print("\nUse the split() method to split a string into a list of substrings.\n")
    s = "Hello, world!"
    print("s = 'Hello, world!'")
    print("s.split(',') output = ", s.split(','))
    #endregion String Methods

    #region String Concatenation
    print("\n**String Concatenation**")
    print("Use the + operator to concatenate strings.\n")
    s = "Hello, " + "world!"
    print("s = 'Hello, ' + 'world!'")
    print("s output = ", s)
    #endregion String Concatenation

    #region String Multiplication
    print("\n**String Multiplication**")
    print("Use the * operator to multiply strings.\n")
    s = "Hello, " * 3
    print("s = 'Hello, ' * 3")
    print("s output = ", s)
    #endregion String Multiplication

    #region String Formatting
    print("\n**String Formatting**")
    """***NOTE***
    String formatting allows you to input variable data into a string template.

    The variable names I want to put into the string are,
    name_of_client = "Joey"
    type_of_test = "midterm"
    grade_of_client = 77
    Example: "Hello, name_of_client, your grade on the type_of_test is grade_of_client"
    """

    # First the conversion target syntax
    # This allows you to alter the output of the variables information
    print("Conversion Target Syntax or Advanced Formatting Expression")
    print("This is the syntax for altering the variables output into the string")

    # The syntax
    print("The syntax is: %[flags][width][.precision]type")

    print("flags = -, +, 0, #, space")
    print("width = minimum number of characters to be printed")
    print("precision = number of digits after the decimal point")
    print("type = d, i, u, f, F, e, E, g, G, x, X, o, s, %")

    """
    flags: 
    - = left-justify
    + = right-justify
    0 = zero padding
    # = alternate form
    space = a space before positive numbers

    Types: 
    d - decimal
    i - integer
    f - float
    F - float but with uppercase letters
    o - octal
    x - hexadecimal
    X - hexadecimal with uppercase letters
    e - exponential
    E - exponential with uppercase letters
    g - general
    G - general with uppercase letters
    s - string
    """

    # The Percentage Sign (%) Method
    print("Use the percentage sign (%) method for string formatting.\n")
    n = "Joey"
    m = "midterm"
    y = "77/100"
    z = 77.85
    x = 77
    l = 2**8
    print(r'Hello %s, your grade on the %s is %s % (n, m, y)')
    s = "Hello %s, your grade on the %s is %s" % (n, m, y)
    print("s output = ", s)

    print(r'Hello %s, your grade on the %s is %i % (n, m, z)')
    s = "Hello %s, your grade on the %s is %i" % (n, m, z)
    # Note that %i converted the 77.85 to 77 for the output.
    print("s output = ", s)

    print(r'Hello %s, your grade on the %s is %f % (n, m, z)')
    s = "Hello %s, your grade on the %s is %f" % (n, m, z)
    print("s output = ", s)

    print(r'Hello %s, your grade on the %s is %.2f % (n, m, z)')
    s = "Hello %s, your grade on the %s is %.2f" % (n, m, z)
    # Note that %.2f rounded the 77.85 to 77.85 for the output.
    print("s output = ", s)

    print(r'Hello %s, your grade on the %s is %d % (n, m, z)')
    s = "Hello %s, your grade on the %s is %d" % (n, m, z)
    # Note that %d converted the 77.85 to 77 for the output.
    print("s output = ", s)

    print(r'Hello %s, your grade on the %s is %x % (n, m, x)')
    s = "Hello %s, your grade on the %s is %x" % (n, m, x)
    # Note that %x converted the 77 to 4d for the output.
    print("s output = ", s)

    print(r'Hello %s, your grade on the %s is %o % (n, m, x)')
    s = "Hello %s, your grade on the %s is %o" % (n, m, x)
    # Note that %o converted the 77 to 115 for the output.
    print("s output = ", s)

    print(r'Hello %s, your grade on the %s is %e % (n, m, l)')
    s = "Hello %s, your grade on the %s is %e" % (n, m, l)
    # Note that %e converted the 256 to 2.560000e+02 for the output.

    d = {"name": "Joey", "test_type": "midterm", "grade": 77.85}
    # You can also use dictionary keywords to access and input the data into a string
    print(r'Hello %(name)s, your grade on the %(test_type)s is %(grade)-2.4f')
    s = "Hello %(name)s, your grade on the %(test_type)s is %(grade)2.4f" % d
    print("s output = ", s)
 
    # The format() Method
    """
    Advanced Formatting Method Syntax Aside:
    {fieldname component!conversionflag:formatsec}
    fieldname = the index or keyword of an argument within the .format(**found here**) method
    component = the index or key of an attribute within the argument (a level of optional nesting)
    conversionflag = the character that tells the format() method to convert the value before formatting
    formatsec = the format specification, which is a string that specifies how the value should be formatted :.2f for example
    
    The formatspec has its own syntax:
    [[fill]align][sign][#][0][width][,][.precision][type]
    fill = any character
    align = <, >, =, or ^
    sign = +, -, or space
    # = alternate form
    0 = zero padding
    width = minimum number of characters to be printed
    precision = number of digits after the decimal point
    type = d, i, u, f, F, e, E, g, G, x, X, o, s, %

    An example is:
    "This is {0:0>2} converted".format(5) = "This is 05 converted"
    0 = zero padding
    > = right align
    2 = width of 2

    A more complex example is:
    "This is {0:0>2.2f} converted".format(5) = "This is 05.00 converted"
    0 = zero padding
    > = right align
    2 = width of 2
    .2 = 2 decimal places
    f = float
    """

    print("\nUse the format() method for string formatting.\n")
    n = "Joey"
    m = "midterm"
    y = "77/100"

    print(r'Hello {}, your grade on the {} is {}'.format(n, m, y))
    s = "Hello {}, your grade on the {} is {}".format(n, m, y)
    print("s output = ", s)
    # This goes automatically by order of the variables, to be more precise...
    print(r'Hello {0}, your grade on the {1} is {2}'.format(n, m, y))
    s = "Hello {0}, your grade on the {1} is {2}".format(n, m, y)
    print("s output = ", s)

    # The f-string Method
    print("\nUse the f-string method for string formatting.\n")
    n = "Joey"
    m = "midterm"
    y = 77.854
    print(r'Hello {n}, your grade on the {m} is {y}')
    s = f"Hello {n}, your grade on the {m} is {y}"
    print("s output = ", s)

    # You can use f-string with the conversion target syntax
    print(r'Hello {n}, your grade on the {m} is {y:.2f}')
    s = f"Hello {n}, your grade on the {m} is {y:.2f}"
    print("s output = ", s)

    # You can also use f-string with dictionary keywords
    d = {"name": "Joey", "test_type": "midterm", "grade": 77.85}
    print(r'Hello {name}, your grade on the {test_type} is {grade:.2f}')
    s = f"Hello {d['name']}, your grade on the {d['test_type']} is {d['grade']:.2f}"
    print("s output = ", s)
    #endregion String Formatting
    


if __name__ == "__main__":
    main()