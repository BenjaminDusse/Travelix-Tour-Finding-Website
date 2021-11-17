from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about.html/", views.about, name="about"),
    path("offers.html/", views.OfferListView.as_view(), name="offers"),
    path("offer_detail.html/<int:pk>/", views.offer_detail, name="offer_detail"),
    path("contact.html/", views.contact, name="contact"),


    path("like_rest/", views.like_rest, name="like_rest"),
    path("dislike_rest/", views.dislike_rest, name="dislike_rest"),



    path("base/", views.base, name="base"),
]

