# Episode 13: Classes 2: Inheritance 
from typing import List

"""
The class is one of the most complex and powerful concepts in many programming languages.

It allows for so much customization that it will require a while for you to even brush the surface of
it's full capabilities.  I intend to cover nearly everything there is to know about classes, but first
we will start with the concept of inheritence.  

What this means is that you can create a class that is a direct descendent of a 'parent' class.  The
child class inherits all of the features of the parent class.

However, unlike humans (heh), classes can have an infinite number of parents. This creates a family
tree for each class. 

The order of the parents does matter because of the following two things:

1. Attribute inheritence search
2. Method resolution order

I will discuss why these two things are important a bit later on after a few examples.

"""
# In an attempt to try to make this a simple, but 'realistic' example
# I will create my own class tree for a container or sequence.

class MyContainer:
    """
    The base class for all containers.  This class is not meant to be instantiated directly.
    """
    def __init__(self, contents: List[str] = None):
        if contents is None:
            self.contents = []
        else:
            self.contents = contents

    def add(self, item: str) -> None:
        """
        Add an item to the container.
        """
        self.contents.append(item)

    def remove(self, item: str) -> None:
        """
        Remove an item from the container.
        """
        self.contents.remove(item)

    def __str__(self) -> str:
        """
        Return a string representation of the container.
        """
        return str(self.contents)
    
"""
The base class is where you try to contain all possible uses of the class.
This is where you will put all of the methods that are common to all sequences.

Here you need to be able to create a container, add items to it, remove items from it
and print the contents of the container.
"""

class MyList(MyContainer):
    """
    A class that represents a list.  This class is a direct descendent of MyContainer.
    """
    def __init__(self, contents: List[str] = None):
        super().__init__(contents)

    def sort(self) -> None:
        """
        Sort the list in place.
        """
        self.contents.sort()

    def reverse(self) -> None:
        """
        Reverse the list in place.
        """
        self.contents.reverse()

    def __str__(self) -> str:
        """
        Return a string representation of the list.
        """
        return "List: " + super().__str__()
    
class MySet(MyContainer):
    """
    A class that represents a set.  This class is a direct descendent of MyContainer.
    """
    def __init__(self, contents: List[str] = None):
        super().__init__(contents)

    def add(self, item: str) -> None:
        """
        Add an item to the set.  If the item is already in the set, do nothing.
        """
        if item not in self.contents:
            self.contents.append(item)

    def remove(self, item: str) -> None:
        """
        Remove an item from the set.  If the item is not in the set, do nothing.
        """
        if item in self.contents:
            self.contents.remove(item)

    def __str__(self) -> str:
        """
        Return a string representation of the set.
        """
        return "Set: " + super().__str__()

