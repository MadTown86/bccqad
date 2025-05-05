# Episode 22: Intermediate Python Tutorial - Data Structures - Memory, Array and Python Lists

"""
References: Data Structures and Algorithms in Python by Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser, 2013.

Precursor:  Time Complexity and Space Complexity are at the heart of why different data structures exist.

Covered:
1. Layman's Terms - What is memory?
2. Low Level Arrays - How arrays are stored in memory!
3. Compact Array and Referential Array?
4. Dynamic Array - Python List?
5. When is an array efficient?
6. When is an array inefficient?

# 1. Layman's Terms - What is memory?
- Think of memory as locations that are each assigned a unique number and can be accessed instantly O(1) by this unique number.  
- Each location has a fixed size called a byte.  A byte is 8 bits.  A bit is a literal 0 or a 1.  Basically is it switched on or off.
- So everything that you may want to store in memory uses up a certain number of bytes. 
- To get more information on how Python implements memory based on object type, you can check out the following link:
https://docs.python.org/3/c-api/memory.html

*The main takeaway in the above is that different things take up different amounts of memory*

# 2. Low Level Arrays - How arrays are stored in memory!
- An array is stored in memory as a 'block' of memory that is sequentially allocated.  This means that
The computer needs to find a chunk of memory large enough to store the entire array.


# 3. Compact Array and Referential Array?
- A compact array is a single block of contiguous memory that is allocated for the entire array.
- Items have to be homogeneous, meaning they have to be the same type of data so that they are all the same size.
- Compact arrays are efficient because each element can be looked up in O(1) time generally speaking.


## Referential Array:
- A referential array is an array of references to other arrays.  This means that the array is not stored in a single block of memory.
- Use case of this is the following:
l = ["John", "Jacob", "Jingle", "Heimer"] : This is a list of strings.  Each string is stored in a separate block of memory.
* This measn there are at least 5 different blocks of memory that are allocated for this list.  Each string, and then the list itself.
- This is not as efficient as a compact array, but it allows for more flexibility in the data structure.

# 4. Dynamic Array - Python List?
- A dynamic array is an array that can grow and shrink in size.  It begins as a default size and then as it grows and nears the initial capacity,
it will increase in size.  Meaning, the system will find a new, larger block, copy the data from the old block to the new block and then free the old block.
## This action of growing and shrinking is called 'resizing' and is a source of inefficiency in Python lists.


# 5. When is an array efficient?
- An array is efficient when the data is static and does not change.  This means that the data is not constantly being added or removed from the array.

# 6. When is an array inefficient?
- An array is inefficient when the data is dynamic and is constantly changing.  This means that the data is being added or removed from the array.

** Main Takeaways **:
1. Different data types and abstractions take up different amounts of memory.
2. Compact Arrays are more efficient than referential arrays - think contiguous memory and homogenous data.
3. Referential arrays are less memory efficient, but in the long run, they are more flexible and make much more sense than trying to use compact arrays for all types of data.
4. Dynamic arrays are a type of referential array that can grow and shrink in size.  This is a source of inefficiency in Python lists.



"""
import sys
# You can use the sys.getsizeof() function to get the size of an object in bytes.  However, it doesn't seek out size of the OBJECTS inside the list.
# It only returns the size of the list object itself. (Compact Arrays = more accurate representation of size, Referential Array = Only showing size of reference list)


# Somewhat Compact Array - except with string header overhead:
s = "string"
print(sys.getsizeof(s)) # 54 bytes

# This is a compact array, where the strings' characters are stored contiguiously in memory.
# contiguous means that the memory locations are sequential and adjacent to each other.

# Referential Array Example:
l = ["John", "Jacob", "Jingle", "Heimer"]
# This is a referential array, where the strings are stored in separate memory locations.
# SO 'l' in memory is an array of references to compact arrays.
print(sum(map(sys.getsizeof, l)) + sys.getsizeof(l))

print("\n")
print("Size of list object: ", sys.getsizeof(l)) # 88 bytes

"""
This may not matter on such a small scale as this, but consider thousands of strings in a list.  
"""

l = [] # Python assigns a default size to this list.  In order to maintain the time complexity of O(1), it can never get to a point where it is full
# So it will always have a little bit of extra space in it.  This is called 'overhead'.
# The main issue with this is that if the quantity of data is constantly fluctuating, the overhead can be a lot of wasted space and the time
# complexity of O(1) may not be accurate.

