## How to build project
```
0. export TMDB_API_KEY="YOUR_KEY_HERE"
1. pip install -r requirements.txt
2. python manage.py makemigrations
3. python manage.py migrate
4. python manage.py populate_db
5. python manage.py runserver 8000
```

There is also a command to delete all the movies (rows) from table: Movies:
```
python manage.py delete_movies
```
and to list all the movies in table: Movies:
```
python manage.py list_movies
```

Same for users:
```
python manage.py delete_users
python manage.py list_users
```

Also, if you want to just test that populate_db works, make it run in a test mode,
 (this will add only one movie):
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
