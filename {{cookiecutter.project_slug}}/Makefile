build:
	docker-compose build {{cookiecutter.project_slug}}

init-material:
	unzip material.zip -d {{cookiecutter.project_slug}}/static/

run:
	python3 manage.py runserver 0.0.0.0:8000

makemigrations:
	python3 manage.py makemigrations

migrate:
	python3 manage.py migrate