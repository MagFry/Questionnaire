## How to build project
```
1. pip install -r requirements.txt
2. python src/manage.py makemigrations
3. python src/manage.py migrate 
4. python src/manage.py runserver 8000
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
