dev_build:
	docker compose -f docker/compose/docker-compose.dev.yml up --build

dev_run:
	docker compose -f docker/compose/docker-compose.dev.yml up