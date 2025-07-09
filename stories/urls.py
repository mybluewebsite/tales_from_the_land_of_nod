from . import views
from django.urls import path

urlpatterns = [
    path("", views.MyStories.as_view(), name="stories"),
]