from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("api/admin/", admin.site.urls),
    path("api/posts/", include("posts.urls")),
    path("tinymce/", include("tinymce.urls")),
]
