from django.urls import path
from . import views

app_name = 'travelix'
urlpatterns = [
    path("", views.home, name="home"),
    path("about.html/", views.about, name="about"),
    path("offers.html/", views.OfferListView.as_view(), name="offers"),
    path("offer_detail.html/<int:pk>/", views.offer_detail, name="offer_detail"),
    path("contact.html/", views.contact, name="contact"),

    path("base/", views.base, name="base"),
]
