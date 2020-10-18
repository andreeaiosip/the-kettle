from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.db.models import Q
from django.contrib import messages
from .models import Product
# Create your views here.

# All products view and search query


def all_products(request):

    products = Product.objects.all()
    query = None
    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

                queries = Q(name__icontains=query) | Q(description__icontains=query)
                products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
    }

    return render(request, 'products/products.html', context)


# One product view

def product_view(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_view.html', context)
