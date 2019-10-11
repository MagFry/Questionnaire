#!/bin/bash

# TODO: wait for postgres to be ready?

cd /usr/src/app
python manage.py makemigrations
python manage.py migrate
python manage.py populate_db

python manage.py runserver 0.0.0.0:8000
