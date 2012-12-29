from django.shortcuts import render
from models import Product


def product_list(request):
    products = Product.objects.all()
    return render(request, 'market/product_list.haml', {'products': products, })
