from django.urls import path
from . import views

urlpatterns = [
    path("", views.Stories.as_view(), name="stories"),
    path('<slug:slug>/', views.tale_detail, name='tale_detail'),
    path('<slug:slug>/edit_suggestion/<int:suggestion_id>/', views.edit_suggestion, name='edit_suggestion'),
    path('<slug:slug>/delete_suggestion/<int:suggestion_id>/', views.delete_suggestion, name='delete_suggestion'),
]