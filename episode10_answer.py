from typing import List

# Episode 10 Practice: More Looping Concepts, help() and Dynamic Typing

def main():
    # 1. What is the output of the problem_1 function below?
    
    l = [1, 2, 3]
    m = [4, 5, 6]

    def problem_1(l, m):
        res = []
        for i in l:
            for j in m:
                res.append(i + j)
    
    print(f'{problem_1(l, m)=}')

    """
    ANSWER:
    This was a trick question because the function doesn't have a return statement, so it
    returns None.

    The res, if returned, would be [4, 5, 6, 6, 7, 8, 7, 8, 9]
    """

    # 2. What is the output of the problem_2 function below?
    x = 10
    def problem_2(x: str) -> List[int]:
        res = [0, 1, 1]
        while res[-1] < int(x):
            res.append(res[-1] + res[-2])
        return res
    
    print(f'{problem_2(x)=}')

    """
    ANSWER:
    [0, 1, 1, 2, 3, 5, 8, 13]"""

    # 3. What is the output of the problem_3 function below?
    l = [1, 2, 3, 4, 5]
    def problem_3(l: list[int]) -> List[int]:
        res = []
        for i in l:
            if i % 2 == 0:
                continue
            res.append(i)
        return res
    
    print(f'{problem_3(l)=}')

    """"
    "ANSWER:
    [1, 3, 5]"

    continue - skips the code underneath it and starts the next loop cycle
    """

    # 4. How does the continue statement function in a loop?
    """
    continue skips the current iteration of the loop from the point it is called and
    continues with the next interation of the loop.

    For example, in the problem_3 above, the continue statement skips the 'res.append(i)'
    line when 'i' is even, thus only odd numbers are appended to the result list.
    """
    # 5. How does the break statement function in a loop?
    """
    break terminates the enclosing loop.  Careful to understand the significance of 'enclosing'
    loop.  If there are nested loops, break will only terminate the loop in which it is called.
    """
    # 6. What is the purpose of the pass statement in Python?
    """
    This is largely a placeholder value.  It is basically just skipped over and the remaining
    code underneath it is still executed.
    """
    # 7. What is the purpose of the help() function in Python?
    """
    The help function can get you information about all Python objects, built-in functions, etc.
    It is useful if you just want a quick reference to the syntax of a function or class.  It 
    doesn't require internet connection or additional typing.  Would be beneficial
    to use interactive prompt to test out the help function on various objects.
    """
    # 8. How is dynamic typing unique as compared to static typed langauges?
    """
    The main takeaway should be that variables aren't typed, objects are.  This means that
    when an object is created in memory via variable assignment, its type is coded in the object
    itself.  The variables themselves are just references to the objects in memory, so if they are
    called, the object is accessed.

    It is considered 'pythonic' to use dynamic typing because it allows for more flexibility in coding.
    You aren't type testing up front, you are coding in a way that will accept any object and deal with it 
    as it comes.  This is different from static typing languages like Java or C++ where variables are
    explicitly typed and must match the type of the object assigned to it.  In static typing, you would get an
    error if you tried to assign a string to an integer variable, for example.
    """
    # 9. What is the difference between 'is' and '==' in Python?
    """
    'is' is checking to see if the two variables are pointing to the exact same object in memory.
    '==' is checking to see if the values of the two objects are equal in value.
    """
    pass

if __name__ == "__main__":
    main()