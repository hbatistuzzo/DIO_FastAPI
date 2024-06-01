run:
	@uvicorn workout_api.main:app --reload

create-migrations:
	@PYTHONPATH=$PYTHONPATH:$(pwd) alembic revision --autogenerate -m $(d)

run-migrations:
	@PYTHONPATH=$PYTHONPATH:$(pwd) alembic upgrade head

#abaixo sugestão do Lucas Marins no forum em 03/05/2024
run-docker:
 docker compose up --detach

stop-docker:
 docker compose down