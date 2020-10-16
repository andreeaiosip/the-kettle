from django.shortcuts import render
from .models import Tea, Coffee

# Create your views here.


def all_coffee(request):

    coffee = Coffee.objects.all()

    context = {
        'coffee': coffee,
    }

    return render(request, 'products/coffee.html', context)

