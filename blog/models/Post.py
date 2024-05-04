import uuid
from django.db import models
from django.contrib.auth.models import User
from blog.common.choices import POST_STATUSES
from blog.common.models import TimeStampedModel, UserStampedModel
from blog.models import Category, Tag


class Post(UserStampedModel,TimeStampedModel):
    post_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    main_content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    category_id = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    thumbnail = models.ImageField(upload_to='thumbnail_img', blank=True, null=True)
    status = models.CharField(max_length=10, choices=POST_STATUSES, default='Draft')
    uri = models.URLField()
    seo_description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.title