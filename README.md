# Sample app deployment for the Demo


## Overview

This project showcases the process of containerizing a Flask application using Docker and then deploying it on AKS. It includes:

- A Dockerfile for building the container image
- Configuration files for AKS deployment
- Sample Flask application code

## Prerequisites

Before running this demo, ensure you have:

- Docker installed on your local machine
- Azure CLI configured with AKS access
- kubectl installed and configured to interact with your AKS cluster

### Configuration Files

- **app.py**: Contains the sample Flask application code.
- **Dockerfile**: Defines how to build the container image.
- **deployment.yaml**: Configures the Kubernetes deployment resource.
- **service.yaml**: Configures the Kubernetes service resource.
