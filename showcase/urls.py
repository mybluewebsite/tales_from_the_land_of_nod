from . import views
from django.urls import path

urlpatterns = [
    path('', views.tale_showcase, name='showcase'),
]