from django.contrib import admin
from demo.mixins import RestrictUpdate
from .models import NewsEntry, NewsGallery


class NewsGalleryInline(admin.TabularInline):
    model = NewsGallery
    extra = 1


@admin.register(NewsEntry)
class NewsEntryAdmin(RestrictUpdate, admin.ModelAdmin):
    list_display = ['title', 'status', 'author', 'created_at']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title']
    fieldsets = [
        (None, {
            'fields': ['title', 'slug', 'summary', 'featured_image', 'status', 'author', 'tags', 'created_at']
        }),
        ('More options', {
            'classes': ('collapse',),
            'fields': ['source', 'modified_at']
        })
    ]
    readonly_fields = ['created_at']
    filter_horizontal = ['tags']
    raw_id_fields = ['author']
    list_filter = ['status', 'author']
    date_hierarchy = 'created_at'
    save_on_top = True
    actions_on_bottom = True
    inlines = [NewsGalleryInline]
