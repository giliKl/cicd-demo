# CI/CD Demonstration Project

This is a comprehensive CI/CD demonstration project designed for graduate-level computer science students. It demonstrates CI/CD pipelines across three major platforms: GitHub Actions, GitLab CI/CD, and Jenkins.

## Project Structure

- **app.py**: Simple Flask web application
- **test_app.py**: Unit tests for the application
- **requirements.txt**: Python dependencies
- **Dockerfile**: Multi-stage build for the application
- **kubernetes/**: Kubernetes deployment manifests
- **.github/workflows/**: GitHub Actions workflow definitions
- **.gitlab-ci.yml**: GitLab CI/CD pipeline configuration
- **Jenkinsfile**: Jenkins pipeline configuration

## Application

The application is a simple Flask web service that provides:

- A root endpoint (`/`) that returns application information
- A health check endpoint (`/health`)

## CI/CD Pipeline Features

All three CI/CD implementations (GitHub, GitLab, Jenkins) follow the same general workflow:

1. **Test**: Run unit tests to verify application functionality
2. **Build**: Create a Docker image and push to a container registry
3. **Deploy**: Deploy the application to a Kubernetes cluster

## Setup Instructions

### Prerequisites

- Git
- Docker
- Kubernetes cluster (or Minikube for local development)
- Access to GitHub, GitLab, or Jenkins

### Local Development

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/cicd-demo.git
   cd cicd-demo
   ```

2. Set up a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run tests:
   ```
   python -m pytest test_app.py -v
   ```

5. Run the application:
   ```
   python app.py
   ```

6. Build and run with Docker:
   ```
   docker build -t cicd-demo:local .
   docker run -p 5000:5000 cicd-demo:local
   ```

## CI/CD Configuration

### GitHub Actions

1. Store your Kubernetes configuration as a secret named `KUBECONFIG` in your GitHub repository settings.
2. Push to the main branch to trigger the workflow.
3. The workflow will automatically:
   - Run tests
   - Build and push a Docker image to GitHub Container Registry (ghcr.io)
   - Deploy to your Kubernetes cluster

### GitLab CI/CD

1. Set up the following CI/CD variables in your GitLab project:
   - `CI_REGISTRY`: Your container registry URL
   - `CI_REGISTRY_USER`: Registry username
   - `CI_REGISTRY_PASSWORD`: Registry password
   - `KUBE_CONFIG`: Your base64-encoded kubeconfig file

2. Push to the main branch to trigger the pipeline.

### Jenkins

1. Create a Jenkins pipeline job using the included Jenkinsfile.
2. Set up the following credentials in Jenkins:
   - `docker-registry-credentials`: Credentials for your Docker registry
   - `kubeconfig`: Your Kubernetes configuration file

3. Configure the pipeline to use your Git repository.

## Container Registry Authentication

Each CI/CD tool handles registry authentication differently:

### GitHub Actions
Uses GITHUB_TOKEN to authenticate with GitHub Container Registry (ghcr.io)

### GitLab
Uses CI_REGISTRY_USER and CI_REGISTRY_PASSWORD variables

### Jenkins
Uses credentials defined in Jenkins credential store

## Runner Types

### GitHub Actions
- **Hosted runners**: Ubuntu, Windows, macOS runners provided by GitHub
- **Self-hosted runners**: Deploy your own runners for specialized environments

### GitLab
- **Shared runners**: Provided by GitLab
- **Specific runners**: Dedicated runners for your projects
- **Docker executor**: Isolates builds in containers
- **Shell executor**: Runs builds directly on the host
- **Kubernetes executor**: Runs builds in Kubernetes pods

### Jenkins
- **Traditional agents**: Persistent machines connected to Jenkins master
- **Dynamic agents**: Ephemeral agents (e.g., Docker, Kubernetes)
- **Cloud agents**: Agents provisioned on demand in cloud environments

## Deployment Strategies

This demo uses a basic deployment to Kubernetes, but you can extend it with:

- **Blue/Green Deployment**: Run two identical production environments
- **Canary Releases**: Gradually roll out changes to a subset of users
- **Rolling Updates**: Default Kubernetes deployment strategy that replaces pods one by one

## Best Practices

1. **Secrets Management**: Never store secrets in your repository
2. **Idempotent Deployments**: Ensure deployments can be run multiple times without issues
3. **Fail Fast**: Tests should run early in the pipeline
4. **Caching**: Cache dependencies to speed up builds
5. **Parallel Execution**: Run independent steps in parallel
6. **Manual Approval**: Add approval steps for production deployments

## Extending the Project

- Add static code analysis
- Implement security scanning
- Add end-to-end tests
- Configure monitoring and alerts
- Implement infrastructure as code
- Add feature flag capability

## Learning Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [GitLab CI/CD Documentation](https://docs.gitlab.com/ee/ci/)
- [Jenkins Documentation](https://www.jenkins.io/doc/)
- [Docker Documentation](https://docs.docker.com/)
- [Kubernetes Documentation](https://kubernetes.io/docs/)