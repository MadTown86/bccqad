# Binary Tree implementation in Python
# pg 314 - Data Structures and Algorithms in Python - Wiley - 2013

from Tree import Tree

class BinaryTree(Tree):
    def left(self, p):
        raise NotImplementedError("Must be implemented by subclass")
    def right(self, p):
        raise NotImplementedError("Must be implemented by subclass")
    
    def sibling(self, p):
        parent = self.parent(p)
        if parent is None:
            return None
        if p == self.left(parent):
            return self.right(parent)
        else:
            return self.left(parent)
        
    def children(self, p):
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)