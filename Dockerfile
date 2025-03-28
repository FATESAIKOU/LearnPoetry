FROM python:3.10-slim

WORKDIR /app

COPY pyproject.toml poetry.lock /app/
COPY ./app /app/app
RUN pip install poetry && poetry install --only main

CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
