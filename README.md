# Github-Automation-using-python

## please refer the dev branch to view all the required files
## make sure to "pip3 install PyGithub requests" libraries

## What is this program?
  - This is a program developed to automate the cumbersome task of initializing a new repository
  - This will
    - create a new local repo in the specific folder
    - initialize the git repository
    - create a readMe.txt file
    - add initial file to the staging area
    - perform the initial commit
    - create a remote github repository
    - link the local repo using the https
    - initial push to the remote repository
   
  - This would save a lot of your time

## How to run this program
  - First download the GitPyScript.py python file
  - copy the file to the root folder (C:\Users\joe)
  - create a folder called bin in the root folder
  - go to the bin folder, copy the path and add it to environment variables
  - download the script.sh shell script
  - copy the shell script file to the bin folder you just created
  - Now open the GitPyScript file which is in your root folder and provide the following info
    - parent directory
    - github token
      - To generate a token in github settings -> developer settings -> personal access tokens -> generate new token
    - github username
  - Open git bash anywhere and give the command "script.sh repo_name" (eg: script.sh MyRepo)
  - Then the local repo will be created on the specified folder (parent directory in the python script) and a remote repo
 

