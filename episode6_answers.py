# Episode 6: Looping Concepts - Practice

"""
My intention here is to start increasing the level of difficulty on the assumption that 
you already understand the concepts from the earlier episodes.
"""
def main():
    # 1. Create a list of 5 numbers and loop through the list to print each number.
    l = [1, 2, 3, 4, 5]
    for i in l:
        print(i)
    # 2. You have the following list: 
    l2 = ['B', 'L', 'U', 'E', 'B', 'E', 'R', 'R', 'Y']
    #     Using a while loop, create a new string that is the reverse of the original.
    #     s = 'YRREBEULB'
    s = ''
    x = len(l2) - 1
    while x >= 0:
        s += l2[x]
        x -= 1
    print(s)
    # 3. You have the following list:
    l3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 54, 88, 72, 30, 54, 80, 123, 88]
    #    Using a for loop, alter l3 to add the elements index value to the elements value.
    #    For example, the first element in l3 is 1, so you would add 0 to 1 to get 1.
    for i in range(len(l3)):
        l3[i] += i
    print(l3)
    # 4. Stretch Problem:
    #    You have the following string: "john doe, jane guthry, and john smith"
    #    Using a while loop, capitalize all of the names in the string and re-create string.
    #    For example, the string would become "John Doe, Jane Guthry, and John Smith"
    """
    Hint: my intent for this problem is not for you to use .split() or any string methods.
    -- I want you to use a while loop to iterate through the string and capitalize each name.

    You will have to use a concept we haven't covered yet (hence why this is a stretch problem)

    if statement syntax:
    
    if condition:
        # do something
    else:
        # do something else

    Objective List:
    1. Think of how to use a while loop and a counter to keep track of the index of the string as you loop.
    2. Think of the unique characters that separate the names or of how to identify the start of the string for the first character.
    3. Think of how to capitalize the first character of each name.
    4. Think of how to re-create the string with the capitalized names.
    """
    s = "john doe, jane guthry, and john smith"
    new_s = ''
    x = 0
    while x < len(s):
        if x == 0:
            new_s += s[x].upper()
        elif s[x-1] == ' ':
            if x < len(s) - 3:
                if s[x:x+3] == 'and':
                    new_s += 'and'
                    x += 2
                else:
                    new_s += s[x].upper()
            else:
                new_s += s[x].upper()
        else:
            new_s += s[x]
        x += 1
    print(new_s)
    # I don't expect you to have gotten this one if you are new to Python and programming in general.
    # If you did, great job!
    # If not, don't worry, the main purpose is to get you starting to think about how to solve problems
    # because that is what programming is all about.  First you solve the problem, then you learn to try
    # to solve it in themost efficient way possible.
    # This was to showcase the use of a while loop and if statements to solve a problem, even if it isn't
    # the most efficient way to do it.


    pass

if __name__ == "__main__":
    main()