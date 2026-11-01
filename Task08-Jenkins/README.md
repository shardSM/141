# Task 8 – Jenkins Pipeline triggered from GitHub

## Problem Statement
a. Create a GitHub repository and upload project files
b. Install and launch Jenkins (http://localhost:8080)
c. Install plugins (Git, GitHub, Pipeline)
d. Create a Pipeline job
e. Configure Pipeline script from SCM with the GitHub repo URL
f. Add a Jenkinsfile to the repository
g. Configure a build trigger (Poll SCM / Webhook)
h. Push code changes to GitHub
i. Verify that Jenkins triggers the build automatically

## Theory
- **Jenkins**: open-source automation server for CI/CD.
- **CI (Continuous Integration)**: every push is automatically built and tested.
- **Pipeline**: the build process written as code in a `Jenkinsfile` (pipeline → stages → steps).
- **agent any**: run on any available Jenkins machine.
- **SCM**: Jenkins reads the Jenkinsfile from the Git repo.
- **Poll SCM**: Jenkins checks the repo on a schedule (`* * * * *` = every minute; cron format: minute hour day month weekday).
- **Webhook**: GitHub notifies Jenkins instantly; needs a public URL, so Poll SCM is used on localhost.

## Steps (Ubuntu)
### a, f. Repo with the files
```bash
git config --global user.name "shardSM"
git config --global user.email "shardulmarathe374@gmail.com"
mkdir jenkins-demo && cd jenkins-demo && git init && git branch -M main
nano hello.py                    # paste hello.py
nano Jenkinsfile                 # paste Jenkinsfile
git add . && git commit -m "Add Jenkins pipeline"
git remote add origin https://github.com/shardSM/jenkins-demo.git   # create this repo on GitHub first
git push -u origin main
```
### b. Install and launch Jenkins (as your own user)
```bash
sudo apt install -y openjdk-17-jdk
wget https://get.jenkins.io/war-stable/latest/jenkins.war
java -jar jenkins.war --httpPort=8080      # keep this terminal open
```
### c. Setup
Open http://localhost:8080 → paste the admin password (printed in the terminal, also in `~/.jenkins/secrets/initialAdminPassword`) → **Install suggested plugins** (includes Git, GitHub, Pipeline) → create admin user. Check: Manage Jenkins → Plugins → Installed.
### d, e. Pipeline job
New Item → `jenkins-demo` → **Pipeline** → OK → Definition **Pipeline script from SCM** → SCM **Git** → Repository URL `https://github.com/shardSM/jenkins-demo.git` → Branch `*/main` → Script Path `Jenkinsfile` → Save.
### g. Trigger
Build Triggers → tick **Poll SCM** → Schedule `* * * * *` → Save → click **Build Now** once (the trigger activates after the first build).
### h, i. Push and verify
```bash
nano hello.py                    # change the last print line
git commit -am "Update message" && git push
```
Within about a minute a new build starts by itself → open it → **Console Output** shows the new message.

## Viva Questions
1. **What is Jenkins?** An automation server used to build, test and deploy code automatically.
2. **What is a Jenkinsfile?** A text file defining the pipeline as code, stored in the repo.
3. **Poll SCM vs webhook?** Polling checks on a schedule; a webhook gets an instant notification from GitHub.
4. **What does `* * * * *` mean?** Every minute (cron syntax).
5. **Why no input() in the script?** Jenkins can't type input, so the build would hang.
6. **Where do you see build output?** Build → Console Output.
