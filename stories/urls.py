from . import views
from django.urls import path

urlpatterns = [
    path("", views.TaleList.as_view(), name="stories"),
]