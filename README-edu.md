## Interactively work with objects in db

```
cd /usr/src/app/
python manage.py shell
from Movies.models import Movies
Movies.objects.filter(movie_id=1)
Movies.objects.all()
```

https://docs.djangoproject.com/en/2.2/intro/tutorial02/


## Interactively work with objects in db
```
http://127.0.0.1:8000/movies/movie_list/ - diplaying list of movies (for now only one movie)
http://127.0.0.1:8000/movies/index/ - basic html to test 
```