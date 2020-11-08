from django.shortcuts import render
from .models import Article


# Create your views here.


def articles(request):
    """ Display all articles """
    articles = Article.all().order_by('pub_date')
    return render(request, 'articles/articles.html', {'articles': articles})

