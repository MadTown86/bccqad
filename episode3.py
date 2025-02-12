# Episode 3: Lists (Tuples and Sets)

def main():
    print("\nSection 3 Examples\n")
    # Creating a list
    l = [1, 2, 3, 4, 5]
    print("l created by definiting all elements, comma separated, within brackets [1, 2, 3, 4, 5] :: ", l)
    l = list(range(1, 6))
    print("l created by using list(range(1, 6)) :: ", l)
    l = ['a', 'b', 'c', 'd', 'e']
    print("l created using brackets and comma separated strings ['a', 'b', 'c', 'd', 'e'] :: ", l)
    l = list('abcde')
    print("The same list created using l = list('abcde') :: ", l)
    # Here we are overwriting l with a new list each time

    print("\n")
    # Note that the \n is used to create two new lines in the output, this is called an 'escape character'

    l = [1, 2, 3, 4, 5]
    print("l starts off equal to: \n", l)
    # Accessing elements in a list
    print("l[0] = ", l[0])
    print("l[1] = ", l[1])
    print("l[2] = ", l[2])

    # The index position starts at 0 and goes to the length of the list - 1
    # So if there are five elements, the last item will be at index of 4

    # You can also access elements from the end of the list
    print("We can access elements with negative index values, -1 is always the last item: l[-1] = \n", l[-1])
    print("Accessing negative index values starts incrementing towards the first element: l[-2] = \n", l[-2])

    print("\n")

    # You can also access a range of elements using slices
    print("Slicing - first number is starting index and inclusive : second number is ending index and exclusive")
    print("l[0:2] = ", l[0:2])
    print("l[1:3] = ", l[1:3])

    print("\n")

    # You can also leave out the first or last index
    print("What happens when you omit the first or last index?")
    print("l[:2] = ", l[:2])
    print("l[2:] = ", l[2:])

    print("\n")

    # You can also use negative numbers
    print("What happens when you use negative numbers?")
    print("l[:-1] = ", l[:-1])
    print("l[-2:] = ", l[-2:])

    print("\n")

    # You can also use a step
    print("What happens when you use a step and a second colon?")
    print("l[::2] = ", l[::2])
    print("l[::-1] = ", l[::-1])

    print("All of the above just 'sliced' portions of the list, l is still equal to: ", l)

    print("\n")

    # You can also change elements in a list by assigning to an index
    l[0] = 10
    print("We just reassigned l[0]'s value to 10, so now l = ", l)
    print("You do this with syntax variable_name[index] = new_value\n")

    # You can also add elements to a list
    l.append(6)
    print("We just used .append(6) to add 6 to the end of l, so l = ", l)

    print("\n")

    # You can also insert elements at a specific index
    l.insert(0, 0)
    print("We just used .insert(0, 0) to add 0 to the beginning of l, so l = ", l)

    print("\n")

    # You can also remove elements from a list
    l.remove(6)
    print("We just used .remove(6) to remove 6 from l, so l = ", l)  

    print("\n")

    # You can also remove elements at a specific index
    l.pop(0)
    print("We just used .pop(0) to remove the first element in l, l now = ", l)
    # If you don't specify an index, it will remove the last element
    # This 'returns' the element that was removed.  So you can assign it to a variable while removing it

    print("\n")

    x = l.pop()
    print("We just popped the last element off of l and assigned it to x with 'x = l.pop()', so x = ", x)
    print("l now = ", l)

    print("\n")

    # You can also clear a list
    l.clear()
    print("We just cleared l using .clear(), so l = ", l)

    print("\n")

    # You can also delete a list
    del l
    print("We just deleted l by using 'del l', so l no longer exists and can't be printed!")

    print("\n")

    # You can also copy a list
    l = [1, 2, 3, 4, 5]
    print("We recreated l, l = ", l)

    print("\n")

    l2 = l.copy()
    print("l2 is a copy", l2)
    print("Does l == l2? ", l == l2)

    print("\n")

    # You can sort a list
    l = [5, 3, 1, 4, 2]
    l.sort()
    print("l sorted using .sort() = ", l)

    print("\n")

    # You can also reverse a list
    l.reverse()
    print("l reversed using .reverse() = ", l)

    print("\n")

    # You can also count the number of times an element appears in a list
    l = [1, 2, 3, 4, 5, 1]
    print("l = ", l)
    print("l.count(1) = ", l.count(1))

    print("\n")

    # You can also find the index of an element
    print("l.index(1) = ", l.index(1))
    print("Note that it only finds and returns the first occurrence of the element, not all of them")

    print("\n")

    # You can also extend a list
    l.extend([6, 7, 8, 9, 10])
    print("Extending a list with l.extend([6, 7, 8, 9, 10]) = ", l)

    print("\n")

    # You can also use the '+' operator to concatenate lists
    l = l + [11, 12, 13, 14, 15]
    print("Concatenating lists using the '+' operator = ", l)

    print("\n")
    
    # Re-creating basic list
    l = [1, 2, 3, 4, 5]
    print("l was re-created, l now = ", l)

    # You can also use the '*' operator to repeat a list
    l = l * 2
    print("Repeating a list using the '*' operator 'l = l * 2' = ", l)

    print("\n")

    # You can use arbitrary nesting of lists to create matrices
    l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print("A matrix created using nested lists: ", l)
    for row in l:
        print(row)

    print("\n")

    # You can also use list comprehension to create lists
    print("List comprehension is a way to create lists using a single line of code")
    l = [i for i in range(10)]
    print("A list created using list comprehension: ", l)

    print("\n")

    # You can also use list comprehension to create lists with conditions
    l = [i for i in range(10) if i % 2 == 0]
    """
    Detailed Explanation:
    the leftmost 'i' is the value that is being appended to the list
    You can put an equation here, a function, or just the value itself

    the 'for i in range(10)' is the loop that is being used to generate the values
    it starts at 0 and goes to the value 9

    the 'if i % 2 == 0' is the condition that must be met for the value to be appended to the list

    To give you how I think of it in my own words:
    "Put 'i' in the list for every 'i' in the range of 0 to 9 if 'i' is an even number (i % 2 == 0) remember % is the modulo operator and
    just returns the remainder"

    You can also break this down into the following code:
    l = [] # Create an empty list
    for i in range(10): # Loop through the range of 0 to 9
        if i % 2 == 0: # If the number is even
            l.append(i) # Add it to the list
    
    The reason for comprehensions is that it is more concise and easier to read and can actually run faster than a standard for loop
    """
    print("A list created using list comprehension with a condition: ", l)

    print("\n")

    l = [[i**2, i**3] for i in range(10) if i % 2 != 0]
    """
    My own words: place the list [i**2, i**3] in the list we are creating for every 'i' in the range of 0 to 9 if 'i' is an odd number (i % 2 != 0)
    """
    print("A list created using list comprehension with a condition and an equation: ", l)

    print("\n")

    print("Episode 3: Tuples and Sets Brief")
    # Tuples are like lists but are 'immutable' meaning they can't be changed
    t = (1, 2, 3, 4, 5)
    print("A tuple created using parentheses (1, 2, 3, 4, 5) :: ", t)
    t = tuple(range(1, 6))
    print("A tuple created using tuple(range(1, 6)) :: ", t)
    # You can access elements in a tuple the same way you do in a list
    print("t[0] = ", t[0])
    print("t[1] = ", t[1])
    print("t[2] = ", t[2])

    # You can't change elements in a tuple so the only methods you can use are count() and index()
    print("t.count(1) = ", t.count(1))
    print("t.index(1) = ", t.index(1))

    print("\n")

    # Sets are like lists but are unordered and have no duplicates
    s = {1, 2, 3, 4, 5}
    print("A set created using curly braces {1, 2, 3, 4, 5} :: ", s)
    s = set(range(1, 6))
    print("A set created using set(range(1, 6)) :: ", s)
    # You can't access elements in a set because they are unordered

    # You can add elements to a set
    s.add(6)
    print("We just added 6 to the set using .add(6), so s = ", s)

    # You can remove elements from a set
    s.remove(6)
    print("We just removed 6 from the set using .remove(6), so s = ", s)    

    # You can also clear a set
    s.clear()
    print("We just cleared the set using .clear(), so s = ", s)

    # You can also delete a set
    del s
    print("We just deleted the set using 'del s', so s no longer exists and can't be printed!")

    # You can also copy a set
    s = {1, 2, 3, 4, 5}
    print("We recreated s, s = ", s)

    s2 = s.copy()
    print("s2 is a copy", s2)
    print("Does s == s2? ", s == s2)

    # You can also use the union() method to combine two sets
    s = {1, 2, 3, 4, 5}
    s2 = {4, 5, 6, 7, 8}
    print("s = ", s)
    print("s2 = ", s2)
    print("s.union(s2) = ", s.union(s2))

    # You can also use the intersection() method to find the common elements between two sets
    print("s.intersection(s2) = ", s.intersection(s2))

    # You can also use the difference() method to find the elements that are in the first set but not the second
    print("s.difference(s2) = ", s.difference(s2))

    # You can also use the symmetric_difference() method to find the elements that are in one set or the other but not both
    print("s.symmetric_difference(s2) = ", s.symmetric_difference(s2))

    """
    Sets are useful for filtering and removing duplicates from lists
    """

    print("\n")

    """
    Comprehensions can also be used with both tuples and sets
    t = (i for i in range(10)) # Tuple comprehension
    s = {i for i in range(10)} # Set comprehension
    """
    


if __name__ == "__main__":
    main()