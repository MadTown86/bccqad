# Episode 20: Intermediate Python Tutorial - Timing Your Functions
from time import perf_counter as pf

def my_timmer(func):
    def wrapper(*args, **kwargs):
        start_time = pf()
        result = func(*args, **kwargs)
        end_time = pf()
        print(f"Function '{func.__name__}' took {end_time - start_time:.8f} seconds")
        return result
    
    return wrapper

# def my_memory(func):
#     def wrapper(*args, **kwargs):
#         import tracemalloc
#         tracemalloc.start()
#         result = func(*args, **kwargs)
#         current, peak = tracemalloc.get_traced_memory()
#         print(f"Function '{func.__name__}' used {current / 10**6:.6f}MB of memory")
#         tracemalloc.stop()
#         return result
    
#     return wrapper

# @my_memory

@my_timmer
def my_function(n: int) -> int:
    """A function that calculates the sum of numbers from 0 to n-1."""

    total = 0
    for i in range(n):
        total += i
    return total

# @my_memory
@my_timmer
def reverse_it(n):
    res = []
    for i in range(-1, -len(n)-1, -1):
        res.append(n[i])
    return res

# @my_memory
@my_timmer
def merge_sort(l1, l2):
    """Merge two sorted lists into a single sorted list."""
    result = []
    i = j = 0
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            result.append(l1[i])
            i += 1
        else:
            result.append(l2[j])
            j += 1
    result.extend(l1[i:])
    result.extend(l2[j:])
    return result

# @my_memory
@my_timmer
def quadratic_function(n):
    """A function that calculates the sum of squares from 0 to n-1."""
    total = 0
    for i in range(n):
        for j in range(n):
            total += i * j
    return total

# @my_memory
@my_timmer
def cubic_function(n):
    """A function that calculates the sum of cubes from 0 to n-1."""
    total = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                total += i * j * k
    return total

if __name__ == "__main__":
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    print("\nStarting the program...")
    result = my_function(10000000)
    print(f"Result: {result}")
    print("Program finished.\n")

    print("Reversing the list...")
    reversed_list = reverse_it(l)
    print(f"Reversed list: {reversed_list}\n")

    # Merge Sort Example:
    l1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    l2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    print("Merging two sorted lists...")
    merged_list = merge_sort(l1, l2)
    print(f"Merged list: {merged_list}\n")

    # Quadratic Function Example:
    print("Calculating the sum of squares...")
    result = quadratic_function(1000)
    print(f"Result: {result}\n")

    # Cubic Function Example:
    print("Calculating the sum of cubes...")
    result = cubic_function(100)
    print(f"Result: {result}\n")

# This code defines a decorator that times how long a function takes to execute.