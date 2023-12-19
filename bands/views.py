from django.shortcuts import render
from .models import Band
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm


# Create your views here.
def user_login(request):
    return render(request, 'registration/login.html')


""" data from the 'login.html' file is sent here to be authenticated
 the username and password will be pulled from the the 'login.html' file
 if correct, the user will be sent to the 'polls:index' page/app
 if there is a problem logging in,'user_auth:login' page is called so you can
 try to login again """


def authenticate_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is None:
        return HttpResponseRedirect(
            reverse('bands:login')
        )
    else:
        login(request, user)
        return HttpResponseRedirect(
            reverse('bands:home')
        )


# home page function, user will be directed to home page when called
def home(request):
    bands = Band.objects.all()
    return render(request, 'registration/home.html', {'bands': bands})


# This where the bands details you have selected to view will be called and
# return a rendered page
def band_details(request, band_id):
    band = Band.objects.get(id=band_id)
    return render(request, 'registration/band_details.html', {'band': band})


# This is where the about of the app will be called to be rendered
def about(request):
    return render(request, 'registration/about.html')


""" To be able to add a band to the app, logging in will be required
 an unregistered user or a user that has not logged in will not be all access
 to add a band. """


@login_required(login_url='login')
def add_band(request):
    if request.method == 'POST':
        name = request.POST['name']
        genre = request.POST['genre']
        formed_date = request.POST['formed_date']
        description = request.POST['description']

        new_band = Band(name=name, genre=genre, formed_date=formed_date,
                        description=description)
        new_band.save()
    return render(request, 'registration/add_band.html')


# log out function will display a message and a link to the home page
def log_out(request):
    return render(request, 'registration/log_out.html')


""" this is where the user will register the account
 after successful register, user is sent to the home page
 if its not successful, user will be sent back to registration page """


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect(reverse('bands:home'))
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})
