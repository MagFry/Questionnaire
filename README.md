## How to build project
```
0. export TMDB_API_KEY="YOUR_KEY_HERE"
1. pip install -r requirements.txt
2. python src/manage.py makemigrations
3. python src/manage.py migrate
4. python src/manage.py populate_db
5. python src/manage.py runserver 8000
```

There is also a command to delete all the movies (rows) from table: Movies:
```
python src/manage.py delete_movies
```
and to list all the movies in table: Movies:
```
python src/manage.py list_movies
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
