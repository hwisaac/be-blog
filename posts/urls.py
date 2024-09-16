from django.urls import path
from posts import views

urlpatterns = [
    path("", views.PostsAPI.as_view(), name="posts"),
    path("<str:slug>/", views.PostDetailAPI.as_view(), name="post-detail"),
]
