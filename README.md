## How to build project
```
1. pip install -r requirements.txt
2. python src/manage.py makemigrations
3. python src/manage.py migrate
4. python src/manage.py populate_db
5. python src/manage.py runserver 8000
```

There is also a command to delete all the movies (rows) from table: Movies:
```
python src/manage.py delete_movies.py
```

## Generate file with movie genres

```
rm -f Data/genres.csv
export TMDB_API_KEY="YOUR_KEY_HERE"
python helpers/movie_genres_getter.py
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
