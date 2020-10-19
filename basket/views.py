from django.shortcuts import render

# Create your views here.


def view_basket(request):
    """ Shopping bag is returned """
    return render(request, 'basket/basket.html')
