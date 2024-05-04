from django.db import models
from django.contrib.auth.models import User

class UserStampedModel(models.Model):
    created_by = models.ForeignKey(User, related_name='%(class)s_created', on_delete=models.SET_NULL, null=True, blank=True)
    updated_by = models.ForeignKey(User, related_name='%(class)s_updated', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        abstract = True

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
