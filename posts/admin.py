from django.contrib import admin
from .models import Post, Tag
from django.db import models
from django.utils.safestring import mark_safe
from django.urls import reverse
from tinymce.widgets import TinyMCE
from django import forms

# Register your models here.


@admin.register(Post)
class PostsAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "updated_at")
    search_fields = ("title",)

    formfield_overrides = {
        models.TextField: {"widget": TinyMCE()},
    }


@admin.register(Tag)
class PostsAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "updated_at")
    search_fields = ("name",)
