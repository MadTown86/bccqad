# Episode 14: Virtual Environments and Pip Package Management

"""
Virtual Environments in Python:

Basic Choices:
1. venv: Built-in module for creating isolated Python environments.    
2. UV: A third party tool for creating python virtual environments. *Not Covered In Video
(There are more but venv is all you need to get started.)

For the beginner, I would just use venv.  It is built-in and does not require any additional installation.

If you want something that is a bit more powerful, you can use UV.

I would start with venv for basic needs and just getting started.

Why use virtual environments?
- To create isolated environments for different projects.
- To avoid dependency conflicts between projects.
- To manage different Python versions for different projects.
- To ensure that each project has its own set of dependencies and packages.

You can automatically create dependencies for a project using pip freeze > requirements.txt.
# This will create a requirements.txt file with all the dependencies for the project.

You can use this file to recreate the environment using pip install -r requirements.txt.
# This will install all the dependencies listed in the requirements.txt file.
"""

"""
In a git bash terminal session:
"""
# Create a virtual environment using venv
# python -m venv myenv

# Activate the virtual environment
# Windows: myenv\Scripts\activate
# Mac/Linux: source myenv/bin/activate

# Install packages using pip
# pip install package_name

# Uninstall packages using pip
# pip uninstall package_name

# Make dependencies file
# pip freeze > requirements.txt

# Install dependencies from requirements.txt
# pip install -r requirements.txt

# Deactivate the virtual environment
# deactivate

# Delete the virtual environment
# rm -rf myenv
