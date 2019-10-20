#!/bin/bash

# TODO: wait for postgres to be ready?

cd /usr/src/app

echo "Running migrations"
python manage.py makemigrations
python manage.py migrate

# automatically add superuser admin:admin
echo "Adding admin user"
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@myproject.com', 'admin')" | python manage.py shell

if [[ "${PIIS_POPULATE_DB}" != "false" ]]; then
  # We have to bind to some port fast enough before Heroku timeouts.
  # Thus, let's download movie posters in the background and start
  # the webpage without waiting for the download to finish.
  # https://devcenter.heroku.com/articles/error-codes#r10-boot-timeout
  echo "Populating db"
  python manage.py populate_db &
fi

# If port is set, let's reuse its value. Otherwise: use the default below.
# The PORT variable is set dynamically by Heroku.
PORT=${PORT:-8000}
python manage.py runserver 0.0.0.0:${PORT}
