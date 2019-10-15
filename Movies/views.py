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

def horror_movies(request):
    movie_type = 'Horror'
    arr = []
    movie = Movies.get_movies_by_genre(movie_type, arr )
    return render(request, 'movies/movies_horror.html', {'movies': movie})

def mystery_movies(request):
    movie_type = 'Mystery'
    arr = ['Horror']
    movie = Movies.get_movies_by_genre(movie_type, arr )
    return render(request, 'movies/movies_mystery.html', {'movies': movie})