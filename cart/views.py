from django.shortcuts import render, get_object_or_404, redirect
from products.models import Product

from cart.models import Cart, CartItems
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def add_to_cart(request, slug):
    product = Product.objects.get(slug=slug)

    user = request.user 
    cart , _ = Cart.objects.get_or_create(user=user, is_paid=False)
    cart_item = CartItems.objects.create(cart=cart, product=product)

    return redirect('cart')


def cart(request):
    # cart_items =  CartItems.objects.filter(cart__is_paid=False, cart__user=request.user)

    cart = Cart.objects.filter(user=request.user, is_paid=False).first()
    cart_items = CartItems.objects.filter(cart=cart)

    subtotal = sum(item.total_price() for item in cart_items )
    # 2% shipping from subtotal     
    shipping = 0.02 * subtotal
    total = subtotal + shipping

    
    context = {
        'cart_items':cart_items,
        'subtotal':subtotal,
        'shipping':shipping,
        'total':total
    }
    return render(request, 'cart/cart.html', context)