from django.urls import path
from . import views

app_name = "pages"
urlpatterns = [
    path("404/", views.error_404, name="404"),
    path("about/", views.about, name="about"),
    path("author/", views.author, name="author"),
    path("contact/", views.contact, name="contact"),
    path("", views.index, name="index"),
    path("index2/", views.index2, name="index2"),
    path("login/", views.login, name="login"),
    path("single-author/", views.single_author, name="single-author"),
]
