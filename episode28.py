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

class MyBST:
    class Node:
        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = self.Node(value)
            print("Inserted Root")
            return self.root
        
        def traversal(node, value):
            if not node:
                return self.Node(value)
            if node.val < value:
                node.right = traversal(node.right, value)
            else:
                node.left = traversal(node.left, value)
            return node
        
        return traversal(self.root, value)
    
    def get_min_value_node(self, node):
        get_min_node = node.val
        current = node
        while current.left:
            current = current.left
        return current
    
    def delete(self, root, val):
        if not root:
            return root
        if val < root.val:
            root.left = self.delete(root.left, val)
        elif val > root.val:
            root.right = self.delete(root.right, val)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            temp = self.get_min_value_node(root.right)
            root.val = temp.val
            root.right = self.delete(root.right, temp.val)
        return root
    

    
    def print_tree(self, func: str = "inorder"):
        if not self.root:
            print("No Tree")
            return
        if func == "inorder":
            print("\nInOrder")
            def inorder(root):
                if not root:
                    return
                left_result = inorder(root.left)
                if left_result:
                    return left_result
                print(root.val)
                right_result = inorder(root.right)
                if right_result:
                    return right_result
            
            return inorder(self.root)

        elif func == "preorder":
            print("\nPreOrder")
            def preorder(root):
                if not root:
                    return
                print(root.val)
                left_result = preorder(root.left)
                if left_result:
                    return left_result
                right_result = preorder(root.right)
                if right_result:
                    return right_result
            
            return preorder(self.root)
        
        elif func == "postorder":
            print("\nPostOrder")
            def postorder(root):
                    if root is None:
                        return None
                    left_result = postorder(root.left)
                    if left_result:
                        return left_result
                    right_result = postorder(root.right)
                    if right_result:
                        return right_result
                    print(root.val)
            
            return postorder(self.root)
        
if __name__ == "__main__":
    B = MyBST()
    values = [50, 30, 20, 40, 70, 60, 80]
    for val in values:  
        B.insert(val)
    
    print("\n")
    B.print_tree("inorder")
    B.delete(B.root, 70)
    B.print_tree("inorder")


