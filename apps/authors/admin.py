from django.contrib import admin
from .models import Author, Position, SocialLink


class SocialLinkInline(admin.StackedInline):
    model = SocialLink
    extra = 1


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'active']
    list_editable = ['position']
    inlines = [SocialLinkInline]


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ['title']
