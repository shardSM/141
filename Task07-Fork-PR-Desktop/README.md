# Task 7 – Clone, Fork, Feature Branch and Pull Request (GitHub Desktop)

## Problem Statement
a. Clone https://github.com/KalyanM45/Spam-EmailDetection.git
b. Demonstrate that branch creation is disallowed for this repository
c. Fork the repository
d. Create a feature branch GIT-EXAM
e. Change/add code in the branch
f. Submit a pull request for review
g. Resolve merge conflicts and incorporate feedback

## Theory
- **Clone**: download a full copy of a remote repository.
- **Write access**: only the owner and collaborators can push branches.
- **Fork**: your own copy of someone else's repo on GitHub with full access.
- **Feature branch**: a branch for one change, keeping main clean.
- **Pull Request**: a request to the original owner to merge your changes; reviewers comment and approve.
- **Merge conflict**: the same lines changed in both places; fixed by hand.

## Install GitHub Desktop on Ubuntu (community build, if not installed)
```bash
wget -qO - https://apt.packages.shiftkey.dev/gpg.key | gpg --dearmor | sudo tee /usr/share/keyrings/shiftkey-packages.gpg > /dev/null
sudo sh -c 'echo "deb [arch=amd64 signed-by=/usr/share/keyrings/shiftkey-packages.gpg] https://apt.packages.shiftkey.dev/ubuntu/ any main" > /etc/apt/sources.list.d/shiftkey-packages.list'
sudo apt update && sudo apt install github-desktop
```

## Steps
a. Sign in (File → Options → Accounts, account shardSM) → **File → Clone repository → URL** → `https://github.com/KalyanM45/Spam-EmailDetection.git` → Clone.
b. **Branch → New branch** → `GIT-EXAM` → **Publish branch** → Desktop says you don't have write access and offers to fork. This proves branch creation is disallowed.
c. Choose **Fork this repository** → "To contribute to the parent project" → Continue. (Or click Fork on the GitHub website.)
d. Make sure the current branch is `GIT-EXAM` (create it again if needed).
e. Repository → Show in Files → add `add_feature.py` → it appears under **Changes** → summary `Add keyword spam checker` → **Commit to GIT-EXAM** → **Push origin / Publish branch**.
f. **Branch → Create Pull Request** → GitHub opens → base: original repo main ← compare: GIT-EXAM → **Create pull request**.
g. Conflicts: **Branch → Update from upstream/main** → Desktop lists conflicted files → **Open in editor** → remove `<<<<<<< ======= >>>>>>>`, keep correct code → **Continue merge** → Push origin. The PR updates automatically. For feedback: edit → commit → push → reply on the PR.

## Terminal equivalent (if GitHub Desktop is unavailable)
```bash
git clone https://github.com/KalyanM45/Spam-EmailDetection.git
cd Spam-EmailDetection
git checkout -b GIT-EXAM
git push origin GIT-EXAM                 # 403 → no permission
# Fork on GitHub, then:
git remote rename origin upstream
git remote add origin https://github.com/shardSM/Spam-EmailDetection.git
nano add_feature.py
git add . && git commit -m "Add keyword spam checker"
git push -u origin GIT-EXAM              # then open the PR on GitHub
```

## Viva Questions
1. **Why does Desktop offer to fork?** We have no write access to the original repo.
2. **Fork vs branch?** A branch is inside one repo; a fork is a separate copy of the whole repo under your account.
3. **What does "Update from upstream" do?** Merges the latest original code into your branch.
4. **How does a reviewer give feedback?** Comments on the PR's Files changed tab; you push fixes to the same branch.
