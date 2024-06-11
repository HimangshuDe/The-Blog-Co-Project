from django.contrib import admin

from blog_app.models import Tag, Post

# Register your models here.
admin.site.register(Post)
admin.site.register(Tag)