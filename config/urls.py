from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from markdownx import urls as markdownx

urlpatterns = [
    path("api/admin/", admin.site.urls),
    path('markdownx/', include(markdownx)),
    path('martor/', include('martor.urls')),

]
