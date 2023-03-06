import sys
import os
import requests
from pprint import pprint
from github import Github
import subprocess
from pathlib import Path
import json

def print_repo(repo):
    # repository full name
    print("Full name:", repo.full_name)
    # repository description
    print("Description:", repo.description)
    # the date of when the repo was created
    print("Date created:", repo.created_at)


def create_local_git_repo():
  
   # create directory if it doesn't exist
    check_dir = Path(path)
    if check_dir.exists():
        print("Directory exists. Skip create directory")
    else:
        subprocess.run(["mkdir", path])

        # create repo folder if it doesn't exist
        print("Creating local repository...")

        # init repo
        subprocess.run(["git", "init"], cwd=path)


def create_readMe():
     # create a readme file
        f = open(path+"/ReadMe.txt", "w")
        f.write("ReadMe file initiated")
        f.close()

def stage_and_commit():
    # stage file created
        subprocess.run(["git", "add", path+"/ReadMe.txt"], cwd=path)
        print("Staging area....")

    # commit file
        subprocess.run(["git", "commit", "-m", "Initial commit"], cwd=path)
        print("Initial commit successfull !")


def create_github_repo():
  
    # generate data for request, set repo to private
    repo_config = '{"name": "%s", "public": "true"}' % repo_name
  
    # create repo
    header = 'Authorization: token ' + token

    # confirm repo now exists under user
    response = subprocess.run(["curl", "--header", header, "--request", "GET", "https://api.github.com/user/repos"], check=True, stdout=subprocess.PIPE)

    print("Remote repo created")

    # convert from completed process for easier parsing
    response_json = json.loads(response.stdout.decode("utf-8"))
 
    # confirm repo is created and extract url
    for repo_id in range(len(response_json)):
        remote_name = response_json[repo_id]['name']
 
        if(remote_name == repo_name):
            print("Repo now created on github")
            remote_url = response_json[repo_id]['html_url']
            break
 
    return remote_url


def add_remote_repo_url(remote_url):
  
   # url for repo
   server = remote_url + ".git"
   print("Repo URL: %s" % server)
  
   # add access token to url
   # https://YOUR_GITHUB_NAME:YOUR_ACCESS_TOKEN@github.com/YOUR_GITHUB_NAME/REPO_NAME.git

   server = server.replace("//", "//%s:%s@" % (username, token))

   # add remote origin
   subprocess.run(["git", "remote", "add", "origin", server], cwd=path)
   print("Add remote origin completed")
  
   return server


def push_local_repo_to_remote(server):
  
   push_url = server
  
   # push to github repo
   subprocess.run(["git", "push", "-u", push_url, "master"], cwd=path)
   pass

# ------------ END OF FUNCTIONS --------------


repo_name = sys.argv[1]
parent_dir = "" # where you need to create the repository
token = ""
username = ""

path = os.path.join(parent_dir, repo_name)

# using an access token
g = Github(token)

#--------------- START----------------
create_local_git_repo()

create_readMe()

stage_and_commit()

url = create_github_repo()
print(url)

# git remote add origin...
server = add_remote_repo_url(url)
print("Local and remote repo linked")

push_local_repo_to_remote(server)
print("Pushed to remote repo")

print("Finished creating the repository")
#--------------------END------------------
    