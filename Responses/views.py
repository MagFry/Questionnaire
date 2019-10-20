from django.shortcuts import render
from Responses.models import Responses
from Users.models import Users
from django.http import HttpResponse

def get_csv(request):
    responses = Responses.objects.all()
    csv = "respond_id,user_id,user_name,movie_id,movie_title,user_rate"
    for response in responses:
        line = str(response.respond_id) + ',' \
             + str(response.user_id.user_id) + ',' \
             + str(response.user_id.user_name) + ',' \
             + str(response.movie_id.movie_id) + ',' \
             + str(response.movie_id.movie_title) + ',' \
             + str(response.user_rate)
        csv = csv + "<br>" + line
    return HttpResponse(csv)
