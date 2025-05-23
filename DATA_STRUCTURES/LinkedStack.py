# Linked Stack Implementation
# pg 262 - Data Structures and Algorithms in Python - Wiley - 2013

class LinkedStack:
    """
    S.push(e) - O(1)
    S.pop() - O(1)
    S.top() - O(1)
    len(S) - O(1)
    S.is_empty() - O(1)
    """

    class _Node:
        __slots__ = '_value', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = None

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def push(self, e):
        self._head = self._Node(e, self._head)
        self._size += 1

    def top(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self._head._element
    
    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer