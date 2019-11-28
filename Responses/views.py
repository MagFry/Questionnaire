from django.shortcuts import render
from Responses.models import Responses, UserMetadata, RespondMetadata
from Users.models import Users
from Movies.models import Movies
from django.http import (HttpResponse, HttpResponseBadRequest,
                         HttpResponseForbidden)
from django.core.management.color import no_style
from django.db import connection
from django.views.decorators.csrf import csrf_exempt
import logging
import traceback
import json

# Get an instance of a logger
logger = logging.getLogger('questionnaire_logger')
delimiter = Responses.get_delimiter()

def get_csv(request):
    users = Users.objects.all()
    imp_users = []
    csv = ""
    for user in users:
        responses_for_one_user = Responses.objects.all().filter(user_id=user.user_id)
        if len(responses_for_one_user) == 200:
            imp_users.append(user.user_id)
        else:
            csv += ("Invalid count of responses: %s for user: %s <br>" % (
                len(responses_for_one_user), user.user_name))
    responses = Responses.objects.all()
    csv += "respond_id" + delimiter + "user_id" + delimiter + \
        "user_name" + delimiter + "movie_id" + delimiter + \
        "movie_title" + delimiter + "user_rate"
    for response in responses:
        rating = response.user_rate
        if rating != -1:
            # in our db rating is: 1-6 and -1 for not seen;
            # the output must be: 0-5 and -1 for not seen;
            rating = rating-1
        if response.user_id.user_id in imp_users:
            line = str(response.respond_id) + delimiter \
                 + str(response.user_id.user_id) + delimiter \
                 + str(response.user_id.user_name) + delimiter \
                 + str(response.movie_id.movie_id) + delimiter \
                 + str(response.movie_id.movie_title) + delimiter \
                 + str(rating)
            csv = csv + "<br>" + line
    return HttpResponse(csv)

def get_all_csv(request):
    users = Users.objects.all()
    responses = Responses.objects.all()
    csv = "respond_id" + delimiter + "user_id" + delimiter + \
        "user_name" + delimiter + "movie_id" + delimiter + \
        "movie_title" + delimiter + "user_rate"
    for response in responses:
        rating = response.user_rate
        if rating != -1:
            # in our db rating is: 1-6 and -1 for not seen;
            # the output must be: 0-5 and -1 for not seen;
            rating = rating-1
        line = str(response.respond_id) + delimiter \
             + str(response.user_id.user_id) + delimiter \
             + str(response.user_id.user_name) + delimiter \
             + str(response.movie_id.movie_id) + delimiter \
             + str(response.movie_id.movie_title) + delimiter \
             + str(rating)
        csv = csv + "<br>" + line
    return HttpResponse(csv)

# Repopulate the db the input file of such format:
# respond_id,user_id,user_name,movie_id,movie_title,user_rate
# but there is no need to include the header line
@csrf_exempt
def db_repopulate(request):
    if request.method == 'GET':
        return render(request, 'responses/db_repopulate.html')
    elif request.method == 'POST':
        logger.info('Repopulating db')
        try:
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            data = body['csv_data']
            new_responds, new_users = Responses.parse_from_csv_data(data)

            # remove all users and all responds from db
            old_users = Users.objects.all()
            for user in old_users:
                user.delete()
            old_respones = Responses.objects.all()
            for resp in old_respones:
                resp.delete()

            # reset the IDs in tables users and responses
            sequence_sql = connection.ops.sequence_reset_sql(no_style(), [Users, Responses])
            with connection.cursor() as cursor:
                for sql in sequence_sql:
                    cursor.execute(sql)

            # add new users and new responses
            for user in new_users:
                Users.objects.create(
                    user_id=user.user_id, user_name=user.user_name)
                logger.info('Adding user with id: %s and name: %s' % (user.user_id, user.user_name))
            for resp in new_responds:
                user_db_object = Users.objects.filter(user_id=resp.user_id)[0]
                movie_db_object = Movies.objects.filter(movie_id=resp.movie_id)[0]
                Responses.objects.create(
                    user_id=user_db_object, movie_id=movie_db_object, user_rate=resp.user_rate)
            logger.info('Successfully repopulated db')
            return HttpResponse('Successfully repopulated db')
        except Exception as e:
            logger.error(traceback.print_exc())
            logger.error(e)
            return HttpResponseBadRequest(traceback.print_exc())
    else:
        return HttpResponseBadRequest('Expected method POST or GET, got: %s' % request.method)
