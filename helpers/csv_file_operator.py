file_path = 'Data/movies.csv'

# returns an array of strings which represent movie id in TMDB
def read_movies_ids(file_path):
    with open(file_path, "r") as ins:
        ids = []
        for line in ins:
            split_line = line.split('\t')
            ids.append(split_line[1])
        return ids

# ids = read_movies_ids(file_path)
# print(ids)

def append_to_file(file_path, line):
    with open(file_path, "a") as file:
        file.write(line+'\n')

# append_to_file('Data/genres.csv', 'abc')
