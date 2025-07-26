from urllib import request
from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Tale, Suggestion
from .forms import SuggestionForm
from django.contrib.auth.decorators import login_required

class Stories(generic.ListView):
    queryset = Tale.objects.filter(status=1).order_by("-created_on")
    context_object_name = "stories"
    template_name = "stories/index.html"
    paginate_by = 6

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
    suggestions = tale.suggestions.all().order_by("-created_on")
    suggestion_count = tale.suggestions.filter(approved=True).count()

    if request.method == "POST":
        suggestion_form = SuggestionForm(data=request.POST)
        if suggestion_form.is_valid():
            suggestion = suggestion_form.save(commit=False)
            suggestion.author = request.user
            suggestion.tale = tale
            suggestion.save()
            messages.add_message(
                request, messages.SUCCESS,
                "Suggestion submitted and awaiting approval"
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

@login_required
def edit_suggestion(request, slug, suggestion_id):
    tale = get_object_or_404(Tale, slug=slug, status=1)
    suggestion = get_object_or_404(Suggestion, pk=suggestion_id)

    if suggestion.author != request.user:
        messages.error(request, "You are not authorised to edit this suggestion.")
        return HttpResponseRedirect(reverse("tale_detail", args=[slug]))

    if request.method == "POST":
        suggestion_form = SuggestionForm(request.POST, instance=suggestion)
        if suggestion_form.is_valid():
            suggestion = suggestion_form.save(commit=False)
            suggestion.tale = tale
            suggestion.approved = False
            suggestion.save()
            messages.success(request, "Suggestion updated and awaiting re-approval!")
        else:
            messages.error(request, "Error updating suggestion: Invalid data.")
    else:
        suggestion_form = SuggestionForm(instance=suggestion)
        pass

    return HttpResponseRedirect(reverse("tale_detail", args=[slug]))

def delete_suggestion(request, slug, suggestion_id):
    """
    view to delete suggestion
    """
    queryset = Tale.objects.filter(status=1)
    tale = get_object_or_404(queryset, slug=slug)
    suggestion = get_object_or_404(Suggestion, pk=suggestion_id)

    if suggestion.author == request.user:
        suggestion.delete()
        messages.add_message(request, messages.SUCCESS, "Suggestion deleted!")
    else:
        messages.add_message(request, messages.ERROR, "You can't delete this suggestion!")

    return HttpResponseRedirect(reverse("tale_detail", args=[slug]))