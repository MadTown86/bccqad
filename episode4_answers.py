# Note, need to import math for the last question.
import math
def main():
    # 1. Create a string using both types of quotation marks.
    s = 'Hello, World!'
    s2 = "Hello, World!"
    print(s, s2)

    # 2. Create a string using a triple-quoted string.
    s3 = """Hello, 
    World!
    My Friend!"""
    print(s3)

    # 3. Create the regular string "H\nE\nL\nL\nO" and using a raw string.  How are they different when printed out?
    s4 = "H\nE\nL\nL\nO"
    s5 = r"H\nE\nL\nL\nO"
    print(s4)
    print(s5)
    
    # 4. What string will be printed out if I slice the string "Hello, World!" with the slice [2:9:2]?  What does the slice [2:9:2] mean?
    """
    The slice will print out "lo o" because it starts at index 2 and goes to index 9 by 2.  Meow moo, Meow moo, count by two.
    """
    print(s[2:9:2])

    # 5. Using a string that contains "Hello, World!", take a slice and concatenate it with a string "Goodbye" to make the output "Goodbye, World!"
    a = "Goodbye"
    b = "Hello, World!"
    c = a + b[5:]
    print(c)
    
    # 4. Create a string with a unicode character in it using the \U escape sequence.  You will have to look up a value for a unicode character.
    d = "Only \U0001FAF5 can prevent forest fires."
    print(d)
    # https://symbl.cc/en/1FAF5-index-finger-pointing-at-the-viewer-emoji/

    # 5. Create three variables and use the three different methods of string formatting.
    d = 99.999999999
    first = "I say %s to %s so I say %s about %-6.2f%% of the time" % (a, b, c, d)
    print(first)
    # **NOTE** %-6.2f is a float with 6 spaces and 2 decimal places.  The - will left justify the number. It also ROUNDS it and you can't change that.
    d_fixed = str(d)[:5]
    # I converted to a string and sliced it to get the display value I desired
    first_altered = "I say %s to %s so I say %s about %s%% of the time" % (a, b, c, d_fixed)
    print(first_altered)

    dd = {"first": a, "second": b, "third": c, "fourth": d_fixed}
    first_with_dict = "I say %(first)s to %(second)s so I say %(third)s about %(fourth)s%% of the time" % dd
    print(first_with_dict)

    second = "I say {} to {} so I say {} about {:-6.2f}%% of the time".format(a, b, c, d)
    print(second)

    second_with_dict = "I say {first} to {second} so I say {third} about {fourth}%% of the time".format(**dd)
    print(second_with_dict)
    # **dd is a way to unpack a dictionary into keyword arguments for the format method, we will go over this in functions episode.

    third = f"I say {a} to {b} so I say {c} about {d:-6.2f}% of the time"
    print(third)
    third_with_dict = f"I say {dd['first']} to {dd['second']} so I say {dd['third']} about {dd['fourth']}% of the time"
    print(third_with_dict)

    # 6. Create the string "Your formatted string value for Pi is: 3.14" using a variable assigned to the long value of Pi, hint import math and use math.pi
    math_pi = math.pi
    print(f'{math_pi=}') # This is a way to automatically print name of variable and value, useful for debugging at times
    fourth = "Your formatted string value for Pi is: %.2f" % math_pi
    print(fourth)


if __name__ == "__main__":
    main()