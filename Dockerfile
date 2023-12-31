# Use an official Python runtime as a parent image
FROM python:3.11

# Set the working directory in the container to where your Django app is located
WORKDIR /usr/src/drb

# Install Poetry
RUN pip install poetry

# Copy pyproject.toml and poetry.lock (if available) first for better layer caching
COPY pyproject.toml poetry.lock* /usr/src/drb/

# Install dependencies using Poetry
RUN poetry config virtualenvs.create false \
    && poetry install --no-root --no-dev --no-interaction

# Copy the current directory contents into the container
COPY . /usr/src/drb

# Make port 8000 available to the world outside this container
EXPOSE 8000

WORKDIR /usr/src/drb/app

# Run the application
CMD ["gunicorn", "versus.wsgi:application", "--bind", "0.0.0.0:8000"]

