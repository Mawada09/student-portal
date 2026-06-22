# Week 3 Docker Report - Student Portal API

## 1. Overview
This report documents the Dockerization of the Student Portal API built in Weeks 1 & 2.
The app was containerized using Docker and Docker Compose, with a PostgreSQL database running as a separate container.

## 2. Files Created

| File | Purpose |
|------|---------|
| `Dockerfile` | Packages the FastAPI app into a container image |
| `docker-compose.yml` | Orchestrates the API + PostgreSQL containers |
| `.dockerignore` | Excludes unnecessary files from the image |
| `requirements.txt` | Pins all Python dependencies for the container |

## 3. Architecture
┌─────────────────────────────────────┐

│         Docker Network              │

│                                     │

│  ┌──────────────┐  ┌─────────────┐ │

│  │  API Container│  │ DB Container│ │

│  │  FastAPI:8000 │◄─►│ Postgres:  │ │

│  │               │  │ 5432       │ │

│  └──────────────┘  └─────────────┘ │

└─────────────────────────────────────┘
## 4. How to Run

```bash
# Start all containers
docker compose up --build

# Stop all containers
docker compose down

# Stop and remove volumes
docker compose down -v
```

## 5. API Tested in Docker

| Endpoint | Method | Status |
|----------|--------|--------|
| `/` | GET | ✅ 200 OK |
| `/students` | POST | ✅ 201 Created |
| `/students/{id}` | GET | ✅ 200 OK |
| `/students` | GET | ✅ 200 OK |
| `/students/{id}` | PUT | ✅ 200 OK |
| `/students/{id}` | DELETE | ✅ 200 OK |

## 6. Summary

| Item | Result |
|------|--------|
| Dockerfile created | ✅ |
| docker-compose.yml created | ✅ |
| API container running | ✅ |
| PostgreSQL container running | ✅ |
| Containers communicate | ✅ |
| Data persists via volumes | ✅ |
| API accessible at localhost:8000/docs | ✅ |
| Pushed to GitHub | ✅ |

**Week 3 Deliverable Status: COMPLETE ✅**