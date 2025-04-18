# Episode 14 and 15: Practice
"""
BELOW THE ANSWERS ARE CODE SNIPPETS AND WILL BE IN BLOCK QUOTES
"""
# 1. Create a new python project location
"""
NOT CODE - DESCRIPTION ONLY
In VSCode open a new window, then select 'open folder' and create a new folder
for use as a test.
"""
# 2. Create a new virtual environment using venv
"""
python -m venv myvenv
"""
# 3. Activate the virtual environment
"""
# source myvenv/bin/activate
"""
# 4. Install the following packages using pip:
#     - requests
#     - numpy
#     - pandas
"""
pip install requests, numpy, pandas
"""
# 5. Create a requirements.txt file using pip freeze > requirements.txt
"""
pip freeze > requirements.txt
"""
# 6. Deactivate the virtual environment
"""
deactivate
"""
# 7. Initialize git source control in the project location
"""
git init
"""
# 8. Create a new remote repository on github.com
"""
NOT CODE - DESCRIPTION ONLY:
Log In -> click repositories -> click new -> entery repository name -> click create repository
"""
# 9. Create two files in the project location and add them to git
"""
touch file1.py file2.py
git add file1.py file2.py
"""
# 10. Commit the changes to git with a message
"""
git commit -m "Initial commit with two files"
git commit -a -m "Secondary Commit"
"""
# 11. Link local repository to remote repository
"""
git remote add origin <remote repository URL>
"""
# 12. Push the local repository to the remote repository
"""
git push -u origin master
"""
