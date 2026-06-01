Today is about:
> Making mistakes safely and recovering professionally.

This is where beginners become confident developers.

---
# 1. Understanding File Changes
Git constantly compares:
* currently files
* staged files
* committed history
That's how it detects changes.
---
### Important Concept
Git tracks:
* Added lines
* removed lines
* modified content
NOT just entire files.
---
# 2. `git diff`
Thus command show :
>Exact changes made in the files.

---
### Create Example
Open:
```
add.txt
```
Add:
```
Learning Git Deeply
```
Save file.

---
### Check Status
```Bash
git status
```
You should see:
```
modified app.txt
```
---
### View Changes
##### Command
```Bash
git diff
```
---
### Example Output
```Diff
+ Learning Git deeply
```
---
### Understanding diff Output
`+` - Added line
`-` - Removed Line

---
### Real World Importance
Before committing:
Professional developers often run:
```Bash
git diff
```
Why?
To verify:
* no accidental code
* no debug statements
* no secrets
* no broken changes
---
# 3. Working Directory vs Staging Area
This confuses many beginners.
### Git has Two Versions of Your Changes
##### Working Directory
Actual files changes
##### Staging Area
prepared snapshot for commit.

---
### Important
`git diff`
shows:
Working Directory vs Staging Area
### Stage file
```bash
git add app.txt
```
---
### Run Diff Again
```bash
git diff
```
Output may now be empty.
Why?
Because changes are already staged.

---
### See Staged Changes
##### Command
```bash
git diff --staged
```
or:
```bash
git diff --cached
```
---
### Professional Workflow
before commit:
```bash
git diff --stagged
```
this checks EXACTLY what will enter commit history.

----
# 4. `git restore`
This command is used to;
> Discard changes safely if not pushed.

---
### What happens?
Git restore file to last commited version
Uncommitted changes disappear.

---
### IMPORTANT WARNING
This is destructive.
Changes are LOST unless committed/staged elsewhere.

---
### Check Status
``` Bash
git status
```
File should be clean now.

---
# 5. Undoing Staged Changes
Suppose:
```Bash
git add app.txt
```
But you changed your mind.

---
### Unstage File
##### Command
```Bash
git restore --staged app.txt
```
---
### What Happens?
File:
- remains modified
- removed from staging area
---
### VERY IMPORTANT DIFFERENCE
This:
```Bash
git restore app.txt
```
removes file changes.

---
### This:
```Bash
git restore --staged app.txt
```
ONLY unstages.
Huge difference.

---
