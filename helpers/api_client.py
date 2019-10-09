import requests
import os

url = "https://api.themoviedb.org/3"
api_key_v3 = os.environ['TMDB_API_KEY']

# Returns a collection of strings, many genres for one particular movie
# E.g. ['Action', 'Adventure', 'Drama']
def get_movie_genres(movie_id, api_key):
    resp = requests.get(url+'/movie/'+movie_id+'?api_key=' + api_key)
    if resp.status_code != 200:
        # This means something went wrong.
        raise RuntimeError('GET /movie/ {}'.format(resp.status_code))
    # [{u'id': 28, u'name': u'Action'}, {u'id': 12, u'name': u'Adventure'}, {u'id': 18, u'name': u'Drama'}]
    genres = resp.json()['genres']
    genres_pretty = []
    for genre in genres:
        genres_pretty.append(genre['name'])
    return genres_pretty

# Example usage:
# genres = get_movie_genres('551', api_key_v3)
# print(genres)
