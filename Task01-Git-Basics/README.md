# Task 1 – Git Basics: init, push, branch, diff

## Problem Statement
a. Initialize a Git repository for a data science project
b. Push it to GitHub to enable version control
c. Create program1.py – print multiplication table of any number
d. Commit, push and check the changes on GitHub
e. Create branch GIT-EXAM and add program2.py – greatest of two numbers
f. Commit, push and demonstrate the difference between master and GIT-EXAM

## Theory
- **Git**: a distributed version control system that tracks changes in files.
- **Repository**: a project folder tracked by Git (history is stored in the hidden `.git` folder).
- **Staging area**: `git add` selects changes for the next commit.
- **Commit**: a saved snapshot of changes with a message.
- **Remote (origin)**: the copy of the repo on GitHub.
- **Push**: uploads local commits to the remote.
- **Branch**: an independent line of development; changes don't affect other branches until merged.
- **git diff**: shows the differences between two branches or commits.

## Before you start
- On GitHub: New repository → name `ds-project` → do NOT tick "Add README" → Create.
- Keep your Personal Access Token ready (GitHub rejects normal passwords for push).

## Steps (Ubuntu terminal)

### a. Initialise the repo
```bash
mkdir ds-project && cd ds-project
git init
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

### b. First commit and push
```bash
echo "# Data Science Project" > README.md
git add README.md
git commit -m "Initial commit"
git branch -M master
git remote add origin https://github.com/<username>/ds-project.git
git push -u origin master        # username + token as password
```

### c, d. program1.py → commit → push
```bash
nano program1.py                 # paste code, Ctrl+O, Enter, Ctrl+X
python3 program1.py              # test
git add program1.py
git commit -m "Add multiplication table program"
git push                         # refresh GitHub to verify
```

### e. New branch + program2.py
```bash
git checkout -b GIT-EXAM
nano program2.py
python3 program2.py
```

### f. Commit, push, compare
```bash
git add program2.py
git commit -m "Add greatest of two numbers"
git push -u origin GIT-EXAM
git diff master GIT-EXAM         # program2.py shown as new file (press q to exit)
git log --oneline --graph --all
```

### Live demonstration for the examiner
```bash
git checkout master && ls        # README.md program1.py
git checkout GIT-EXAM && ls      # README.md program1.py program2.py
```
On GitHub, switch the branch dropdown between master and GIT-EXAM.

## Expected Result
- GitHub shows two branches: master (README, program1.py) and GIT-EXAM (also program2.py).
- `git diff master GIT-EXAM` lists program2.py as a new file.

## Viva Questions
1. **Difference between Git and GitHub?** Git is the version control tool on your computer; GitHub is a website that hosts Git repositories online.
2. **What does `git add` do?** Moves changes to the staging area so they are included in the next commit.
3. **What is `-u` in `git push -u`?** Sets the upstream branch, so later a plain `git push` works.
4. **`git checkout -b` vs `git branch`?** `git branch X` only creates the branch; `checkout -b X` creates it and switches to it.
5. **Why use branches?** To develop features safely without affecting the main code.
6. **How to see all branches?** `git branch` (local), `git branch -a` (local + remote).
