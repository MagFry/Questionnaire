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
        if response.user_id.user_id in imp_users:
            line = str(response.respond_id) + ',' \
                 + str(response.user_id.user_id) + ',' \
                 + str(response.user_id.user_name) + ',' \
                 + str(response.movie_id.movie_id) + ',' \
                 + str(response.movie_id.movie_title) + ',' \
                 + str(response.user_rate)
            csv = csv + "<br>" + line
    return HttpResponse(csv)
