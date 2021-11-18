from django.contrib import admin
from .models import Tag, Category, Rest_area, Comment, Client

admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Rest_area)
admin.site.register(Comment)
admin.site.register(Client)