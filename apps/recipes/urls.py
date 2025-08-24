from django.urls import path
from . import views

app_name = "recipes"
urlpatterns = [
    path("recipe/sidebar/", views.recipe_with_sidebar, name="recipe-with-sidebar"),
    path("recipe/no-sidebar/", views.recipe_without_sidebar, name="recipe-without-sidebar"),
    path("shop/", views.shop, name="shop"),
    path("recipe1/", views.single_recipe1, name="single-recipe1"),
    path("recipe2/", views.single_recipe2, name="single-recipe2"),
    path("single-shop/", views.single_shop, name="single-shop"),
    path("submit/", views.submit_recipe, name="submit-recipe"),
]
