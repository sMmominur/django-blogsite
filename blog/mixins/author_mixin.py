from django.contrib import admin
from django.db import models
from django.contrib.auth.models import User

# Set created_by and updated_by based on the request user
class AuthorMixin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        user = request.user
        if not obj.created_by:
            obj.created_by = user
        obj.updated_by = user
        obj.save()

