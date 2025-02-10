# Episode 6: Reading Files
import json

def main():
    """
    Without going into great detail, I am just giving you examples of how to read and write files in Python.
    """
    # 'Context Manager' to open a file in a way that auto-closes file
    with open("episode6_input.txt", 'r') as f:
        lines = f.readlines()

    print(lines)
    pass

if __name__ == "__main__":
    main()