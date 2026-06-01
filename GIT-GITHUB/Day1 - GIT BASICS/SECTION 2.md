Now we start with practical implemenatation of the Git and Github from terminal.
# 1. Create your Folder
```Bash
mkdir git-pract
cd git-pract
```
***
What happened?
	
	mkdir - Create a new folder.
	cd -  Moves inside the folder
***
### Verify Current Directory
```Bash
pwd
```
#EXAMPLE
```Bash
/c/Users/Pratyaksh/git-practice
```
***
# 2. Initialize Git Repository
### Command
```Bash
git init
```
***
#EXAMPLE 
```Bash
Initaialized empty Git repository in ...
```
***
### What Actually Happened?
Git created a hidden folder:
```Bash
.git
```
This folder stores:
- commits
- branches
- configuration
- history
- logs
This is the brain of Git.
***
# 3. View Hidden Files
## Windows Git Bash
```Bash
ls -a
```
## Output
```Bash
.  ..  .git
```
---
### IMPORTANT CONCEPT
A folder becomes a Git repository ONLY after:
```Bash
git init
```
***
# 4. Check Repository Status
## Command
```Bash
git status
```
---
## Example Output
```Bash
On branch master

No commits yet

nothing to commit
```
***
### Understanding `git status`
This is the MOST used Git command.
Real developers use it constantly.
It tells:
- modified files
- staged files
- untracked files
- current branch
***
# 5. Create Your First File
## Command
```Bash
touch app.txt
```
If `touch` doesn't work on Windows CMD:
```Bash
echo Hello > app.txt
```
***
### Check Files
```Bash
ls
```
***
# 6. Check Git Status Again
```Bash
git staus
```
***
`Example`
```Bash
Untracked files:
	app.txt
```
---
### What is "Untracked"?
git sees the file exists,
BUT Git is NOT tracking it yet.
***
# 7. Add Files to Staging Area
### Command
```Bash
git add app.txt
```
---
### What Does `git add` Actually Do?
It moves changes from :

``Working Directory + Staging Area``
Meaning :
	"Git, prepares this file for commit".

---
# Check Status Again
```Bash
git status
```
---
## Example Output
```
Changes to be committed:
	new file: app.txt
```
---
# IMPORTANT INDUSTRY CONCEPT
## Staging Area Exists Because:
Developers often modify MANY files:
But maybe they only want to commit:
* 2 files now
* 5 files later
* Git staging gives precise control.
***
# 8 Create Your First Commit
### Command
```bash
git commit -m "Initial Commit"
```
---
`Example`
```Bash
[master (root-commit) xxxxxx]
1. file changed 
```
----
### What is a Commit?
A commit is :
* a snapshot
* a save point
* a version checkpoint
Think;
```Commit - Permanent history Record```

----
### Important Rule
Good Developer commit:
* frequently
* meaningfully
* cleanly
Bad Commit
```Bash
git commit -m "Stuff"
```
Good Commit 
```bash
git commit -m "Add login Verification"
```
---
# 9. Check Status Again
``` bash
git status
```
---
Output
```bash
nothing to commit, working tree clean
```
This means:
✅ Everything saved  
✅ No pending changes

---
# 10. View Commit History
Command
```bash
git log
```
---
`Èxample`
```Bash 
commit 8f7c2...
Author: Your Name
Date: ...

    Initial commit
```
---
### Important Concept
Each commit has:
- unique hash ID
- author
- timestamp
- message
---
### Better Log Format
##### Command
```Bash
git log --oneline
```
---
`Example`
```Bash
8f7c2 Initial commit
```
Real developers use this a LOT.

---
### Make Another Commit (REAL WORKFLOW)
### ADD Content to File
```bash
echo "Learning git" >> app.txt
```
---
### Check Status
```Bash
git status
```
You should see:
```bash
modified: app.txt
```
---
### Stage changes
```Bash
git add app.txt
```
----
### Commit Again
```Bash
git commit -m "Add learning message"
```
---
### View History
```Bash
git log --oneline
```
---
`Example`
```bash
a12bc Add learning message
8f7c2 Initial commit
```
---
### Real Developer Workflow
This cycle repeats DAILY:
```
Edit Files
↓
git status
↓
git add
↓
git commit
↓
git push 
```
Memorize this.

---
### COMMON BEGINNER MISTAKES
##### Mistake 1
Forgetting `git add`
Result
```bash
nothing added to commit
```
---
##### Mistake 2
Writing bad commit messages
Avoid:
- update
- changes
- final
- work
---
#### Mistake 3
Not checking `git status`
Professionals constantly run:
```
git status
```
---
### Best practises
##### Use Small Commits
GOOD:
```Bash
add navbar component
```
BAD:
```bash
Entire project changes
```
---
##### Commit Frequently
Do NOT wait 2 days

---
### Always Check Before Commit
```Bash
git status
git diff
```
---

# Interview Questions
Q1 What is a Git commit?
Q2 Difference between tracked and untracked files?
Q3 What does `git add` do internally?
Q4 Why does Git have a staging area?