# Task 2 – Git Branches and Pull Request

## Problem Statement
a. Initialize a Git repository for a data science project
b. Push it to GitHub to enable version control
c. Create program1.py – check whether a number is even or odd
d. Commit, push and check the changes on GitHub
e. Create branch GIT-EXAM and add program2.py – reverse of a string
f. Commit, push and demonstrate the difference between master/main and GIT-EXAM
g. Create a pull request to merge GIT-EXAM into master/main

## Theory
- **Git**: a distributed version control system that tracks changes in files.
- **Commit**: a saved snapshot of changes with a message.
- **Branch**: an independent line of development; changes don't affect other branches until merged.
- **Pull Request (PR)**: a request on GitHub to merge one branch into another. Others can review the changes, comment and approve before merging.
- **Base branch**: the branch changes are merged INTO (master).
- **Compare branch**: the branch changes come FROM (GIT-EXAM).
- **Merge**: combines the history of two branches into one.

## Before you start
- On GitHub: New repository → name `ds-project-2` → do NOT tick "Add README" → Create.
  (Any name works, but it must match the URL in `git remote add`. If the repo doesn't exist, push fails with "Repository not found".)
- Keep your Personal Access Token ready (Ubuntu asks for it as the password).

## Steps (Ubuntu terminal)

### a. Initialise the repo
```bash
mkdir ds-project-2 && cd ds-project-2
git init
git config --global user.name "shardSM"
git config --global user.email "shardulmarathe374@gmail.com"
```

### b. First commit and push
```bash
echo "# Data Science Project" > README.md
git add README.md
git commit -m "Initial commit"
git branch -M master
git remote add origin https://github.com/shardSM/ds-project-2.git
git push -u origin master        # username: shardSM, password: token
```

### c, d. program1.py → commit → push
```bash
nano program1.py                 # paste code, Ctrl+O, Enter, Ctrl+X
python3 program1.py              # test: enter 7 → "7 is Odd"
git add program1.py
git commit -m "Add even odd program"
git push                         # refresh GitHub to verify
```

### e. New branch + program2.py
```bash
git checkout -b GIT-EXAM
nano program2.py
python3 program2.py              # test: enter hello → "olleh"
```

### f. Commit, push, compare
```bash
git add program2.py
git commit -m "Add reverse string program"
git push -u origin GIT-EXAM
git diff master GIT-EXAM         # program2.py shown as new file (press q to exit)
git log --oneline --graph --all
```

Live demonstration:
```bash
git checkout master && ls        # README.md program1.py
git checkout GIT-EXAM && ls      # README.md program1.py program2.py
```

### g. Create and merge the Pull Request (on GitHub)
1. Open the repo on GitHub → a yellow bar shows "GIT-EXAM had recent pushes" → click **Compare & pull request**.
   (Or: Pull requests tab → New pull request.)
2. Set **base: master** ← **compare: GIT-EXAM**.
3. Title: `Add reverse string program` → add a short description → **Create pull request**.
4. Show the examiner the **Files changed** tab (program2.py added).
5. Click **Merge pull request** → **Confirm merge**.
6. Bring the merged code back to your computer:
```bash
git checkout master
git pull
ls                               # program2.py is now in master too
```

## Expected Result
- Before the PR: master has README.md and program1.py; GIT-EXAM also has program2.py.
- After merging: master contains program2.py as well, and the PR shows as "Merged".

## Viva Questions
1. **What is a Pull Request?** A GitHub feature to propose merging one branch into another, so changes can be reviewed before they enter the main code.
2. **Base vs compare branch?** Base receives the changes (master); compare provides them (GIT-EXAM).
3. **Why not push directly to master?** PRs allow code review and discussion, preventing mistakes in the main branch.
4. **What does `git pull` do?** Downloads new commits from GitHub and merges them into the current branch (fetch + merge).
5. **What does `s[::-1]` mean?** Slicing with step -1, which returns the string in reverse order.
6. **What does `%` do?** Gives the remainder; `n % 2 == 0` means n is even.
