from rest_framework.serializers import ModelSerializer, SerializerMethodField
from posts.models import Post


class PostListSerializer(ModelSerializer):
    tags = SerializerMethodField()

    class Meta:
        model = Post
        exclude = ("content",)

    def get_tags(self, post):
        tags = post.tags.all()
        return [tag.name for tag in tags]


class PostDetailSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
