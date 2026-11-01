# Task 9 – Containerise an AI model with Docker

## Problem Statement
a. Create a project folder with AI model files (app.py, requirements.txt)
b. Create a Dockerfile
c. Write Dockerfile instructions to set up the environment and run the model
d. Build the Docker image
e. Run the container
f. Verify the container is running
g. Test the app in the browser / API (localhost:5000)
h. Stop the container

## Theory
- **Docker**: packages an app with all its dependencies so it runs the same everywhere.
- **Image**: a read-only template built from a Dockerfile. **Container**: a running instance of an image.
- **Dockerfile instructions**: FROM (base image), WORKDIR (folder), COPY (files in), RUN (commands at build time), EXPOSE (port), CMD (command at start).
- **Port mapping** `-p 5000:5000`: host port → container port.
- **Containers vs VMs**: containers share the host OS kernel, so they are lighter and start faster.
- **The model**: Logistic Regression trained on the Iris dataset; Flask serves it as a REST API (`POST /predict`).

## Steps (Ubuntu)
```bash
sudo usermod -aG docker $USER && newgrp docker   # only if you get "permission denied"
mkdir iris-docker && cd iris-docker
nano app.py                      # a
nano requirements.txt            # a
nano Dockerfile                  # b, c
docker build -t iris-app .       # d
docker images                    # image listed
docker run -d -p 5000:5000 --name iris iris-app   # e
docker ps                        # f: STATUS "Up"
curl localhost:5000              # g (or open http://localhost:5000 in the browser)
curl -X POST localhost:5000/predict -H "Content-Type: application/json" \
     -d '{"features":[5.1,3.5,1.4,0.2]}'          # → {"species":"setosa"}
docker logs iris                 # app logs
docker stop iris                 # h
docker rm iris                   # optional cleanup
```

## Viva Questions
1. **Image vs container?** An image is the template; a container is a running instance of it.
2. **What does `-d` do?** Runs the container in the background (detached).
3. **What does `-p 5000:5000` do?** Maps host port 5000 to container port 5000.
4. **RUN vs CMD?** RUN executes while building the image; CMD runs when the container starts.
5. **Why host 0.0.0.0 in Flask?** So the app accepts connections from outside the container.
6. **How do you see running containers?** `docker ps` (including stopped ones: `docker ps -a`).
