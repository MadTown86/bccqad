# EPISODE 29: Intermediate Python Tutorial - Positional List Implementation

"""
Positional List Implementation:
- A positional list is a bit unique in that it uses a wrapper class to represent the position of an element in the list.
- This allows for more efficient insertion and deletion operations compared to a standard linked list.

It essentially allows you to have one more accessor to the list.
- The wrapper class is called Position and it contains a reference to the node in the list.

From a known position, you can step after and before the position to get the next and previous elements.
This can save on time when you need to sort or search for elements in the list as you can start from a known position
and increment or decrement the position.

The reason I wanted to cover this is because of its use of the wrapper class and the fact that it is a bit different
from the standard doubly linked list implementation.


Things of note to review:
1. Position wrapper class
2. _validate method

Also note that instead of passing in nodes when creating, deleting, or replacing elements,
we pass in the position of the element.  It is validated (aka checked to make sure it belongs to the list) and 
then the node is passed.

Claude.AI's Take On Difference Between Positional List and Linked List:
The Key Difference
The doubly linked list base class approach creates a two-layer architecture:

Lower layer: Raw doubly linked list with nodes
Upper layer: Positional interface with validated position objects

This separation allows the positional list to provide safety guarantees while still achieving O(1) operations through the underlying linked structure.
The position objects act as "safe handles" that the list can control and invalidate as needed, rather than exposing raw pointers that users might misuse.
"""

# Positional List Implementation (Doubly Linked List Base)
# pg 282 - Data Structures and Algorithms in Python - Wiley - 2013

from DATA_STRUCTURES._DoublyLinkedBase import _DoublyLinkedBase

class PositionalList(_DoublyLinkedBase):
    """
    A positional lists methods are all O(1) except for the iterator.
    """

    class Position:
        def __init__(self, container, node):
            # Container here is the PositionalList instance, passed in automatically
            # This is the 'self' in the __init__ method of the PositionalList class
            # That maintains a reference to that specific instance of the PositionalList
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            return not (self == other)
        
    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise Exception("p must be a Position instance")
        if p._container is not self:
            raise Exception("p does not belong to this container")
        if p._node._next is None:
            raise Exception("p is no longer valid")
        return p._node
    
    def _make_position(self, node):
        if node is self._header or node is self._trailer:
            return None
        else:
            return self.Position(self, node)
        
    def first(self):
        return self._make_position(self._header._next)
    
    def last(self):
        return self._make_position(self._trailer._prev)
    
    def before(self, p):
        node = self._validate(p)
        return self._make_position(node._prev)
    
    def after(self, p):
        node = self._validate(p)
        return self._make_position(node._next)
    
    def __iter__(self):
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    # Mutator Methods (AKA Changed From Base Class)
    def _insert_between(self, e, predecessor, successor):
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)
    
    def add_first(self, e):
        return self._insert_between(e, self._header, self._header._next)
    
    def add_last(self, e):
        return self._insert_between(e, self._trailer._prev, self._trailer)
    
    def add_before(self, p, e):
        original = self._validate(p)
        return self._insert_between(e, original._prev, original)
    
    def add_after(self, p, e):
        original = self._validate(p)
        return self._insert_between(e, original, original._next)
    
    def delete(self, p):
        original = self._validate(p)
        return self._delete_node(original)
    
    def replace(self, p, e):
        original = self._validate(p)
        old_value = original._element
        original._element = e
        return old_value
    

if __name__ == "__main__":
    pl = PositionalList()
    pos1 = pl.add_first(1)
    pos2 = pl.add_last(2)
    pos3 = pl.add_last(3)
    pos4 = pl.add_last(4)
    pos5 = pl.add_last(5)
    pos6 = pl.add_last(6)


    # print the list manually
    first = pl.first()
    last = pl.last()
    while first != last:
        print(first.element())
        first = pl.after(first)
    print(last.element())
    print("\n")
    # delete the 4th element
    first = pl.first()
    last = pl.last()

    while first != last:
        if first == pos4:
            pl.delete(first)
            break
        first = pl.after(first)

    for i in pl:
        print(i)

