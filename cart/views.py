from django.shortcuts import render, get_object_or_404, redirect
from products.models import Product
import uuid
from cart.models import Cart, CartItem

# Create your views here.

# function private

def _cart_id(request):
    user_info = str(request.user.id) if request.user.is_authenticated else 'guest'
    cart_id = f'{user_info}_{uuid.uuid4().hex}'

    return cart_id


def add_to_cart(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    cart_id = _cart_id(request)
    cart, created = Cart.objects.get_or_create(cart_id=cart_id)
    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not item_created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect("index")

    

    
    
    # 1_1322-fsdf32432432-21321-safssa6a6

    #    1_1322-fsdf32432432-21321-safssa6a6


    # if condition:
    #     cde 
    # else:
    #     code

    

