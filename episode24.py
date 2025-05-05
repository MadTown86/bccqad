# Episode 24: Intermediate Python Tutorial - Stacks and Queues

"""
What is Covered?
1. What is a Stack?
2. How to implement a Stack in Python?
3. What is a Queue?
4. How to implement a Queue in Python?
5. Why use a Stack or Queue? (And comparison to arrays)
6. Stacks and Queues in real life
"""

# 1. What is a Stack?
"""
* Tower of Hanoi puzzle: A visualization of how stacks can work together to solve a problem.
Last In First Out (LIFO) principle.
- A linked list, the head is always relocated to the last element and you traverse the list
in reverse order.
"""

# 2. How to implement a Stack in Python?

class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class MyStack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = StackNode(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            return None
        popped_node = self.top
        self.top = self.top.next
        return popped_node.data

    def peek(self):
        if self.is_empty():
            return None
        return self.top.data

    def is_empty(self):
        return self.top is None

    def print_stack(self):
        current_node = self.top
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

# 3. What is a Queue?
"""
First In First Out (FIFO) principle.
- Head is always the first element and you traverse the list in order (from head to tail).
"""

# 4. How to implement a Queue in Python?

class QueueNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class MyQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        # Create a new node and add it to the end of the queue
        new_node = QueueNode(data)
        if self.is_empty():
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        # Remove the front node from the queue
        if self.is_empty():
            return None
        dequeued_node = self.front
        self.front = self.front.next
        if not self.front:
            self.rear = None
        return dequeued_node.data

    def peek(self):
        # Return the front node's data without removing it
        if self.is_empty():
            return None
        return self.front.data

    def is_empty(self):
        return self.front is None

    def print_queue(self):
        current_node = self.front
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

# 5. Why use a Stack or Queue? (And comparison to arrays)
"""
- Grow and shrink dynamically.
- Efficient memory usage.
- No need to specify size in advance.
- Efficient insertions and deletions.

Stack:
A stack is used when you need to keep track of the order of operations, such as a web browser's back button,
or a function call stack in programming languages.

Queue:
A queue is used when you need to process items in the order they were added, such as a printer queue or a 
task scheduler.
"""

# 6. Stacks and Queues in real life
"""
- A stack of cards analogy: You can only add or remove cards from the top of the stack, the 
rest of the stack is 'protected'.

- A queue of people waiting in line: The first person in line is the first person to be served.
"""

if __name__ == "__main__":
    # Create a stack and perform some operations
    stack = MyStack()
    stack.push(1)
    stack.push(2)
    stack.push(3)

    print("Stack:")
    stack.print_stack()
    print("Popped:", stack.pop())
    print("Peek:", stack.peek())
    print("Stack after pop:")
    stack.print_stack()

    # Create a queue and perform some operations
    queue = MyQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    print("Queue:")
    queue.print_queue()
    print("Dequeued:", queue.dequeue())
    print("Peek:", queue.peek())
    print("Queue after dequeue:")
    queue.print_queue()