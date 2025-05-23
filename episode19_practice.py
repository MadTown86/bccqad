# Episode 19 Practice Questions:

# 1. What Big(O) time complexity is the following code?
def f1(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

# 2. What Big(O) time complexity is the following code?
def f2(n):
    for i in range(n):
        print(n[i])


# 3. What Big(O) time complexity is the following code?
def f3(l, value):
    mid = len(l) // 2
    if l[mid] == value:
        return mid
    elif l[mid] < value:
        return f3(l[mid + 1:], value)
    else:
        return f3(l[:mid], value)
    
# 4. What Big(O) time complexity is the following code?
def f4(n):
    if n == 0:
        return 1
    else:
        return n * f4(n - 1)
    
# 5. What Big(O) time complexity is the following code?
def f5(n):
    if n == 0:
        return 1
    else:
        return f5(n - 1) + f5(n - 1)
    
# 6. What is the fastest time complexity?
# 7. What is the second fastest time complexity?
# 8. Define linear time complexity.