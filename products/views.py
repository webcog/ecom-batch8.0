from django.shortcuts import render
from products.models import Product
from category.models import Category
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    category = Category.objects.all()
    products = Product.objects.all()
    context = {
        "category":category,
        "products":products,
    }

    return render(request, 'index.html',context)

# @login_required(login_url="login")
def shop(request):
    products = Product.objects.all()
    context = {
        "products":products
    }
    return render(request, 'shop.html', context)


# @login_required(login_url="login")
def detail(request, slug):
    product = Product.objects.get(slug=slug)
    context = {
        "product":product,
    }
    return render(request, 'detail.html', context)