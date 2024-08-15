FROM python:3.12

# Set the working directory
WORKDIR /app

# Copy the backend files to the working directory
COPY . /app

# Install Poetry and dependencies
RUN pip install poetry && poetry install

# Expose any necessary ports
EXPOSE 8000

# Start the FastAPI application
CMD ["poetry", "run", "uvicorn", "main:app", "--workers", "4", "--host", "0.0.0.0", "--port", "8000"]
