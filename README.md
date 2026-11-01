# VSEC Practical Exam – DevOps & Git

Each folder contains the code files and a README with the problem statement, theory, steps (Ubuntu) and viva questions.

| Task | Topic |
|------|-------|
| [01](Task01-Git-Basics) | Git basics – init, push, branch, diff |
| [02](Task02-Git-PR) | Git branches + Pull Request |
| [03](Task03-Git-Conflicts) | Multiple branches, pull and merge conflicts |
| [04](Task04-Gitignore) | Ignoring files with .gitignore |
| [05](Task05-GitHub-Desktop) | Branching and .gitignore with GitHub Desktop |
| [06](Task06-Fork-PR) | Clone, fork, feature branch and PR (Git Bash) |
| [07](Task07-Fork-PR-Desktop) | Clone, fork, feature branch and PR (GitHub Desktop) |
| [08](Task08-Jenkins) | Jenkins pipeline triggered from GitHub |
| [09](Task09-Docker) | Containerise an AI model with Docker |
| [10](Task10-Docker-Compose) | Multi-container app with Docker Compose |
| [11](Task11-Minikube) | Deploy and scale on Kubernetes (Minikube) |
| [12](Task12-CICD) | CI/CD – Jenkins + Docker + Kubernetes |

## One-time setup (run first on the lab machine)
```bash
git config --global user.name "shardSM"
git config --global user.email "shardulmarathe374@gmail.com"
git config --global pull.rebase false
git config --global credential.helper 'cache --timeout=3600'
```
- `pull.rebase false` avoids the "divergent branches" error when pulling.
- The credential helper remembers your token for 1 hour.
- Use `python3` to run programs on Ubuntu.
- Create each repo on GitHub BEFORE pushing, otherwise you get "Repository not found".

## Ports used
| Port | Used by |
|------|---------|
| 8080 | Jenkins |
| 5000 | AI model API |
| 3000 | Frontend (Task 10) |
