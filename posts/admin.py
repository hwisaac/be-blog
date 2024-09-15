from django.contrib import admin
from .models import Post
from markdownx.admin import MarkdownxModelAdmin
from martor.widgets import AdminMartorWidget
from django.db import models
from django.utils.safestring import mark_safe
from django.urls import reverse


# Register your models here.


@admin.register(Post)
class PostsAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "created_at",
        "updated_at",
    )
    search_fields = ("title",)

    # formfield_overrides를 통해 TextField에 AdminMartorWidget을 사용하도록 지정
    formfield_overrides = {
        models.TextField: {"widget": AdminMartorWidget},
    }
