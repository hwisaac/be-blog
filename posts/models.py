from django.db import models
from common.models import CommonModel
from django.utils.text import slugify

from tinymce.models import HTMLField

# Create your models here.
class Tag(CommonModel):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "태그"
        db_table = "tags"

class Post(CommonModel):
    title = models.CharField(max_length=255, blank=True ,default="")
    slug = models.SlugField(max_length=255, unique=True, blank=True, default="")
    summary = models.CharField(max_length=500, blank=True, default="")
    views = models.PositiveBigIntegerField(blank=True, default=0)
    thumbnail = models.ImageField(blank=True,  upload_to='thumbnails/')
    tags = models.ManyToManyField(Tag, blank=True, verbose_name='태그')
    content = HTMLField(default="")
    # tags,

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            # 중복된 슬러그가 있을 경우 처리
            original_slug = self.slug
            queryset = Post.objects.filter(slug=self.slug)
            counter = 1
            while queryset.exists():
                self.slug = f"{original_slug}-{counter}"
                counter += 1
                queryset = Post.objects.filter(slug=self.slug)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "포스트"
        db_table = "posts"

    def __str__(self):
        return self.title


# class Comment(CommonModel):
#     email = models.EmailField(null=True, blank=True)
#     content = models.CharField(max_length=255, null=True, blank=True, default="")
#     password = models.CharField(max_length=20, null=True, blank=True, default="")
