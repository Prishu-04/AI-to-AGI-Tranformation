
# 1.What is Version Control
Version Control is a System that tracks changes in your files over time so you can:
* Go back to an old version.
* See who changed what.
* Recover deleted work.
* Work Safely in teams
**Example** : Think of like Google Doc history, but for code.
***
### Technical Explanation
A version control system (VCS) records snapshots of a project at different points in time.
Each snapshot :
- Represents the full state of your project
- Is stored efficiently (not full copies every time)
- Can be compared, restored, or branched
**Example** : Git is distributed version control system, meaning :
Every developer has a full copy of the repository history locally.
***
### Real World Example
Imagine you're building a project
* Day1 : Login System
* Day2 : You Break "" Accidentally
* Day3 : You want to go back to day1 version

Without Git:
* You manually search files (painful)
With Git
* You run a command and restore instantly
***
### Why Companies Use Version Control
In real companies:
- 10–500 developers work on same project
- Bugs happen daily
- Features are constantly added

Version control ensures:
- No code is lost
- Collaboration is safe
- Changes are traceable
***
# 2. Why Git Exists
Before Git:
- Developers used folders like:
    - project_final
    - project_final_v2
    - project_final_really_final 😭

Problems:
- Confusion
- File overwrites
- No history tracking

Git solved this by:
- Tracking every change
- Allowing branching (multiple versions at once)
- Making collaboration easy
***
# 3. Git vs GitHub
### Git
- Tool installed on your computer
- Works offline
- Tracks changes locally
### GitHub
- Cloud platform
- Stores Git repositories online
- Enables collaboration

Think:
- Git = engine
- GitHub = cloud storage + social network for code
***
# 4. How Git Works Internally (Very Important)
Git has 3 main areas:
1. **Working Directory**
    - Your actual files
2. **Staging Area**
    - Files prepared for commit
3. **Repository (.git)**
    - Permanent history storage

**Flow
```
Working Directory → Staging Area → Repository
```
***
# 5. Installing Git
Check if installed:
```Bash
git --version
```

**If not installed:
- Windows: install Git Bash
- Linux:
```Bash
sudo apt install git
```
***
# 6. Configuring Git (IMPORTANT)
**First-time setup:
```Bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

**Check Config:
```Bash

```
***
### Why this matters
Every commit is linked to:
- Name
- Email
In companies, this is how contributions are tracked.
***
# 7. Basic Terminal Navigation (Must Know)
```Bash
pwd        # show current directory
ls         # list files
cd folder  # move into folder
cd ..      # go back
mkdir test # create folder
```
***
