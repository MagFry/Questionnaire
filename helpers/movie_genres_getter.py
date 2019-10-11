import helpers.api_client as api_client
import helpers.csv_file_operator as csv_file_operator

# each line will be in the following format (example):
# 110	'Drama', 'Mystery', 'Romance'
def create_file_with_movies_genres():
    ids = csv_file_operator.read_movies_ids(csv_file_operator.file_path)
    for id in ids:
        genres = api_client.get_movie_genres(id, api_client.api_key_v3)
        genres_prettier = str(genres)
        genres_prettier = genres_prettier.replace('[','')
        genres_prettier = genres_prettier.replace(']','')
        line = id + '\t' + genres_prettier
        print(line)
        csv_file_operator.append_to_file('Data/genres.csv', line)

create_file_with_movies_genres()
