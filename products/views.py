from django.shortcuts import render
from products.models import Product
from category.models import Category

# Create your views here.

def index(request):
    category = Category.objects.all()
    context = {
        "category":category
    }

    return render(request, 'index.html',context)


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