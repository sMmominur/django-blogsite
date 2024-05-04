import uuid
from django.db import models
from blog.common.models import TimeStampedModel, UserStampedModel
from blog.models import Post

class Comment(UserStampedModel,TimeStampedModel):
    comment_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    post_id = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True, blank=True)
    author = models.CharField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return self.content
