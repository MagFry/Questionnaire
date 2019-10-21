# Questionnaire

## How to run project locally 
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

to get a csv of all ratings, visit: http://localhost:8000/responses/get_csv/


## Deployment

visit: https://piis-app.herokuapp.com

to get a csv of all ratings, visit: https://piis-app.herokuapp.com/responses/get_csv/


## Description of the project

The website is a questionnaire with 200 movies fetched from TMDB. The movies are grouped in genres categories. Each category is placed in a distinct subpage. In the welcome page, the user types his username. There exists a constraint which allows using only one username. When another person wants to use the same nick, a user is redirected to type username again. When the user clicks the next page button and all the movies in the subpage are not rated, the proper window with information is displayed. When the user closes the browser before clicking next page button, only the answers from the previous page are saved to the database. https://piis-app.herokuapp.com/responses/get_csv/ page shows only the answers of users who completed all questions. The design of the layout of the webpage facilitates the rating process for the user.

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
