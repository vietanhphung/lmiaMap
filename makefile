
build_container:
	docker build -t lmia .

destroy_container:
	docker system prune -a

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

run_container:
	docker start lmia-container;
	docker exec -it lmia-container /bin/bash

copy:
	@if [ -z "$(f)" ]; then \
		echo "Usage: make copy f=<filename>"; \
	else \
		docker cp $(f) $(shell docker ps -q):/app; \
		echo "cp $(f) $(docker ps -q):/app;";  \
	fi

stop_container:
	docker stop lmia-container

restart_container:
	docker restart lmia-container
help:
	@echo "Makefile Commands:"
	@echo "  build_container    - Build the Docker image named 'lmia'."
	@echo "  destroy_container   - Remove all stopped containers and prune unused images."
	@echo "  run                - Run the Docker container based on the 'lmia' image, expose port 5000."
	@echo "  copy               - Copy a file into the running container."
	@echo "  stop               - Stop all running container."
	@echo "                      Usage: make copy f=<filename>"
