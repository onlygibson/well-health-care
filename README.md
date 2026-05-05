# Well Health Care - Full Stack Healthcare App

A full-stack healthcare appointment application built with a frontend, backend API, Docker, Jenkins CI, Kubernetes, and Trivy security scanning.

## Project Overview

This project demonstrates a complete DevOps workflow for building, containerizing, validating, deploying, and hardening a healthcare web application.

The application includes:

- Frontend healthcare appointment page
- Backend API service
- Dockerfiles for frontend and backend
- Docker Compose file for local container testing
- Jenkins pipeline for CI validation
- Kubernetes manifests for deployment
- Trivy scanning for Docker and Kubernetes security checks

## Tech Stack

- HTML
- CSS
- JavaScript
- Python
- Docker
- Docker Compose
- Jenkins
- Kubernetes
- kubectl
- Trivy
- Git/GitHub

## Project Structure

```text
well-health-care/
├── backend/
│ ├── Dockerfile
│ ├── main.py
│ └── requirements.txt
├── frontend/
│ ├── Dockerfile
│ ├── index.html
│ ├── script.js
│ └── style.css
├── kubernetes-manifests/
│ ├── namespace.yaml
│ ├── backend-deployment.yaml
│ ├── backend-service.yaml
│ ├── frontend-deployment.yaml
│ └── frontend-service.yaml
├── docker-compose.yml
├── Jenkinsfile
└── README.md
```

## Frontend

The frontend is a healthcare appointment web page where users can view available healthcare services and submit appointment information.

Frontend features:

- Healthcare services section
- Appointment booking form
- Responsive user interface
- Nginx-based Docker image
- Kubernetes NodePort Service for local access

## Backend

The backend provides the API layer for the healthcare appointment application.

Backend features:

- Python API service
- Health check endpoint
- Appointment submission support
- Containerized backend service
- Internal Kubernetes ClusterIP Service

## Docker

The application includes separate Dockerfiles for the frontend and backend.

Build the backend image:

```bash
docker build -t well-health-backend:1.0 ./backend
```

Build the frontend image:

```bash
docker build -t well-health-frontend:1.0 ./frontend
```

## Docker Compose

Run the application locally using Docker Compose:

```bash
docker compose up --build
```

## Jenkins CI Pipeline

A Jenkins pipeline was created to validate the project structure and configuration files before deployment.

The pipeline validates:

- Backend Dockerfile
- Frontend Dockerfile
- Docker Compose file
- Required Dockerfile instructions
- Project readiness before deployment

## Kubernetes Deployment

The application is deployed to Kubernetes using manifest files.

Apply all Kubernetes resources:

```bash
kubectl apply -f kubernetes-manifests/
```

Check pods:

```bash
kubectl get pods -n well-health-care
```

Check services:

```bash
kubectl get svc -n well-health-care
```

Check all Kubernetes resources:

```bash
kubectl get all -n well-health-care
```

Access the frontend locally:

```text
http://localhost:30082
```

## Kubernetes Resources

The Kubernetes setup includes:

- Namespace: `well-health-care`
- Backend Deployment
- Backend ClusterIP Service
- Frontend Deployment
- Frontend NodePort Service

## Security Hardening with Trivy

Trivy was used to scan the Kubernetes manifests for security misconfigurations.

Security improvements applied:

- Disabled service account token automounting
- Added `allowPrivilegeEscalation: false`
- Added `seccompProfile: RuntimeDefault`
- Added CPU and memory requests
- Added CPU and memory limits
- Dropped Linux capabilities where supported
- Validated manifests using `kubectl --dry-run`
- Confirmed backend and frontend pods remained stable after applying changes

Run Trivy scan:

```bash
trivy config kubernetes-manifests/
```

## Validation Commands

Dry-run validation:

```bash
kubectl apply --dry-run=client -f kubernetes-manifests/
```

Apply manifests:

```bash
kubectl apply -f kubernetes-manifests/
```

Check running pods:

```bash
kubectl get pods -n well-health-care
```

Check services:

```bash
kubectl get svc -n well-health-care
```

Check all resources:

```bash
kubectl get all -n well-health-care
```

## Current Status

The application has been successfully deployed to Kubernetes.

Current working state:

- Backend pod: Running
- Frontend pod: Running
- Frontend service: NodePort `30082`
- Backend service: ClusterIP `8000`
- Kubernetes manifests validated
- Trivy security hardening applied where safe

## Key Learning Outcomes

This project helped demonstrate:

- How to containerize frontend and backend applications
- How to build a Jenkins CI pipeline
- How to deploy full-stack applications to Kubernetes
- How Kubernetes Deployments and Services work
- How to expose a frontend app using NodePort
- How to keep backend services internal using ClusterIP
- How to scan Kubernetes manifests with Trivy
- How to apply security hardening without breaking running workloads
