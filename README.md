# HumanizeIQ FastAPI Microservice

## Overview
This is a FastAPI microservice with a protected endpoint and Docker support. The project follows a strict Git workflow and is designed for easy deployment and testing.

---

## Features
- **Endpoint:** `/aman/test` (GET)
- **Authentication:** HTTP Bearer token required for all endpoints
- **Dockerized:** Easily build and run as a container
- **Git Workflow:** All code changes go to `dev` branch; `main` is protected and only updated via Pull Requests

---

## API Usage

### Authentication
All endpoints require a Bearer token. The default token is:

```
supersecrettoken
```

### Example Request
```bash
curl -H "Authorization: Bearer supersecrettoken" http://localhost:8000/aman/test
```

---

## Local Development

1. **Install dependencies:**
   ```bash
   pip install fastapi uvicorn
   ```
2. **Run the app:**
   ```bash
   uvicorn app:app --reload --port 8000
   ```

---

## Docker Usage

### Build the Docker Image
```bash
docker build -t docker/humanize/aman .
```

### Run the Container Locally
```bash
docker run -d -p 8000:8000 docker/humanize/aman
```

### Test the Endpoint
```bash
curl -H "Authorization: Bearer supersecrettoken" http://localhost:8000/aman/test
```

---

## DockerHub Deployment

1. **Login to DockerHub:**
   ```bash
   docker login
   ```
2. **Tag the image:**
   ```bash
   docker tag docker/humanize/aman <your-dockerhub-username>/humanize-aman:latest
   ```
3. **Push to DockerHub:**
   ```bash
   docker push <your-dockerhub-username>/humanize-aman:latest
   ```

---

## Git Workflow

- **Branches:**
  - `main`: Protected, production-ready code only
  - `dev`: All development and feature work
- **Rules:**
  - All code must be pushed to `dev`
  - No direct pushes to `main` allowed
  - All changes to `main` must come via Pull Requests (PRs) from `dev`
  - Enable branch protection for `main` in your repository settings

---

## Contributing
1. Create a feature branch from `dev`
2. Commit and push your changes to `dev`
3. Open a Pull Request to merge `dev` into `main`
4. Wait for review and approval before merging

---

## Notes
- Update the Bearer token and authentication logic for production use.
- For more endpoints or features, follow the same authentication pattern. 