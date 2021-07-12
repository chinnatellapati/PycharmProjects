from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# products -->Index


def index(request):
    return HttpResponse("Welcome to Index page in Django")

def new(request):
    return HttpResponse("New products app")