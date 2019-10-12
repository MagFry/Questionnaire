## Interactively work with objects in db

```
cd /usr/src/app/
python manage.py shell
from Movies.models import Movies
Movies.objects.filter(movie_id=1)
Movies.objects.all()
```

https://docs.djangoproject.com/en/2.2/intro/tutorial02/
