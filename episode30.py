# Episode 30: Intermediate Python: Heaps

"""
A heap is a special binary tree that satisfies additional properties:
Heap Order Property: For every position p other than the root, the key of p is greater than or equal to the key of its parent.
Complete Binary Tree: All levels are completely filled except potentially the last level, which is filled form left to right.

Height:
A complete binary tree of height h has 2^h - 1 nodes.
h = log2(n + 1) - 1

When inserting a new node, it is added to the next available position in the last level of the tree.

If the new node's key invalidates the heap order property, it is 'bubbled up' to restore the property.
The process of bubbling up involves comparing the new node's key with its parent's key and swapping them if the new node's key is smaller.

up-heap bubbling: The process of moving a node up the tree to restore the heap order property.
down-heap bubbling: The process of moving a node down the tree to restore the heap order property.
"""

