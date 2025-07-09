from django.contrib import admin
from .models import Tale, Suggestion
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Tale)
class TaleAdmin(SummernoteModelAdmin):

    list_display = ("title", "slug", "status")
    search_fields = ["title", "content"]
    list_filter = ("status", "created_on")
    prepopulated_fields = {"slug": ("title",)}
    summernote_fields = ("content",)


admin.site.register(Suggestion)
