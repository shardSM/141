# Task 3 – Multiple Branches, Pull and Merge Conflicts

## Problem Statement
a. Initialize a Git repository for a data science project
b. Push it to GitHub to enable version control
c. Create branch GIT-EXAM-1 and create program2 – check if a string is a palindrome
d. Create program1.py – print squares of numbers from 1 to 10
e. Commit, push and check the changes on GitHub
f. Create a new branch GIT-EXAM-2
g. Pull the changes from branch GIT-EXAM-1
h. Create program2.py – check if a string is a palindrome
i. Modify program1.py (to demonstrate conflicts)
j. Commit, push and demonstrate the difference between master, GIT-EXAM-1 and GIT-EXAM-2
k. Create a pull request to merge GIT-EXAM-2 into GIT-EXAM-1

## Theory
- **Branch**: an independent line of development.
- **git pull**: fetches commits from a remote branch and merges them into the current branch (fetch + merge).
- **Merge conflict**: happens when the SAME lines of the SAME file are changed differently in two branches. Git can't decide which version to keep, so a human must choose.
- **Conflict markers**:
  - `<<<<<<< HEAD` – start of the version in your current branch
  - `=======` – separator
  - `>>>>>>> branch-name` – end of the version from the other branch
- **Resolving**: edit the file, keep the correct code, delete the markers, then `git add` and `git commit`.
- **Pull Request**: proposes merging one branch into another; GitHub shows whether it can merge automatically or has conflicts.

## Branch plan (what ends up where)
| Branch | Contents |
|--------|----------|
| master | README.md only |
| GIT-EXAM-1 | README.md, program1.py, program2.py (original versions) |
| GIT-EXAM-2 | Created from master, pulls GIT-EXAM-1, then changes program1.py and program2.py |

## Before you start
- On GitHub: New repository → name `ds-project-3` → do NOT tick "Add README" → Create.
- Keep your Personal Access Token ready.

## Steps (Ubuntu terminal)

### a. Initialise the repo
```bash
mkdir ds-project-3 && cd ds-project-3
git init
git config --global user.name "shardSM"
git config --global user.email "shardulmarathe374@gmail.com"
git config --global pull.rebase false     # makes git pull use merge (avoids the "divergent branches" error)
```

### b. First commit and push
```bash
echo "# Data Science Project" > README.md
git add README.md
git commit -m "Initial commit"
git branch -M master
git remote add origin https://github.com/shardSM/ds-project-3.git
git push -u origin master                 # username: shardSM, password: token
```

### c. Branch GIT-EXAM-1 + palindrome program
```bash
git checkout -b GIT-EXAM-1
nano program2.py                          # paste program2.py code, Ctrl+O, Enter, Ctrl+X
python3 program2.py                       # test: madam → Palindrome
```

### d. program1.py (still on GIT-EXAM-1)
```bash
nano program1.py                          # paste program1.py code
python3 program1.py                       # prints 1 squared is 1 ... 10 squared is 100
```

### e. Commit and push GIT-EXAM-1
```bash
git add .
git commit -m "Add palindrome and squares programs"
git push -u origin GIT-EXAM-1             # check GitHub: switch branch dropdown to GIT-EXAM-1
```

### f. Create GIT-EXAM-2 from master
```bash
git checkout master
git checkout -b GIT-EXAM-2
ls                                        # only README.md
```

### g. Pull changes from GIT-EXAM-1
```bash
git pull origin GIT-EXAM-1
ls                                        # README.md program1.py program2.py
```

### h. program2.py in GIT-EXAM-2
program2.py came in with the pull. Open it and write an improved palindrome version
(ignores capital letters and spaces):
```bash
nano program2.py
```
```python
# Check whether a string is a palindrome (ignores case and spaces)
s = input("Enter a string: ")
clean = s.replace(" ", "").lower()
if clean == clean[::-1]:
    print(s, "is a Palindrome")
else:
    print(s, "is not a Palindrome")
```
```bash
python3 program2.py                       # test: Nurses Run → Palindrome
```

### i. Modify program1.py (to demonstrate conflicts)
```bash
nano program1.py
```
Change the print line to:
```python
    print(f"Square of {i} = {i ** 2}")
```

### j. Commit, push and compare all three branches
```bash
git add .
git commit -m "Modify squares format and improve palindrome"
git push -u origin GIT-EXAM-2

git diff master GIT-EXAM-1                # program1.py and program2.py are new in GIT-EXAM-1
git diff GIT-EXAM-1 GIT-EXAM-2            # changed print line + improved palindrome
git log --oneline --graph --all           # history of all three branches
```
(press q to exit long output)

### Creating the conflict
A conflict needs BOTH branches to change the same line. So change the same line in GIT-EXAM-1 too:
```bash
git checkout GIT-EXAM-1
nano program1.py
```
Change the print line to something different:
```python
    print(f"{i} x {i} = {i * i}")
```
```bash
git add program1.py
git commit -m "Change squares format in GIT-EXAM-1"
git push
```

### k. Pull Request: GIT-EXAM-2 → GIT-EXAM-1
1. GitHub → Pull requests → **New pull request**.
2. Set **base: GIT-EXAM-1** ← **compare: GIT-EXAM-2**.
3. GitHub shows **"Can't automatically merge"**. This is the conflict. Click **Create pull request** anyway.

**Resolve on GitHub:**
4. Click **Resolve conflicts**. The file shows:
```
<<<<<<< GIT-EXAM-2
    print(f"Square of {i} = {i ** 2}")
=======
    print(f"{i} x {i} = {i * i}")
>>>>>>> GIT-EXAM-1
```
5. Delete the three marker lines and keep one print line → **Mark as resolved** → **Commit merge**.
6. Click **Merge pull request** → **Confirm merge**.

**OR resolve in the terminal (good to show the examiner):**
```bash
git checkout GIT-EXAM-2
git pull origin GIT-EXAM-1                # CONFLICT (content): Merge conflict in program1.py
git status                                # shows program1.py as "both modified"
nano program1.py                          # delete <<<<<<< ======= >>>>>>> lines, keep one version
python3 program1.py                       # make sure it runs
git add program1.py
git commit -m "Resolve merge conflict in program1.py"
git push
```
Then refresh the PR: it now says "This branch has no conflicts" → Merge pull request → Confirm merge.

### After merging
```bash
git checkout GIT-EXAM-1
git pull
cat program1.py                           # shows the version you kept
```

## Expected Result
- master: README.md only. GIT-EXAM-1 and GIT-EXAM-2: both programs, with different versions of program1.py.
- The PR first shows a conflict in program1.py; after resolving, GIT-EXAM-2 merges into GIT-EXAM-1.

## Viva Questions
1. **What is a merge conflict?** When the same lines of a file are changed differently in two branches, so Git can't merge them automatically.
2. **How do you resolve a conflict?** Open the file, choose the correct code, remove the conflict markers, then `git add` and `git commit`.
3. **What do `<<<<<<<`, `=======`, `>>>>>>>` mean?** Start of the current branch's version, separator, end of the incoming branch's version.
4. **Why did step i alone not cause a conflict?** GIT-EXAM-1 hadn't changed program1.py since the pull, so Git could merge automatically. A conflict needs changes on both sides.
5. **git pull vs git fetch?** fetch only downloads commits; pull downloads and merges them.
6. **What does `git status` show during a conflict?** The files marked "both modified" that need resolving.
7. **How to cancel a merge with conflicts?** `git merge --abort`.
