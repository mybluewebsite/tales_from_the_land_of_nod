from django.shortcuts import render
from django.contrib import messages
from .models import Showcase
from .forms import CollaborateForm


def tale_showcase(request):
    if request.method == "POST":
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.add_message(request, messages.SUCCESS, "Collaboration request received! You should expect to receive a " \
            "response in the next 24 hours.")

    showcase = Showcase.objects.all().order_by('-updated_on').first()
    collaborate_form = CollaborateForm()

    return render(
        request,
        "showcase/showcase.html",
        {"showcase": showcase, "collaborate_form": collaborate_form},
    )