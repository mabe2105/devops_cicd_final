# devops_cicd_final

A simple python flask application to host the best web app ever.

FluxCD monitors this repo and updates the package with the latest version from the feature branches after a successful deployment.

According to GitOps the pipeline will break if your tests are not up to par with coverage standards.

# Requirements:
    Python 3.8+
    Minikube
    Docker & Docker-compose

### Application:

    requirements.txt

### Development:

    requirements-dev.txt

# Development setup

1. `python3 -m venv .venv && source .venv/bin/activate `
2. `pip3 install --upgrade pip`
3. `pip3 install -r requirements-dev.txt`
4. `pre-commit install`

# Testing & linting

- Pre-commit hooks are in place that makes sure that every time you commit, checks will be run, like unit tests and pylint.

If you want you can run tests or linting manually.

## Linting

- Show warnings & errors:  `pylint shop_app`
- Errors only:  `pylint shop_app --errors-only`

## Tests

- Run unit tests only:  `pytest --cov=shop_app tests`

- To run pre-commit: `pre-commit run --all-files`

- To test with selenium go to src/tests/e2e and run `docker-compose up -d` then `pytest ./tests/e2e/`

# Deployment

## Docker

Build from root folder

- `docker build -t shop_app -f ./src/Dockerfile .`

- `docker tag shop_app ghcr.io/mabe2105/shop_app`

- `docker login ghcr.io`

- `docker run -dp 5000:5000 ghcr.io/mabe2105/shop_app`

## Minikube

Go to src/k8s/

- `kubectl apply -f create_pod.yml`

- `kubectl expose pod shop-app-pod --selector "app=shop_app" --type=LoadBalancer --port=5000`

- `minikube service shop-app-pod`
