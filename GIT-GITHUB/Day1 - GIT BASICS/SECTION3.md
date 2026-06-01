# 1. Multiple File Workflow
Real projects do NOT have one file.
`Example`
```
project/
 ├── app.js
 ├── index.html
 ├── style.css
 └── README.md
```
Develoeprs constantly:
* modify multiple files
* stage only some changes
* commit carefully
---
# 2. Create Multiple Files
Inside your repo:
```Bash
touch index.html style.css app.js
```
Check:
```Bash
ls
```
---
### Check Git Status
```Bash
git status
```
---
`Example Output
```Bash
Untracked files:  app.js  index.html  style.css
```
---
### IMPORTANT CONCEPT
Git tracks EACH file independently.
Every file can be:
- untracked
- modified
- staged
- committed
at different times.
---
# 3. Stage All Files
### Command
```Bash
git add .
```
---
### What Does `.` Mean?
```Bash
.
```
means:
> current directory

So:
```Bash
git add .
```
means:
> Add ALL changes in current folder

---
### VERY IMPORTANT WARNING
Beginners overuse:
```
git add .
```
Problem:  
You may accidentally commit:
- passwords
- API keys
- unnecessary files
- build folders
Professional developers often stage selectively.
---
# 4. Selective Staging (INDUSTRY PRACTICE)
Instead of:
```Bash
git add .
```
You can do:
```Bash
git add app.js
```
or:
```Bash
git add style.css
```
---
### Real Company Scenario
Suppose:
- `app.js` has working feature
- `style.css` is broken
You should commit ONLY working code.
That’s why staging exists.

---
# 5. Understanding File States
Git files move through states:
```
Untracked
↓
Tracked
↓
Modified
↓
Staged
↓
Committed
```
---
### VISUAL FLOW
```
Edit File
↓
git status
↓
git add
↓
git commit
```
This becomes muscle memory.

---
# 6 Read `git status` like a Professional
Run:
```Bash
git status
```
---
## Common Sections
### Untracked Files
Git sees file but not tracking.
### Changes Not Staged
Modified but not added.
### Changes To Be Committed
Ready for commit.

---
# PROFESSIONAL HABIT
Run:
```Bash
git status
```
BEFORE:
- add
- commit
- push
- pull
Always know repository state.
---
# 7. Introduction to `.gitignore`
### What is `.gitignore` ?
A file telling Git:
	Ignore these files/folders

---
### Why Needed?
projects generate unnecessary files:
* cache 
* logs
* build outputs
* dependencies 
* secrets
YOU SHOULD NOT COMMIT THEM.
---
### create `.gitignore`
```Bash
touch .gitignore
```
---
### Add Content
Example:
```
node_modules/
.env
*.log
dist/
```
---
### Meaning
`node_module/`
Ignore dependency folder.

`.env`
Ignore secret environment variables.

`*.log`
Ignore all log files.

`dist/`
Ignore build folder.

---
### Critical Security Rule
NEVER commit ;
* passwords
* API keys
* tokens
* `.env`
---
# 8. Rea Projects Structure
Professional repo example:
```
project/
 ├── src/
 ├── public/
 ├── README.md
 ├── .gitignore
 ├── package.json
 └── tests/
```
---
# 9. Commit Message Standards
Bad;
```Bash
git commit -m "update"
```
---
Good:
```Bash
git commit -m "Add login form validation"
git commit -m "Fix navbar mobile alignment"
git commit -m "Create authentication middleware"
```
---
### Industry Best practice
Commit message should answer:
	What changed?
NOT:
	Why life is difficult

---
# 10. Git history Visualisation
Run:
```Bash
git log --oneline
```
---
### Better Visualization
```Bash
git log --oneline --graph
```
Example:
```
* a1b2c Add navbar
* 9f8e7 Fix login
* 2c4d1 Initial commit
```
---
# 11. Practical Team Scenario
Imagine:
You work at Google 
You're assigned : Login feature
Another developer : Dashboard feature
You should:
* work separately
* commit clearly
* avoid breaking main codebase.
This is where branching becomes important (Day 3).
---
# 12. Daily Industry Workflow
Real Engineers repeat this;
```Bash
git pull
git checkout feature-branch
# write code
git status
git add .
git commit -m "Add feature"
git push
```
Daily Constantly.

---
# 13. Productivity Tips
### Shortcut 1
Compact status:
```bash
git status -s
```
Example;
```
M app.js
?? notes.txt
```
---
### Shortcut 2
One-line logs:
```Bash
git log --oneline
```
---
### Shortcut 3
See last commit;
```Bash
git log -1
```
----
# 14. Common Debugging Situations
### Problem 1:
Forget to add file. 
Solution;
```Bash
git add filename
git commit
```
---
### Problem 2:
Wrong commit message.
(Learn fixes later).

----
### Problem 3:
Accidentally commited secret:
URGENT:
* remove immediately
* rotate credentials
---
# 15. Practice Exercise
## Exercise 1
Create:
```
README.md
```
Commit it properly.

---
## Exercise 2
Create:
```
debug.log
```
Ignore it using `.gitignore`.

---
## Exercise 3
Modify:
```
app.jsstyle.css
```
Stage ONLY one file.

---
# 16. Mini Project
Create this structure:
```
portfolio-site/ ├── index.html ├── style.css ├── app.js ├── README.md └── .gitignore
```
Tasks:
- initialize Git
- create 5 commits
- use meaningful commit messages
---
# 17. Interview Questions
Q1 Why is `.gitignore` important?
Q2 Difference between `git add .` and  `git add file.txt`
Q3 What happens internally during commit?
Q4 Why are meaningful commit messages important?