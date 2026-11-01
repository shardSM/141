# VSEC Practical Exam – DevOps & Git

Each folder contains the code files and a README with the aim, theory, steps (Ubuntu) and viva questions.

| Task | Topic |
|------|-------|
| [01](Task01-Git-Basics) | Git basics – init, push, branch, diff |
| [02](Task02-Git-PR) | Git branches + Pull Request |
| [03](Task03-Git-Conflicts) | Multiple branches, pull and merge conflicts |

## One-time setup (run first on the lab machine)
```bash
git config --global user.name "shardSM"
git config --global user.email "shardulmarathe374@gmail.com"
git config --global credential.helper 'cache --timeout=3600'
```
The last line remembers your token for 1 hour, so you don't paste it on every push.
