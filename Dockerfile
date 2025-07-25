FROM python:3.11-slim as builder

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
RUN pip install -e .

# Stage de test et couverture
FROM builder as test
RUN pip install pytest pytest-cov
RUN mkdir /testreports /coverage
RUN pytest \
    --junitxml=/testreports/junit.xml \
    --cov=app \
    --cov-report=xml:/coverage/coverage.xml \
    --cov-report=html:/coverage/htmlcov

# Stage des rapports
FROM scratch as reports
COPY --from=test /app/testreports /testreports
COPY --from=test /app/coverage /coverage

# Stage final
FROM builder as final
CMD ["python", "run.py"]