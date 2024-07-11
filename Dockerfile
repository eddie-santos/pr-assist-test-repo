# Use a lightweight Python 3.12 base image
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy poetry.lock and pyproject.toml to ensure consistent dependencies
COPY pyproject.toml poetry.lock ./

# Install Poetry and project dependencies
RUN pip install poetry && poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

# Copy the rest of the application code
COPY . .

# Expose the port that the FastAPI application will listen on
EXPOSE 8000

# Command to run the FastAPI application with Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]