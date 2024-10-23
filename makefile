# Makefile for managing Docker containers for the LMIA project

# Build Docker image
build_container:
	docker build -t lmia .

# Stop and remove all containers and images
destroy_container:
	make destroy_all

# Initialize and run the container with MySQL settings
init_container:
	docker run  \
	--name lmia-container \
	-e MYSQL_ROOT_PASSWORD="!@AQWERSAASD!@#" \
	-e MYSQL_DATABASE="lmia_db" \
	-e MYSQL_USER="user" \
	-e MYSQL_PASSWORD="1234" \
	-v mysql_data:/var/lib/mysql \
	-p 5000:5000 \
	lmia /bin/bash

# Start the container and follow logs
run_container:
	docker start lmia-container; \
	docker logs -f lmia-container

# Copy a file into the running container
copy:
	@if [ -z "$(f)" ]; then \
		echo "Usage: make copy f=<filename>"; \
	else \
		docker cp $(f) $(shell docker ps -q):/app; \
		echo "cp $(f) $(docker ps -q):/app"; \
	fi

# Stop the running container
stop_container:
	docker stop lmia-container

# Restart the container
restart_container:
	docker restart lmia-container

# Stop all running containers
stop_all_containers:
	docker stop $(docker ps -q)

# Destroy all containers and images
destroy_all:
	docker stop $(docker ps -q) || true; \
	docker rm $(docker ps -a -q); \
	docker rmi $(docker images -q)

# Help command to list available commands
help:
	@echo "Makefile Commands:"
	@echo "  build_container       - Build the Docker image named 'lmia'. Only use for initial setup." 
	@echo "  init_container        - Run the Docker container with MySQL setup, expose port 5000. Only use for initial setup."
	@echo "  run_container         - Start the container and follow logs."
	@echo "  destroy_container     - Stop and remove all containers and images."
	@echo "  copy                  - Copy a file into the running container. Usage: make copy f=<filename>."
	@echo "  stop_container        - Stop the 'lmia-container'."
	@echo "  stop_all_containers   - Stop all running containers."
	@echo "  restart_container     - Restart the 'lmia-container'."
	@echo "  destroy_all           - Remove all containers and images."
	@echo "  help                  - Show this help message."
