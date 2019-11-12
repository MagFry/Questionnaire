from django.db import models
from Movies.models import Movies
from Users.models import Users

class UserMetadata:
    def __init__(self, user_id, user_name):
      self.user_id = user_id
      self.user_name = user_name
class RespondMetadata:
    def __init__(self, respond_id, movie_id, user_id, user_rate):
        self.respond_id = respond_id
        self.movie_id = movie_id
        self.user_id = user_id
        self.user_rate = user_rate

class Responses(models.Model):
    respond_id = models.AutoField(primary_key=True)
    movie_id = models.ForeignKey(Movies, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    user_rate = models.IntegerField()

    def __str__(self):
        return self.respond_id

    def user_in_users(users, user_id):
        for user in users:
            if user.user_id == user_id:
                return True
        return False

    def parse_from_csv_data(data):
        new_responds = []
        new_users = []
        respond_id = 0
        for line in data.split('\n'):
            if line == '':
                continue
            if line.startswith('respond_id,user_id'):
                continue
            line_split = line.split(',')
            if len(line_split) != 6:
                raise ValueError('Cannot parse from csv, line cannot be split into 6 parts')
            # respond_id = int(line_split[0])
            respond_id = respond_id + 1
            user_id = int(line_split[1])
            user_name = line_split[2]
            movie_id = int(line_split[3])
            movie_title = line_split[4]
            user_rate = int(line_split[5])
            if user_rate != -1:
                # in our db rating is: 1-6 and -1 for not seen;
                # the output must be: 0-5 and -1 for not seen;
                user_rate = user_rate+1
            if Responses.user_in_users(new_users,user_id) == False:
                new_users.append(UserMetadata(user_id=user_id, user_name=user_name))
            new_responds.append(RespondMetadata(
                respond_id=respond_id,movie_id=movie_id,user_id=user_id,user_rate=user_rate))
        return new_responds, new_users
