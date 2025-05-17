# BCC - Episode 28: Binary Search Tree : Insertion and Deletion

"""
Binary Search Tree:
Remember this is a tree where each parent has only two children. The left child
is always les than the parent and the right child is always greater than the parent.

Insertion and Deletion are a bit more cumbersome because you need to maintain the
tree structure and 'rearrange' nodes and references if a certain deletion causes children/parents
to be out of order.

Insertion:
1. If the tree is empty, create a new node and make it the root.
2. If the value to be inserted is less than the current node's value, go to the left subtree.
3. If the value to be inserted is greater than the current node's value, go to the right subtree.
4. Repeat steps 2 and 3 until you find an empty spot where the new node can be inserted.
5. Insert the new node at that position.

Deletion:
1. If the node to be deleted is a leaf node (no children), simply remove it.
2. If the node to be deleted has one child, replace the node with its child.
3. If the node to be deleted has two children, find the in-order successor (smallest value in the right subtree)
   or in-order predecessor (largest value in the left subtree) and replace the node's value with that.
4. Delete the in-order successor or predecessor node.
5. Ensure the tree remains a valid binary search tree after deletion.
6. If the node to be deleted is the root, handle it separately to ensure the tree remains valid.
"""

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    # If the tree is empty, return a new node
    if root is None:
        return Node(key)

    # Otherwise, recur down the tree
    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    # Return the unchanged node pointer
    return root

def delete_node(root, key):
    # Base case
    if root is None:
        return root

    # Recur down the tree
    if key < root.val:
        root.left = delete_node(root.left, key)
    elif key > root.val:
        root.right = delete_node(root.right, key)
    else:
        # Node with only one child or no child
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        # Node with two children: Get the inorder successor (smallest in the right subtree)
        temp = min_value_node(root.right)

        # Copy the inorder successor's content to this node
        root.val = temp.val

        # Delete the inorder successor
        root.right = delete_node(root.right, temp.val)

    return root

def min_value_node(node):
    current = node

    # Loop down to find the leftmost leaf
    while current.left is not None:
        current = current.left

    return current

def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.val, end=' ')
        inorder_traversal(node.right)

if __name__ == "__main__":
    # Create the root node
    root = Node(10)
    
    # Insert nodes
    root.left = Node(5)
    root.right = Node(15)
    root.left.left = Node(3)
    root.left.right = Node(7)
    root.right.right = Node(20)

    # Insert a new node
    root = insert(root, 6)

    # Print the inorder traversal of the tree
    def inorder_traversal(node):
        if node:
            inorder_traversal(node.left)
            print(node.val, end=' ')
            inorder_traversal(node.right)
    inorder_traversal(root)
    print()

    # Delete a node
    root = delete_node(root, 5)
    # Print the inorder traversal of the tree
    def inorder_traversal(node):
        if node:
            inorder_traversal(node.left)
            print(node.val, end=' ')
            inorder_traversal(node.right)
    inorder_traversal(root)
    print()

    
