# Task 11 – Deploy and scale the AI app on Kubernetes (Minikube)

## Problem Statement
Set up a local Kubernetes cluster with Minikube to deploy and scale the Dockerised AI application.

## Theory
- **Kubernetes (K8s)**: orchestrates containers – deployment, scaling, self-healing, load balancing.
- **Minikube**: a single-node Kubernetes cluster on a local machine.
- **Pod**: smallest unit; wraps one or more containers.
- **Deployment**: keeps the desired number of pod replicas running; replaces failed pods.
- **Service (NodePort)**: exposes pods on a port of the node, with load balancing.
- **kubectl**: command-line tool to control the cluster.
- **Scaling**: changing replicas to handle more load.

## Steps (Ubuntu)
```bash
# Install (if missing)
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube
sudo snap install kubectl --classic

minikube start --driver=docker   # don't use sudo
minikube status

# Build the image from Task 9 and load it into the cluster
cd ../Task09-Docker && docker build -t iris-app . && cd ../Task11-Minikube
minikube image load iris-app

kubectl apply -f k8s.yaml        # deploy
kubectl get deployments
kubectl get pods                 # 2 pods Running
kubectl get svc                  # iris-service listed
kubectl scale deployment iris-app --replicas=4
kubectl get pods                 # now 4 pods
minikube service iris-service --url   # open the URL in the browser

kubectl delete pod <pod-name>    # self-healing: a new pod replaces it
minikube dashboard               # optional GUI
```

## Viva Questions
1. **What is Kubernetes?** A container orchestration platform that deploys, scales and heals containers automatically.
2. **Pod vs container?** A pod wraps one or more containers that share network and storage.
3. **What does a Deployment do?** Keeps the desired number of replicas running.
4. **How do you scale?** `kubectl scale deployment iris-app --replicas=4`.
5. **Why imagePullPolicy: Never?** The image is loaded locally into Minikube, not downloaded from Docker Hub.
6. **What is a NodePort Service?** Exposes pods on a port of the cluster node so they're reachable from outside.
