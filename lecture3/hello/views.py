from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def devin(request):
    return HttpResponse("Hello, Devin")

def isabel(request):
    return HttpResponse("Hello, Isabel")

def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}!")