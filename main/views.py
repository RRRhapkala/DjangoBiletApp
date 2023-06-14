from django.shortcuts import render
from main.exceptions import *
from main.logic import *
from django.contrib import messages
from django.contrib.auth import logout
# Create your views here.

def main_page(request):
    print(request.user.username)
    context = {"events": get_events()}
    return render(request, 'main_page.html', context)

def addevent_page(request):
    context = {}
    if request.method == 'POST':
            add_event(request)
            return redirect('main')
    
    return render(request, 'addevent_page.html', context)

def event_page(request, id):
    event = Event.objects.get(id = id)
    context = {
        "event": event
    }
    if request.method == "POST":
        submit_reservation(request)
    return render(request, "event_page.html", context)
    

def register_page(request):
    if request.method == 'POST':
        try:
            register_user(request)
            return redirect('main')
        except InvalidCridentialsException as e:
            messages.error(request, e)
            return redirect('main')
    return render(request, 'register_page.html', {})

def login_page(request):
    if request.method == 'POST':
        try:
            login_user(request)
            return redirect('main')
        except InvalidCridentialsException as e:
            messages.error(request, e)
            return redirect('main')
    return render(request, 'login_page.html', {})

def profile_page(request):
    context = get_events_for_user(request)
    if request.method == 'POST':
        if request.POST.get("action") == "Cancel":
            cancel_reservation(request)
            return redirect("profile")
        elif request.POST.get("action") == "Signout":
            logout(request)
            return redirect('login')
    return render(request, 'profile_page.html', context)
