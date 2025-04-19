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

Forms of import covered:
1. import module_name
2. from module_name import function_name
3. from module_name import * (imports everything from the module)
4. import module_name as alias_name (imports the module with an alias)
5. from module_name import function_name as alias_name (imports the function with an alias)

*EXTRAS*:
Dot Notation For Importing Modules Within Packages:
1. You can import modules from packages using dot notation.

Example of a package structure:
    
    ```
    my_package/
    ├── __init__.py
    ├── module1.py
    ├── module2.py
    └── sub_package/
        ├── __init__.py
        └── module3.py
    ```

If you want to import module3 from module2, you can do it like this:
    
    ```python
    from my_package.sub_package.module3 import function_name
    ```
If you want to import module2 from module1, you can do it like this:
        
        ```python
        from my_package.module2 import function_name
        ```

If you want to import module1 from module3, you can do it like this:
            
            ```python
            from my_package.module1 import function_name
            ```

Module Search Path: (Where Python Looks for Modules and Packages When Importing)
1. The current directory (where the script is being run from).
2. The directories listed in the PYTHONPATH environment variable.
3. The standard library directories (where Python's built-in modules are located).
4. Any directories specified in the sys.path list.
5. The site-packages directory (where third-party packages are installed).

# Adding a Module or Package to the Python Path:
import sys
sys.path.append('/path/to/your/module_or_package')
# This allows you to import modules or packages that are not in the default Python path.

# You can check the current Python path using:
print(sys.path)

# If working with packages in the interactive prompt, you can use the following command
to reload the package after changes are made:
import importlib
importlib.reload(module_name)
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

FURTHER WARNING:
USING any of the 'FROM ... import' statements gives you access to the names in that module.
This means that you could potentially change the value of the name in the module itself.
This is not a good idea and should be avoided.

To put it into layman's terms:
You can alter the original values of attributes in the module that you imported.  Meaning, 
you are changing attributes in a different file from where you are executing the code.
This can be a large source of bugs in your code if you are not careful.  
"""