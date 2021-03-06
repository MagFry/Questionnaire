import requests
import os
import os.path

url = "https://api.themoviedb.org/3"
api_key_v3 = os.environ['TMDB_API_KEY']

# https://developers.themoviedb.org/3/movies/get-movie-details
def get_movie_json(movie_id, api_key):
    resp = requests.get(url+'/movie/'+str(movie_id)+'?api_key=' + api_key)
    if resp.status_code != 200:
        # This means something went wrong.
        raise RuntimeError('GET /movie/%s %s' % (movie_id,resp.status_code))
    return resp.json()

# Returns a collection of strings, many genres for one particular movie
# E.g. ['Action', 'Adventure', 'Drama']
def get_movie_genres(movie_json):
    # [{u'id': 28, u'name': u'Action'}, {u'id': 12, u'name': u'Adventure'}, {u'id': 18, u'name': u'Drama'}]
    genres = movie_json['genres']
    genres_pretty = []
    for genre in genres:
        genres_pretty.append(genre['name'])
    return genres_pretty

# Returns a string of genres, comma separated
# E.g. 'Action,Adventure,Drama'
def get_movie_genres_comma_separated(movie_json):
    # [{u'id': 28, u'name': u'Action'}, {u'id': 12, u'name': u'Adventure'}, {u'id': 18, u'name': u'Drama'}]
    genres = movie_json['genres']
    genres_comma_sep = ""
    for genre in genres:
        genres_comma_sep = genres_comma_sep + ',' + genre['name']
    # remove first comma
    return genres_comma_sep[1:]

# Returns bool, true if file was downloaded
def download_poster(movie_json, images_dir):
    poster_file = movie_json['poster_path']
    local_poster_path = str(movie_json['id']) + '.jpg'
    if os.path.isfile(images_dir+'/'+poster_file):
        return False
    elif os.path.isfile(images_dir+'/'+local_poster_path):
        return False
    else:
        resp = requests.get("https://image.tmdb.org/t/p/original/"+poster_file)
        open(images_dir+"/"+local_poster_path, 'wb').write(resp.content)
        return True

def get_polish_movie_details(movie_id, api_key):
    resp = requests.get(url+'/movie/'+str(movie_id)+'/translations?api_key=' + api_key)
    if resp.status_code != 200:
        # This means something went wrong.
        raise RuntimeError('GET /movie/%s/translations %s' % (movie_id,resp.status_code))
    movie_json = resp.json()
    translations = movie_json['translations']
    details = {}
    for translation in translations:
        if translation['iso_3166_1'] == 'PL':
            details['title'] = translation['data']['title']
            details['overview'] = translation['data']['overview']
            return details
    if details == {}:
        details['title'] = ""
        details['overview'] = ""
    return details
