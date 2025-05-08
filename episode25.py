# Episode 25: Intermediate Python Tutorial - Data Structures - Trees Overview

"""
*Core Takeaways*:
1. Just remember that a tree data structure has a root node that can't have a parent, and each node can have multiple children.
2. Creating rules for how many children a node can have and how a child needs to relate to its parent, is what allows us to create different types of trees.
3. Certain types of trees, used with certain types of data allow for faster searching and sorting of data vs. other types of data structures.

What is Covered?
1. What is a tree data structure?
2. How to implement a tree in simple terms?
3. How to implement a tree in Python?
4. Why use trees?
5. What are some different types of tree structures?


1. What is a tree data structure?
-- A tree is a hierarchical data structure that consists of nodes connected by edges.
-- Each node contains a value and may have child nodes, which are connected to it by edges.
-- The top node of the tree is called the root, and nodes without children are called leaves.

An example of how tree structures are used in programming:
-- File systems: Directories and files are organized in a tree structure, where directories can contain files and other directories.
-- HTML DOM: The Document Object Model (DOM) represents the structure of an HTML document as a tree, where each element is a node in the tree.

2. How to implement a tree in simple terms (using nodes)?
-- A tree has only one origin point, which is the root node.
-- A parent can have multiple children, root is the only node without a parent.
-- Each child node can have its own children, but always only has one parent.
-- You change the base node class from linked list to add a list of children.

"""

# 3. How to implement a tree in Python?
class TreeNode:
    """
    Base class for a tree node.

    ***Note that this is a simple way to implement a tree node.

    You can also implement one without using nodes, or to make traversing up the tree easier, you can add a parent reference to each node.
    This is a more complex implementation, but it allows you to traverse the tree in both directions.
    """
    def __init__(self, value):
        self.value = value
        self.children = [] # List of child nodes, order of these nodes can matter when searching tree for values.
        self.parent = None # Optional: reference to the parent node, if you want to traverse up the tree.

    def add_child(self, child_node):
        self.children.append(child_node)

    def __repr__(self):
        return str(self.value)
    
class MyTree:
    def __init__(self, root_value):
        self.root = TreeNode(root_value) # You want to maintain a reference to the root, otherwise you lose it.

    def add_child(self, parent_value, child_value):
        """
        Searches for parent node by value, and adds a child node to it.
        """
        parent_node = self.find_node(self.root, parent_value)
        if parent_node:
            new_child = TreeNode(child_value)
            parent_node.add_child(new_child)

    def find_node(self, current_node, value):
        """
        Searches for a node by value in the tree.

        It does this recursively.
        """
        if current_node.value == value:
            return current_node
        for child in current_node.children:
            found_node = self.find_node(child, value)
            if found_node:
                return found_node
        return None

    def print_tree(self, node=None, level=0):
        """
        Prints the tree structure in a readable format.
        """
        if node is None:
            node = self.root
        print(" " * level * 2 + str(node.value))
        for child in node.children:
            self.print_tree(child, level + 1)

# Depth Definitions:
# - The depth of a tree is the number of edges from the root to the deepest leaf node.
# - The depth of a node is the number of edges from the root to that node.

# - Height Definitions:
# - The height of a tree is the number of edges from the root to the deepest leaf node.
# - The height of a node is the number of edges from that node to the deepest leaf node.


"""
4. Why use trees?
-- For certain types of data, trees are more efficient than other data structures.
-- Trees allow for faster searching and sorting of data than other data structures, but the data must be organized in a certain way and not all data types are
suitable for trees.
-- Trees are also more flexible than other data structures, as they can be easily modified and expanded.

5. What are some different types of tree structures?
-- There are many different types of trees, but the most common ones are:
-- 1. Binary Tree: Each node has at most two children (left and right).
-- 2. Binary Search Tree (BST): A binary tree where the left child is less than the parent and the right child is greater than the parent.
-- 3. General Tree: No limitation on the number of children a node can have.
-- 4. AVL Tree: A self-balancing binary search tree where the difference in heights between the left and right subtrees is at most one.
"""