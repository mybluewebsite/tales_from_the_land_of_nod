from django.shortcuts import render
from django.views import generic
from .models import Tale

class MyStoriesView(generic.ListView):
    queryset = Tale.objects.all()
    template_name = "my_stories.html"