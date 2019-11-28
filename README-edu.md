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

## Experiments

To experiment with rating stars, visit:
```
http://localhost:8000/movies/test_rating/
```

Choose a rating (1 to 6 or cross for not seen) and then click the Rate button.


# Heroku deployment
* https://devcenter.heroku.com/articles/using-terraform-with-heroku#set-up-terraform
* https://www.terraform.io/docs/providers/heroku/r/build.html
* https://elements.heroku.com/addons/heroku-postgresql
* https://devcenter.heroku.com/articles/heroku-postgresql#provisioning-heroku-postgres
* https://devcenter.heroku.com/articles/heroku-postgresql#provisioning-heroku-postgres

install heroku cli on ubuntu:
```
echo "deb https://cli-assets.heroku.com/apt ./" > /etc/apt/sources.list.d/heroku.list
curl https://cli-assets.heroku.com/apt/release.key | apt-key add -
apt-get update
apt-get install -y heroku
```

example commands:
```
heroku login
heroku ps -a piis-app
heroku logs -a piis-app
heroku dyno:restart -a piis-app
heroku config -a piis-app
heroku ps:exec -a piis-app
```

https://devcenter.heroku.com/articles/heroku-cli-commands

### connect with db
```
$ docker exec -ti piis_db_1 bash
psql -h localhost -U postgres
\connect Questionnaire
# list tables
\dt
SELECT * FROM "Users_users";
# list sequences
SELECT c.relname FROM pg_class c WHERE c.relkind = 'S';
# returns e.g.
# Users_users_user_id_seq
# Responses_responses_respond_id_seq
```
