# Episode 23: Intermediate Python Tutorial - Data Structures - Linked Lists

"""
  Linked List Implementation in Python
  
  What is Covered?
  1. What is a Linked List?
  2. How to implement a Linked List in Python?
  3. Why use a Linked List? (And comparison to arrays)
  4. Stacks and Queues using Linked List - Discussion Next Episode
"""

# 1. What is a linked list?
"""
A data structure that uses class instances called 'nodes' to store data and reference to the next list.

1. Singly Linked List:
    Each node has a reference to the next node.
    # Allows for traversal in one direction.
    # Example: 1 -> 2 -> 3 -> None

2. Doubly Linked List:
    Each node has a reference to the next and previous nodes.
    # Allows for traversal in both directions.
    # Example: None <- 1 <-> 2 <-> 3 -> None
"""

# 2. How to implement a Linked List in Python?
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        # If the list is empty, make the new node the head
        if not self.head:
            self.head = new_node
            return
        # Otherwise, traverse to the end of the list and append the new node
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

    def delete_node(self, key):
        # Setting the starting point at the head of the list
        current_node = self.head
        prev_node = None

        # Loop while a reference to current_node is not None and key not found
        while current_node and current_node.data != key:
            # Make the step by moving stored references
            prev_node = current_node
            current_node = current_node.next

        # If end of list is reached
        if not current_node:
            print(f"Node with data {key} not found.")
            return

        if prev_node:
            prev_node.next = current_node.next
        else:
            self.head = current_node.next

        del current_node
        print(f"Node with data {key} deleted.")

    def search(self, key):
        current_node = self.head
        while current_node:
            if current_node.data == key:
                return True
            current_node = current_node.next
        return False
# 3. Why use a linked list?
"""
1. Dynamic Size:
    - Linked lists can grow and shrink in size as needed, unlike arrays which have a fixed size.
    -- This makes linked lists more memory efficient for certain applications.
2. Efficient Insertions/Deletions:
    - Inserting or deleting a node in a linked list is O(1) if you have a reference to the node.
    -- In contrast, inserting or deleting an element in an array requires shifting elements, which is O(n).
3. No Memory Wastage:
    - Linked lists do not require contiguous memory allocation, which can lead to memory fragmentation.
    -- This is particularly useful in systems with limited memory resources.
4. Flexibility:
    - Linked lists can be easily modified to create more complex data structures like stacks, queues, and graphs.
    -- This flexibility allows for a wide range of applications in computer science and programming.

An Array vs Linked List:
1. Arrays:
    - Fixed size, contiguous memory allocation.
    - Random access to elements (O(1) time complexity).
    - Inefficient insertions/deletions (O(n) time complexity).

2. Linked Lists:
    - Dynamic size, non-contiguous memory allocation.
    - Sequential access to elements (O(n) time complexity).
    - Efficient insertions/deletions (O(1) time complexity if you have a reference to the node).
"""

# 4. Stacks and Queues using Linked List - Discussion Next Episode
"""
I will give a brief explanation and see if you can figure out how to implement them.
1. Stack:
-LIFO (Last In First Out) data structure.
-Operations: push (add), pop (remove), peek (view top element).
-Key difference is that instead of maintaining a reference to the root node, you maintain a reference to
the tail node and the linked list is traversed in reverse order.

2. Queue:
-FIFO (First In First Out) data structure.
-Operations: enqueue (add), dequeue (remove), front (view front element).
-You can implement a queue using a linked list by maintaining references to both the head and tail nodes.
-This allows for efficient enqueue and dequeue operations.
"""
    
if __name__ == "__main__":
    # Creating a Linked List Just With Nodes
    # Create Nodes Separately
    node1 = Node("One")
    node2 = Node("Two")
    node3 = Node("Three")

    # Link Nodes Together
    node1.next = node2
    node2.next = node3
    root = node1 # You want to maintain a reference to the first node that you don't overwrite

    # Print the linked list
    print("Linked List - Self Made Simple:")
    current_node = root # Copy the reference to the first node and use it to traverse the list
    while current_node:
        print(current_node.data, end=" -> ")
        current_node = current_node.next
    print("None")
    
    # Create a linked list and append some data
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)

    # Print the linked list
    print("Linked List:")
    linked_list.print_list()

    # Search for a node
    print("Searching for 2:", linked_list.search(2))
    print("Searching for 4:", linked_list.search(4))

    # Delete a node
    linked_list.delete_node(2)
    print("After deleting 2:")
    linked_list.print_list()