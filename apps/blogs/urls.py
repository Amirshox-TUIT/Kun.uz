from django.urls import path
from . import views

app_name = 'blogs'

urlpatterns = [
    path("grid/", views.blog_grid, name="blog-grid"),
    path("list/", views.blog_list, name="blog-list"),
    path("category/", views.category, name="category"),
    path("single/", views.single_blog, name="single-blog"),
]
