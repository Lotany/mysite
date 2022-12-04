from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(response):
    return HttpResponse("<h1>Tech with lotan</h1>")

def signup(response):
    return HttpResponse("<h1>my first poridge</h1>")
    