# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory inside the Docker container to /app. This will be the base directory for any subsequent commands.
WORKDIR /app

# Create a directory named api inside the /app directory. This is where FastAPI application code will be copied.
# RUN mkdir /app/api


# Install Python dependencies
# COPY requirements.txt .
COPY requirements.txt /app/requirements.txt

# Copy .env file into the container
COPY .env /app

# Install Python Dependencies 
# --no-cache-dir: Ensures no cache is saved, reducing image size and ensuring fresh installs.
RUN python3 -m pip install --no-cache-dir --upgrade  -r /app/requirements.txt   
RUN apt-get update && \
    apt-get install -y unixodbc-dev msodbcsql17

# Copy the entire current directory to /app/api inside the Docker container.
COPY . /app

# ENV PATH ${APP_ROOT}/.local/bin:${PATH}

# Expose the port that FastAPI runs on
EXPOSE 8000
# Start both FastAPI and Streamlit
CMD ["python3", "-m", "api.main"]
