from django.shortcuts import render
from .models import Showcase


def tale_showcase(request):
    """
    Renders the Showcase page
    """
    showcase = Showcase.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "showcase/showcase.html",
        {"showcase": showcase},
    )