up:
	docker compose down
	docker compose up -d
down:
	docker compose down --remove-orphans
attach:
	docker attach fam_app
inspect:
	docker exec -it fam_app /bin/bash