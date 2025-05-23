# Positional List Implementation (Doubly Linked List Base)
# pg 282 - Data Structures and Algorithms in Python - Wiley - 2013

from _DoublyLinkedBase import _DoublyLinkedBase

class PositionalList(_DoublyLinkedBase):
    """
    A positional lists methods are all O(1) except for the iterator.
    """

    class Position:
        def __init__(self, container, node):
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

