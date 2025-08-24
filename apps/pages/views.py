from django.shortcuts import render

def error_404(request):
    return render(request, "pages/404.html")

def about(request):
    return render(request, "pages/about.html")

def author(request):
    return render(request, "pages/author.html")

def contact(request):
    return render(request, "pages/contact.html")

def index(request):
    return render(request, "pages/index.html")

def index2(request):
    return render(request, "pages/index2.html")

def login(request):
    return render(request, "pages/login.html")

def single_author(request):
    return render(request, "pages/single-author.html")
