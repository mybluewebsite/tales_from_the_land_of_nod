from django.shortcuts import render
from django.http import HttpResponse

def my_stories(request):
    return HttpResponse("Welcome to The Land of Nod's stories section!")