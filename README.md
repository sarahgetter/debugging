# Python Application

## Description
A Python script that performs complex operations and demonstrates advanced debugging techniques, including nested function calls, exception handling, and multithreading.

## Files
- `script.py`: The main Python script.
- `Dockerfile`: Docker configuration to containerize the application.
- `requirements.txt`: Python dependencies.
- `kubernetes-deployment.yaml`: Kubernetes configuration to deploy the application on GCP.
- `Makefile`: Makefile to automate common tasks.
- `.dockerignore`: File to ignore unnecessary files during Docker build.

## Getting Started

### Prerequisites
- Docker
- Kubernetes
- Google Cloud SDK (for GCP deployment)

### Running Locally

1. Build the Docker image:
    ```sh
    make build
    ```

2. Run the Docker container:
    ```sh
    make run
    ```

### Deploying to GCP

1. Authenticate with GCP:
    ```sh
    make gcp-auth
    ```

2. Configure Kubernetes cluster:
    ```sh
    make gcp-cluster
    ```

3. Push the Docker image to GCP Container Registry:
    ```sh
    make push
    ```

4. Deploy the application to GCP Kubernetes cluster:
    ```sh
    make deploy
    ```

## License
This project is licensed under the MIT License.
