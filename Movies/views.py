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