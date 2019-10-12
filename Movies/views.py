from django.shortcuts import render
file_path = 'Data/movies.csv'
from numpy import loadtxt
import pandas as pd
from .models import Movies
