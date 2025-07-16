from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("showcase/", include("showcase.urls"), name="showcase-urls"),
    path("summernote/", include("django_summernote.urls")),
    path("stories/", include("stories.urls")),
]
