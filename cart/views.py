from django.shortcuts import render, get_object_or_404, redirect
from products.models import Product

from cart.models import Cart, CartItems
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def add_to_cart(request, slug):
    product = Product.objects.get(slug=slug)

    user = request.user 
    cart , _ = Cart.objects.get_or_create(user=user, is_paid=False)
    # cart_item = CartItems.objects.create(cart=cart, product=product)
    cart_item , created = CartItems.objects.get_or_create(cart=cart, product=product)

    if not created:
        cart_item.quantity = cart_item.quantity + 1
        cart_item.save()



    return redirect('cart')

@login_required(login_url='login')
def cart(request):
    # cart_items =  CartItems.objects.filter(cart__is_paid=False, cart__user=request.user)

    cart = Cart.objects.filter(user=request.user, is_paid=False).first()
    cart_items = CartItems.objects.filter(cart=cart)

    subtotal = sum(item.total_price() for item in cart_items )
    # 2% shipping from subtotal     
    tax = 0.02 * subtotal
    shipping = 180
    total = subtotal + shipping + tax

    
    context = {
        'cart_items':cart_items,
        'subtotal':subtotal,
        'shipping':shipping,
        'total':total,
        'tax':tax,
    }
    return render(request, 'cart/cart.html', context)



@login_required(login_url='login')
def remove_item(request, item_id):
    if request.method == "POST":
        cart_item = get_object_or_404(CartItems, id=item_id)
        cart_item.delete()
    return redirect('cart')
    # post 