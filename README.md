# Docker Full-Stack Student Information System

## 1. Project introduction

This is a simple full-stack student information application built to demonstrate how to containerize a frontend and a backend separately, connect them, and publish both images to Docker Hub.

The frontend is a static HTML/CSS/JavaScript website served by Nginx. The backend is a Python Flask REST API. Nginx forwards requests beginning with `/api/` to the backend service over a Docker network.

## 2. Objectives

- Develop a frontend user interface.
- Develop a backend REST API.
- Verify communication between frontend and backend.
- Build separate Docker images.
- Run both components as containers.
- Publish both images to Docker Hub.
- Pull the published images and run the application again.

## 3. Technologies

- Python 3.12
- Flask and Gunicorn
- HTML, CSS and JavaScript
- Nginx
- Docker and Docker Compose
- Docker Hub
- Ubuntu and Visual Studio Code

## 4. Directory structure

```text
docker-fullstack-app/
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── index.html
│   ├── nginx.conf
│   └── Dockerfile
├── .dockerignore
├── docker-compose.yml
└── README.md
```

## 5. How the application works

1. The browser loads the frontend from Nginx on port 8080.
2. The user selects **Load students from backend**.
3. JavaScript sends `GET /api/students` to the Nginx frontend.
4. Nginx proxies that request to the `backend` service on port 5000 using the shared Docker network.
5. Flask returns JSON data.
6. JavaScript displays the student records in the browser.

The frontend does not need to know the backend container's IP address. Docker's internal DNS resolves the service name `backend`.

## 6. Backend Dockerfile explanation

- `FROM python:3.12-slim`: starts from a smaller Python 3.12 base image.
- `WORKDIR /app`: sets `/app` as the working directory.
- `ENV PYTHONDONTWRITEBYTECODE=1`: prevents Python from writing `.pyc` files.
- `ENV PYTHONUNBUFFERED=1`: sends Python logs directly to the container output.
- `COPY requirements.txt .`: copies dependency definitions first, helping Docker reuse the dependency layer when application code changes.
- `RUN pip install --no-cache-dir -r requirements.txt`: installs Flask, Flask-CORS and Gunicorn without retaining pip's download cache.
- `COPY app.py .`: copies the backend source code.
- `EXPOSE 5000`: documents the port used by the API.
- `CMD [...]`: starts the API with Gunicorn, a production-oriented WSGI server.

## 7. Frontend Dockerfile explanation

- `FROM nginx:1.27-alpine`: uses a lightweight Nginx image.
- `COPY index.html ...`: copies the website into Nginx's web root.
- `COPY nginx.conf ...`: installs the Nginx configuration that serves the website and proxies `/api/` requests to the backend.
- `EXPOSE 80`: documents the HTTP port.

## 8. Check Docker

```bash
docker --version
docker compose version
docker info
```

If `docker info` cannot connect to the Docker daemon, start Docker before continuing.

## 9. Build and run both components locally

From the project root:

```bash
docker compose build
docker compose up -d
docker compose ps
```

Open `http://localhost:8080` in a browser and select **Load students from backend**.

Test the API through the frontend proxy:

```bash
curl http://localhost:8080/api/health
curl http://localhost:8080/api/students
```

Expected health response includes:

```json
{
  "status": "success",
  "message": "Backend API is running inside a Docker container."
}
```

View logs:

```bash
docker compose logs
docker compose logs backend
docker compose logs frontend
```

Stop and remove the Compose containers and network after testing:

```bash
docker compose down
```

This does not delete the built images.

## 10. Build images separately

Run these commands from the project root:

```bash
docker build -t student-backend:1.0 ./backend
docker build -t student-frontend:1.0 ./frontend
docker images
```

## 11. Create Docker Hub repositories

1. Sign in at https://hub.docker.com/.
2. Create a repository named `student-backend`.
3. Create a second repository named `student-frontend`.
4. Choose Public if the assignment requires publicly accessible images.
5. Record both repository URLs for the submission.

## 12. Authenticate with Docker Hub

Run:

```bash
docker login
```

Complete the browser/device authentication flow or enter your Docker Hub credentials in the terminal prompt. Never put a password or access token in source code, Dockerfiles, README files, or screenshots.

## 13. Tag images

Replace `YOUR_DOCKERHUB_USERNAME` with your actual Docker Hub username:

```bash
docker tag student-backend:1.0 YOUR_DOCKERHUB_USERNAME/student-backend:1.0
docker tag student-frontend:1.0 YOUR_DOCKERHUB_USERNAME/student-frontend:1.0
```

A tag gives the local image the full repository name and version expected by Docker Hub.

## 14. Push images

```bash
docker push YOUR_DOCKERHUB_USERNAME/student-backend:1.0
docker push YOUR_DOCKERHUB_USERNAME/student-frontend:1.0
```

Verify that both repositories show the `1.0` tag on Docker Hub.

Repository links:

- `https://hub.docker.com/r/YOUR_DOCKERHUB_USERNAME/student-backend`
- `https://hub.docker.com/r/YOUR_DOCKERHUB_USERNAME/student-frontend`

## 15. Pull and run the published images

First stop the Compose application if it is running:

```bash
docker compose down
```

Pull both published images:

```bash
docker pull YOUR_DOCKERHUB_USERNAME/student-backend:1.0
docker pull YOUR_DOCKERHUB_USERNAME/student-frontend:1.0
```

Create a Docker network:

```bash
docker network create student-network
```

Run the backend with the network alias `backend`:

```bash
docker run -d --name student-backend --network student-network --network-alias backend YOUR_DOCKERHUB_USERNAME/student-backend:1.0
```

Run the frontend and publish port 8080:

```bash
docker run -d --name student-frontend --network student-network -p 8080:80 YOUR_DOCKERHUB_USERNAME/student-frontend:1.0
```

Check the containers:

```bash
docker ps
```

Open `http://localhost:8080`, select **Load students from backend**, and confirm that student records appear.

Test the API:

```bash
curl http://localhost:8080/api/health
curl http://localhost:8080/api/students
```

After collecting evidence, stop and remove these test containers and network:

```bash
docker rm -f student-frontend student-backend
docker network rm student-network
```

## 16. Evidence checklist

Include the following in the assignment submission:

- [ ] Complete source code and project directory.
- [ ] Backend Dockerfile.
- [ ] Frontend Dockerfile.
- [ ] Screenshot of `docker compose ps` showing both running containers.
- [ ] Screenshot of the application in the browser displaying records returned by the backend.
- [ ] Screenshot of `docker images` showing both images.
- [ ] Screenshot of both Docker Hub repositories and their `1.0` tags.
- [ ] Screenshot of successful `docker push` output for both images.
- [ ] Screenshot of successful `docker pull` output for both images.
- [ ] Screenshot showing the application working after pulling and running the published images.
- [ ] The two Docker Hub repository links.

## 17. Expected result

The frontend and backend run in separate containers. The browser displays student records returned by the Flask API. Both Docker images are published to separate Docker Hub repositories and can be pulled and run again.

---

**Security note:** Do not commit Docker Hub passwords, access tokens, or other credentials to this project.
