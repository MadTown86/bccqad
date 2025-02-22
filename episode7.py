# Episode 7: Reading Files
import json

def main():
    def mini_reader(to_path="episode7_input.txt"):
        with open(file=to_path, mode='r') as f:
            print(f.read())
    """
    Without going into great detail, I am just giving you examples of how to read and write files in Python.

    https://docs.python.org/3/library/functions.html#open

    'r' - Open for reading (default if ommitted)
    'w' - Open for writing, truncating the file first
    'a' - Open for appending, creating the file if it does not exist
    'r+' - Open for reading and writing

    Syntax: open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
    
    *note that 'file' in the above syntax is the name of a local file (e.g. 'episode6_input.txt') or 
    a full path to a file (e.g. '.../username/Documents/episode6_input.txt')
    """
    path2 = "episode7_output.txt"
    path3 = "episode7_output.json"
    #region Basic Open and Context Manager
    # 'Basic Open'
    f = open("episode7_input.txt", 'r')
    f.close() # need to remember to close the file after opening.

    # 'Context Manager' to open a file in a way that auto-closes file
    with open("episode7_input.txt", 'r') as f:
        pass # Just a placeholder
    #endregion

    # 'read()' - reads the entire file and returns it as one large string with newline characters
    print("\n'read()' - reads the entire file and returns it as one large string with newline characters")
    with open("episode7_input.txt", 'r') as f:
        print(f.read())

    #region Different Methods for Reading Files, truncating files and seeking
    # 'readline()' - reads a single line from the file
    print("\n'readline()' - reads a single line from the file\n")
    with open("episode7_input.txt", 'r') as f:
        print(f.readline())

    # 'readlines()' - reads all lines from the file and returns a list of strings that were separated by newline escapes
    print("\n'readlines()' - returns a list of strings that were separated by newline escapes\n")
    with open("episode7_input.txt", 'r') as f:
        print(f.readlines())

    # 'seek()' - moves the cursor to a certain position in the file
    print("\n'seek()' - moves the cursor to a certain position in the file\n")
    with open("episode7_input.txt", 'r+') as f: # or 'w'
        f.seek(10) # moves the cursor to the beginning of the file
        print(f.read())
    #endregion

    # 'truncate()' - truncates the file to a certain size
    print("\n'truncate()' - truncates the file to a certain size\n")
    with open("episode7_input.txt", 'r+') as f: # or 'w'
        f.truncate(10) # truncates the file to 10 characters, set to 0 to delete all contents
    mini_reader()

    #region Different Methods for Writing Files
    # 'write()' - writes a string to the file
    print("\n'write()' - writes a string to the file")
    with open("episode7_output.txt", 'w') as f:
        f.write("Hello, World!")
    mini_reader(path2)
        # Notice how this will overwrite the file if it already exists.

    # 'writelines()' - writes a list of strings to the file
    print("\n'writelines()' - writes a list of strings to the file\n")
    with open("episode7_output.txt", 'w') as f:
        f.writelines(["Hello, World!\n", "My name is GrovesDaMan.\n",
                        "I am a Python programmer.\n", "I am trying to teach so I can better learn myself.\n"])
    mini_reader(path2)
        # Notice how this will overwrite the file if it already exists.
    #endregion

    #region JSON
    """
    JSON is a popular format for storing and exchanging data.  It is a text format that is completely language independent.

    JSON is built on two structures:
    1. A collection of key/value pairs.  In Python, this is a dictionary.
    2. An ordered list of values.  In Python, this is a list.

    I have come across JSON in the form of API responses and data storage.  I will cover its simple use here.
    """
    # 'json.dump()' - writes a Python object to a file in JSON format
    print("\n'json.dump()' - writes a Python object to a file in JSON format\n")
    with open("episode7_output.json", 'w') as f:
        json.dump({"a": 1, "b": 2, "c": 3}, f)
    mini_reader(path3)

    # 'json.load()' - reads a JSON file and returns a Python object
    print("\n'json.load()' - reads a JSON file and returns a Python object\n")
    with open("episode7_output.json", 'r') as f:
        d = json.load(f)
        print(f'{d=}')
        print(type(d)) # it is recognized as the dictionary class without further conversion
    #endregion



if __name__ == "__main__":
    data = """The sample for episode6 isn't much.  Its short
and hopefully sweet
and should get the point
across, I hope.
"""
    with open("episode7_input.txt", 'w') as f:
        f.write(data)
    main()