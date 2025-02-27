# Episode 8 Answers

def main():
    # 1. What is the syntax of function creation in Python?
    """
    def function_name(arg1, arg2, ...):
        # code block
        return value
    """
    # 2. How do you call a function in Python? - aka, calling a function is the term for using a function.
    """
    function_name(arg1, arg2, ...)
    """
    
    # 2. What order do the argument types follow for function creation?
    """
    Positional, keyword, default, *vargs, **kwargs
    """
    # 3. Create a function that takes a string as an argument and a number as an argument, then prints
    #    the string that many times.
    def repeater(s, n):
        for i in range(n):
            print(s)
    repeater("Hello, World!", 3)

    # 4. Create a function that takes a LIST of numbers as an argument and returns the sum of the numbers.
    def sum_list(l):
        return sum(l)
    
    # 5. Create a function that takes a variable amount of positional arguments and returns the sum of those arguments.
    def sum_varargs(*args):
        return sum(args)
    print(sum_varargs(1, 2, 3, 4, 5))

    # 6. Create a function that mimics the behavior of the list() built-in function and how it processes single string arguments.
    def to_stringlist(arg: str) -> list:
        res = []
        for i in arg:
            res.append(i)
        return res
    print(to_stringlist("Hello"))
    

    # 7. Create a function that takes a string as an argument and returns the string reversed.
    def reverse_string(s):
        return s[::-1]
    print(reverse_string("Hello"))

if __name__ == "__main__":
    main()