from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Tale

class TaleList(generic.ListView):
    queryset = Tale.objects.filter(status=1).order_by("-created_on")
    context_object_name = "stories"
    template_name = "stories/index.html"
    paginate_by = 3

def tale_detail(request, slug):
    """
    Display an individual :model:`stories.Tale`.

    **Context**

    ``post``
        An instance of :model:`stories.Tale`.

    **Template:**

    :template:`stories/tale_detail.html`
    """

    queryset = Tale.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "stories/tale_detail.html",
        {"tale": post},
    )