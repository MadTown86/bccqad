# BCC - Episode 19: Intermediate Python - Big O Notation

"""
Sources:
https://en.wikipedia.org/wiki/Big_O_notation
https://www.geeksforgeeks.org/analysis-algorithms-big-o-analysis/

gemini 2.0 - ChatGPT

To give the basest of explanations, Big O Notation is the way to express
how time efficient a function is when considering worst case scenarios.

size of input : time it takes to run the function

You will often hear time complexity and space complexity when discussing Big O
notation.

Time complexity is how long a function takes to run in relation to the size of the input.
Space complexity is how much memory a function uses in relation to the size of the input.

We are only discussing time complexity in this episode.

Why Make a Rating System such as Big O?
The deeper you get into programming, the more you will need to consider how efficient your code is.

If you plan on using large data sets or having a lot of users, inefficient code can lead to slow
performance, crashes and bad user experience.  It can also lead to increased costs, especially
if you need to use cloud services that charge based on usage.

How do we use Big O?
1. Memorize the common Big O notations and how they relate to the different types of algorithms.
2. Learn how to analyze the time and space complexity of your code.
3. Learn how to optimize your code for better performance. (refactoring)

Basic Big O Notations - From Fastest to Slowest:
1. O(1) - Constant Time Complexity
2. O(log n) - Logarithmic Time Complexity
3. O(n) - Linear Time Complexity
4. O(n log n) - Linearithmic Time Complexity
5. O(n^2) - Quadratic Time Complexity
6. O(2^n) - Exponential Time Complexity
7. O(n!) - Factorial Time Complexity

"""

# Big O Notation:  In order of fastest to slowest:

# 1. O(1) - Constant Time Complexity:
l = [1, 2, 3, 4, 5]
print(l[0])  # O(1) - Accessing an element in a list by index is constant time complexity.
# This means that the time it takes to access the element does not depend on the size of the list.

# This is the best time complexity you can get.
"""
Calling up the value by directly accessing the index is fast and efficient, there is no 'searching'
for the value, it is already known.  Other examples of O(1) time complexity include:
# 1. Accessing a value in a dictionary by key.
# 2. Accessing a value in a set by value.
# 3. Accessing a value in a tuple by index.
# 4. Accessing a value in a string by index.
# 5. Accessing a value in a list by index.
# 6. Accessing a value in a numpy array by index.
# 7. OR - calling a function that does not depend on the size of the input, or perform any
loops or recursion.
"""

# 2. O(log n) - Logarithmic Time Complexity:
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Binary Search Example: O(log n)
# This is a search algorithm that finds the position of a target value within a sorted array.

def binary_search(arr, target):     # arr is the list to search, target is the value you want to find
    left, right = 0, len(arr) - 1   # setting first index value and last index value
    while left <= right:            # setting the end condition for the loop as long as left marker is less than length of list
        mid = (left + right) // 2   # finding the middle index of the list using floor division (integer output)
        if arr[mid] == target:      # if the middle index value is equal to the target value
            return mid              # then return index of the value
        elif arr[mid] < target:     # if the value at the middle index is less than the target value
            left = mid + 1          # then move the left marker to the right of the middle index
        else:
            right = mid - 1         # else move the right marker to the left of the middle index
    return -1                       # if the target value is not found, return -1

binary_search(l, 10)       

# The time complexity of this algorithm is O(log n) because the size of the input is halved with each iteration.
# This means that the time it takes to find the target value increases logarithmically with the size of the input.
# This is a very efficient search algorithm and is much faster than a linear search (O(n)) for large lists.

"""Laymans Aside:
So a logarithmic function, when plotted on a graph, looks like a curve that starts off steep and
then flattens out.

The actual action being performed is a comparison of the middle value to the target value and then
a halving of the remaining list. Then it continues the while loop, halving the list again if the value isn't found.
The 'WORST CASE' scenario is that the target value is the very last value or very first value in the list.

So any algorithm or search function that halves the input size with each iteration is O(log n).

Examples of other common O(log n) search algorithms or operations include:
# 1. Binary search in a sorted array.
# 2. When searching, inserting or deleting elements in a balanced binary tree.
# 3. Inserting or deleting elements in a min/max heap.
# 4. merge-sort algorithm for combining two sorted lists.
"""

# 3. O(n) - Linear Time Complexity:
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Linear Search Example: O(n)
# This is a search algorithm that finds the position of a target value within an unsorted array.

def linear_search(arr, target):     # arr is the list to search, target is the value you want to find
    for i in range(len(arr)):       # loop through the list using the length of the list as the range
        if arr[i] == target:        # if the value at the current index is equal to the target value
            return i                # then return the index of the value
    return -1                      # if the target value is not found, return -1

