# Task 4 – Ignoring Files with .gitignore

## Problem Statement
a. Initialize a Git repository for a data science project
b. Push it to GitHub to enable version control
c. Create branch GIT-EXAM-1 and create program2 – check if a string is a palindrome
d. Create program1.py – print squares of numbers from 1 to 10
e. Commit, push and check the changes on GitHub
f. Create a directory IGNORE and add test1.txt and test2.txt into it
g. Create a .gitignore file and add the IGNORE directory to it
h. Commit, push and demonstrate that the IGNORE directory and its files are not pushed to GitHub

## Theory
- **.gitignore**: a text file listing files and folders that Git should NOT track. Ignored files never show in `git status`, never get committed and never reach GitHub.
- **Why ignore files?**
  - Secrets: passwords, API keys, `.env` files
  - Large files: datasets (`*.csv`), trained models (`*.pkl`, `*.h5`) – very common in data science
  - Auto-generated files: `__pycache__/`, `*.log`, virtual environments (`venv/`)
- **Common patterns**:
  - `IGNORE/` – a whole folder
  - `*.log` – every file ending in .log
  - `secret.txt` – one specific file
  - `!keep.log` – exception: track this file even if a pattern ignores it
- **Important**: .gitignore only affects files that are NOT already tracked. If a file was committed before, remove it from tracking with `git rm -r --cached <path>`.
- The .gitignore file itself IS committed, so everyone who clones the repo ignores the same files.

## Before you start
- On GitHub: New repository → name `ds-project-4` → do NOT tick "Add README" → Create.
- Keep your Personal Access Token ready.

## Steps (Ubuntu terminal)

### a. Initialise the repo
```bash
mkdir ds-project-4 && cd ds-project-4
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
git remote add origin https://github.com/shardSM/ds-project-4.git
git push -u origin master                 # username: shardSM, password: token
```

### c. Branch GIT-EXAM-1 + palindrome program
```bash
git checkout -b GIT-EXAM-1
nano program2.py                          # paste code, Ctrl+O, Enter, Ctrl+X
python3 program2.py                       # test: madam → Palindrome
```

### d. program1.py
```bash
nano program1.py
python3 program1.py
```

### e. Commit and push
```bash
git add .
git commit -m "Add palindrome and squares programs"
git push -u origin GIT-EXAM-1             # check GitHub: branch GIT-EXAM-1 has both files
```

### f. Create the IGNORE folder with two files
```bash
mkdir IGNORE
echo "This is test file 1" > IGNORE/test1.txt
echo "This is test file 2" > IGNORE/test2.txt
ls IGNORE                                 # test1.txt test2.txt
git status                                # BEFORE .gitignore: IGNORE/ shows as untracked (red)
```

### g. Create .gitignore
```bash
echo "IGNORE/" > .gitignore
cat .gitignore                            # IGNORE/
git status                                # AFTER: IGNORE/ is gone, only .gitignore shows
```

### h. Commit, push and demonstrate
```bash
git add .
git commit -m "Add .gitignore to ignore IGNORE folder"
git push
```

Proof that IGNORE is not tracked:
```bash
git ls-files                              # lists tracked files: no IGNORE files
git check-ignore -v IGNORE/test1.txt      # .gitignore:1:IGNORE/  IGNORE/test1.txt
git add IGNORE/test1.txt                  # Git refuses: "paths are ignored by one of your .gitignore files"
echo "new line" >> IGNORE/test1.txt
git status                                # still clean: changes inside IGNORE are not noticed
```
On GitHub (branch GIT-EXAM-1): README.md, program1.py, program2.py and .gitignore are visible, but there is NO IGNORE folder.

## If IGNORE was already committed by mistake
```bash
git rm -r --cached IGNORE                 # stop tracking it (files stay on your computer)
git commit -m "Stop tracking IGNORE folder"
git push
```

## Expected Result
- The IGNORE folder exists locally with test1.txt and test2.txt.
- `git status` doesn't show it, and GitHub doesn't contain it.
- .gitignore itself is pushed to GitHub.

## Viva Questions
1. **What is .gitignore?** A file listing paths Git should not track, commit or push.
2. **Why is .gitignore useful in data science?** To keep large datasets, model files, secrets and cache folders out of the repository.
3. **Does .gitignore work on already-committed files?** No. Use `git rm -r --cached <path>` first.
4. **How do you check whether a file is ignored?** `git check-ignore -v <file>`.
5. **How do you ignore all .log files?** Add `*.log` to .gitignore.
6. **Is the .gitignore file itself pushed?** Yes, so the same rules apply for everyone who clones the repo.
7. **What does `git ls-files` show?** All files currently tracked by Git.
