from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("accounts/", include("allauth.urls")),
    path("admin/", admin.site.urls),
    path("showcase/", include("showcase.urls"), name="showcase-urls"),
    path("stories/", include("stories.urls"), name="stories-urls"),
    path("summernote/", include("django_summernote.urls")),
]
