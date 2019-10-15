from django.shortcuts import render
from .models import Movies
from django.shortcuts import render, redirect
#from . import forms
from django.utils.safestring import mark_safe
import json
from django.contrib.auth.decorators import login_required


def movie_list(request):
    movie = Movies.objects.filter(movie_id=1)
    return render(request, 'movies/movies_list.html', {'movies':movie})
    if request.method == "POST":
        your_name = request.POST["your_name"]
        movie = Movies.objects.filter(movie_id=1)
        return render(request, 'movies/movies_list.html', {'movies':movie, 'your_name': your_name})
    else:
        movie = Movies.objects.filter(movie_id=1)
        return render(request, 'movies/movies_list.html', {'movies':movie})

def index(request):
    return render(request, 'movies/index.html')

movies_categories = [
    { 'movie_type': 'Horror', 'genres_to_be_excluded': [], 'this_page': 'movies/movies_category.html' },
    { 'movie_type': 'Mystery', 'genres_to_be_excluded': ['Horror'], 'this_page': 'movies/movies_category.html' },
    {  'this_page': 'movies/index.html' },
]

def collect_ratings(request):
    # TODO: implement collecting the ratings

    # render new page with movies to be rated
    request.session['movies_category_index'] = int(request.session.get('movies_category_index',0)) + 1
    movie_category = movies_categories[request.session['movies_category_index']]
    movie_type = movie_category['movie_type']
    genres_to_be_excluded = movie_category['genres_to_be_excluded']
    movies = Movies.get_movies_by_genre(movie_type, genres_to_be_excluded )
    return render(request, movie_category['this_page'],
        {'movies': movies, 'category': movie_type})

# first page with ratings
def first_movies_category(request):
    request.session['movies_category_index'] = 0

    movie_category = movies_categories[request.session['movies_category_index']]
    movie_type = movie_category['movie_type']
    genres_to_be_excluded = movie_category['genres_to_be_excluded']
    movies = Movies.get_movies_by_genre(movie_type, genres_to_be_excluded )
    return render(request, movie_category['this_page'],
        {'movies': movies, 'category': movie_type})
