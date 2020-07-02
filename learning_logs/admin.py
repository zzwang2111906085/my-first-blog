from django.contrib import admin
from .models import Post

# Register your models here.
admin.site.register(Post)  # 为了让模型可见，我们需要在admin页面上注册
