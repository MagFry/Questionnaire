from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from . import forms

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = forms.NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # save user to db
            instance = form.save(commit=False)
            # redirect to a new URL:
            instance.save()
            return redirect('movie:list')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = forms.NameForm()

    return render(request, 'users/get_name.html', {'form': form})