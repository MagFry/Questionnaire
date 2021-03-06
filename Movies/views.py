from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import (HttpResponse, HttpResponseBadRequest,
                         HttpResponseForbidden)
from django.shortcuts import redirect
from Responses.models import Responses
from Movies.models import Movies
from Users.models import Users
import json
import logging
import traceback


# Get an instance of a logger
logger = logging.getLogger('questionnaire_logger')

movies_categories = [
    {'movie_type': 'Horror', 'genres_to_be_excluded': []},
    {'movie_type': 'Mystery', 'genres_to_be_excluded': ['Horror']},
    {'movie_type': 'Romance', 'genres_to_be_excluded': ['Horror', 'Mystery']},
    {'movie_type': 'Adventure', 'genres_to_be_excluded': ['Horror', 'Mystery', 'Romance']},
    {'movie_type': 'Western', 'genres_to_be_excluded': ['Horror', 'Mystery', 'Romance', 'Adventure']},
    {'movie_type': 'Crime', 'genres_to_be_excluded': ['Horror', 'Mystery', 'Romance', 'Adventure', 'Western']},
    {'movie_type': 'Science Fiction', 'genres_to_be_excluded': ['Horror', 'Mystery', 'Romance', 'Adventure', 'Western', 'Crime']},
    {'movie_type': 'Fantasy', 'genres_to_be_excluded': ['Horror', 'Mystery', 'Romance', 'Adventure', 'Western', 'Crime', 'Science Fiction']},
    {'movie_type': 'Comedy', 'genres_to_be_excluded': ['Horror', 'Mystery', 'Romance', 'Adventure', 'Western', 'Crime', 'Science Fiction', 'Fantasy']},
    {'movie_type': 'Family', 'genres_to_be_excluded': ['Horror', 'Mystery', 'Romance', 'Adventure', 'Western', 'Crime', 'Science Fiction', 'Fantasy', 'Comedy']},
    {'movie_type': 'History', 'genres_to_be_excluded': ['Horror', 'Mystery', 'Romance', 'Adventure', 'Western', 'Crime', 'Science Fiction', 'Fantasy', 'Comedy', 'Family']},
    {'movie_type': 'War', 'genres_to_be_excluded': ['Horror', 'Mystery', 'Romance', 'Adventure', 'Western', 'Crime', 'Science Fiction', 'Fantasy', 'Comedy', 'Family', 'History']},
    {'movie_type': 'Drama', 'genres_to_be_excluded': ['Horror', 'Mystery', 'Romance', 'Adventure', 'Western', 'Crime', 'Science Fiction', 'Fantasy', 'Comedy', 'Family', 'History', 'War']},
    {'movie_type': 'Thriller', 'genres_to_be_excluded': ['Horror', 'Mystery', 'Romance', 'Adventure', 'Western', 'Crime', 'Science Fiction', 'Fantasy', 'Comedy', 'Family', 'History', 'War', 'Drama']},
]
movies_categories_pl = {
    'Horror': 'Horror',
    'Mystery': 'Tajemnica',
    'Romance': 'Romans',
    'Adventure': 'Przygodowy',
    'Western': 'Western',
    'Crime': 'Zbrodnia',
    'Science Fiction': 'Science Fiction',
    'Fantasy': 'Fantastyka',
    'Comedy': 'Komedia',
    'Family': 'Familijny',
    'History': 'Historyczny',
    'War': 'Wojenny',
    'Drama': 'Dramat',
    'Thriller': 'Thriller',
}

# TODO: do not use @csrf_exempt in serious websites
# https://stackoverflow.com/questions/6506897/csrf-token-missing-or-incorrect-while-post-parameter-via-ajax-in-django#6533544
# This view inserts ratings into db.
@csrf_exempt
def insert_rating(request):
    logger.info('Inserting new votes')
    if request.method == 'POST':
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)

            user_id = request.session['user_id']
            user_db_object = Users.objects.filter(user_id=user_id)[0]
            ratings = body['ratings']
            for rating_obj in ratings:
                movie_rating = rating_obj['movie_rating']
                movie_id = rating_obj['movie_id']
                movie_db_object = Movies.objects.filter(movie_id=movie_id)[0]
                logger.info(
                    'Saving new vote into db: user_id: ' + str(user_id) +
                    ', user_name: '+ str(user_db_object.user_name) +
                    ', movie_id: '+ str(movie_id) +
                    ', movie_title: '+ str(movie_db_object.movie_title) +
                    ', movie_rating: ' + str(movie_rating))
                vote_db_object = Responses.objects.create(
                    user_id=user_db_object, movie_id=movie_db_object, user_rate=movie_rating)
            return HttpResponse('Successfully inserted new votes')
        except:
            logger.error(traceback.print_exc())
            return HttpResponseBadRequest(traceback.print_exc())
    else:
        return HttpResponseBadRequest('Expected method POST, got: %s' % request.method)

def test_rating(request):
    movies0 = Movies.objects.filter(movie_id=1)
    movies1 = Movies.objects.filter(movie_id=25)
    movies = [movies0[0], movies1[0]]
    return render(request, 'movies/test_rating.html', {'movies': movies })



# This view prints a poll with movies to be rated.
def rating(request):
    all_movies_count = 200
    user_id = request.session['user_id']
    responses_for_one_user = Responses.objects.filter(user_id=user_id)
    unassessed_movies_ids = Movies.get_unassessed_movies(
        user_id, responses_for_one_user,all_movies_count)
    progress = all_movies_count - len(unassessed_movies_ids)

    if int(request.session['movies_category_index']) == len(movies_categories):
        # it could happen that a user refreshed the page without assessing any movies,
        # it would then lead the user to the next movies category and some
        # movies would be left unassessed
        if len(unassessed_movies_ids) != 0:
            movie_type = 'Other (left unrated)'
            movie_type_pl = 'Inne (pominięte wcześniej)'
            movies = Movies.get_movies_by_ids(unassessed_movies_ids)
            # render new page with movies to be rated
            return render(request, 'movies/rating.html',
                {'movies': movies, 'category': movie_type, 'category_pl': movie_type_pl,
                'progress': progress})
        else:
            # all movies were rated, so render bye page
            return render(request, 'movies/bye.html')
    else:
        movie_category = movies_categories[request.session['movies_category_index']]
        movie_type = movie_category['movie_type']
        movie_type_pl = movies_categories_pl[movie_type]
        genres_to_be_excluded = movie_category['genres_to_be_excluded']
        movies = Movies.get_movies_by_genre(movie_type, genres_to_be_excluded )
        # set values for next view
        request.session['movies_category_index'] = int(request.session.get('movies_category_index',0)) + 1
        # render new page with movies to be rated
        progress = all_movies_count - len(unassessed_movies_ids)
        return render(request, 'movies/rating.html',
            {'movies': movies, 'category': movie_type, 'category_pl': movie_type_pl,
            'progress': progress})
