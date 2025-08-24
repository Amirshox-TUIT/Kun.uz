from django.shortcuts import render

def blog_grid(request):
    return render(request, "blogs/blog-grid.html")

def blog_list(request):
    return render(request, "blogs/blog-list.html")

def category(request):
    return render(request, "blogs/category.html")

def single_blog(request):
    return render(request, "blogs/single-blog.html")
