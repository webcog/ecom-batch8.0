from django.urls import path
from cart.views import add_to_cart, cart


urlpatterns = [
    path("add-to-cart/<str:slug>", add_to_cart, name="add_to_cart"),
    path("cart/", cart, name="cart")
]
