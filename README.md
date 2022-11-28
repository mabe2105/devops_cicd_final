# devops_cicd_final

A simple python flask application to host the best web app ever.

After starting, you can access it on -

# Requirements:
    Python 3.8+
    Docker

### Application:

    requirements.txt

### Development:

    requirements-dev.txt

# Development setup

1. ` python3 -m venv .venv && source .venv/bin/activate `
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

# Docker

Build from root folder

- `docker build -t shop_app -f ./src/Dockerfile .`

- `docker tag shop_app ghcr.io/mabe2105/shop_app`

- `docker login ghcr.io`

- `docker run -dp 5000:5000 ghcr.io/mabe2105/shop_app`
