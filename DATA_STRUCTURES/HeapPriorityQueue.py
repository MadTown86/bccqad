# Heap Priority Queue Implementation
# pg 377 - Data Structures and Algorithms in Python - Wiley - 2013

from PriorityQueueBase import PriorityQueueBase

class HeapPriorityQueue(PriorityQueueBase):
    """
    Construction - Bottom Up - O(n)
    Construction - Top Down - O(n log n)
    len(P), P.is_empty: O(1)
    P.min(): O(1)
    P.add(k,v): O(log n)*
    P.remove_min(): O(log n)*
    *Amortized if array based
    """
    def __str__(self):
        output = "Heap Priority Queue:\n"
        for i in range(len(self._data)):
            output += f"Index: {i}, Key: {self._data[i]._key}, Value: {self._data[i]._value}\n"

        return output

    def _parent(self, j):
        return (j-1) // 2
    
    def _left(self, j):
        return 2 * j + 1
    
    def _right(self, j):
        return 2 * j + 2
    
    def _has_left(self, j):
        return self._left(j) < len(self._data)
    
    def _has_right(self, j):
        return self._right(j) < len(self._data)
    
    def _swap(self, i, j):
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _upheap(self, j):
        parent = self._parent(j)
        if j > 0 and self._data[j] < self._data[parent]:
            self._swap(j, parent)
            self._upheap(parent)

    def _downheap(self, j):
        if self._has_left(j):
            left = self._left(j)
            small_child = left
            if self._has_right(j):
                right = self._right(j)
                if self._data[right] < self._data[left]:
                    small_child = right
            if self._data[small_child] < self._data[j]:
                self._swap(j, small_child)
                self._downheap(small_child)

    def _heapify(self):
        start = self._parent(len(self) - 1)
        for j in range(start, -1, -1):
            self._downheap(j)

    def __init__(self, contents=()):
        self._data = [self._Item(k, v) for k, v in contents]
        if len(self._data) > 1:
            self._heapify()
    
    def __len__(self):
        return len(self._data)
    
    def add(self, key, value):
        self._data.append(self._Item(key, value))
        self._upheap(len(self._data) - 1)

    def min(self):
        if self.is_empty():
            raise ValueError('Priority queue is empty')
        item = self._data[0]
        return (item._key, item._value)
    
    def remove_min(self):
        if self.is_empty():
            raise ValueError('Priority queue is empty')
        self._swap(0, len(self._data) - 1)
        item = self._data.pop()
        self._downheap(0)
        return (item._key, item._value)
    
# Test the HeapPriorityQueue class
if __name__ == "__main__":
    contents = [(1, 'A'), (2, 'B'), (3, 'C'), (4, 'D'), (5, 'E'), \
    (5, 'B'), (1, 'B'), (3, 'C'), (2, 'D'), (4, 'E'), (0, 'F')]
    pq = HeapPriorityQueue(contents)

    print(pq.min())  # Output: (0, 'F')

    print(pq)
    
    