# Task 6 – Clone, Fork, Feature Branch and Pull Request (Git Bash)

## Problem Statement
a. Clone https://github.com/KalyanM45/AI-ProjectGallery.git
b. Demonstrate that branch creation is disallowed for this repository
c. Fork the repository
d. Create a feature branch GIT-EXAM
e. Change/add code in the branch
f. Submit a pull request for review
g. Resolve merge conflicts and incorporate feedback

## Theory
- **Clone**: download a full copy of a remote repo (`git clone <url>`).
- **Write access**: only the owner/collaborators can push branches to a repo. Others get "Permission denied (403)".
- **Fork**: your own copy of someone else's repo on GitHub, where you have full access.
- **upstream** = the original repo; **origin** = your fork.
- **Feature branch**: a separate branch for one change.
- **Pull Request**: asks the original owner to merge your branch; they review, comment, approve.
- **Syncing a fork**: `git fetch upstream` + `git merge upstream/main` brings the latest original code into your branch (this is where conflicts get resolved).

## Steps (Ubuntu terminal)

### a. Clone
```bash
git config --global user.name "shardSM"
git config --global user.email "shardulmarathe374@gmail.com"
git clone https://github.com/KalyanM45/AI-ProjectGallery.git
cd AI-ProjectGallery
git branch -a                    # shows the default branch (main or master)
```

### b. Show that branch creation is disallowed
```bash
git checkout -b GIT-EXAM
git push origin GIT-EXAM         # ERROR: Permission denied / 403 → can't create branches on this repo
```
A local branch can be created, but it can't be pushed to someone else's repo.

### c. Fork
On GitHub, open the repo → click **Fork** → Create fork. You now have `github.com/shardSM/AI-ProjectGallery`.

### d. Point the clone to your fork
```bash
git remote rename origin upstream
git remote add origin https://github.com/shardSM/AI-ProjectGallery.git
git remote -v                    # origin = your fork, upstream = original
git checkout GIT-EXAM            # (already created in step b)
```

### e. Add your code
```bash
nano my_contribution.py          # paste the code, Ctrl+O, Enter, Ctrl+X
python3 my_contribution.py
git add my_contribution.py
git commit -m "Add keyword-based sentiment checker"
git push -u origin GIT-EXAM      # works now – it's your fork
```

### f. Pull Request
On your fork, click **Compare & pull request** → base repository: KalyanM45/AI-ProjectGallery, base: main (or master) ← compare: GIT-EXAM → title + description → **Create pull request**.

### g. Conflicts and feedback
```bash
git fetch upstream
git merge upstream/main          # use upstream/master if that's the default branch
git status                       # conflicted files show as "both modified"
nano <conflicted-file>           # remove <<<<<<< ======= >>>>>>> and keep the right code
git add .
git commit -m "Resolve merge conflicts with upstream"
git push                         # the PR updates automatically
```
For review feedback: make the change → commit → push to GIT-EXAM → reply to the comment on the PR.

## Expected Result
- Pushing a branch to the original repo fails (403).
- The fork has a GIT-EXAM branch with my_contribution.py and an open PR to the original repo.

## Viva Questions
1. **Clone vs fork?** Clone copies a repo to your computer; fork copies it to your GitHub account.
2. **Why couldn't we create a branch?** We don't have write access to someone else's repository.
3. **What are origin and upstream?** origin = your fork, upstream = the original repo.
4. **How do you keep a fork updated?** `git fetch upstream` + `git merge upstream/main`.
5. **What happens to a PR when you push more commits?** It updates automatically.
6. **Who can merge the PR?** Only the owner or collaborators of the original repo.
