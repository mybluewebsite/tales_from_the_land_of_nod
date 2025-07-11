from django.shortcuts import render
from django.views import generic
from .models import Tale

class TaleList(generic.ListView):
    queryset = Tale.objects.filter(status=1).order_by("-created_on")
    context_object_name = "stories"
    template_name = "stories/index.html"
    paginate_by = 3