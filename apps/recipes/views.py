from django.shortcuts import render

def recipe_with_sidebar(request):
    return render(request, "recipes/recipe-with-sidebar.html")

def recipe_without_sidebar(request):
    return render(request, "recipes/recipe-without-sidebar.html")

def shop(request):
    return render(request, "recipes/shop.html")

def single_recipe1(request):
    return render(request, "recipes/single-recipe1.html")

def single_recipe2(request):
    return render(request, "recipes/single-recipe2.html")

def single_shop(request):
    return render(request, "recipes/single-shop.html")

def submit_recipe(request):
    return render(request, "recipes/submit-recipe.html")
