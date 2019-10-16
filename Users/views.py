from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from . import forms
from .models import Users
from django.http import HttpResponseBadRequest

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = forms.NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # save form input to session, but do not yet save to db
            # (we want to first check if such a user doesn't already exist)
            new_user = form.save(commit=False)
            user_name_local = new_user.user_name
            # ensure that the previous session data can’t be accessed again from the user’s browser
            request.session.flush()

            request.session['user_name'] = user_name_local

            # tell the session object explicitly that it has been modified
            request.session.modified = True

            users_with_that_name = Users.objects.filter(user_name=user_name_local)
            if len(users_with_that_name) != 0:
                return render(request, 'users/wrong_name.html')

            # add new user to DB
            new_user.save()

            # get user ID from DB
            user_from_db = Users.objects.filter(user_name=user_name_local)[0]
            request.session['user_id'] = user_from_db.user_id
            request.session['movies_category_index'] = 0
            request.session['movies_rated'] = 0
            request.session['movies_rated_next'] = 0

            return redirect('movies/rating')
        else:
            return render(request, 'users/empty_name.html')

    else:
        # if a GET (or any other method) we'll create a blank form
        form = forms.NameForm()
        return render(request, 'users/get_name.html', {'form': form})
