# Django Webb App 

## Description

A Django web app, complete with user registration, sign in, password update/email reset, account profile update and account deletion. Developed in a docker container and integrated with Posgresql.

## Installation

1. Install and run the Docker ingine
	- https://docs.docker.com/engine/
2. `cd django-web-app` 
3. Run Docker container in detached mode
	- `docker-compose up -d`
4. Initialize database for the first time
	- `docker-compose exec web python manage.py migrate`
5. Interact with web app
	- http://127.0.0.1:8000/

## Additional Configuration

1. Create first admin account
	- `docker-compose exec web python manage.py createsuperuser`
2. Login to admin account 
	- http://127.0.0.1:8000/admin 
3. Run build in test scripts
	- `docker-compose exec web python manage.py test`