# Enterprise EV Charging Management API

An asynchronous, containerized backend microservice designed to manage, simulate, and track Electric Vehicle (EV) charging sessions across a fleet of charging stations.

## Architecture & Tech Stack

This project implements an enterprise-grade, distributed architecture:

- **Web Framework:** FastAPI (Python) for high-performance, strictly-typed HTTP routing.
- **Database:** PostgreSQL for robust, relational data storage.
- **ORM:** SQLAlchemy with Pydantic for data validation and serialization.
- **Message Broker:** Redis for high-speed, in-memory task queuing.
- **Background Workers:** Celery & Celery Beat for asynchronous job execution and scheduling.
- **Infrastructure:** Fully containerized using Docker & Docker Compose for reproducible environments.

## Core Features

- **Station Management:** Register and track the status of physical charging stations (`Available`, `Occupied`, `Faulted`).
- **Session Tracking:** Monitor active charging sessions, logging UTC timestamps and calculating total charge duration dynamically.
- **Strict Data Validation:** Business logic prevents physically impossible scenarios (e.g., ending battery levels lower than starting levels, or exceeding 100%).
- **Automated Charging Simulator (Asynchronous):** A Celery background worker runs continuously, polling the database and automatically incrementing the battery levels of all active sessions, seamlessly mimicking physical hardware behavior without blocking the main API threads.

## Local Development & Setup

Prerequisites: You must have [Docker](https://www.docker.com/) and Docker Compose installed.

1. **Clone the repository:**

   ```bash
   git clone <your-github-repo-url>
   cd ev_charging_manager

   ```

2. **Boot the infrastructure**
   docker compose up --build

   this command spins up four interconnected containers: FastAPI server, the PostgresSQL database, the Redis message broker, and the Celery background worker

3 **Access the API**
once the container is running, navigate to the interactive FastAPI UI to test the endpoints
http://localhost:8000/docs

V2 Roadmap & Future Enhancements
The next phase of this project will focus on user-facing applications and cloud deployment: - Role-Based Access Control Frontend UI: Developing a web dashboard where Authorized Engineers/personel can view deep system analytics, full session histories, and backend diagnostics. - Providing a streamlined view for Standard Employees/Users to check station availability, physical locations, and current battery levels

        - Cloud Development: Migrate the Dockerized infrastrure from local development to a cloud provider to expose a public URL for remote access across multiple devices

Developed by Ernest Crudup Jr
