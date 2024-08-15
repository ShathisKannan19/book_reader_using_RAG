FROM python:3.8-slim

# Install Jupyter
RUN pip install jupyter

# Create a directory for your notebooks
WORKDIR /app/notebooks

# Copy the contents of the current directory to /app/notebooks in the container
COPY . /app/notebooks/

# Set environment variable for OpenAI API key
ENV OPENAI_API_KEY=''

# Expose the Jupyter port
EXPOSE 8888

# Run Jupyter Notebook
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]