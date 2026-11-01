# Task 5 – Branching and .gitignore using GitHub Desktop

## Problem Statement
Same as Task 4 (a–h), but performed with GitHub Desktop instead of the terminal.

## Theory
- **GitHub Desktop**: a graphical app for Git. It runs the same Git commands (init, commit, push, branch) through buttons.
- Terminal vs Desktop: `git init` = New repository, `git add` + `git commit` = Commit button, `git push` = Push origin, `git checkout -b` = New branch.
- .gitignore works the same way: ignored files don't appear in the Changes tab.

## Install on Ubuntu (community build – only if not installed in the lab)
```bash
wget -qO - https://apt.packages.shiftkey.dev/gpg.key | gpg --dearmor | sudo tee /usr/share/keyrings/shiftkey-packages.gpg > /dev/null
sudo sh -c 'echo "deb [arch=amd64 signed-by=/usr/share/keyrings/shiftkey-packages.gpg] https://apt.packages.shiftkey.dev/ubuntu/ any main" > /etc/apt/sources.list.d/shiftkey-packages.list'
sudo apt update && sudo apt install github-desktop
```
If it can't be installed, ask the examiner whether to use the terminal steps from Task 4.

## Steps
1. Open GitHub Desktop → **File → Options → Accounts → Sign in** (account shardSM).
2. **a.** File → **New repository** → name `ds-project-5` → choose a local path → tick "Initialize with README" → **Create repository**.
3. **b.** Click **Publish repository** → Publish. It is now on GitHub.
4. **c.** **Branch → New branch** → `GIT-EXAM-1` → Create branch.
5. Open the folder (Repository → **Show in Files**) and create `program2.py` (palindrome code).
6. **d.** Create `program1.py` (squares code).
7. **e.** Both files appear under **Changes** → summary `Add palindrome and squares programs` → **Commit to GIT-EXAM-1** → **Publish branch**. Check GitHub.
8. **f.** In the folder, create `IGNORE/` with `test1.txt` and `test2.txt` → they appear under Changes.
9. **g.** Right-click `IGNORE/test1.txt` in Changes → **Ignore folder (IGNORE)**. Or Repository → **Repository settings → Ignored files** → type `IGNORE/` → Save. The IGNORE files disappear from Changes and `.gitignore` appears.
10. **h.** Commit `.gitignore` → **Push origin** → on GitHub, branch GIT-EXAM-1 shows .gitignore but NO IGNORE folder.

## Expected Result
GitHub shows README, program1.py, program2.py and .gitignore on GIT-EXAM-1. The IGNORE folder exists only on the computer.

## Viva Questions
1. **What is GitHub Desktop?** A GUI client for Git and GitHub.
2. **Which Git commands does the Commit button run?** `git add` + `git commit`.
3. **What does Publish repository do?** Creates the repo on GitHub and pushes it (`git remote add` + `git push -u`).
4. **How do you ignore a folder in GitHub Desktop?** Right-click → Ignore folder, or Repository settings → Ignored files.
5. **Terminal or GUI – which is better?** Same Git underneath; the GUI is easier for beginners, the terminal is faster and scriptable.
