FROM python:3.12

WORKDIR /app

# Copy poetry configuration files first
COPY pyproject.toml poetry.lock* /app/

# Install Poetry and the project dependencies
RUN pip install poetry && poetry install --no-root

# Copy the rest of the application files
COPY . /app

EXPOSE 8501

# Run the Streamlit app
CMD ["poetry", "run", "streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
