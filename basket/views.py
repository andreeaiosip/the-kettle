from django.shortcuts import render, redirect, reverse, HttpResponse

# Create your views here.


def view_basket(request):
    """ Shopping basket is returned """
    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """ Add a quantity of the specified product to the shopping basket """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
    else:
        basket[item_id] = quantity

    request.session['basket'] = basket
    return redirect(redirect_url)




def update_basket(request, item_id):
    """Update the quantity of the product in the basket. """

    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})
    if quantity > 0:
        basket.pop(item_id)

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))

