from django.contrib import admin
from .models import Showcase
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Showcase)
class ShowcaseAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)