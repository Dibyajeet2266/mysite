from django.contrib import admin
from .models import Post
# Register your models here.

from blog.models import Post

admin.site.register(Post)
