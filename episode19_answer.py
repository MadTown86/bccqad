# Episode 19 Practice Answers:

# 1. What Big(O) time complexity is the following code?
def f1(n):
    for i in range(n):
        for j in range(n):
            print(i, j)
"""
The time complexity is O(n^2) because there are two nested loops, each iterating n times.
The total number of iterations is n * n = n^2.
"""

# 2. What Big(O) time complexity is the following code?
def f2(n):
    for i in range(n):
        print(n[i])
"""
The time complexity is O(n) because there is a single loop that iterates n times.
The total number of iterations is n.
"""

# 3. What Big(O) time complexity is the following code?
def f3(l, value):
    mid = len(l) // 2
    if l[mid] == value:
        return mid
    elif l[mid] < value:
        return f3(l[mid + 1:], value)
    else:
        return f3(l[:mid], value)
    
"""
The time complexity is O(log n) because the function is performing a binary search.
Each recursive call reduces the size of the list by half.
This results in a logarithmic number of calls, specifically log2(n).
The base of the logarithm is 2 because the list is divided in half each time.
"""
    
# 4. What Big(O) time complexity is the following code?
def f4(n):
    if n == 0:
        return 1
    else:
        return n * f4(n - 1)
    
"""
The time complexity is O(n) because the function is performing a linear recursive call.
Each call to f4 reduces n by 1 until it reaches 0.
"""
    
# 5. What Big(O) time complexity is the following code?
def f5(n):
    if n == 0:
        return 1
    else:
        return f5(n - 1) + f5(n - 1)
"""
The time complexity is O(2^n) because the function is performing an exponential recursive call.
Each call to f5 results in two more calls to f5, leading to a binary tree of calls.
The number of calls grows exponentially with n.
"""
    
# 6. What is the fastest time complexity?
"""
The fastest time complexity is O(1), which represents constant time complexity.
This means that the time taken to execute the algorithm does not depend on the size of the input.
For example, accessing an element in an array by index is O(1).
"""
# 7. What is the second fastest time complexity?
"""
The second fastest time complexity is O(log n), which represents logarithmic time complexity.
This means that the time taken to execute the algorithm grows logarithmically with the size of the input.
For example, binary search has a time complexity of O(log n) because it divides the input size in half with each step.
"""
# 8. Define linear time complexity.
"""
Linear time complexity, denoted as O(n), means that the time taken to execute the algorithm grows linearly with the size of the input.
This means that if the input size doubles, the time taken to execute the algorithm also doubles.
For example, a simple loop that iterates through all elements of an array has a linear time complexity of O(n).
"""