# Christmas Docker: Santa's Parcel Management System
Welcome to Christmas Docker, a system designed to manage Santa's parcels and elves efficiently during the festive season!

# Overview
This system offers functionalities for managing parcels and elves for Santa's gift distribution. It includes operations to add parcels, assign them to specific elves, manage elf schedules, grant leaves, and parental leaves.

# Technology Stack
Backend: FastAPI for providing web services and CRUD operations for parcels and elves.
Database: SQLite for storing data.
Deployment: Docker for containerization, DockerHub for container registry, and GitHub Actions for CI/CD.

# Installation and Usage
1. Clone the Repository:
git clone https://github.com/xAleksandrax/christmas_docker.git
cd christmas_docker
2. Run with Docker Compose:
docker-compose up -d
3. Access the Application:
Open your web browser and go to http://localhost:8000.

# Deployment and CI/CD
Docker Deployment
The project can be deployed using Docker Compose, ensuring all necessary services are up and running smoothly.

# CI/CD with GitHub Actions
Continuous Integration and Continuous Deployment (CI/CD) is set up using GitHub Actions. On each push to the main branch, the workflow is triggered to build the Docker image, push it to DockerHub, and deploy it to the server.

# Environment Variables
PORT: Define the port number for the FastAPI server. Default is 8000.
DATABASE_URL: Set the database URL for connecting to the SQLite database.
# Contributing
Contributions are welcome! Fork the repository, make changes, and submit a pull request. For significant changes, please open an issue first to discuss the proposed adjustments.
