import uuid
from django.db import models
from blog.common.models import TimeStampedModel, UserStampedModel

class Tag(UserStampedModel, TimeStampedModel):
    tag_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tag_name = models.CharField(max_length=50)
    tag_slug = models.SlugField(max_length=60,unique=True,blank=True)
    
    def __str__(self):
        return self.tag_name
    
