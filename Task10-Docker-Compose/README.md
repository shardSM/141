# Task 10 – Multi-container AI app with Docker Compose

## Problem Statement
Use Docker Compose to orchestrate separate containers for the AI model, the database and the frontend of a web-based AI application.

## Theory
- **Docker Compose**: defines and runs multi-container apps from one YAML file (`docker-compose.yml`).
- **Service**: one container definition (model, db, frontend).
- **build vs image**: `build` makes an image from a Dockerfile; `image` uses a ready-made one (postgres, nginx).
- **depends_on**: start order between services.
- **Network**: Compose puts all services on one network; they reach each other by service name (e.g. host `db`).
- **Volume**: persistent storage so database data isn't lost when containers stop.
- **Microservices**: each part runs and scales independently.

## Folder structure
```
Task10-Docker-Compose/
├── docker-compose.yml
├── model/      (app.py, requirements.txt, Dockerfile – from Task 9)
└── frontend/   (index.html)
```

## Steps (Ubuntu)
```bash
cd Task10-Docker-Compose
docker compose up -d --build     # build and start all 3 (older systems: docker-compose)
docker compose ps                # model, db, frontend all "running"
```
- Open http://localhost:3000 → click **Predict** → species appears (frontend → model API).
- API directly: http://localhost:5000
```bash
docker compose exec db psql -U user -d aidb -c "\l"   # database is running
docker compose logs model        # logs of one service
docker compose down              # stop and remove all containers
```

## Viva Questions
1. **What is Docker Compose?** A tool to define and run multi-container applications with one YAML file.
2. **Command to start everything?** `docker compose up -d`.
3. **How do containers talk to each other?** Through Compose's network, using service names as hostnames.
4. **Why use a volume for the database?** So data persists when the container is removed.
5. **What does depends_on do?** Controls the start order of services.
6. **Port mapping "3000:80"?** Host port 3000 → nginx's port 80 in the container.
