# Todo Application

This is a simple Todo application built with FastAPI.

## Features

- Create, Read, Update, and Delete (CRUD) operations for todos.

## Requirements

- Python 3.10+
- Poetry

## Setup

### Local Run

1. Install dependencies:
   ```bash
   poetry install
   ```

2. Run the application:
   ```bash
   poetry run uvicorn app.main:app --reload
   ```

3. Open your browser and navigate to `http://127.0.0.1:8000/docs` to access the API documentation.

### Docker Run

1. Build the Docker image:
   ```bash
   docker build -t todo-app .
   ```

2. Run the Docker container:
   ```bash
   docker run -d -p 8000:8000 todo-app
   ```

3. Open your browser and navigate to `http://127.0.0.1:8000/docs`.

### Testing

1. Run the tests:
   ```bash
   poetry run pytest
   ```# Todo Application

This is a simple Todo application built with FastAPI.

## Features

- Create, Read, Update, and Delete (CRUD) operations for todos.

## Requirements

- Python 3.10+
- Poetry

## Setup

### Local Run

1. Install dependencies:
   ```bash
   poetry install
   ```

2. Run the application:
   ```bash
   poetry run uvicorn app.main:app --reload
   ```

3. Open your browser and navigate to `http://127.0.0.1:8000/docs` to access the API documentation.

### Docker Run

1. Build the Docker image:
   ```bash
   docker build -t todo-app .
   ```

2. Run the Docker container:
   ```bash
   docker run -d -p 8000:8000 todo-app
   ```

3. Open your browser and navigate to `http://127.0.0.1:8000/docs`.

### Testing

1. Run the tests:
   ```bash
   poetry run pytest
   ```