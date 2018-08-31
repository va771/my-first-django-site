from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#of course!

def index(request):
    return HttpResponse("<h3>Привет мир!</h3>")