from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),


    path("like_rest/", views.like_rest, name="like_rest"),
    path("dislike_rest/", views.dislike_rest, name="dislike_rest"),



    path("base/", views.base, name="base"),
]

