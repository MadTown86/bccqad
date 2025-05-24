# Sorted Priority Queue Implementation
# pg 369 - Data Structures and Algorithms in Python - Wiley - 2013

from PriorityQueueBase import PriorityQueueBase
from PositionalList import PositionalList

class SortedPriorityQueue(PriorityQueueBase):
    def __init__(self):
        self._data = PositionalList()

    def __len__(self):
        return len(self._data)
    
    def add(self, key, value):
        newest = self._Item(key, value)
        walk = self._dta.last()
        while walk is not None and newest < walk.element():
            walk = self._data.before(walk)
        if walk is None:
            self._data.add_first(newest)
        else:
            self._data.add_after(walk, newest)

    def min(self):
        if self.is_empty():
            raise ValueError('Priority queue is empty')
        p = self._data.first()
        item = p.element()
        return (item._key, item._value)
    
    def remove_min(self):
        if self.is_empty():
            raise ValueError('Priority queue is empty')
        item = self._data.delete(self._data.first())
        return (item._key, item._value)
    
# Test the SortedPriorityQueue class
if __name__ == "__main__":
    pq = SortedPriorityQueue()
    pq.add(5, "A")
    pq.add(5, "B")
    pq.add(1, "B")
    pq.add(3, "C")
    pq.add(2, "D")
    pq.add(4, "E")
    pq.add(0, "F")
    print(pq.min())  # Output: (0, 'F')
    
    print(pq.remove_min())  # Output: (0, 'F')
    print(pq.min())  # Output: (1, 'B')
    print(len(pq))  # Output: 5
    print(pq.remove_min())  # Output: (1, 'B')
    print(pq.min())  # Output: (2, 'D')