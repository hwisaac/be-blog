from rest_framework.serializers import ModelSerializer, SerializerMethodField
from posts.models import Post


class PostListSerializer(ModelSerializer):
    tags = SerializerMethodField()

    class Meta:
        model = Post
        exclude = (
            "content",
            "related_post_1",
            "related_post_2",
        )

    def get_tags(self, post):
        tags = post.tags.all()
        return [tag.name for tag in tags]

class RelatedPostSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = (
            "id",
            "slug",
            "title",
            "summary",
            "thumbnail",
            "views",
        )


class PostDetailSerializer(ModelSerializer):
    tags = SerializerMethodField()
    related_post_1 = RelatedPostSerializer()
    related_post_2 = RelatedPostSerializer()

    class Meta:
        model = Post
        fields = "__all__"

    def get_tags(self, post):
        tags = post.tags.all()
        return [tag.name for tag in tags]
