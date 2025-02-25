from django.shortcuts import render
from django.http import HttpRequest
from .models import Article

def home_page(request):
    articles = Article.objects.all()
    context = {"articles": articles}
    #context = {}
    return render(request, 'home_page.html', context) 

def article_page(request, slug):
    article = Article.objects.get(slug=slug)
    context = {"article": article}
    #context = {}
    return render(request, 'article_page.html', context)

def contacts(request):
    assert isinstance(request, HttpRequest)
    return render(request, 'contacts.html')

def about(request):
    assert isinstance(request, HttpRequest)
    return render(request, 'about.html')

def team(request):
    assert isinstance(request, HttpRequest)
    return render(request, 'team.html')


