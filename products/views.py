from django.shortcuts import render
from products.models import Product
# Create your views here.

def index(request):
    return render(request, 'index.html')


def shop(request):
    products = Product.objects.all()
    context = {
        "products":products
    }
    return render(request, 'shop.html', context)

def detail(request, slug):
    product = Product.objects.get(slug=slug)
    context = {
        "product":product,
    }
    return render(request, 'detail.html', context)