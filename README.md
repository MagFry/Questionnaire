# Questionnaire

## How to run project
```
export TMDB_API_KEY="YOUR_KEY_HERE"
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
# gets metadata about 200 movies and inserts into Movies db
python manage.py populate_db
python manage.py runserver 8000
```

and visit: http://localhost:8000/

## Management commands

There is also a command to delete all the movies (rows) from table: Movies:
```
python manage.py delete_movies
```
and to list all the movies in table: Movies:
```
python manage.py list_movies
```

List all ratings:
```
python manage.py list_ratings
```

Same for users:
```
python manage.py delete_users
python manage.py list_users
```

Also, if you want to just test that populate_db works, make it run in a test mode,
 (this will add only 1 movie):
```
PIIS_TEST=true python manage.py populate_db
```

### Run

Deploy the website locally on Linux using Docker containers:
```
./tasks docker_build
./tasks up
```

Stop and remove the containers:
```
./tasks down
```

### Tests
Run Django tests:
```
./tasks test
```

Run testinfra tests:
```
./tasks itest
```
