# Episode 6: looping concepts
 
def main():

    """
    For loop
    While loop

    Some advanced concepts from itertools module.

    ***Aside***
    I want to introduce the concept of 'iterables' and 'iterators'.  You will most likely hear these terms used a lot.
    The technical way to describe what they are is quite complex in my opinion.  

    So all you need to know off the bat is that an 'iterable' is something that you can loop through. A list, tuple, string, set, dictionary, etc.
    """
    
    #region For Loop - Different Data Types
    # lists
    l = [1, 2, 3, 4, 5]

    # Loop Through ACTUAL values
    print("For Loop: Through list data type")
    print(r'for i in l:' + '\n' + r'     print(i)')
    print("Output:")
    for i in l:
        print(i)
    
    # Loop Through INDEXES
    print("\nFor Loop: Through list data type")
    print(r'for i in range(len(l)):' + '\n' + r'     print(l[i])')
    print("Output:")
    for i in range(len(l)):
        print(l[i])

    """
    Core difference?:
    You have access to the value AND location when you index via the range function.
    This means you can change these values if need by and alter the original list.

    This is a common pattern in Python, however, if you are not changing anything, then looping through actual values is fine.
    """


    # Loop Through Tuples
    # Loop Through ACTUAL values
    t = (1, 2, 3, 4, 5)
    print("\nFor Loop: Through tuple data type")
    print(r'for i in t:' + '\n' + r'     print(i)')
    print("Output:")
    for i in t:
        print(i)

    # Loop Through INDEXES
    print("\nFor Loop: Through tuple data type")
    print(r'for i in range(len(t)):' + '\n' + r'     print(t[i])')
    print("Output:")
    for i in range(len(t)):
        print(t[i])

    # Loop Through Strings
    # Loop Through ACTUAL values
    s = "Hello, World!"
    print("\nFor Loop: Through string data type")
    print(r'for i in s:' + '\n' + r'     print(i)')
    print("Output:")
    for i in s:
        print(i)

    # Loop Through INDEXES
    print("\nFor Loop: Through string data type")
    print(r'for i in range(len(s)):' + '\n' + r'     print(s[i])')
    print("Output:")
    for i in range(len(s)):
        print(s[i])

    # Loop Through Sets
    # Loop Through ACTUAL values
    se = {1, 2, 3, 4, 5}
    print("\nFor Loop: Through set data type")
    print(r'for i in se:' + '\n' + r'     print(i)')
    print("Output:")
    for i in se:
        print(i)

    # No indexes, so can't loop through indexes

    # Loop Through Dictionaries
    # Default is to loop through keys
    # Loop Through keys
    d = {"a": 1, "b": 2, "c": 3}
    print("\nFor Loop: Through dictionary data type")
    print(r'for k in d:' + '\n' + r'     print(k)')
    print("Output:")
    for k in d:
        print(k)

    # Loop Through key:value pairs
    d = {"a": 1, "b": 2, "c": 3}
    print("\nFor Loop: Through dictionary data type")
    print(r'for k, v in d.items():' + '\n' + r'     print(k, v)')
    print("Output:")
    for k, v in d.items():
        print(k, v)
    #endregion

    #region While Loop
    # While Loop
    print("\nWhile Loop")
    print(r'x = 0' + '\n' + r'while x < 5:' + '\n' + r'     print(x)' + '\n' + r'     x += 1')
    print("Output:")
    x = 0
    while x < 5:
        print(x)
        x += 1

    # Another example
    print("\nWhile Loop")
    print(r's = "Hello, World!"' + '\n' + 'cursor = 0' + '\n' + 'while cursor < len(s):' + '\n' + '     print(s[cursor])' + '\n' + '     cursor += 1')
    print("Output:")
    s = 'Hello, World!'
    cursor = 0
    while cursor < len(s):
        print(s[cursor])
        cursor += 1
    #endregion

    #region itertools module
    """
    The itertools module allows you to do some advanced looping techniques when you need to loop through multiple sets of data.

    When you get to a point where you start needing to loop through and pair up multiple sets of data that are organized differently,
    then you will want to look into the itertools module.  

    **Main reason is that it can be more efficient than trying to do it manually.  Both in terms of performance and readability.**
    
    https://docs.python.org/3/library/itertools.html

    """

    # itertools.chain()
    # Combines multiple iterables into one so they run back to back
    import itertools

    print("\n'itertools.chain()'")
    print(r'for i in itertools.chain([1, 2, 3], (4, 5, 6), "abc"):' + '\n' + r'     print(i)')
    print("Output:")
    for i in itertools.chain([1, 2, 3], (4, 5, 6), "abc"):
        print(i)

    # itertools.pairwise()
    # Pairs up elements in an iterable
    print("\n'itertools.pairwise()'")
    print(r'for i in itertools.pairwise([1, 2, 3, 4, 5]):' + '\n' + r'     print(i)')
    print("Output:")
    for i in itertools.pairwise([1, 2, 3, 4, 5]):
        print(i)

    # itertools.zip_longest()
    # Pairs up elements in an iterable, but fills in missing values with a default value
    print("\n'itertools.zip_longest()'")
    print(r'for i in itertools.zip_longest([1, 2, 3, 4, 5], "abc", fillvalue="N/A"):' + '\n' + r'     print(i)')
    print("Output:")
    for i in itertools.zip_longest([1, 2, 3, 4, 5], "abc", fillvalue="N/A"):
        print(i)
    #endregion
    

    



if __name__ == "__main__":
    main()