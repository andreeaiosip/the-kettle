from django.shortcuts import render
from .models import Article


# Create your views here.


def all_articles(request):
    """ Display all articles """
  

    return render(request, 'articles/articles.html')

