from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("Привет, это мой первый Django-проект!")
# Create your views here.
