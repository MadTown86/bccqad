# BCC - Summary of Episodes 14-18

"""
Topics:
1. Virtual Environments
2. Source Control (Git, GitHub)
3. Python Modules and Packages (Structure)
4. Exceptions and Error Handling
5. Debugging Console/Tools: VSCode
"""

# 1. Virtual Environment (VENV):
# 
# Process Flow: create -> activate -> install packages -> deactivate
#
# Create Virtual Environments (From GitBash or Terminal):
# python -m venv env_name
# source env_name/bin/activate (Linux/Mac)
#
# Enable Virtual Environment:
# source env_name/bin/activate (Linux/Mac)
# env_name\Scripts\activate (Windows)
#
# Install Packages (Pip):
# pip install package_name
# pip install -r requirements.txt (install all packages in a file)
# pip freeze > requirements.txt (create a file with all packages in the current environment)
#
# Deactivate Virtual Environment:
# deactivate

#
# 2. Source Control (Git, GitHub):
#
# Install Git:
# https://git-scm.com/downloads
#
# Initialize Git Repository:
# git init
# git init <directory_name> (create a new directory and initialize it as a git repository)
# git clone <repository_url> (clone a remote repository to your local machine)
#
# After creating and modifying files - ADD TO SOUCE CONTROL:
# git add <file_name> (add a specific file to the staging area)
# git add . (add all files in the current directory to the staging area)
# git add -A (add all files in the current directory and subdirectories to the staging area)
# 
# Commit Changes:
# git commit -m "commit message" (commit changes with a message)
#
# Link To Remote Repository (GitHub):
# git remote add origin <repository_url> (link your local repository to a remote repository)
# git remote -v (view the remote repositories linked to your local repository)
# git push -u origin master (push your changes to the remote repository)
# git push origin <branch_name> (push your changes to a specific branch in the remote repository)
# git pull origin <branch_name> (pull changes from a specific branch in the remote repository)
# git fetch origin <branch_name> (fetch changes from a specific branch in the remote repository without merging)





