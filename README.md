# unt
## Running locally
You will need:
1. Python 3.9+
2. [Poetry](https://python-poetry.org/docs/#installation)
3. Google Chrome
4. [Chromedriver](https://chromedriver.chromium.org/downloads) (get the version that matches Chrome, and add executable to PATH)

Steps:
1. Clone this repo
2. Navigate to repo root
3. Install dependencies

```
poetry config virtualenvs.in-project true --local
poetry install
```
4. Add repo directory to PYTHONPATH environment variable
5. Run tests

```
poetry run pytest
```

## Running in Docker
1. Clone repo
2. Navigate to repo root
3. Build image
```
docker build -t uit:local .
```
4. Run tests
```
docker run uit:local /bin/bash -c "poetry run pytest"
```
