dev:
	docker-compose -f docker-compose.yml -f docker-compose.override.yml up --build

test:
	pytest --cov=backend

migrate:
	bash scripts/migrate.sh

deploy:
	bash scripts/deploy.sh