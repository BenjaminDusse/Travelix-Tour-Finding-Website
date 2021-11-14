from django.contrib import admin
from .models import Tag, Category, Rest_area, Review, Client

admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Rest_area)
admin.site.register(Review)
admin.site.register(Client)