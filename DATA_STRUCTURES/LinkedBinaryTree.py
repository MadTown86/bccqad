# Linked Binary Tree Implementation
# pg 320 - Data Structures and Algorithms in Python - Wiley - 2013
from BinaryTree import BinaryTree


class LinkedBinaryTree(BinaryTree):
    """
    len() - O(1)
    root() - O(1)
    parent(p) - O(1)
    left(p) - O(1)
    right(p) - O(1)
    is_empty() - O(1)
    num_children(p) - O(1)
    is_leaf(p) - O(1)
    depth(p) - O(dp + 1)
    height = O(n)
    add_root(e) - O(1)
    add_left(p, e) - O(1)
    add_right(p, e) - O(1)
    replace(p, e) - O(1)
    delete(p) - O(1)
    attach(p, t1, t2) - O(1)
    """
    class _Node:
        __slots__ = '_element', '_parent', '_left', '_right'

        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    class Position(BinaryTree.Position):
        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            return type(self) is type(other) and self._node is other._node
        
    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError("p must be a Position instance")
        if p._container is not self:
            raise ValueError("p does not belong to this container")
        if p._node._parent is p._node:
            raise ValueError("p is no longer valid")
        return p._node
    
    def _make_position(self, node):
        return self.Position(self, node) if node is not None else None
    
    def __init__(self):
        self._root = None
        self._size = 0

    def __len__(self):
        return self._size
    
    def root(self):
        return self._make_position(self._root)
    
    def parent(self, p):
        node = self._validate(p)
        return self._make_position(node._parent)
    
    def left(self, p):
        node = self._validate(p)
        return self._make_position(node._left)
    
    def right(self, p):
        node = self._validate(p)
        return self._make_position(node._right)
    
    def num_children(self, p):
        node = self._validate(p)
        count = 0
        if node._left is not None:
            count += 1
        if node._right is not None:
            count += 1
        return count
    
    def _add_root(self, e):
        if self._root is not None:
            raise ValueError("Root already exists")
        self._root = self._Node(e)
        self._size = 1
        return self._make_position(self._root)
    
    def _add_left(self, p, e):
        node = self._validate(p)
        if node._left is not None:
            raise ValueError("Left child already exists")
        new_node = self._Node(e, node)
        node._left = new_node
        self._size += 1
        return self._make_position(new_node)
    
    def _add_right(self, p, e):
        node = self._validate(p)
        if node._right is not None:
            raise ValueError("Right child already exists")
        new_node = self._Node(e, node)
        node._right = new_node
        self._size += 1
        return self._make_position(new_node)
    
    def _replace(self, p, e):
        node = self._validate(p)
        old_value = node._element
        node._element = e
        return old_value
    
    def _delete(self, p):
        node = self._validate(p)
        if self.num_children(p) == 2: raise ValueError("p has two children")
        child = node._left if node._left else node._right
        if child is not None:
            child._parent = node._parent
        if node is self._root:
            self._root = child
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        self._size -= 1
        node._parent = node
        return node._element
    
    def _attach(self, p, t1, t2):
        node= self._validate(p)
        if not self.is_leaf(p):
            raise ValueError("p must be a leaf")
        if not type(self) is type(t1) is type(t2):
            raise TypeError("t1 and t2 must be of the same type as this tree")
        self._size += len(t1) + len(t2)
        if not t1.is_empty():
            t1._root._parent = node
            node._left = t1._root
            t1._root = None
            t1._size = 0
        if not t2.is_empty():
            t2._root._parent = node
            node._right = t2._root
            t2._root = None
            t2._size = 0
