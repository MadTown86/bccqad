# Episode 27: Intermediate Python Tutorial - Tree Traversals - BFS vs DFS

"""
BFS: Breadth First Search
- Traverses the tree level by level, visiting all nodes at the current levl

DFS: Depth First Search
- Traverses the tree by going as deep as possible down one branch
before backtracking to explore other branches.
: This is how pre-order, in-order, and post-order traversals work.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.value)
    
def bfs(node, value):
    """
    Searches for a node by value in the tree using breadth-first search (BFS).
    This is a level-order traversal.
    """
    if node is None:
        return None

    queue = [node]  # Initialize the queue with the root node

    while queue:
        current_node = queue.pop(0)  # Dequeue the first node
        print(current_node.value)  # Process the current node

        if current_node.value == value:
            return current_node

        # Enqueue left and right children
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)

    return None  # Value not found in the tree
    
if __name__ == "__main__":
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

    # Breadth First Search (BFS) - Level Order Traversal

    print("BFS Traversal:")
    bfs(root, 12)  # Searching for node with value 5
