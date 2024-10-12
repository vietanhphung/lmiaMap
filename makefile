
build_container:
	docker build -t lmia .

destroy_container:
	docker system prune -a

run:
	docker run -it -p 5000:5000 lmia /bin/bash

copy:
	@if [ -z "$(f)" ]; then \
		echo "Usage: make copy f=<filename>"; \
	else \
		docker cp $(f) $(shell docker ps -q):/app; \
		echo "cp $(f) $(docker ps -q):/app;";  \
	fi

help:
	@echo "Makefile Commands:"
	@echo "  build_container    - Build the Docker image named 'lmia'."
	@echo "  destroy_container   - Remove all stopped containers and prune unused images."
	@echo "  run                - Run the Docker container based on the 'lmia' image, expose port 5000."
	@echo "  copy               - Copy a file into the running container."
	@echo "                      Usage: make copy f=<filename>"
