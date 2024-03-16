from django.urls import path
from cart.views import add_to_cart, cart, remove_item


urlpatterns = [
    path("add-to-cart/<str:slug>", add_to_cart, name="add_to_cart"),
    path("cart/", cart, name="cart"),
    path("remove_item/<int:item_id>", remove_item, name="remove_cart_item")
]
