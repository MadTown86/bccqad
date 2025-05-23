# Linked Queue Implementation
# pg 264 - Data Structures and Algorithms in Python - Wiley - 2013

class LinkedQueue:
    """
    len(Q) - O(1)
    Q.is_empty() - O(1)
    Q.first() - O(1)
    Q.enqueue(e) - O(1)
    Q.dequeue() - O(1)
    """
    class _Node:
        __slots__ = '_value', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = None

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def first(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self._head._element
    
    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return answer
    
    def enqueue(self, value):
        new_node = self._Node(value, None)
        if self.is_empty():
            self._head = new_node
        else:
            self._tail._next = new_node
        self._tail = new_node
        self._size += 1
