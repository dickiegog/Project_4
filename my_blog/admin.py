from django.contrib import admin
from .models import Post, Comment  # Import your models

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
