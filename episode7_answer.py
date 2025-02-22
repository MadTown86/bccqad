# Episode 7 Answer
def main():
    # 1. What is one basic benefit of using a context manager when working with files?
    """
    The context manager handles automatically closing files even if an exception occurs.  
    """
    # 2. What is the difference between 'read()' and 'readline()'?
    """
    read() returns the entire file as one string, readline() returns a single line from the file as a string()
    """
    # 3. Write a script that creates a file called 'episode7_practice.txt' and writes
    #    "Hello, this is a practice file.\nI am practicing reading and writing files in Python." to it.
    with open("episode7_practice.txt", 'w') as f:
        f.write("Hello, this is a practice file.\nI am practicing reading and writing files in Python.")
    # 4. Read the file you created in multiple ways using 'read()', 'readline()', and 'readlines()'.
    with open("episode7_practice.txt", 'r') as f:
        print('read()')
        print(f.read())
        print("\n")
        f.seek(0)
        print('readline()')
        print(f.readline())
        print("\n")
        f.seek(0)
        print('readlines()')
        print(f.readlines())
        print("\n")
        """
        Note: you have to use seek(0) to reset the cursor to the beginning of the file after each time you read.
        A file is read linearly from the cursor position and does not automatically reset to the beginning.
        """
    # 5. Write a script that reads 'episode7_practice.txt' and prints out the first 10 characters of the file.
    with open("episode7_practice.txt", 'r') as f:
        print(f.read(10))
    # 6. Write a script that truncates the file to just the first line.  Note, use code to figure out
    #    how many characters to truncate the file to.  Be sure to use the correct mode when opening the file.
    with open("episode7_practice.txt", 'r+') as f:
        s = f.read()
        s.find('\n')
        f.truncate(s.find('\n'))
        f.seek(0)
        print(f.read())

if __name__ == "__main__":
    main()