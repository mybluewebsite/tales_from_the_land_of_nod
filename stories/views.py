from urllib import request
from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Tale, Suggestion
from .forms import SuggestionForm

class Stories(generic.ListView):
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
    tale = get_object_or_404(queryset, slug=slug)
    suggestions = tale.comments.all().order_by("-created_on")
    suggestion_count = tale.comments.filter(approved=True).count()

    if request.method == "POST":
        suggestion_form = SuggestionForm(data=request.POST)
        if suggestion_form.is_valid():
            suggestion = suggestion_form.save(commit=False)
            suggestion.author = request.user
            suggestion.tale = tale
            suggestion.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )

    suggestion_form = SuggestionForm()

    return render(
        request,
        "stories/tale_detail.html",
        {
            "tale": tale, 
            "suggestions": suggestions, 
            "suggestion_count": suggestion_count,
            "suggestion_form": suggestion_form,
        },
    )

def edit_suggestion(request, slug, comment_id):
    """
    view to edit suggestions on a tale.
    """
    if request.method == "POST":

        queryset = Tale.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        suggestion = get_object_or_404(Suggestion, pk=comment_id)
        suggestion_form = SuggestionForm(data=request.POST, instance=suggestion)

        if suggestion_form.is_valid() and suggestion.author == request.user:
            suggestion = suggestion_form.save(commit=False)
            suggestion.post = post
            suggestion.approved = False
            suggestion.save()
            messages.add_message(request, messages.SUCCESS, 'Suggestion Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating suggestion!')

    return HttpResponseRedirect(reverse('tale_detail', args=[slug]))