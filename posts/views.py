from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q
from .models import Post, Tag
from .serializers import PostDetailSerializer, PostListSerializer
from rest_framework import exceptions
import logging
from rest_framework.pagination import PageNumberPagination
from rest_framework import status

# Create your views here.

logger = logging.getLogger("django")


class PostsAPI(APIView):

    class PostPagination(PageNumberPagination):
        page_size = 6
        page_size_query_param = "page_size"
        max_page_size = 100

    def get(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by("-updated_at")
        # 검색어 필터링 (q 파라미터)
        query = request.query_params.get("q")
        if query:
            posts = posts.filter(
                Q(title__icontains=query) | Q(summary__icontains=query)
            )

        # 태그 필터링 (tag 파라미터)
        tag_name = request.query_params.get("tag")
        if tag_name:
            try:
                tag = Tag.objects.get(
                    name__iexact=tag_name
                )  # 대소문자 구분 없이 필터링
                posts = posts.filter(tags=tag)
            except Tag.DoesNotExist:
                posts = Post.objects.none()  # 태그가 없으면 빈 결과 반환

        paginator = self.PostPagination()
        paginated_posts = paginator.paginate_queryset(posts, request)

        serializer = PostListSerializer(paginated_posts, many=True)
        total_items = posts.count()
        total_pages = paginator.page.paginator.num_pages
        current_page = paginator.page.number

        response_data = {
            "posts": serializer.data,
            "total_items": total_items,
            "current_page": current_page,
            "total_pages": total_pages,
        }

        return Response(response_data, status=status.HTTP_200_OK)


class PostDetailAPI(APIView):
    def get_object(self, slug):
        try:
            return Post.objects.get(slug=slug)
        except Post.DoesNotExist:
            raise exceptions.NotFound

    def get(self, request, slug):
        post = self.get_object(slug)
        logger.info(f"[PostDetailAPI, GET] slug : {slug}")
        serializer = PostDetailSerializer(post)
        return Response(serializer.data)
