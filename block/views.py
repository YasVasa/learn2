from django.shortcuts import render
#from django.http import HttpResponse
from .models import Article

def home_page(request):
    articles = Article.objects.all()
    context = {"articles": articles}
    #context = {}
    return render(request, 'home_page.html', context) 