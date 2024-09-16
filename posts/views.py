from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer
from rest_framework import exceptions
import logging

# Create your views here.

logger = logging.getLogger("django")


class PostsAPI(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


class PostDetailAPI(APIView):
    def get_object(self, slug):
        try:
            return Post.objects.get(slug=slug)
        except Post.DoesNotExist:
            raise exceptions.NotFound

    def get(self, request, slug):
        post = self.get_object(slug)
        logger.info(f"[PostDetailAPI, GET] slug : {slug}")
        serializer = PostSerializer(post)
        return Response(serializer.data)
