def main():
    # 1. What are the 3 ways to create a list?
    print("\nQuestion 1: What are the 3 ways to create a list?")
    l1 = [1, 2, 3, 4, 5]
    l2 = list((1, 2, 3, 4, 5))
    l3 = [i for i in range(1, 6)]
    print(l1, l2, l3)
    # 2. What are the 3 ways to create a tuple?
    print("\nQuestion 2: What are the 3 ways to create a tuple?")
    t1 = (1, 2, 3, 4, 5)
    t2 = tuple([1, 2, 3, 4, 5])
    t3 = (i for i in range(1, 6))
    print(t1, t2, t3)
    # 3. What are the 3 ways to create a set?
    print("\nQuestion 3: What are the 3 ways to create a set?")
    ss1 = {1, 2, 3, 4, 5}
    ss2 = set((1, 2, 3, 4, 5))
    ss3 = {i for i in range(1, 6)}
    print(ss1, ss2, ss3)
    # 4. How is a set different from the other two?
    print("\nQuestion 4: How is a set different from the other two?")
    ans = """
    A set is unordered, so it can't be indexed. It also can't have duplicate values.  A set is 'mutable' meaning you can add or remove items from it.
    """
    print(ans)
    # 5. How is a tuple different from the other two?
    print("\nQuestion 5: How is a tuple different from the other two?")
    ans = """
    A tuple is immutable, meaning you can't change the values in it.  It is ordered and can be indexed.  It can have duplicate values.
    """
    print(ans)
    # 6. Create this list: [1, 2, 3, 4, 5] without typing it all out.
    print("\nQuestion 6: Create this list: [1, 2, 3, 4, 5] without typing it all out.")
    l1 = list(range(1, 6))
    l2 = [i for i in range(1, 6)]
    print(l1, l2)
    # 7. Create this list using a comprehension: [1, 3, 5, 7, 9]
    print("\nQuestion 7: Create this list using a comprehension: [1, 3, 5, 7, 9]")
    l = [i for i in range(1, 10, 2)]
    print(l)
    # 8. Create this list using a comprehension: [2, 4, 6, 8, 10]
    print("\nQuestion 8: Create this list using a comprehension: [2, 4, 6, 8, 10]")
    l = [i*2 for i in range(1, 6)]
    print(l)
    # 9. Create this list using a slice of #8's list: [4, 6, 8]
    print("\nQuestion 9: Create this list using a slice of #8's list: [4, 6, 8]")
    l2 = l[1:4]
    print(l2)
    # 10. Create this list using a slice of #8's list: [2, 6, 10]
    print("\nQuestion 10: Create this list using a slice of #8's list: [2, 6, 10]")
    l3 = l[0:5:2]
    print(l3)

if __name__ == "__main__":
    main()