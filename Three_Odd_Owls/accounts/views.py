"""
View functions for user registration and login.
"""
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login

def register(request):
    """
    View function for user registration.

    This view function handles GET and POST requests to the 'register/'
    URL. If a GET request is received, it returns a rendered template with a
    UserCreationForm. If a POST request is received, it attempts to validate
    the form data and create a new user. If the form data is valid, the user is
    created and the user is redirected to the 'login/' URL. If the form data is
    invalid, the form is re-rendered with error messages.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def login(request):
    """
    View function for user login.

    This view function handles GET and POST requests to the 'login/'
    URL. If a GET request is received, it returns a rendered template with an
    AuthenticationForm. If a POST request is received, it attempts to validate
    the form data and log the user in. If the form data is valid, the user is
    logged in and redirected to the 'home' URL. If the form data is invalid,
    the form is re-rendered with error messages.

    """
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})
