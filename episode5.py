# Episode 5: Dictionaries (Mappings)
from copy import deepcopy

def main():

    """
    A dictionary is a collection of key:value pairs.  They are unordered, mutable and support arbitrary nesting.

    Keys must be unique and immutable.  Values can be any type.

    Other languuages call dictionaries 'hash maps', 'associative arrays', or 'hash tables'. 
    """

    #region Dictionary Creation

    # 1. Curly braces
    print("\nOne way to create a dictionary is with curly braces.")
    print("d = {\"a\": 1, \"b\": 2, \"c\": 3}")
    d = {"a": 1, "b": 2, "c": 3}
    print(f'{d=}')

    # 2. dict() constructor
    print("\nA second way to create a dictionary is with the dict() constructor.")
    print("d = dict(a=1, b=2, c=3)")
    d = dict(a=1, b=2, c=3)
    print(f'{d=}')

    # 3. dict() constructor with a list of tuples
    print("\nA third way to create a dictionary is with the dict() constructor and a list of tuples.")
    print("d = dict([(\"a\", 1), (\"b\", 2), (\"c\", 3)])")
    d = dict([("a", 1), ("b", 2), ("c", 3)])
    print(f'{d=}')
    #endregion

    #region Useful Dictionary Operations
    # 1. Accessing a value
    print("\nAccessing a value in a dictionary.")
    print("d[\"a\"]")
    print(f'{d["a"]=}')

    # 2. Adding a key:value pair
    print("\nAdding a key:value pair to a dictionary.")
    print("d[\"d\"] = 4")
    d["d"] = 4
    print(f'{d=}')

    # 3. Removing a key:value pair
    print("\nRemoving a key:value pair from a dictionary.")
    print("del d[\"d\"]")
    del d["d"]
    print(f'{d=}')

    # 4. Checking if a key exists
    print("\nChecking if a key exists in a dictionary.")
    print("\"a\" in d")
    print(f'{"a" in d=}')

    # 5. Getting a list of keys
    print("\nGetting a list of keys in a dictionary.")
    print("list(d.keys())")
    print(f'{list(d.keys())=}')

    # 6. Getting a list of values
    print("\nGetting a list of values in a dictionary.")
    print("list(d.values())")
    print(f'{list(d.values())=}')

    # 7. Getting a list of key:value pairs
    print("\nGetting a list of key:value pairs in a dictionary.")
    print("list(d.items())")
    print(f'{list(d.items())=}')

    # 8. Getting a value with a default value
    print("\nGetting a value with a default value.")
    print("d.get(\"a\", 0)")
    print(f'{d.get("a", 0)=}')
    print("d.get(\"z\", 0)")
    print(f'{d.get("z", 0)=}')

    # 9. Removing all key:value pairs
    print("\nRemoving all key:value pairs from a dictionary.")
    print("d.clear()")
    d.clear()
    print(f'{d=}')

    # 10. Shallow Copying a dictionary
    print("\nCopying a dictionary.")
    print("d = {\"a\": 1, \"b\": 2, \"c\": 3}")
    print("d2 = d.copy()")
    d = {"a": 1, "b": 2, "c": 3}
    d2 = d.copy()
    print(f'{d2=}')
    d2["d"] = 4
    print(f'{d=}')
    print(f'{d2=}')
    print("This is a shallow copy so they are independent of each other if not nested.")

    # 11. Deep Copy for Nested Dictionary
    print("\nDeep Copying a dictionary.")
    print("d = {\"a\": {\"b\": 1, \"c\": 2}, \"d\": {\"e\": 3, \"f\": 4}}")
    print("d2 = deepcopy(d)")
    d = {"a": {"b": 1, "c": 2}, "d": {"e": 3, "f": 4}}
    d2 = deepcopy(d)
    d3 = d.copy()

    print(f'\nStarting {d=}')
    print(f'Starting {d2=}')
    print(f'Starting {d3=}')

    print(f'\nChanging D with: d["a"]["b"] = 5')
    d["a"]["b"] = 5
    print(f'{d=}')
    print(f'{d2=}')
    print(f'{d3=}')
    print("The deep copy allows for true copying of dictionary so no more relationships exist between them.")
    

    # 11. Merging two dictionaries
    print("\nMerging two dictionaries.")
    print("d = {\"a\": 1, \"b\": 2, \"c\": 3}")
    print("d2 = {\"d\": 4, \"e\": 5, \"f\": 6}")
    print("d.update(d2)")
    d = {"a": 1, "b": 2, "c": 3}
    d2 = {"a": 5, "d": 4, "e": 5, "f": 6} # a is overwritten
    d.update(d2)
    print(f'{d=}')

    # 12. Using a dictionary comprehension
    print("\nUsing a dictionary comprehension.")
    print("d = {i: i**2 for i in range(1, 6)}")
    d = {i: i**2 for i in range(1, 6)}
    print(f'{d=}')

    # 13. Using a dictionary comprehension with a condition
    print("\nUsing a dictionary comprehension with a condition.")
    print("d = {i: i**2 for i in range(1, 6) if i % 2 == 0}")
    d = {i: i**2 for i in range(1, 6) if i % 2 == 0}
    print(f'{d=}')
    #endregion

    #region Nested Dictionaries
    # 1. Nested dictionary creation
    print("\nCreating a nested dictionary.")
    print("d = {\"a\": {\"b\": 1, \"c\": 2}, \"d\": {\"e\": 3, \"f\": 4}}")
    d = {"a": {"b": 1, "c": 2}, "d": {"e": 3, "f": 4}}
    print(f'{d=}')

    # 2. Accessing a value in a nested dictionary
    print("\nAccessing a value in a nested dictionary.")
    print("d[\"a\"][\"b\"]")
    print(f'{d["a"]["b"]=}')

    # 3. Adding a key:value pair to a nested dictionary
    print("\nAdding a key:value pair to a nested dictionary.")
    print("d[\"a\"][\"g\"] = 5")
    d["a"]["g"] = 5
    print(f'{d=}')
    #endregion

    """
    **NOTE** 
    You can access nested variables using this method in both dictionaries and lists.

    You simply stack the brackets to access the nested value. This is called 'chaining'.
    """






if __name__ == "__main__":
    main()