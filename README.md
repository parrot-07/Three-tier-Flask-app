# Three-tier-Flask-app

Three-Tier Flask Application (Nginx + Flask + MySQL)

This project demonstrates a three-tier web application architecture using Docker Compose, designed and debugged with the goal of deploying via Jenkins CI/CD to an AWS EC2 instance.

<img width="400" height="200" alt="image" src="https://github.com/user-attachments/assets/509aba4c-6834-4e81-a928-a295795d49d8" />


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

 resolver 127.0.0.11 valid=10s;

❌ Issue 2: flask container was not up but restarting

Fixes Applied:

Identified a python syntax error through the docker container logs

Corrected the try except syntax in app.py 

Now deploying the code on an EC2 instance after integrating it with jenkins for CI/CD

Steps:

* Launch an EC2 instance (I have taken t3.medium because jenkins is heavy and t2 micro cannot handle it)
* install  docker and docker compose
* install jenkins
* edit security groups with required inbound rules , here open ports 8080, 5000, 80

In jenkins
- create a pipeline with the github link
- configure the pipeline with git SCM, give the git repository url and also the script as Jenkinsfile
- apply and save the changes.. good to go.. !! build your pipeline
- See your output on http://<ec2publicIP>:80/
