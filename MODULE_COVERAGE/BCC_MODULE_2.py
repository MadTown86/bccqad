# Blue Collar Codes - Python Module Coverage - Episode 2
# itertools

# https://docs.python.org/3/library/itertools.html

"""
Itertools module provides 'tools' to help one 'iterate'.  If you need to loop through
multiple datasets or create all permuations/combinations this is the module.

This Episode's Coverage:
-chain() - chain iterables together
-pairwise() - iterate through pairs
-zip_longest() - zip - except iterates to end of longest w/ filler char
-permutations() - every possible permutations of a given iterable in k-length pairs

"""

#import statement
import itertools

# chain()
l1 = [1, 2, 3]
l2 = ['a', 'b', 'c']

for x in itertools.chain(l1, l2):
    print(x * 2)

"""
Chain allows you to continue iterating through multiple containers.  Good for running a
function on multiple datasets without wasting the code to call function separately.

Note*: This returns a generator, which means it doesn't return the full chained list.
It needs to be iterated through to reach all values.

This returns [2, 4, 6, 'aa', 'bb', 'cc']
"""

print('*' * 30 + '\n')

# pairwise()
for x in itertools.pairwise(l1):
    print(x)

for x in itertools.pairwise(itertools.chain(l1, l2)):
    print(x)

"""
Pairwise allows you to access values in pairs of two as you iterate.

The output is:
[(1, 2), (2, 3)] - first example with l1
[(1, 2), (2, 3), (3, 'a'), ('a', 'b'), ('b', 'c')]
"""

print('*' * 30 + '\n')

# zip_longest()
l3 = ['i', 'j', 'k', 'l']

for x in itertools.zip_longest(l2, l3, fillvalue='-'):
    print(x)

"""
Zip longest is just zip that will continue iteration and allow you 
to choose a fill-value.

The output is:
[('a', 'i'), ('b', 'j'), ('c', 'k'), ('-', 'l')]

Note*: The last pair used the fill-value
"""

print('*' * 30 + '\n')

# permutations()
l4 = 'abcdefg'
res = []
for perm in itertools.permutations(l4, 2):
    res.append(perm)

print(res)

"""
Permutations will create all combinations of given length (2nd argument).
among the input arguments values.  In this examples case, it will create
all possible 2-pair permutations of the string 'abcdefg'

Too many to list the output, but it is a list of tuples containing
pairs starting with ('a', 'b'), ('a', 'c'), ('a', 'd'), etc.
"""
