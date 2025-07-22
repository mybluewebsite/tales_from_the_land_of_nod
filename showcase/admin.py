from django.contrib import admin
from .models import Showcase, CollaborateRequest
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Showcase)
class ShowcaseAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)

@admin.register(CollaborateRequest)
class CollaborateRequestAdmin(admin.ModelAdmin):

    list_display = ('message', 'read',)