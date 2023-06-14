from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from main.exceptions import *
from main.models import Event
from main.forms import EventForm
import datetime
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

  
def get_events():
    return {
        "popular": Event.objects.filter(category="Popular"),
        "top": Event.objects.filter(category="Top"),
    }

def add_event(request):
    event_form = EventForm(request.POST)
    if event_form.is_valid():
        event_form.save()
    else:
        raise InvalidEventForm(event_form.errors)
    

def get_events_for_user(request):
    events = Event.objects.filter(users__in = [request.user])
    future_events = events.filter(date__gte = datetime.datetime.now())
    past_events = events.filter(date__lt = datetime.datetime.now())
    return {
            "futureEvents": future_events,
            "pastEvents": past_events
            }

def submit_reservation(request):
    event_id = request.POST.get("event_id")
    event = Event.objects.get(id=event_id)
    event.users.add(request.user)
    event.save()

def cancel_reservation(request):
    event_id = request.POST.get("event_id")
    event = Event.objects.get(id=event_id)
    event.users.remove(request.user)
    event.save()
