from django.contrib import admin
from .models import Tale, Suggestion
from django_summernote.admin import SummernoteModelAdmin

admin.site.register(Tale)
admin.site.register(Suggestion)
