# Episode 16 Practice:
# 1. What makes a directory a package?
"""
All it needs is a file called __init__.py in that directoyr.
"""
# 2. What are modules?
"""
Files containing Python code.  (.py files)
"""
# 3. What is the syntax for using a function/method from a module when using import?
"""
import math

math.sqrt(4) (you need dot notation to access.  Good to avoid name collisions)
"""
# 4. What is the syntax for using a function/method from a module when using from import?
"""
from math import sqrt
sqrt(4) (no dot notation needed, but can cause name collisions)
"""
# 5. What is the syntax for using a function/method from a module when using from import *?
"""
from math import *

sqrt(4) (no dot notation needed, but can cause name collisions)
floor(4.5) (no dot notation needed, but can cause name collisions)
"""
# 6. What is the syntax for using a function/method from a module when using import as?
"""
import math as m
m.sqrt(4) (you need dot notation to access but use 'm'.  Good to avoid name collisions)
"""
# 7. What is the syntax for using a function/method from a module when using from import as?
"""
from math import sqrt as s
s(4) (no dot notation needed, potential name collisions, but you can alter its alias.)
"""
# 8. How do you add a package/directory to the module search path?
"""
import sys
sys.path.append('/path/to/your/package')
# This allows you to import modules or packages that are not in the default Python path.
"""