# Episode 10: More Looping Concepts, help() and Dynamic Typing
"""
This episode is going to cover the following:
1. Nested Loops
2. Break
3. Continue
4. Pass
5. Helper Functions
    -help()
6. Dynamic Typing - Bare Bottomed Basics
    -Introduction to 'is', 'id' 
"""

# 1. Nested Loops
l = [1, 2, 3, 4, 5]
l2 = [6, 7, 8, 9, 10]

res = []
for i in l:
    for j in l2:
        res.append(i + j)
print(res)
# Note here that the outcome might not be what you expect.
# To accomplish looping through both simultaneously, you can use the 
# zip() function to combine the two lists into a single iterable.
res = []
for i, j in zip(l, l2):
    res.append(i + j)
print(res)

# 2. break (lowercase)
"""
Break is used to break out of the current loop.  If it is the only loop,
then it will break out of the loop entirely.  
"""

for i in l:
    if i == 3:
        break
    print(i)
    # This will print 1 and 2, then break out of the loop.

# Nested Loop Example
res = []
for i in l:
    for j in l2:
        if j == 8:
            break
        res.append(i + j)

print(f'{res=}')

# 3. continue (lowercase)
"""
Continue is used to skip the current iteration of the loop and continue to the next iteration.
"""
res = []
for i in l:
    if i == 3:
        continue
    res.append(i)
    # This will print 1, 2, 4, 5.  It skips 3.

# Combination of break and continue
res = []
for i in l:
    if i == 3:
        continue
    for j in l2:
        if j == 8:
            break
        res.append(i + j)
print(f'{res=}')

# 4. pass (lowercase)
# Pass is used as a placeholder when you don't want to do anything.
for i in l:
    pass
    # This will do nothing, but it will not throw an error.

# More 'realistic' example and example of 'flag' variable
"""
Goal, you have two lists of numbers. 'a' and 'b'.
You want to add each number from A to every number in
B only while conditions are met.

Example:
res = [a1b1, a1b2, a1b3, a1b4, a1b5, a2b1, a2b2 ...]

Conditions:
1. The sum is even
2. The length of the resulting list is less than 20 elements.
3. The number from element 'b' is skipped if not odd after 
4th time it is encountered.
"""

a = [35, 70, 99, 10, 11]
b = [1, 2, 3, 4, 5]

flag = 0 # This increments every time an even number in list 'b' is reached
res = [] # The results container (list)
for i in a:
    if len(res) >= 20:
        break
    for j in b:
        if len(res) >= 20:
            break # Have to check again in case the inner loop adds an element over 20.
        if flag < 5:
            if j % 2 == 0:
                flag += 1
            if (i + j) % 2 == 0:
                res.append(i + j)
        else:
            if j % 2 == 0:
                continue
            elif (i + j) % 2 == 0:
                res.append(i + j)
                flag = 0

print(f'{res=}')

"""
The above example is contrived, but it shows how you can use break and continue in a nested loop.
It also shows how you can use a 'flag' variable to keep track of how many times a condition is met.

This should just get you thinking about how to use these concepts in your own code.  

***NOTE*** 
Oftentimes, you can organize conditional statements to avoid redundant code and maximize efficiency.

For example, is it possible to re-organize the conditions to avoid redundant even/odd checks in the above code?

This isn't a prime example of this, I continue to work on trying to better understand the logic flow.
"""

"""
Aside: 
There are websites of problems that will increase your ability to think logically solve through these challenges.

Watching other 'master's of the craft destroy some problems with as little code as possible is a 
great way to learn.  I recommend CodeInGame for timed coding match challenges.  Although, you will learn your place very quickly,
it is a great way to see how others solve problems and to learn from them.

Leetcode, HackerRank, CodeSignal, CodeWars, etc.
"""

# 5. help()
"""
This function looks up the documentation for a given object and outputs it to STDOUT.
"""

help(print)
# This will output the documentation for the 'print' function.
help(str)
# This will output the documentation for the 'str' class.

# 6. Dynamic Typing - Bare Bottomed Basics

"""
One of the core things to understand about what 'Dynamic Typing' means in Python is that
types live with the objects in memory, they aren't attached to variable names at all.
"""

# Example Dynamic Typing 1
a = 5
print(type(a))
# This will output <class 'int'> because the '5' object is an integer.

"""
What this means is that variable names are just references or pointers to actually existent objects in memory.
The NAMES of the variables are stored in the namespace of the program.  This namespace allows you to access
the objects in memory by using their names.  If you ever delete a variable, you are just removing the reference
to the object in memory, not the object itself.  Python has what is called a 'garbage collector' that checks for 
objects in memory that no longer have references (aka variable names pointing to them) and deletes them.
"""

# Example Dynamic Typing 2 
a = 'Hello'
b = 'Hello'
print(a is b)
# 'is' is used to check if two variables are pointing to the same object in memory.
# This will output True because for some strings and small integers, Python will store them in memory and point multiple variables
# to the same object.  This is called 'interning'.

print(id(a))
print(id(b))
# This will output the same memory address for both 'a' and 'b'.  It returns the memory address for the object.

# Example Dynamic Typing 3
del a
# This will delete the variable 'a' from the namespace, but the object 'Hello' will still exist because
# 'b' is still pointing to it.
print(b)
del b
# Now 'Hello' will be deleted from memory because there are no more references to it.

"""
In other languages, you have to declare the type of the variable when you create it.

Example:
int a = 5;

Then 'a' is an integer and can only be an integer.  In Python you can simply keep reassigning different objects
to the same variable name.  This is why Python is called 'dynamically typed'.  The type of the variable is determined
by the object that it is pointing to in memory.

"""  

b = 5
print(type(b))







