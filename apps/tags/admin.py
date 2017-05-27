from django.contrib import admin
from demo.mixins import RestrictUpdate
from .models import Tag


@admin.register(Tag)
class TagAdmin(RestrictUpdate, admin.ModelAdmin):
    list_per_page = 15
