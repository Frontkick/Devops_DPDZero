# 🐳 DevOps Assignment – Multi-Service App with Reverse Proxy

This project sets up a simple system with:

- Two backend services (Service 1 in Go, Service 2 in Python/Flask)
- An Nginx reverse proxy that routes traffic based on URL path
- Docker Compose for container orchestration

---

## 📁 Project Structure


```
.
├── docker-compose.yml
├── nginx
│ ├── default.conf
│ └── Dockerfile
├── service_1
│ ├── main.go
│ ├── Dockerfile
│ |── go.mod
| └── README.md
├── service_2
│ ├── app.py
│ ├── Dockerfile
│ ├── pyproject.toml
│ ├── uv.lock
| └── README.md
└── README.md
```

---


---

## 🧠 Features

| Feature                    | Description                                                                 |
|---------------------------|-----------------------------------------------------------------------------|
| 🐳 Dockerized Services     | Each service runs in a container                                             |
| 🔁 Reverse Proxy (Nginx)   | Routes `/service1` to Service 1 and `/service2` to Service 2                |
| 📡 Health Check (Ping)     | Each service exposes a `/ping` endpoint for health                          |
| 📜 Logging                 | Nginx logs each request with path and timestamp                             |
| 🔍 Clean Bridge Networking | All services use Docker bridge network (no host networking)                 |

---

## 🚀 Getting Started

<!-- ### ✅ Prerequisites

- Docker
- Docker Compose
- Go 1.22+ (for local dev of Service 1)
- Python 3.10+ (for local dev of Service 2)

--- -->

### 🔧 Setup

1. Clone this repo:
   ```bash
   git clone https://github.com/Frontkick/Devops_DPDZero
   cd Devops_DPDZero
   docker compose up --build

### 🌍  Access Services
#### Service 1 (Go)

    http://localhost:8080/service1/ping →    { "status": "ok", "service": "1" }

    http://localhost:8080/service1/hello →   { "message": "Hello from Service 1" }

#### Service 2 (Flask)

    http://localhost:8080/service2/ping →    { "status": "ok", "service": "2" }

    http://localhost:8080/service2/hello →    { "message": "Hello from Service 2" }



##    🌟 Bonus Features Implemented
✅ Automated Health Checks

- Docker performs periodic health checks by calling the `/ping` endpoint (e.g., every 30s)
- Ensures both services are running and healthy


✅ Request Logging

   - Nginx logs all incoming requests with timestamp and request path



✅ Bridge Networking Only

   - No host mode used
 
   - All containers communicate over Docker's bridge network

✅ Clean Modular Docker Setup

   - Separated Dockerfiles for dev and prod

   - Clean service separation with clear folder structure