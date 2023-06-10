from django.shortcuts import render
from main.exceptions import *
# Create your views here.

def main_page(request):
    return render(request, "main_page.html", {"price": 100})