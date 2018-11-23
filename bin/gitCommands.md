 #####Overview of git commands (and ideally how to use in Sourcetree)

 git clone  
    - "copying"/creating a connection between Git server and local system
```python 
cd ~ # navigate to home
mkdir repos # create directory to contain all git repos
cd ~/repos # navigate to repos folder

git clone nameof.git # cloning the git from git server
git config --global core.askpass # if windows error occurs -> should ask for pw
ls # to see what is in repo
```

 git config




 git add and  git status

  - moves changes from the working directory to the Git staging area. 
    Staging area is where you prepare a snapshot of a set of changes before
     committing them to official history

```python 
echo "Textcontent of script" >> filename.txt # -> git sees file that is untracked
git add filename.txt # corresponds to staging/vormerken in Sourcetree
git status # check for staged/unstaged files (git rm --cached filename to unstage)

```
    

 git commit

- takes the staged snapshot and commits it to project history.
Combined with git add this defines basic workflow for Git usage.
Up until here everything is on local system and nothing on remote repo.

```python 
git commit -m 'Commit message'
```


 git push
 
 - you publish local history by pushing branches to other repositories
```python 
git push origin master # specifies that you are pushing to master branch
```

 git pull

- get a file from the remote server into your local repository
```python 
git pull --all # pulls all changes from remote server / might be up to date
```

#### beyond basic workflow:

 git branch
 
 - branches allow you to update files and only share information when you're ready.
 They represent an independent line of development for your repo. Can be thought of as a new 
 working directory, staging area and project history.
- When you are ready to make plans known to all (merge) delete the no-longer needed 
branch
- branches are just pointers to commits

```python 
git branch second-branch # create a branch but does not switch you to that branch

```

 git checkout
- to begin working on a branch you have to check out the branch you want to use
- checkout command works hand in hand with git branch. ->  when you create new branch
you want 


```python 
git checkout second-branch

```

- when changing a file and checking git status, we see that on the corresponding path
- stage file using git add filename
- commit file using git commit filename -m "message"


 git merge

- a fast-forward branch can be done when having alinear path from current branch tip to target branch
Not actually a merge but rather an integration. "Combines histories".
Common for "short lived topic branches with smaller changes", not so common for longer running 
features.

```python 
git status
git checkout master
git merge second-branch
git branch -d second branch 
# deletes branch second branch. Still accessible from master using a commit id 

```

- to summarize: created branch, checked out, made change to new branch, committed 
change, integradet change back to main, deleted branch we are no longer using.
- now: push all to remote repository (Local/Master is 2 steps before origin/Master so far)
- git push origin master

- since second-branch never interacted with remote repository we have a straight forward path

### Learn about code review tutorial 
(https://www.atlassian.com/git/tutorials/learn-about-code-review-in-bitbucket-cloud) 
 
- create repository and add teammate, clone and make changes on new branch, if using command line or sourcetree

- you want to work on your own set of code separately from the main codebase.
Branches allow just that. After creation of branch, work on it and commiting code,
pull updates from Bitbucket to keep branch up-to-date and then push all to Bitbucket.

- Once you've got code changes on a branch in Bitbucket, you can create a pull request
-> code review takes place (feedback, questions etc. and hopefully approval) 
 
 - setup not completely recreated. Using existing repository instead and creating second branch
 
 ```python 
git branch new-branch
git fetch && git checkout new-branch
```
 
 
 
 