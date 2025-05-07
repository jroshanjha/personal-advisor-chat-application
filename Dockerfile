# # Use official Python image
# # FROM python:3.11

# FROM python:3.11-alpine

# # Set working directory
# WORKDIR /app

# # Copy project files
# COPY . /app

# # Install dependencies
# # RUN pip install --no-cache-dir -r requirements.txt
# RUN pip install -r requirements.txt

# # Expose the port Streamlit runs on
# EXPOSE 8501

# # Run Streamlit
# CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]

# FROM python:3.11-alpine
# COPY . /app
# WORKDIR /app
# RUN pip install -r requirements.txt
# CMD python -u app.py


# Use official Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy app files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Optionally preload the model (to avoid downloading at runtime)
RUN python modular/download_model.py

# Expose port
EXPOSE 8501

# Run Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]


# # Use official lightweight Python image
# FROM python:3.10-slim

# # Set environment variables
# ENV PYTHONDONTWRITEBYTECODE=1
# ENV PYTHONUNBUFFERED=1

# # Set working directory
# WORKDIR /app

# # Install system dependencies
# RUN apt-get update && apt-get install -y \
#     build-essential \
#     && rm -rf /var/lib/apt/lists/*

# # Copy requirements and install
# COPY requirements.txt .
# RUN pip install --upgrade pip && pip install -r requirements.txt

# # Copy rest of the app
# COPY . .

# # Create logs directory
# RUN mkdir -p logs

# # Expose the port Streamlit runs on
# EXPOSE 8501

# # Run Streamlit
# CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]



# # # Use a Python base image
# FROM python:3.10-slim

# # Create app directory
# WORKDIR /app

# # Copy files
# COPY requirements.txt .
# COPY download_model.py .
# COPY main.py .

# # Install dependencies
# RUN pip install --upgrade pip && \
#     pip install -r requirements.txt

# # Optionally preload the model (to avoid downloading at runtime)
# RUN python download_model.py

# # Run the app
# CMD ["python", "main.py"]


# 🚀 How to Build & Run
# # Step 1: Build the Docker image
# docker build -t ner-app .

# # Step 2: Run the container
# docker run --rm ner-app