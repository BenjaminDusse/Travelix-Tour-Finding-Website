from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path("", views.PostListView.as_view(), name="post_list"),
    path("post_detail.html/<int:pk>/", views.post_detail, name="post_detail"),
]