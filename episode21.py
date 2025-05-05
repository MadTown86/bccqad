# Episode 21: Intermediate Python Tutorial - Data Structures - More On Classes, Node Base Class, and __slots__

"""
This episode is going to cover a bit on class object structure and where the __slots__ variable comes into play.
We are also going to gloss over a node base class and touch upon where they are used in data structures.

A node is a basic unit of a data structure, such as a linked list or tree.

A node is a class that is made specifically for a data structure.  It contains a data field and then one or more
pointers to other nodes.

A few important things to remember about nodes:
1. The use of nodes requires additional memory resources, moreso than a list or tuple.
2. Nodes are linked together by reference, not by index value.
3. Nodes are good for data structures that require dynamic memory allocation.
4. Their main use case is in linked lists and trees.
5. Linked lists are suited for data that is constantly changing, such as a queue or stack.
6. Trees are suited for data that is hierarchical in nature, such as a file system or organization chart.
"""

# Example of a node class:
class Node:
    __slots__ = ['data', 'next', 'prev']
    """
    A node class that can be used for linked lists or trees.
    """
    def __init__(self, data):
        self.data = data
        self.next = None  # Pointer to the next node in the linked list
        self.prev = None  # Pointer to the previous node in the linked list (for doubly linked lists)
        self.children = []  # Pointer to the children nodes (for tree structures)
        self.parent = None  # Pointer to the parent node (for tree structures)

"""
So it is important to think about how you are storing and accessing the data in this structure.
1. You are traversing the data linearly, you can't access random elements.  You have to go through the entire list.
2. You are using more memory than you would with a list or tuple.
"""



