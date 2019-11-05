from django.shortcuts import render
from Responses.models import Responses
from Users.models import Users
from django.http import HttpResponse

def get_csv(request):
    users = Users.objects.all()
    imp_users = []
    for user in users:
        responses_for_one_user = Responses.objects.all().filter(user_id=user.user_id)
        if len(responses_for_one_user) == 200:
            imp_users.append(user.user_id)
    responses = Responses.objects.all()
    csv = "respond_id,user_id,user_name,movie_id,movie_title,user_rate"
    for response in responses:
        rating = response.user_rate
        if rating != -1:
            # in our db rating is: 1-6 and -1 for not seen;
            # the output must be: 0-5 and -1 for not seen;
            rating = rating-1
        if response.user_id.user_id in imp_users:
            line = str(response.respond_id) + ',' \
                 + str(response.user_id.user_id) + ',' \
                 + str(response.user_id.user_name) + ',' \
                 + str(response.movie_id.movie_id) + ',' \
                 + str(response.movie_id.movie_title) + ',' \
                 + str(rating)
            csv = csv + "<br>" + line
    return HttpResponse(csv)

def get_all_csv(request):
    users = Users.objects.all()
    responses = Responses.objects.all()
    csv = "respond_id,user_id,user_name,movie_id,movie_title,user_rate"
    for response in responses:
        rating = response.user_rate
        if rating != -1:
            # in our db rating is: 1-6 and -1 for not seen;
            # the output must be: 0-5 and -1 for not seen;
            rating = rating-1
        line = str(response.respond_id) + ',' \
             + str(response.user_id.user_id) + ',' \
             + str(response.user_id.user_name) + ',' \
             + str(response.movie_id.movie_id) + ',' \
             + str(response.movie_id.movie_title) + ',' \
             + str(rating)
        csv = csv + "<br>" + line
    return HttpResponse(csv)
