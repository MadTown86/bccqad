# Episode 15: Git Basics - Source Control

"""
Source Control:
This is the concept of recording every and all changes made to files within a 
directory (folder) and preferably on a remote server.

1. Download git from:
https://git-scm.com/downloads
*Download your flavor of GIT for your OS (Windows, Mac, Linux, etc.)
*Make sure to enable the option to add git to your PATH variable during installation.
*Make sure to enable the option to enable git bash during installation.

2. Create a free remote server account on github.com (I am most familiar, there are others):

A very useful git CLI website for practicing git commands is:
https://learngitbranching.js.org/

I am most familiar with github.com as a remote server for git
"""

# Git Basics:

# 1. Initializing a git repository:
# git init

# 2. Adding files that you want to track:
# git add <filename> or git add . (to add all files in the directory)

# 3. Committing Changes To Be Stored:
# git commit -m "Your commit message here"

# 4. Checking the status of your git repository:
# git status

# 5. Checking the history of your git repository:
# git log
# git log --oneline (for a more compact view of the history)

# 6. Creating a remote repository from your local repository:
# ***First you need to create a remote repository on github.com
# git remote add origin <remote repository URL>
# git push -u origin master (to push your local repository to the remote repository)
# git push (to push changes to the remote repository after the initial push)

# 7. Pulling changes from the remote repository to your local repository:
# git pull origin master (to pull changes from the remote repository to your local repository)
# git pull (to pull changes from the remote repository to your local repository after the initial pull)

# 8. Untracking files:
# git rm --cached <filename> (to untrack a file from the git repository)
# git rm -r --cached . (to untrack all files in the directory)

# 9. Ignoring files:
# Create a .gitignore file in the root of your repository and add the files you want to ignore:

# 10. Branching:
# git branch <branch_name> (to create a new branch)
# git checkout <branch_name> (to switch to a branch)
# git checkout -b <branch_name> (to create and switch to a new branch)

# 11. Merging:
# git merge <branch_name> (to merge a branch into the current branch)
# git merge --abort (to abort a merge)
# git merge --continue (to continue a merge after resolving conflicts)
# git merge --abort (to abort a merge)

# 12. Rebasing:
# git rebase <branch_name> (to rebase the current branch onto another branch)
# git rebase --continue (to continue a rebase after resolving conflicts)
# git rebase --abort (to abort a rebase)

"""
General Git Process Flow:
1. Git init : creates a new git repository in the current directory where git init is run
2. Git add <filename> : This adds files to what is called the 'staging area'
This basically means it is going to be tracked by git.
3. Git commit -m "<message>" : This commits the changes to the local repository with a message.
Committing is just saving the changes to the local repository.

Simple Description:
You use git init to turn whatever current directory you are in into a git repository.  Then
you add files to it that you want to track changes for and or keep a remote copy of.  After
you add all the files you want to track, you then commit the changes along with a 'message'.
After you make this commit, the changes to the files are saved to the local repository.  Then
you can push the changes to the remote repository.

Why use remote repository?
Well it gives you access to your code from anywhere.  If you have a home computer and then
a laptop for travel, well you can work on the same project on either device.
"""