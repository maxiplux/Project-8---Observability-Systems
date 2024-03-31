# Project 8 - Observability Systems

![Micro Services Calculator Architecture](DevOps%20-%20Project%20-%20Observability%20Systems.png)

## Architecture

This project involves team collaboration to deploy a web application onto a cloud-based Kubernetes cluster. The deployment includes an active monitoring setup using observability systems. Students have a choice among several observability technologies, including Fluentd, Prometheus, Grafana, ELK (Elasticsearch, Logstash, Kibana), EFK (Elasticsearch, Fluentd/Fluent bit, Kibana), and Loki/Prometheus/Grafana configurations.

## Requirements

- **Web App**: Create or use an existing web app.
- **Dockerization**: Dockerize the app with a Dockerfile.
- **DockerHub Account**: Ensure you have a DockerHub account.
- **Docker Images**: Build Docker images in x86_64 and arm64 formats and push them to DockerHub.
- **Deployment**: Deploy the app on a Kubernetes cluster (e.g., AWS EKS, Local).
- **Observability Systems**:
  - **Loki**: Set up Loki to scrape logs.
  - **Prometheus**: Set up Prometheus to scrape metrics and store it.
  - **Grafana**: Use Grafana to visualize metrics from Prometheus and Loki.

## Solution
![Technical desing solution](diagram-export-3-30-2024-11_11_35-PM.png)
### Architecture Components:

- **User**: The user interacts with the system via Docker.
- **Docker**: Serves as the entry point for the user, managing containerized applications.
- **Kubernetes Namespace `weclouddata`**:
  - **Microservice-1 (Add-Subtract)**: A Java application running on port 8081.
  - **Microservice-2 (Multiplication-Division)**: A Java application with Envoy proxy running on port 8082.

- **Kubernetes Namespace `istio`**:
  - **Prometheus**: Monitoring system with a time-series database, accessible on port 8082.
  - **Grafana**: Analytics and monitoring platform visualizing data, accessible on port 3000.
  - **Loki**: Log aggregation system, accessible on port 3100.
