# Episode 18 Practice Questions - Answers:

# 1. What are breakpoints and how do you set them in VSCode?
"""
You can set breakpoints in VSCode by clicking in the gutter to the left of the line numbers in your code editor.
A red dot will appear, indicating a breakpoint has been set.
When you run the code in debug mode, execution will pause at the breakpoint.
"""
# 2. Name a few windows in the debugging console of VSCode?
"""
The debugging console in VSCode includes several windows such as:
- Variables: Displays the current variables in scope and their values.
- Watch: Allows you to add expressions to watch and see their values as you step through the code.
- Call Stack: Shows the current call stack, allowing you to see the function calls that led to the current point in execution.
"""
# 3. What is the purpose of the "Step Over" button in the debugger?
"""
The "Step Over" button allows you to execute the current line of code and move to the next line in the same function.
If the current line contains a function call, it will execute the entire function but not step into it.***
"""
# 4. What is the purpose of the "Step Into" button in the debugger?
"""
The "Step Into" button allows you to execute the current line of code and, if it contains a function call, step into that function.
This lets you debug the function line by line.
"""
# 5. What is the purpose of the "Step Out" button in the debugger?
"""
The "Step Out" button allows you to finish executing the current function and return to the calling function.
This is useful when you want to quickly exit a function without stepping through all its lines.
"""