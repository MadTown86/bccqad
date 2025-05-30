# Priority Queue Base Class Implementation
# pg 365 - Data Structures and Algorithms in Python - Wiley - 2013

class PriorityQueueBase:

    class _Item:
        __slots__ = '_key', '_value'
        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __lt__(self, other):
            return self._key < other._key
        
    def is_empty(self):
        return len(self) == 0