from django.contrib import admin
from .models import Tag, Category, Post, Comment, Social_Network, Social_Network_Post


admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Social_Network)
admin.site.register(Social_Network_Post)
