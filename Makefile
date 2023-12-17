.EXPORT_ALL_VARIABLES:

include .env
export $(shell sed 's/=.*//' .env)

.PHONY: list
list:
	@make -qp | awk -F':' '/^[a-zA-z0-9][^$$#\/\t=]*:([^=]|$$)/ {split($$1,A,/ /); for(i in A)print(A[i])}' | sort

test:
	pytest --cov=./tests --cov-report=xml -s -vv

analise-estatica:
	black .
	isort . --profile black
	flake8 .
	bandit .

docker-down:
	docker compose down --remov-orphans

docker-up: docker-down
	docker compose up -d --build --remove-orphans

docker-analise-estatica: docker-up
	docker compose run \
	--rm \
	--no-deps \
	--user 1000:1000 \
	--entrypoint="make analise-estatica" \
	api

docker-api-bash:
	docker compose exec api /bin/bash

docker-db-bash:
	docker compose exec db /bin/bash

docker-alembic-upgrade:
	docker compose exec api alembic upgrade head

docker-script-sql:
	docker compose exec db psql -U postgres -d projeto -f /script.sql
