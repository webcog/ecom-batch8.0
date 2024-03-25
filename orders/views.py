from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from orders.models import Order, OrderProduct
from cart.models import Cart, CartItems
from orders.forms import OrderForm
# Create your views here.

@login_required(login_url='login')
def checkout(request):
    cart = Cart.objects.filter(user=request.user, is_paid=False).first()
    cart_items = CartItems.objects.filter(cart=cart)

    subtotal = sum(item.total_price() for item in cart_items )
    # 2% shipping from subtotal     
    tax = 0.02 * subtotal
    shipping = 180
    total = subtotal + shipping + tax

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user 
            order.order_total = total
            order.tax = tax
            order.shipping_charges = shipping
            order.save()
            





    context = {
        'cart_items':cart_items,
        'subtotal':subtotal,
        'shipping':shipping,
        'total':total,
        'tax':tax,
    }
    return render(request, 'orders/checkout.html', context)