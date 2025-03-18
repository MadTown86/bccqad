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

    # 2. What is the output of the problem_2 function below?
    x = input("Enter the upper bounds of the Fibonacci sequence: ")
    def problem_2(x: str) -> List[int]:
        res = [0, 1, 1]
        while res[-1] < int(x):
            res.append(res[-1] + res[-2])
        return res

    # 3. What is the output of the problem_3 function below?
    l = [1, 2, 3, 4, 5]
    def problem_3(l: list[int]) -> List[int]:
        res = []
        for i in l:
            if i % 2 == 0:
                continue
            res.append(i)
        return res

    # 4. How does the continue statement function in a loop?
    # 5. How does the break statement function in a loop?
    # 6. What is the purpose of the pass statement in Python?
    # 7. What is the purpose of the help() function in Python?
    # 8. How is dynamic typing unique as compared to static typed langauges?
    # 9. What is the difference between 'is' and '==' in Python?
    pass

if __name__ == "__main__":
    main()