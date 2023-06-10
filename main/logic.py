from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from main.exceptions import *
#logic of the website
# def get_event, def get_profile, def add_event, def book_event, def cancel_event
def register_user(request):
    user = User.objects.create(username=request.POST.get("username"))
    user.set_password(request.POST.get("password"))
    user.save()
    login(request, user)


def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return redirect('main')
      
    else:
        raise InvalidCridentialsException('Invalid email or password')

  
        