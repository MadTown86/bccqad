# Episode 26: Intermediate Python Tutorial - Recursion - Tree Traversals

"""
# What is Covered?
1. Creation of a tree data structure using nodes.
2. Implementation of a recursive function to traverse the tree in pre-order, in-order, and post-order and find a node by value.
"""

# 1. My Own Tree Implementation

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.value)
    
def my_pre_order(node, value):
    """
    Searches for a node by value in the tree using pre-order.
    *Beneficial search pattern for ordered trees, especially binary trees 
    where the left child is less than the parent and the right child is greater than the parent.

    This is a depth-first search (DFS) algorithm.
    """
    if node is None:
        return None
    print(node.value)
    if node.value == value: # Value is checked before going to the children
        return node
    left_result = my_pre_order(node.left, value)
    if left_result:
        return left_result
    right_result = my_pre_order(node.right, value)
    return right_result

def my_in_order(node, value):
    """
    Searches for a node by value in the tree using in order. 
    """
    if node is None:
        return None
    print(node.value)
    left_result = my_in_order(node.left, value)
    if left_result:
        return left_result
    if node.value == value: # Value is checked after going to the left child
        return node
    right_result = my_in_order(node.right, value)
    return right_result

def my_post_order(node, value):
    """
    Searches for a node by value in the tree using post-order.
    """
    if node is None:
        return None
    print(node.value)
    left_result = my_post_order(node.left, value)
    if left_result:
        return left_result
    right_result = my_post_order(node.right, value)
    if right_result:
        return right_result
    if node.value == value: # Value is checked after going to both children
        return node
    
def my_breadth_first(node, value):
    """
    Searches for a node by value in the tree using breadth-first search.
    
    Using a queue to keep track of nodes to visit, vs. recursion.
    
    """
    if node is None:
        return None

    queue = [node]
    while queue:
        current_node = queue.pop(0)
        print(current_node.value)
        if current_node.value == value:
            return current_node
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)
    return None

if __name__ == "__main__":
    # Create a simple tree for demonstration
    root = Node(1)
    N2 = Node(2)
    N3 = Node(3)
    N4 = Node(4)
    N5 = Node(5)
    N6 = Node(6)
    N7 = Node(7)
    N8 = Node(8)
    N9 = Node(9)
    N10 = Node(10)
    N11 = Node(11)
    N12 = Node(12)
    N13 = Node(13)
    N14 = Node(14)
    N15 = Node(15)

    root.left = N2
    root.right = N3

    N2.left = N4
    N2.right = N5
    
    N3.left = N6
    N3.right = N7

    N4.left = N8
    N4.right = N9

    N5.left = N10
    N5.right = N11

    N6.left = N12
    N6.right = N13

    N7.left = N14
    N7.right = N15

    """
    Tree Structure Diagram:
        1
       / \
      2   3
     / \ 
    4   5

    """

    # Test the tree traversal functions
    print("Pre-order search for 12:", my_pre_order(root, 12))
    print("In-order search for 12:", my_in_order(root, 12))
    print("Post-order search for 12:", my_post_order(root, 12))
    print("Breadth-first search for 12:", my_breadth_first(root, 12))
    
