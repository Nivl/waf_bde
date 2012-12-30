from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from models import Product


@login_required
def product_list(request):
    products = Product.objects.all()
    return render(request, 'market/product_list.haml', {'products': products, })
