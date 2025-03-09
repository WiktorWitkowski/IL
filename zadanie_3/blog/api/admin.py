from django.contrib import admin
from .models import Author, Post, PostChangeHistory


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("ip",)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "author",
        "description",
        "keywords",
        "url",
        "created_at",
        "updated_at",
    )
    ordering = ['created_at']


@admin.register(PostChangeHistory)
class PostChangeHistoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "keywords",
        "url",
        "created_at",
        "post",
    )
