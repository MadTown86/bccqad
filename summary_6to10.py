# Summary of Episodes 6-10:
# 1. Looping Concepts
# 2. Files
# 3. Functions
# 4. Control Flow Statements (Conditionals)
# 5. Dynamic Typing
# 6. Helper Functions (help())

import random
from math import isinf
from typing import List, Tuple
from collections import defaultdict

"""
Prime Directive: To automatically create a list of lines on a cartesian plane and
print data to file.

Then extract plot point information from a the file, 
sort the points by slope, and organize them into a dictionary based on their slope values.

Write this dictionary to a JSON file, where the keys are the slope values and the values are the
list of points with that slope.
"""

"""
Intro Explanation:
I am breaking up the solution to this problem into smaller chunks to make it easier to
understand and easier to debug. Each function will handle a specific part of the problem.
The main function will call each of these smaller functions in order to accomplish the task.

*NOTE*: This is just a practice example to showcase what we have learned.

It is not meant to be an example of best practices or production code.
"""

def random_points(n: int = 1000) -> List[Tuple[int, int]]:
    """
    Create a random list of points without duplicates

    Default Value: 1000 points
    :param n: Number of points to generate
    :return: List of tuples representing points (x, y)
    """
    res = set()
    for item in range(n):
        x = random.randint(-25, 25)
        y = random.randint(-25, 25)
        a = random.randint(-25, 25)
        b = random.randint(-25, 25)
        res.add(((x, y), (a, b)))
    return list(res)


def create_file(content: str, filename: str = "summary_6to10.txt") -> None:
    """
    Create a text file with the given content
    :param content: Content to write to the file
    :param filename: Name of the file to create (default: summary_6to10.txt)
    """
    if content:
        if not filename.endswith('.txt'):
            filename += '.txt'
            print(f"Filename changed to {filename}")
        with open(filename, 'w') as f:
            f.writelines(content)
        print(f"File {filename} created with content.")
    else:
        print("No content to write to file.")


def retrieve_file(filename: str = "summary_6to10.txt") -> str:
    """
    Retrieve the content of a text file
    :param filename: Name of the file to read (default: summary_6to10.txt)
    :return: Content of the file as a string
    """
    try:
        with open(filename, 'r') as f:
            content = f.read()
        print(f"File {filename} retrieved successfully.")
        content = eval(content) # Eval can turn a string representation of a Python object, into that Python Object
        return content
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return ""
    
def slope_calc(point1: Tuple[int, int], point2: Tuple[int, int]) -> float:
    """
    Calculate the slope between two points
    :param point1: First point as a tuple (x1, y1)
    :param point2: Second point as a tuple (x2, y2)
    :return: Slope as a float
    """
    x1, y1 = point1
    x2, y2 = point2
    if x2 - x1 == 0:
        return float('inf')  # Vertical line slope is undefined (infinity)
    return (y2 - y1) / (x2 - x1)
    
def calculate(data: List[Tuple[int, int]]) -> defaultdict:
    """
    Calculate the slope of each point and organize them into a dictionary based on their slope values
    :param data: List of tuples representing points (x, y)
    :return: Dictionary with slope values as keys and lists of points as values
    """
    slopes = defaultdict(list)
    for item in data:
        slopes[slope_calc(item[0], item[1])].append(item)

    
    for slope in list(slopes.keys()):
        if len(slopes[slope]) < 2:
            print()
            del slopes[slope]
            
    for slope in slopes:
        print([slopes[slope]])
    return slopes

def write_json(data: defaultdict, filename: str = "summary_6to10.json") -> None:
    """
    Write the slope dictionary to a JSON file
    :param data: Dictionary with slope values as keys and lists of points as values
    :param filename: Name of the JSON file to create (default: summary_6to10.json)
    """
    import json
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
    print(f"JSON file {filename} created with slope data.")

def load_print_json(filename: str = "summary_6to10.json") -> None:
    """
    Load and print the content of a JSON file
    :param filename: Name of the JSON file to read (default: summary_6to10.json)
    """
    import json
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
        print(f"JSON file {filename} loaded successfully.")
        for slope, points in data.items():
            if len(points) >= 2:
                print(f"Slope: {slope}, Points: {points}...")
    except FileNotFoundError:
        print(f"JSON file {filename} not found.")

def main():
    """
    The writing to files is redundant, but is done here to
    demonstrate the process.
    """
    # 1. Generate random points
    points = random_points(1000)
    
    # 2. Create a text file with the points
    create_file(str(points), "summary_6to10.txt")
    
    # 3. Retrieve the content of the text file
    content = retrieve_file("summary_6to10.txt")
    
    # 4. Calculate slopes and organize them into a dictionary
    slopes = calculate(content)
    
    # 5. Write the slope dictionary to a JSON file
    write_json(slopes, "summary_6to10.json")
    
    # 6. Load and print the content of the JSON file
    load_print_json("summary_6to10.json")

if __name__ == "__main__":
    main()

