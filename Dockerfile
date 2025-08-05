# ---------- Base Stage ----------
FROM bitnami/python:3.13 AS base

WORKDIR /app

COPY pyproject.toml ./

RUN pip install --upgrade pip setuptools wheel \
    && pip install .

COPY src ./src


# ---------- Test Stage ----------
FROM base AS test

RUN pip install ".[test]"

COPY tests ./tests

RUN echo '#!/bin/sh\n\
    python -m pytest --junitxml=./reports/pytest.xml --cov-report=term-missing:skip-covered --cov=src tests/ | tee ./reports/pytest-coverage.txt' > docker-entrypoint.sh

RUN chmod +x docker-entrypoint.sh

CMD ["/bin/sh", "-c", "./docker-entrypoint.sh"]


# ---------- Production Stage ----------
FROM base AS prod

WORKDIR /app/src
CMD ["python", "main.py"]
