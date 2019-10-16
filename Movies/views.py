from django.shortcuts import render
from .models import Movies
from django.shortcuts import render, redirect
#from . import forms
from django.utils.safestring import mark_safe
import json
from django.contrib.auth.decorators import login_required
from django.http import (HttpResponse, HttpResponseBadRequest,
                         HttpResponseForbidden)
from Responses.forms import VoteForm
from django.views.decorators.csrf import csrf_exempt
from django.http import QueryDict
import os
# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger('questionnaire_logger')

movies_categories = [
    {'movie_type': 'Horror', 'genres_to_be_excluded': []},
    {'movie_type': 'Mystery', 'genres_to_be_excluded': ['Horror']},
    {'movie_type': 'Romance', 'genres_to_be_excluded': ['Horror, Mystery']},
    {'movie_type': 'Adventure', 'genres_to_be_excluded': ['Horror, Mystery', 'Romance']},
    {'movie_type': 'Western', 'genres_to_be_excluded': ['Horror, Mystery', 'Romance', 'Adventure']},
    {'movie_type': 'Crime', 'genres_to_be_excluded': ['Horror, Mystery', 'Romance', 'Adventure', 'Western']},
    {'movie_type': 'Science Fiction', 'genres_to_be_excluded': ['Horror, Mystery', 'Romance', 'Adventure', 'Western', 'Crime']},
    {'movie_type': 'Fantasy', 'genres_to_be_excluded': ['Horror, Mystery', 'Romance', 'Adventure', 'Western', 'Crime', 'Sci-Fi']},
    {'movie_type': 'Comedy', 'genres_to_be_excluded': ['Horror, Mystery', 'Romance', 'Adventure', 'Western', 'Crime', 'Sci-Fi', 'Fantasy']},
    {'movie_type': 'Family', 'genres_to_be_excluded': ['Horror, Mystery', 'Romance', 'Adventure', 'Western', 'Crime', 'Sci-Fi', 'Fantasy', 'Comedy']},
    {'movie_type': 'History', 'genres_to_be_excluded': ['Horror, Mystery', 'Romance', 'Adventure', 'Western', 'Crime', 'Sci-Fi', 'Fantasy', 'Comedy', 'Family']},
    {'movie_type': 'War', 'genres_to_be_excluded': ['Horror, Mystery', 'Romance', 'Adventure', 'Western', 'Crime', 'Sci-Fi', 'Fantasy', 'Comedy', 'Family', 'History']},
    {'movie_type': 'Drama', 'genres_to_be_excluded': ['Horror, Mystery', 'Romance', 'Adventure', 'Western', 'Crime', 'Sci-Fi', 'Fantasy', 'Comedy', 'Family', 'History', 'War']},

]

def test(request):
    return render(request, 'movies/rating-star.html')
def test2(request):
    return render(request, 'movies/rating-star2.html')

# TODO: do not use it in serious websites
# https://stackoverflow.com/questions/6506897/csrf-token-missing-or-incorrect-while-post-parameter-via-ajax-in-django#6533544
@csrf_exempt
def insert_rating(request):
    logger.info('Inserting new votes')
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        # TODO: get from session
        user_id = 444
        ratings = body['ratings']
        for rating_obj in ratings:
            movie_rating = rating_obj['movie_rating']
            movie_id = rating_obj['movie_id']
            logger.info('Got new vote: user_id: ' + str(user_id) + ' movie_id: '+ str(movie_id) + ' movie_rating: ' + str(movie_rating))

        return HttpResponse('Successfully inserted new votes')
    else:
        return HttpResponseBadRequest('Expected method POST, got: %s' % request.method)


def collect_ratings(request):
    # TODO: implement collecting the ratings
    # if this is a POST request we need to process the form data
    #return HttpResponseBadRequest('method: %s' % request.method)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = VoteForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            new_vote = form.save(commit=False)
            return HttpResponseBadRequest('valid form: %s' % new_vote)
            new_vote.save()
            logger.info('Saving new vote: %s' % new_vote)
            logger.info('Saving new vote: %s' % new_vote.user_rate)
        else:
            return HttpResponseBadRequest('invalid form: %s. \nRequest: %s' % (form.errors, request.body))



    # render new page with movies to be rated
    request.session['movies_category_index'] = int(request.session.get('movies_category_index',0)) + 1
    if int(request.session['movies_category_index']) == len(movies_categories):
        return render(request, 'movies/bye.html')
    else:
        movie_category = movies_categories[request.session['movies_category_index']]
        movie_type = movie_category['movie_type']
        genres_to_be_excluded = movie_category['genres_to_be_excluded']
        movies = Movies.get_movies_by_genre(movie_type, genres_to_be_excluded )
        request.session['movies_count'] = len(movies)
        request.session['movies_rated'] = int(request.session['movies_rated']) + len(movies)
        return render(request, 'movies/movies_category.html',
            {'movies': movies, 'category': movie_type})

# first page with ratings
def first_movies_category(request):
    request.session['movies_category_index'] = 0

    movie_category = movies_categories[request.session['movies_category_index']]
    movie_type = movie_category['movie_type']
    genres_to_be_excluded = movie_category['genres_to_be_excluded']
    movies = Movies.get_movies_by_genre(movie_type, genres_to_be_excluded )
    request.session['movies_count'] = len(movies)
    request.session['movies_rated'] = 0
    return render(request, 'movies/movies_category.html',
        {'movies': movies, 'category': movie_type})
