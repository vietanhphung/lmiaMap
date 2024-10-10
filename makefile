
build_container:
	docker build -t lmia .


destroy_container:
	docker system prune -a

run:
	docker run lmia

copy:
	@container_id = $(docker ps -q);\
	docker cp testfile.py e7f999b0a098:/app

macrun:
	docker run -it lmia /bin/bash
macstop:
	docker ps


copy:
	@if [ -z "$(file)" ]; then \
		echo "Usage: make copy file=<filename>"; \
	else \
		docker cp $(file) $(shell docker ps -q):/app; \
		echo "cp $(file) $(docker ps -q):/app;";  \
	fi
