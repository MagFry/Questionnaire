#!/bin/bash

# TODO: wait for postgres to be ready?

cd /usr/src/app

echo "Running migrations"
python manage.py makemigrations
python manage.py migrate
echo "Populating db"
python manage.py populate_db

# automatically add superuser admin:admin
echo "Adding admin user"
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@myproject.com', 'admin')" | python manage.py shell

python manage.py runserver 0.0.0.0:8000
