from django.shortcuts import render
file_path = 'Data/movies.csv'
from numpy import loadtxt
import pandas as pd
from .models import Movies


# Create your views here.
def read_data_to_dict(request, file_path):
    with open(file_path, "r") as ins:
        ids = []
        ids_tmdb = []
        title = []
        for line in ins:
            split_line = line.split('\t')
            ids.append(split_line[0])
            ids_tmdb.append(split_line[1])
            title.append(split_line[2])

    list = []
    #keys = ["file_id", "file_id_tmdb", "title"]
    #temp_dict = {}
    array_lenght = len(ids)

    for i in range(array_lenght):
        temp_dict = {"file_id":int(ids[i]), "file_id_tmdb":int (ids_tmdb[i]),  "title": title[i] }
        list.append(temp_dict)


    for item in list:

        id = item.get('file_id')
        id_tmdb = item.get('file_id_tmdb')
        title = item.get('title')

        movie_l = Movies.objects.create(movie_id=id, movie_id_tmdb=id_tmdb, movie_title=title)
        movie_l = Movies(
            movie_id=id,
            movie_id_tmdb=id_tmdb,
            movie_title=title
        )

        movie_l.save(force_insert=True)