from django.contrib import admin
from .models import Article



@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            "fields": ("title", "author", "slug", "image")
        }),
        ("Important dates", {
            "fields": ("created", "edited")
        }),
        ("Content", {
            "fields": ("content", "status")
        })
    )

    readonly_fields = ("created", "edited", "slug")
    
    list_display = ["title", "author", "status"]
    list_filter = ("status",)
    search_fields = ("title", "author__username")