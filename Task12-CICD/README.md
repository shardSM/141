# Task 12 – CI/CD pipeline: Jenkins + Docker + Kubernetes

## Problem Statement
Set up a CI/CD pipeline with Jenkins, Docker and Kubernetes to automate development-to-deployment of the AI model.

## Theory
- **CI/CD**: Continuous Integration (auto build + test on every push) and Continuous Delivery/Deployment (auto release).
- **Flow**: push to GitHub → Jenkins detects change → Docker builds image → test → image loaded into Minikube → Kubernetes rolling update.
- **Image tag BUILD_NUMBER**: every build is a new version, which allows rollback.
- **Rolling update**: Kubernetes replaces pods gradually, so there's no downtime.
- **Rollback**: `kubectl rollout undo deployment/iris-app`.

## Steps (Ubuntu)
### 1. Repo
```bash
git config --global user.name "shardSM"
git config --global user.email "shardulmarathe374@gmail.com"
mkdir ai-cicd && cd ai-cicd && git init && git branch -M main
# add app.py, requirements.txt, Dockerfile, k8s.yaml, Jenkinsfile (from this folder)
git add . && git commit -m "CI/CD pipeline"
git remote add origin https://github.com/shardSM/ai-cicd.git    # create on GitHub first
git push -u origin main
```
### 2. Start Minikube and Jenkins AS YOUR USER (separate terminals, keep both open)
```bash
minikube start --driver=docker
java -jar jenkins.war --httpPort=8080
```
### 3. Jenkins job
New Item → `ai-cicd` → Pipeline → **Pipeline script from SCM** → Git → `https://github.com/shardSM/ai-cicd.git` → Branch `*/main` → Script Path `Jenkinsfile` → tick **Poll SCM** `* * * * *` → Save → **Build Now**.
### 4. Verify
Stage View shows Build → Test → Load into Minikube → Deploy turning green.
```bash
kubectl get pods
kubectl describe deployment iris-app | grep Image   # iris-app:<build number>
```
### 5. Automatic deployment
Change the home message in app.py → commit → push → Jenkins builds by itself → `minikube service iris-service --url` shows the new message.

## Common problems
- **docker: permission denied** → `sudo usermod -aG docker $USER` then log out/in (or `newgrp docker`).
- **kubectl/minikube not found inside Jenkins** → Jenkins must run as your user (`java -jar jenkins.war`), not as a system service.

## Viva Questions
1. **What is CI/CD?** Automating build, test and deployment whenever code changes.
2. **What does each tool do here?** Jenkins = automation, Docker = packaging, Kubernetes = running and scaling.
3. **Why tag images with BUILD_NUMBER?** Each build is a unique version, so you can track and roll back.
4. **What is a rolling update?** Pods are replaced gradually with the new version, avoiding downtime.
5. **How do you roll back?** `kubectl rollout undo deployment/iris-app`.
6. **What triggers the pipeline?** Poll SCM detects a new commit on GitHub.
