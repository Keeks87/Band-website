"""
View functions for the 'band' web application.

This module contains functions that define the behavior of the web application's
views. Each function corresponds to a specific URL pattern, and is responsible
for rendering the appropriate template or processing user input.

"""
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login

def index(request):
    """
    View function for the home page.

    This function renders the 'index.html' template.

    """
    return render(request, "index.html")

def about(request):
    """
    View function for the 'about' page.

    This function renders the 'about.html' template.

    """
    return render(request, 'about.html')

def contact(request):
    """
    View function for the 'contact' page.

    This function renders the 'contact.html' template.

    """
    return render(request, 'contact.html')

def home(request):
    """
    View function for the 'home' page.

    This function renders the 'home.html' template.

    """
    return render(request, 'home.html')

def join_us(request):
    """
    View function for the 'join_us' page.

    This function renders the 'join_us.html' template.

    """
    return render(request, 'join_us.html')

@csrf_exempt
def user_login(request):
    """
    View function for the user login page.

    This function processes the user's login information, authenticates the user,
    and logs the user in if the information is valid. If the information is not
    valid, an error message is displayed.

    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

def logout_view(request):
    """
    View function for logging out the user.

    This function logs out the user and redirects them to the login page.

    """
    logout(request)
    return redirect('login')

def sign_up(request):
    """
    View function for the user sign up page.

    This function processes the user's registration information, creates a new
    user account, and logs the user in.

    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
    else:
        form = UserCreationForm()

    return render(request, 'registration/sign_up.html', {"form": form})

