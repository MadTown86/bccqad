# Episode 30: Intermediate Python: Heaps

"""
A heap is a special binary tree that satisfies additional properties:
Heap Order Property: For every position p other than the root, the key of p is greater than or equal to the key of its parent.
This is a max-heap property.
In a min-heap, the key of p is less than or equal to the key of its parent.
Complete Binary Tree: All levels are completely filled except potentially the last level, which is filled from left to right.
The complete binary tree property ensures that the tree is balanced and allows for efficient insertion and deletion operations.

Height:
A complete binary tree of height h has 2^h - 1 nodes.
h = log2(n + 1) - 1

When inserting a new node, it is added to the next available position in the last level of the tree.

If the new node's key invalidates the heap order property, it is 'bubbled up' to restore the property.
The process of bubbling up involves comparing the new node's key with its parent's key and swapping them if the new node's key is smaller.

up-heap bubbling: The process of moving a node up the tree to restore the heap order property.
down-heap bubbling: The process of moving a node down the tree to restore the heap order property.
"""

# 1. Overview of Heaps
# 2. Implementation Of Bottom-Up Building
# 3. Implementation of Insertion, Deletion, and Heapify (reordering)

"""
**SNIPPET**
# Priority Queue Base Class Implementation
class PriorityQueueBase:

    class _Item:
        __slots__ = '_key', '_value'
        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __lt__(self, other):
            return self._key < other._key
        
    def is_empty(self):
        return len(self) == 0
"""

from DATA_STRUCTURES.PriorityQueueBase import PriorityQueueBase

class HeapPriorityQueue(PriorityQueueBase):
    """
    This is a min-heap priority queue implementation.

    Construction - Bottom Up - O(n)
    Construction - Top Down - O(n log n)
    len(P), P.is_empty: O(1)
    P.min(): O(1)
    P.add(k,v): O(log n)*
    P.remove_min(): O(log n)*
    *Amortized if array based
    """
    def __str__(self):
        output = "Heap Priority Queue:\n"
        for i in range(len(self._data)):
            output += f"Index: {i}, Key: {self._data[i]._key}, Value: {self._data[i]._value}\n"

        return output

    def _parent(self, j):
        return (j-1) // 2
    
    def _left(self, j):
        return 2 * j + 1
    
    def _right(self, j):
        return 2 * j + 2
    
    def _has_left(self, j):
        return self._left(j) < len(self._data)
    
    def _has_right(self, j):
        return self._right(j) < len(self._data)
    
    def _swap(self, i, j):
        # Swap positions of the nodes
        # in the array representation of the heap
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _upheap(self, j):
        # Bubble up the node at index j
        parent = self._parent(j)
        if j > 0 and self._data[j] < self._data[parent]:
            self._swap(j, parent)
            self._upheap(parent)

    def _downheap(self, j):
        # Take parent position of 'j' with _parent calculation based on over length of array
        if self._has_left(j): # If position isn't out of bounds
            left = self._left(j) # Calculate left child position
            small_child = left # Retaining value of left child index
            if self._has_right(j): # If, based on j, right child is in bounds
                right = self._right(j) # Use calculation to get index position of right child
                if self._data[right] < self._data[left]: # Compare index positions to make sure right is smaller than left
                    small_child = right # If so, set small_child to right child index
            if self._data[small_child] < self._data[j]: # Compare the keys of the small child and the parent
                self._swap(j, small_child) # If the small child is smaller than the parent, swap their positions in the index
                self._downheap(small_child) # Recursively call downheap on the small child to ensure the heap order property is maintained

    def _heapify(self):
        # Start = len(self) // 2 - 1
        # Additional Unused Values Here For Display Purposes
        LenthOfIndex = len(self._data)-1
        start = self._parent(len(self) - 1)
        left_child = 2 * start + 1
        right_child = 2 * start + 2
        for j in range(start, -1, -1):
            self._downheap(j)

    def __init__(self, contents=()):
        self._data = [self._Item(k, v) for k, v in contents]
        if len(self._data) > 1:
            self._heapify()
    
    def __len__(self):
        return len(self._data)
    
    def add(self, key, value):
        self._data.append(self._Item(key, value))
        self._upheap(len(self._data) - 1)

    def min(self):
        if self.is_empty():
            raise ValueError('Priority queue is empty')
        item = self._data[0]
        return (item._key, item._value)
    
    def remove_min(self):
        if self.is_empty():
            raise ValueError('Priority queue is empty')
        self._swap(0, len(self._data) - 1)
        item = self._data.pop()
        self._downheap(0)
        return (item._key, item._value)
    
# Test the HeapPriorityQueue class
if __name__ == "__main__":
    contents = [(1, 'A'), (2, 'B'), (3, 'C'), (4, 'D'), (5, 'E'), \
    (5, 'B'), (1, 'B'), (3, 'C'), (2, 'D'), (4, 'E'), (0, 'F')]
    pq = HeapPriorityQueue(contents)

    print(pq.min())  # Output: (0, 'F')

    print(pq)
    
    


