from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path("login/", views.Login, name="login"),
    path("register/", views.Register, name="register"),
]

