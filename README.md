# Three-tier-Flask-app

Three-Tier Flask Application (Nginx + Flask + MySQL)

This project demonstrates a three-tier web application architecture using Docker Compose, designed and debugged with the goal of deploying via Jenkins CI/CD to an AWS EC2 instance.

🧱 Architecture Overview

Client (Browser)
     ↓
Nginx (Reverse Proxy – Port 80)
     ↓
Flask Application (Gunicorn – Port 5000)
     ↓
MySQL Database (Port 3306)

Each tier runs in its own Docker container and communicates using Docker internal networking.

<img width="500" height="300" alt="image" src="https://github.com/user-attachments/assets/5125d0c0-3e2b-4518-b6cc-e392ae258f60" />

Components Explained

🔹 Nginx (Web Tier)

Acts as a reverse proxy

Listens on port 80

Forwards traffic to the Flask backend

Uses Docker DNS resolver to dynamically resolve backend service


Key config:

resolver 127.0.0.11 valid=10s;
proxy_pass http://backend:5000;

🔹 Flask + Gunicorn (Application Tier)

Flask app served via Gunicorn (production-ready WSGI server)

Binds to 0.0.0.0:5000 to allow container access

Uses environment variables to connect to MySQL

Includes proper error handling to avoid container crashes

🔹 MySQL (Database Tier)

Uses official mysql:8.0 image

Initializes database at startup

Data persisted using Docker volumes

🐳 Docker Compose Configuration

All services run on the same Docker network

Inter-service communication via service names (not container names)

Persistent storage for MySQL using named volumes


Start the application:

docker compose up -d --build

Stop the application:

docker compose down

🐞 Issues Faced & Troubleshooting

❌ Issue 1: host not found in upstream backend

Cause:

Nginx could not resolve the backend service at startup


Fixes Applied:

Used Docker Compose service name (backend) in proxy_pass

Ensured all services were on the same Docker network

Added Docker DNS resolver to Nginx config:


resolver 127.0.0.11 valid=10
