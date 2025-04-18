# Episode 16: Modules and Packages

"""
Modules, Packages and Basic Importing:
1. Modules are files that contain Python code.
2. Packages are directories that contain modules.
3. Importing is the process of bringing modules and packages into your code.

To let Python know that a directory contains Python modules,
you need to create a file called __init__.py in that directory.  
This file can be empty or contain code that you want to run when the package is imported.

Every folder that you want to be treated as a package must contain an __init__.py file.

You can import modules and packages using the import statement.

You simply import it using the name of the file without the .py extension.

Forms of import being covered:
1. import module_name
2. from module_name import function_name
3. from module_name import * (imports everything from the module)
4. import module_name as alias_name (imports the module with an alias)
5. from module_name import function_name as alias_name (imports the function with an alias)

"""

# Importing a module
import math
print(math.sqrt(16))  # Output: 4.0
# Note the name of the module is needed to access the function within the module.

# Giving an imported module a different name
import math as m
print(m.sqrt(16))  # Output: 4.0
# You can use this to shorten the name of a module if you anticipate having to type it a lot.

from math import sqrt
print(sqrt(16))  # Output: 4.0
# Note how this allows you to access the function without neeeding to use the module name.

from math import sqrt as s 
print(s(16))  # Output: 4.0
# This allows you to use a shorter name for the fnction

from math import *
print(sqrt(16))  # Output: 4.0
"""
Warning: 
This effectively sandwiches all names in the math module into the current namespace.
This can cause name conflicts and should only be used when you are sure that
you maintained unique names in your code.
"""