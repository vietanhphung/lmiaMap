# Use an official base image
FROM ubuntu:20.04

# Set the timezone environment variable
ENV TZ=America/New_York
ENV DEBIAN_FRONTEND=noninteractive 
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
# Install necessary packages including Python, pip, virtualenv, and MySQL
RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv mysql-server tzdata && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy requirements.txt before other files
COPY requirements.txt .

# Create a virtual environment
RUN python3 -m venv venv

# Activate the virtual environment and install dependencies
RUN ./venv/bin/pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Set environment variable to use the virtual environment's Python
ENV PATH="/app/venv/bin:$PATH"

# Expose MySQL port
EXPOSE 3306

# Start MySQL server and your application (if applicable)
ENTRYPOINT service mysql start && chmod +x init_db.sh && /bin/bash 