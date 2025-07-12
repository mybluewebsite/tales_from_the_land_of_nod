from django.urls import path
from . import views

urlpatterns = [
    path("", views.Stories.as_view(), name="stories"),
    path('<slug:slug>/', views.tale_detail, name='tale_detail'),
]