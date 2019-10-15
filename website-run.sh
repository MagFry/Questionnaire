#!/bin/bash

# TODO: wait for postgres to be ready?

cd /usr/src/app

# automatically add superuser admin:admin
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@myproject.com', 'admin')" | python manage.py shell

python manage.py makemigrations
python manage.py migrate
python manage.py populate_db

python manage.py runserver 0.0.0.0:8000
