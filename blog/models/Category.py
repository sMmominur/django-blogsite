import uuid
from django.db import models
from django.utils.text import slugify
from django.core.exceptions import ValidationError
from blog.common.choices import CATEGORY_STATUSES
from blog.common.models import TimeStampedModel, UserStampedModel

class Category(UserStampedModel, TimeStampedModel):
    category_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True, blank=True)
    status = models.CharField(max_length=10, choices=CATEGORY_STATUSES, default='Active')
    category_img = models.ImageField(upload_to='media/category_img', blank=True, null=True,verbose_name='Category Image')
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        user = kwargs.pop('user', None)
        if user and not self.created_by:
            self.created_by = user
        if user:
            self.updated_by = user
        if not self.name:
            raise ValidationError({'name': 'Name field is required.'})

        super().save(*args, **kwargs)

    class Meta:
        unique_together = ('slug',)