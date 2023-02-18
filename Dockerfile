FROM python:3.11-slim-buster

WORKDIR /app

RUN pip install poetry==1.3.2
COPY poetry.lock pyproject.toml ./
RUN poetry config virtualenvs.create false && poetry install --no-root --no-interaction --no-ansi

COPY . .