# The time complexity of this algorithm is O(n) - linear - because the worst case scenario is that the
# function has to check every element in the list before finding the target value.  So with every
# increase in the size of the input, the time it takes to find the target value increases directly.

# 4. O(nlog n) - Linearithmic Time Complexity:
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Merge Sort Example: O(nlog n)
# This is a sorting algorithm that divides the input array into two halves, sorts them and then merges them back together.
# This is a divide and conquer algorithm.

def merge_sort(arr):                        # arr is the list to sort
    if len(arr) <= 1:                       # if the length of the list is less than or equal to 1
        return arr                          # then return the list as it is already sorted
    mid = len(arr) // 2                     # find the middle index of the list using floor division (integer output)
    left_half = merge_sort(arr[:mid])       # recursively call merge_sort on the left half of the list
    right_half = merge_sort(arr[mid:])      # recursively call merge_sort on the right half of the list
    
    return merge(left_half, right_half)     # merge the two sorted halves back together

def merge(left, right):                     # left and right are the two sorted halves of the list
    result = []                             # create an empty list to store the merged values
    i = j = 0                               # set the left and right index markers to 0
    while i < len(left) and j < len(right): # while both index markers are less than the length of their respective lists
        if left[i] < right[j]:              # if the value at the left index marker is less than the value at the right index marker
            result.append(left[i])          # then append the value at the left index marker to the result list
            i += 1                          # increment the left index marker by 1
        else:                               # else if the value at the right index marker is less than or equal to the value at the left index marker
            result.append(right[j])         # then append the value at the right index marker to the result list
            j += 1                          # increment the right index marker by 1
    result.extend(left[i:])                 # extend the result list with any remaining values in the left half of the list
    result.extend(right[j:])                # extend the result list with any remaining values in the right half of the list
    return result                           # return the merged sorted list


# 5. O(n^2) - Quadratic Time Complexity:
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Bubble Sort Example: O(n^2)
# This is a sorting algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order.

def bubble_sort(arr):                     # arr is the list to sort
    n = len(arr)                          # get the length of the list
    for i in range(n):                    # loop through the list using the length of the list as the range
        for j in range(0, n-i-1):         # loop through the list again, but only up to the last sorted element
            if arr[j] > arr[j+1]:         # if the value at the current index is greater than the value at the next index
                arr[j], arr[j+1] = arr[j+1], arr[j]  # then swap the two values
    return arr                            # return the sorted list

# The worst case scenario is that the function has to check every element in the list for every other element in the list.
# So with every increase in the size of the input, the time it takes to sort the list increases quadratically.
# This is a very ineffficent sorting algorithm.

# Other examples of O(n^2) time complexity include:
# selection sort, insertion sort, and any algorithm that uses nested loops to iterate through the input.

# 6. O(2^n) - Exponential Time Complexity:
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Fibonacci Sequence Example: O(2^n)
# This is a sequence of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1.

# Using Naive Recursion:
def fibonacci(n):                     # n is the index of the Fibonacci sequence
    if n <= 1:                         # if n is less than or equal to 1
        return n                      # then return n (0 or 1)
    else:                             # else
        return fibonacci(n-1) + fibonacci(n-2)  # return the sum of the two preceding numbers in the sequence
    

# The time complexity of this algorithm is O(2^n) because the function calls itself twice for each term in the sequence.


# 7. O(n!) - Factorial Time Complexity:
l = ['a', 'b', 'c']
# Permutations Example: O(n!)
def permutations(lst):                  # lst is the list to find permutations of
    if len(lst) == 0:                   # if the length of the list is 0
        return [[]]                     # then return an empty list
    result = []                         # create an empty list to store the permutations
    for i in range(len(lst)):           # loop through the list using the length of the list as the range
        current = lst[i]                # set the current value to the value at the current index
        remaining = lst[:i] + lst[i+1:]  # set the remaining values to all values in the list except the current value
        for p in permutations(remaining):  # recursively call permutations on the remaining values
            result.append([current] + p)  # append the current value and the permutation of the remaining values to the result list
    return result                       # return the list of permutations

# You can think of this as factorial because the number of permutations of n items is n! (n factorial).

"""
Final Thoughts:
When you have to analyze the time complexity of your code and it involves multiple functions or recursions,
you need to separate out the functions and give them each a big O rating.

Then you usually give the overall algorithm the highest big O rating among the functions.
This is because Big O is trying to rate algorithms based on the worst case scenario.
# So if you have a function that is O(n) and another function that is O(n^2), the overall algorithm is O(n^2).
"""




