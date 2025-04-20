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

# Expose port
EXPOSE 8501

# Run Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
