# Shakespeare AI Assistant

This project is an AI-powered assistant that provides comprehensive access to the complete works of William Shakespeare. Users can query the backend API to ask questions about Shakespeare's works, such as summaries, themes, character analysis, and more.

## Overview

The Shakespeare AI Assistant is built as a **Cloud-Native Microservice Application**, designed for scalability and efficiency. It leverages modern cloud infrastructure and DevOps best practices to ensure seamless deployment, monitoring, and updates.

### Key Technologies:
- **Docker**: Containerization of the application for consistent environments across development and production.
- **Kubernetes**: Orchestration of containerized workloads for high availability and scaling.
- **Google Cloud Kubernetes Cluster**: Deployment on GKE (Google Kubernetes Engine) for cloud-native scalability.
- **CI/CD with GitHub Actions**: Automates the process of building, testing, and deploying the application on each push to the repository.
- **Model Monitoring with WhyLogs/WhyLabs**: Tracks model performance and logs data, alerting on any significant performance degradation.

### Continuous Integration and Deployment:
The project utilizes a continuous integration and deployment pipeline. Upon pushing code to the remote GitHub repository, GitHub Actions automatically build, deploy, and update the application on the Google Cloud Kubernetes Cluster.

### Prerequisite: 
1. Before deploying this project for the very first time, ensure that you have an **empty Google Cloud Kubernetes Cluster** running. This is where your application will be deployed. For example:
```
$ gcloud container clusters create my-cluster --num-nodes=2 --zone=us-west1-a
```

2. The following secret values need to be configured in your repository's GitHub Actions secrets:

- `PROJECT_ID` - Your Google Cloud Project ID
- `GKE_SA_KEY` - Google Cloud Service Account Key in JSON format
- `OPENAI_API_KEY` - API key for OpenAI's language model
- `ASSISTANT_ID` - Unique identifier for the AI assistant instance
- `WHYLABS_API_KEY` - API key for WhyLabs (used for model monitoring)
- `WHYLABS_DEFAULT_ORG_ID` - Organization ID for WhyLabs
- `WHYLABS_DEFAULT_DATASET_ID` - Dataset ID for WhyLabs

Ensure these values are securely stored and never hard-coded in your source files.
