from django.contrib import admin
from demo.mixins import RestrictUpdate
from .models import Author, Position, SocialLink


class SocialLinkInline(admin.StackedInline):
    model = SocialLink
    extra = 1


@admin.register(Author)
class AuthorAdmin(RestrictUpdate, admin.ModelAdmin):
    list_display = ['name', 'position', 'active']
    list_editable = ['position']
    inlines = [SocialLinkInline]


@admin.register(Position)
class PositionAdmin(RestrictUpdate, admin.ModelAdmin):
    list_display = ['title']
