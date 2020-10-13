from django.shortcuts import render

# Create your views here.


def index(request):
    """ Index page is returned """
    return render(request, 'home/index.html')
