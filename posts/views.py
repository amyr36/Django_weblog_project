from django.shortcuts import render
from .models import Article
from django.http import HttpResponse

app_name = "blogs"

def blog_list(request):
    article = Article.publish.all()
    return render(request, "blogs/list.html", {"article": article})

def blog_detail(request, slug):
    article = Article.publish.get(slug=slug)
    return render(request, "blogs/detail.html", {"article": article})    


