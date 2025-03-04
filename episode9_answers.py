# Episode 9 Practice

def main():
    # 1. What is the syntax of an if statement in Python?
    """
    if condition:
        # code block to execute if condition is true
    """
    # 2. What is the syntax of an if-else statement in Python?
    """
    if condition:
        # code block to execute if condition is true
    else:
        # code block to execute if condition is false
    """
    # 3. What is the syntax of an if-elif-else statement in Python?
    """
    if condition:
        # code block to execute if condition is true
    elif another_condition:
        # code block to execute if another_condition is true
    else:
        # code block to execute if none of the above conditions are true
    """
    # 4. Create a script that takes a number as input and prints whether the number is even or odd.
    def even_or_odd(num):
        if num % 2 == 0:
            return f"{num} is even"
        else:
            return f"{num} is odd"
    print(even_or_odd(10))
    # 5. Stretch Problem:
    """
    Create a function that will have the following:
    1. A string positional argument first
    2. A default argument that takes a string 'case'
        - ['upper', 'lower', 'capitalize', 'none']
        - default is 'none'
        - 'upper' will alter original string into all uppercase
        - 'lower' will alter original string into all lowercase
        - 'capitalize' will capitalize the first character of the string
        - 'none' will leave the string as is
    3. A second default argument that takes a string 'output'.
        - ['list', 'string']
        - default is 'string'
        - 'list' will return the string as a list of characters
        - 'string' will return the output as a string
    4. Accept a variable amount of keyword arguments.
        - ['reverse', 'leading whitespace', 'trailing whitespace', 'strip', 'none']
        - default is 'none'
        - 'reverse' will reverse the string
        - 'leading whitespace' will add a space before the string
        - 'trailing whitespace' will add a space after the string
        - 'strip' will remove leading and trailing whitespace
        - 'none' will leave the string as is
    5. The function should handle errors gracefully and return a message if the mode is not recognized.
    """
    def string_arranger(s: str, case: str = 'none', output: str = 'string', **kwargs):
        if case == 'upper':
            s = s.upper()
        elif case == 'lower':
            s = s.lower()
        elif case == 'capitalize':
            s = s.capitalize()
        elif case != 'none':
            return "Error: Unrecognized case mode."
        
        if output == 'list':
            result = list(s)
        elif output == 'string':
            result = s
        else:
            return "Error: Unrecognized output mode."
        
        if kwargs.get('reverse', False):
            result = result[::-1]
        if kwargs.get('leading whitespace', False):
            result = [' '] + result
        if kwargs.get('trailing whitespace', False):
            result += [' ']
        if kwargs.get('strip', False):
            result = [char for char in result if char != ' ']
        
        return result
    print(string_arranger("hello World", case='capitalize', output='list', reverse=True, leading_whitespace=True))

if __name__ == "__main__":
    main()