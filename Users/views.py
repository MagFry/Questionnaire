from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import NameForm

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        username_form = NameForm(request.POST)
        # check whether it's valid:
        if username_form.is_valid():
            # save user to db
            username_form.save()
            # redirect to a new URL:
            return HttpResponseRedirect('movies/movies_list.html')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'users/get_name.html', {'form': form})