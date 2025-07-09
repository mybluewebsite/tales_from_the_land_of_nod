from . import views
from django.urls import path

urlpatterns = [
    path("", views.MyStoriesView.as_view(), name="home"),
]