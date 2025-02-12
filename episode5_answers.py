from copy import deepcopy

def main():
    """ASIDE: Dictionary Copies and what it means to be MUTABLE
    
    When you make a copy of a dictionary, you are copying the reference to the
    same dictionary in memory.  This means that if you do the following:

    d = {"a": 1, "b": 2, "c": 3}
    d2 = d
    d2["d"] = 4
    
    Both REFERENCES 'd' and 'd2' will have the new key:value pair. 
    d = {"a": 1, "b": 2, "c": 3, "d": 4}
    d2 = {"a": 1, "b": 2, "c": 3, "d": 4}

    This is one of the things to watch out for when working with mutable objects.

    If you want a TRUE copy of a dictionary, you have to use the deepcopy method from
    the copy module.
    
    """


    # 1. What must be true about any keyword used for the keyword:value pair assignment of a dictionary?
    """
    It has to be immutable.  So it can be a string, number, or tuple, but not a list or another dictionary.
    """
    # 2. What are 2 ways to create a dictionary?
    print("\nQuestion 2: What are 2 ways to create a dicitonary? - Output:")
    d1 = {'a': 1, 'b': 2, 'c': 3}
    d2 = dict(a=1, b=2, c=3)
    d3 = dict([('a', 1), ('b', 2), ('c', 3)])
    d4 = dict(zip(['a', 'b', 'c'], [1, 2, 3]))
    print(f'{d1=}')
    print(f'{d2=}')
    print(f'{d3=}')
    print(f'{d4=}')
    
    # 3. Create the following dictionary:
    #    d = {"a": 1, "b": 2, "c": 3}
    """
    Above
    """

    # 4. Overwrite the 'b' key's VALUE of 2 in the above dictionariy 'd' with the dictionary below:
    #    {"e": [1, 2, 3]}
    print("\nOverwrite the 'b' key's VALUE of 2 in the above dictionariy 'd' with the dictionary below - Output:")
    d1['b'] = {"e": [1, 2, 3]}
    print(f'{d1=}')

    # 5. Append a 4 to the list in the 'e' key of the nested dictionary in the above 'd' dictionary.
    print("\nQuestion 5: Append a 4 to the list in the 'e' key of the nested dictionary in the above 'd' dictionary - Output:")
    d1['b']['e'].append(4)
    print(f'{d1=}')

    # 6. What is one way to remove the 'e' key from the above 'd' dictionary?
    d5 = deepcopy(d1)
    print(f'D5 starts as: {d5=}')
    print(f'D1 starts as: {d1=}')
    print("\nQuestion 6: What is one way to remove the 'e' key from the above 'd' dictionary? - Output:")
    
    del d5['b']['e']
    d1['b'].pop('e')
    
    print(f'Output: {d5=}')
    print(f'Output: {d1=}')

    # 7. Create dictionary 'd2' with the following key: value pairs:
    #    d2 = {"a": 2, "f": 4, "g": {'e': 5}}
    print("\nQuestion 7: Create dictionary 'd2' with the following key: value pairs - Output:")
    d2 = {"a": 2, "f": 4, "g": 5}
    print(f'{d2=}')
    
    # 8. If you were to merge the two dictionaries, what would the resultant list of keys be for the dictionary?
    print("\nQuestion 8: If you were to merge the two dictionaries with .update(), what would the resultant list of key:value pairs be - Output:")
    """
    d.keys() == ['a', 'b', 'c', 'f', 'g']
    """
    d1.update(d2)
    print(f'{d1.keys()=}')

    # 9. If you were to merge the two dictionaries, what would the value of the 'a' key be?
    print("\nQuestion 9: If you were to merge the two dictionaries with .update(), what would the value of the 'a' key be - Output:")
    """
    'a' would equal 2 and be overwritten.
    """
    print(f'{d1["a"]=}')
    
if __name__ == "__main__":
    main()